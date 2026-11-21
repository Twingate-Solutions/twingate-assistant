---
source: https://www.twingate.com/docs/web-app-access
type: docs
fetched: 2026-11-19
source_version: 001868be9d880d7280c40e9d3c55e3bcfd7d6eb627a6b758fa4155ce80ca0e09
trust: official
---

# Privileged Access for Web Apps Overview

## Summary
Privileged Access for Web Apps is the web app component of Twingate Privileged Access Management (Beta; free for up to five Resources). A Twingate Gateway acts as a Layer 7 reverse proxy in front of internal web apps and injects a signed ES256 JWT (Gateway Access Token) and optional headers into every request. Apps get authenticated user identity without OIDC, client secrets, or redirect flows. The Gateway can also serve trusted HTTPS with automatically provisioned certificates.

## Key Information
- Flow: Browser → Twingate Client → Gateway → App. The Controller authorizes the user against their existing Twingate session and the Resource's Security Policy, then issues a GAT scoped to user, device, and Resource.
- JWKS endpoint (unauthenticated): `https://<your-tenant>.twingate.com/api/v1/jwk/ec`
- JWT header: `alg: ES256`, `typ: GAT`, `kid`.
- Payload claims: `rnw`, `jti`, `iss`, `aud`, `exp`, `iat`, `ver`, plus `user.*` (id, username, email, first_name, last_name, groups), `device.*` (id, location), and `resource.*` (id, type=`WEB_APP`, address, aliases, gateway_metadata).
- `user.groups` always includes `twingate:authenticated`. Use it for authorization decisions.
- No headers are injected until you configure at least one.
- Use cases: add identity to apps with no auth, trusted-header SSO (Jenkins), JWKS-based SSO (Grafana), and HTTPS without per-app certs.
- Header sources: Gateway-wide (applies to all apps) and per-Resource rewrites. Per-Resource rewrites apply after Gateway-wide headers and override same-named ones.

## Prerequisites
- Twingate account with admin privileges
- Deployed Gateway with a Web App Resource
- At least one Connector in the same Remote Network
- For HTTPS: a CA registered with Twingate (self-signed, HashiCorp Vault, or Google Cloud CAS) and user devices that trust the CA (manually or via MDM such as Iru or Intune)

## Step-by-Step (Kubernetes Operator)
1. In the Admin Console, create a Remote Network and an API key with Read, Write & Provision permissions.
2. Install the Twingate Kubernetes Operator with the Gateway subchart and `gateway.webApp.enabled: true`. Add the Resource alias and address to `gateway.tls.dnsNames`.
3. Annotate the app's Kubernetes Service (see below). The operator creates the Web App Resource.
4. Deploy a Connector in the same Remote Network.
5. Grant users or Groups access to the Resource.
6. Verify the JWT in the app, or configure the off-the-shelf app to trust the injected headers.

## Configuration Values
**Template variables:** `{{jwt}}`, `{{username}}`, `{{groups}}`, `{{clientGeoLatLong}}`, `{{clientGeoCity}}`, `{{clientGeoRegion}}`, `{{clientGeoCountry}}`

**Recommended header:** `Authorization: Bearer {{jwt}}`. Fallback plaintext headers: `X-Twingate-User: {{username}}`, `X-Twingate-Groups: {{groups}}`.

**Helm (Gateway-wide, a map):**
```yaml
gateway:
  webApp:
    enabled: true
    requestHeaders:
      Authorization: "Bearer {{jwt}}"
```

**Service annotations:** `resource.twingate.com: "true"`, `resource.twingate.com/type: "WebApp"`, `resource.twingate.com/gatewayName`, `resource.twingate.com/gatewayNamespace`, `resource.twingate.com/downstreamPort`, `resource.twingate.com/downstreamTLSMode: "TLS13"`, `resource.twingate.com/requestHeaderRewrites: '{"Authorization": "Bearer {{jwt}}"}'` (JSON string)

**TwingateResource CRD:** `spec.type: WebApp`, `gatewayRef.name`, `downstream.port`, `upstream.port`, `requestHeaderRewrites` (list of name/value pairs)

**Terraform:** `twingate_web_app_resource` with `gateway_id`, `remote_network_id`, `address`, `alias`, `downstream`, `upstream`, `request_header_rewrites` (map)

## Gotchas
- `typ` is `GAT`, not `JWT`. Libraries that enforce `typ=JWT` will reject valid tokens, so configure them to accept `GAT`.
- Plaintext identity headers are only safe if they come solely from the Gateway.
- Reject expired tokens (`exp`) in your middleware.
- The header configuration format differs per surface (Helm map, CRD list, annotation JSON string, Terraform map). Check which one you're editing.
- SaaS apps that redirect to other domains or external IdPs during sign-in may behave unexpectedly as Web App Resources.

## Related Docs
- Web App quick start guide (Gateway)
- Developer guides: Express.js, Django, Next.js, Next.js + Auth.js
- Application integration guides (Grafana, Jenkins)
- Kubernetes Operator install and user guide
- Privileged Access Management Overview
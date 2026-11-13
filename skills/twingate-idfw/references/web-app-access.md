---
source: https://www.twingate.com/docs/web-app-access
type: docs
fetched: 2026-11-13
source_version: 89cffb7e2a6003bbefde974fd82c4f9042470c93756ed7a7a12b893354b34013
trust: official
---

# Privileged Access for Web Apps Overview

## Summary
Privileged Access for Web Apps (part of Twingate Identity Firewall) places internal web apps behind a Twingate Gateway acting as a Layer 7 reverse proxy. The Gateway injects a signed ES256 JWT (Gateway Access Token) and optional identity headers into each request, so apps get user identity without OIDC, client secrets, or redirects. It is in Beta and free for up to five Resources.

## Key Information
- Flow: Browser → Twingate Client → Gateway → App. The Controller authorizes the user and issues a GAT scoped to user, device, and Resource.
- The Gateway can provision TLS certificates on demand from a registered CA, giving trusted `https://` URLs.
- The app verifies the JWT against the JWKS endpoint: `https://<your-tenant>.twingate.com/api/v1/jwk/ec` (unauthenticated).
- JWT header: `alg: ES256`, `typ: GAT` (not `JWT`), `kid`.
- Key claims: `user.{id,username,email,first_name,last_name,groups}`, `device.{id,location}`, `resource.{id,type,address,aliases,gateway_metadata}`, plus `exp`, `iat`, `jti`, `aud` (network name), `rnw`, `ver`.
- `user.groups` always includes `twingate:authenticated`. Use groups for authorization.
- Use cases: add auth to apps with none, trusted-header SSO (Jenkins), JWKS validation (Grafana), HTTPS without per-app certs.

## Prerequisites
- Twingate account with admin privileges
- Deployed Gateway with a Web App Resource
- For HTTPS: a CA registered with Twingate (self-signed, HashiCorp Vault, or Google Cloud CAS), and user devices that trust it (manually or via MDM such as Iru or Intune)

## Step-by-Step (Operator setup)
1. In the Admin Console, create a Remote Network and an API key with Read, Write & Provision permissions.
2. Install the Twingate Kubernetes Operator with the Gateway subchart and `gateway.webApp.enabled: true`. Add the Resource alias and address to `gateway.tls.dnsNames`.
3. Annotate the app's Service with `resource.twingate.com: "true"`, `resource.twingate.com/type: "WebApp"`, `resource.twingate.com/gatewayName`, and header rewrites.
4. Deploy at least one Connector in the same Remote Network.
5. Grant users or Groups access to the Resource.
6. Verify the JWT in the app, or configure the off-the-shelf app to trust the injected headers.

## Configuration Values
- Template variables: `{{jwt}}`, `{{username}}`, `{{groups}}`, `{{clientGeoLatLong}}`, `{{clientGeoCity}}`, `{{clientGeoRegion}}`, `{{clientGeoCountry}}`
- Recommended header: `Authorization: Bearer {{jwt}}`. Fallbacks: `X-Twingate-User: {{username}}`, `X-Twingate-Groups: {{groups}}`
- Gateway-wide headers (Helm): `gateway.webApp.requestHeaders` (a map)
- Per-Resource rewrites (applied after Gateway-wide headers, so they override same-named ones):
  - Terraform: `twingate_web_app_resource` with `request_header_rewrites` map, `downstream.port`, `upstream.port`, `gateway_id`, `remote_network_id`, `address`, `alias`
  - CRD `TwingateResource` (`type: WebApp`): `requestHeaderRewrites` as a list of name/value pairs, plus `gatewayRef`, `downstream`, `upstream`
  - Service annotation: `resource.twingate.com/requestHeaderRewrites` as a JSON string, plus `downstreamPort` and `downstreamTLSMode` (e.g. `TLS13`)

## Gotchas
- No headers are injected until you configure at least one.
- Some JWT libraries require `typ == JWT` and reject `GAT`. Configure them to accept `GAT`.
- Plaintext identity headers are only safe if they come solely from the Gateway. Prefer the JWT.
- The three header config surfaces use different shapes (map, list, JSON string).
- Reject expired tokens (`exp`) in your middleware.
- SaaS apps that redirect to other domains or external IdPs during sign-in may not work as Web App Resources.

## Related Docs
- Web App quick start guide
- Developer guides (Express.js, Django, Next.js, Next.js + Auth.js)
- Application integration guides (Grafana, Jenkins)
- Kubernetes Operator install and user guide
- Identity Firewall Overview
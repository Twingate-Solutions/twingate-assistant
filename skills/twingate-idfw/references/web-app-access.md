---
source: https://www.twingate.com/docs/web-app-access
type: docs
fetched: 2026-10-25
source_version: 2212827ba9e42f1ee4effd068c5f2b4e61425be16f0c436023b874d22f15f878
trust: official
---

# Twingate Privileged Access for Web Apps

## Page Title
Privileged Access for Web Apps Overview

## Summary
Twingate Privileged Access for Web Apps places internal web applications behind a Twingate Gateway acting as a Layer 7 reverse proxy, injecting a signed ES256 JWT (Gateway Access Token) into every HTTP request. Apps verify the JWT via a standard JWKS endpoint to get user identity without OIDC, client secrets, or redirect flows. HTTPS with automatic certificate management is included.

## Key Information
- Gateway injects `Authorization: Bearer <jwt>` (and other configurable headers) on every forwarded request
- JWT signed with ES256; verified via JWKS endpoint: `https://<tenant>.twingate.com/api/v1/jwk/ec`
- JWT `typ` header is `GAT` (not `JWT`) — some libraries reject this; configure to accept `GAT`
- Free for up to 5 Resources (beta)
- Per-Resource header rewrites override Gateway-wide headers of the same name

## Prerequisites
- Twingate account with admin privileges
- Deployed Twingate Gateway with Web App Resource configured
- **For HTTPS:** CA registered with Twingate (self-signed, HashiCorp Vault, or Google Cloud CAS) + user devices trusting that CA

## JWT Structure

**Header:**
```json
{ "alg": "ES256", "typ": "GAT", "kid": "<key-id>" }
```

**Key Payload Claims:**

| Claim | Description |
|---|---|
| `user.email` / `user.username` | User identity |
| `user.groups` | Twingate groups (always includes `twingate:authenticated`) |
| `device.id` | Device identifier |
| `resource.id` / `resource.type` | Always `WEB_APP` |
| `exp` | Expiry; reject if past |
| `aud` | Your Twingate network/tenant name |

## Configuration Values

**Header Template Variables:**

| Variable | Value |
|---|---|
| `{{jwt}}` | Full signed ES256 JWT |
| `{{username}}` | User email/username |
| `{{groups}}` | Comma-separated group names |
| `{{clientGeoCity}}` / `{{clientGeoCountry}}` | Location fields |

**Terraform (per-Resource):**
```hcl
resource "twingate_web_app_resource" "internal_app" {
  request_header_rewrites = {
    "X-Twingate-User" = "{{username}}"
    "Authorization"   = "Bearer {{jwt}}"
  }
}
```

**Kubernetes Operator — Gateway-wide headers (Helm values):**
```yaml
gateway:
  webApp:
    enabled: true
    requestHeaders:
      Authorization: "Bearer {{jwt}}"
```

**Kubernetes Operator — Per-Resource (TwingateResource manifest):**
```yaml
requestHeaderRewrites:
  - name: X-Twingate-User
    value: "{{username}}"
```

**Service annotation (JSON string):**
```yaml
resource.twingate.com/requestHeaderRewrites: '{"Authorization": "Bearer {{jwt}}"}'
```

## Gotchas
- `typ: GAT` breaks JWT libraries that enforce `typ: JWT` — must configure library to accept `GAT`
- Headers are opt-in; no headers injected by default until configured
- SaaS apps with their own auth/redirect flows may conflict with Gateway architecture
- Plaintext headers (non-JWT) should only be trusted if confirmed to originate from the Gateway
- `user.groups` always includes `Everyone` and `twingate:authenticated` in addition to assigned groups

## Related Docs
- Twingate Kubernetes Operator install & user guide
- Developer guides: Express.js, Django, Next.js, Next.js + Auth.js
- Application integration guides: Grafana, Jenkins
- Identity Firewall Overview
- CA options: Self-signed, HashiCorp Vault, Google Cloud CAS
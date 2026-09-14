---
source: https://www.twingate.com/docs/web-app-access
type: docs
fetched: 2026-09-13
source_version: 6e4b808f0b33de564cdc5a4f148c7d42300a77d7e7845f5896bd8e36a211e711
---

# Twingate Privileged Access for Web Apps

## Page Title
Privileged Access for Web Apps Overview

## Summary
Twingate Privileged Access for Web Apps acts as a Layer 7 reverse proxy, injecting a signed ES256 JWT (Gateway Access Token) into every HTTP request forwarded to internal web applications. Apps verify the JWT against Twingate's JWKS endpoint to get user identity without OIDC integration or redirect flows. Currently in beta.

## Key Information
- Gateway injects signed JWT per-request with user identity, device info, and resource metadata
- No OIDC integration, client secrets, or redirect flows required
- JWT contains user groups for authorization decisions
- `X-Twingate-*` convenience headers available for logging/personalization without JWT parsing
- Headers are opt-in; no identity injected until at least one header is configured
- Gateway-wide headers apply to all proxied apps; per-Resource rewrites override them for specific apps

## Prerequisites
- Twingate account with administrator privileges
- Deployed Twingate Gateway with a Web App Resource configured
- Kubernetes Operator (recommended deployment method)
- Beta access (contact Twingate)

## Configuration Values

**JWKS Endpoint:**
```
https://<your-tenant>.twingate.com/api/v1/jwk/ec
```

**JWT Header fields:** `alg: ES256`, `typ: GAT` (not `JWT`), `kid: <key-id>`

**Template Variables for Header Values:**
| Variable | Description |
|---|---|
| `{{jwt}}` | Full signed ES256 JWT |
| `{{username}}` | User email/username |
| `{{groups}}` | Comma-separated Twingate Group names |
| `{{clientGeoLatLong}}` | Lat/lon |
| `{{clientGeoCity}}` | City |
| `{{clientGeoRegion}}` | Region/state |
| `{{clientGeoCountry}}` | Country code |

**Recommended header config:**
- `Authorization: Bearer {{jwt}}`
- `X-Twingate-User: {{username}}`
- `X-Twingate-Groups: {{groups}}`

**Helm (gateway-wide headers):**
```yaml
gateway:
  webApp:
    enabled: true
    requestHeaders:
      Authorization: "Bearer {{jwt}}"
```

**TwingateResource (per-resource rewrites):**
```yaml
requestHeaderRewrites:
  - name: X-Twingate-User
    value: "{{username}}"
```

**Service annotation (per-resource rewrites):**
```yaml
resource.twingate.com/requestHeaderRewrites: '{"Authorization": "Bearer {{jwt}}"}'
```

## Key JWT Payload Fields
- `user.id`, `user.email`, `user.username`, `user.first_name`, `user.last_name`
- `user.groups` — always includes `twingate:authenticated` and `Everyone`
- `device.id`, `device.location.*`
- `resource.id`, `resource.type` (always `WEB_APP`), `resource.address`, `resource.aliases`
- `exp`, `aud` (tenant network name), `jti`

## Gotchas
- **`typ: GAT` not `JWT`** — Some JWT libraries reject tokens where `typ ≠ "JWT"`. Configure library to accept `GAT` or it will fail signature verification even with a valid token.
- Headers are **opt-in** — without configuration, requests reach your app with no identity headers
- Per-Resource rewrites are applied **after** gateway-wide headers, overriding same-named headers
- `user.groups` always includes built-in groups (`twingate:authenticated`, `Everyone`) plus assigned groups

## Related Docs
- Kubernetes Operator install guide
- Developer guides (Express.js, Django, Next.js, Next.js + Auth.js middleware)
- Application integration guides (Grafana, Jenkins — no-code trusted-header auth)
- Identity Firewall Overview
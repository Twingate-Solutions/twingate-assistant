---
source: https://www.twingate.com/docs/web-app-access
type: docs
fetched: 2026-10-18
source_version: 03d4bb26570929c1504e44a6fca8512e39a10f2cbec7da2979330c41f31190ad
trust: official
---

# Privileged Access for Web Apps Overview

## Page Title
Twingate Privileged Access for Web Apps (Beta)

## Summary
Twingate Privileged Access for Web Apps places internal web applications behind a Twingate Gateway acting as a Layer 7 reverse proxy. The Gateway injects a signed ES256 JWT (Gateway Access Token) into every HTTP request, carrying user identity, device info, and resource metadata. Apps verify the JWT against Twingate's JWKS endpoint—no OIDC integration or client secrets required.

## Key Information
- **Feature status**: Beta — contact Twingate to request access
- **Auth flow**: Controller issues GAT scoped to user+device+resource; Client presents token to Gateway; Gateway injects headers on each forwarded request
- **JWKS endpoint**: `https://<your-tenant>.twingate.com/api/v1/jwk/ec` (unauthenticated, standard JWKS)
- **JWT signing**: ES256 algorithm, `typ` header is `GAT` (not `JWT`)—some libraries reject non-`JWT` types; configure library to accept `GAT`
- **Header sources**: Gateway-wide headers (all web apps on that Gateway) and per-Resource rewrites (single Resource); per-Resource rewrites override Gateway-wide headers of the same name

## Prerequisites
- Twingate account with administrator privileges
- Deployed Twingate Gateway with a Web App Resource configured
- **For HTTPS**: CA registered with Twingate (options: self-signed, HashiCorp Vault, Google Cloud CAS) + user devices trusting that CA (manual or MDM)

## Configuration Values

### Template Variables for Header Injection
| Variable | Description |
|---|---|
| `{{jwt}}` | Full signed ES256 JWT |
| `{{username}}` | User's email/username |
| `{{groups}}` | Comma-separated Twingate Group names |
| `{{clientGeoLatLong}}` | Lat/lon |
| `{{clientGeoCity}}` / `{{clientGeoRegion}}` / `{{clientGeoCountry}}` | Location fields |

### Recommended Header Config
| Header Key | Value Template |
|---|---|
| `Authorization` | `Bearer {{jwt}}` |
| `X-Twingate-User` | `{{username}}` |
| `X-Twingate-Groups` | `{{groups}}` |

### Kubernetes Operator — Gateway-wide headers (Helm values)
```yaml
gateway:
  webApp:
    enabled: true
    requestHeaders:
      Authorization: "Bearer {{jwt}}"
```

### Kubernetes Operator — Per-Resource rewrites (TwingateResource CRD)
```yaml
requestHeaderRewrites:
  - name: X-Twingate-User
    value: "{{username}}"
```

### Service Annotation (JSON string)
```
resource.twingate.com/requestHeaderRewrites: '{"Authorization": "Bearer {{jwt}}"}'
```

## Key JWT Claims
- **`typ`**: `GAT` (not `JWT`)
- **`iss`**: `twingate`
- **`aud`**: tenant slug
- **`user.groups`**: always includes `twingate:authenticated` and `Everyone`; use for authorization
- **`device.id`**: identifies specific device
- **`resource.type`**: always `WEB_APP`

## Gotchas
- JWT `typ` is `GAT`—libraries enforcing `typ: JWT` will reject tokens; must configure to accept `GAT`
- No headers are injected until at least one is explicitly configured
- SaaS apps with their own auth/redirect flows may conflict with the Gateway architecture
- HTTPS requires a registered CA and trusted CA on all user devices

## Related Docs
- Twingate Kubernetes Operator install & user guide
- Developer guides: Express.js, Django, Next.js, Next.js + Auth.js
- Application integration guides: Grafana, Jenkins
- Identity Firewall Overview
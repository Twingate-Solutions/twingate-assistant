---
source: https://www.twingate.com/docs/web-app-access
type: docs
fetched: 2026-08-14
source_version: 67257a2d02ee7284198568f2d3e0c6bdd2f0527f0efbc8b86cc75f315ebde087
---

<!-- triage: unassigned -->

# Twingate Privileged Access for Web Apps

## Summary
Twingate Privileged Access for Web Apps (Beta) acts as a Layer 7 reverse proxy via the Gateway, injecting signed ES256 JWTs into every HTTP request forwarded to internal web apps. Apps verify the JWT against Twingate's JWKS endpoint to get user identity without OIDC integration, client secrets, or redirect flows. Group-based authorization and convenience headers are also injected per-request.

## Key Information
- **Beta feature** — requires contacting Twingate for access
- Gateway issues a Gateway Access Token (GAT) scoped per user/device/resource
- JWT is ES256-signed; verify via JWKS endpoint
- `typ` header is `GAT` (not `JWT`) — some libraries will reject this by default
- Headers are opt-in; no headers injected until configured
- Gateway-wide headers apply to all proxied apps; per-Resource rewrites override same-named gateway-wide headers

## Prerequisites
- Twingate account with administrator privileges
- Deployed Twingate Gateway with a Web App Resource configured
- Beta access granted by Twingate

## How It Works (Request Flow)
1. User navigates to internal web app in browser
2. Twingate Client intercepts and routes to assigned Gateway
3. Client requests Gateway Access Token (GAT) from Controller if none cached
4. Controller authorizes against existing session + Security Policy, issues ES256 JWT
5. Client connects to Gateway, presents token; Gateway verifies
6. Gateway injects configured headers into each HTTP request forwarded upstream
7. App verifies JWT against JWKS endpoint

## Configuration Values

**JWKS Endpoint:**
```
https://<your-tenant>.twingate.com/api/v1/jwk/ec
```

**JWT Header fields:** `alg: ES256`, `typ: GAT`, `kid: <key-id>`

**Key JWT Payload Claims:**

| Claim | Description |
|---|---|
| `user.id` | Stable Twingate user ID |
| `user.email` / `user.username` | User email |
| `user.groups` | Groups authorizing access (always includes `twingate:authenticated`) |
| `device.id` | Device identifier |
| `resource.id` / `resource.type` | Always `WEB_APP` |
| `exp` / `iat` | Expiry / issued-at timestamps |

**Header Template Variables:**

| Variable | Value |
|---|---|
| `{{jwt}}` | Full signed JWT |
| `{{username}}` | User email/username |
| `{{groups}}` | Comma-separated group names |
| `{{clientGeoCountry}}` / `{{clientGeoCity}}` / `{{clientGeoRegion}}` | Location fields |

**Recommended Header Config:**
- `Authorization: Bearer {{jwt}}`
- `X-Twingate-User: {{username}}`
- `X-Twingate-Groups: {{groups}}`

**Kubernetes Operator — Gateway-wide headers (Helm):**
```yaml
gateway:
  webApp:
    enabled: true
    requestHeaders:
      Authorization: "Bearer {{jwt}}"
```

**Kubernetes Operator — Per-Resource rewrites (TwingateResource):**
```yaml
requestHeaderRewrites:
  - name: X-Twingate-User
    value: "{{username}}"
```

**Service annotation (JSON string):**
```
resource.twingate.com/requestHeaderRewrites: '{"Authorization": "Bearer {{jwt}}"}'
```

## Gotchas
- **`typ: GAT` not `JWT`**: Libraries enforcing standard `typ: JWT` will reject tokens — configure library to accept `GAT`
- Headers are **opt-in** — no identity injected until at least one header is configured
- Per-Resource rewrites are applied **after** gateway-wide headers and will override same-named headers
- Always validate `exp` claim; reject expired tokens in middleware

## Related Docs
- Developer guides: Express.js, Django, Next.js, Next.js + Auth.js middleware
- Application integration guides: Grafana, Jenkins (trusted-header auth, no code changes)
- Identity Firewall Overview
- Twingate Kubernetes Operator docs
---
source: https://www.twingate.com/docs/web-app-integrations
type: docs
fetched: 2026-08-23
source_version: 5c38a49e663f0d948540eac1f94d7cd79b48abb340646a270e40d640d98e9453
---

# Web App Integrations for Identity Firewall

## Summary
Configures self-hosted web applications to authenticate users via Twingate Identity Firewall headers without code changes. The Gateway injects user identity into HTTP headers or JWTs that the target app already reads natively. Supports apps like Grafana and Jenkins through their built-in proxy/header auth mechanisms.

## Key Information
- Works with apps that support header-based or JWT-based authentication natively
- No OIDC integration or code modifications required
- Gateway injects identity data using template variables into request headers
- Users auto-provision on first request — no pre-created accounts needed
- Group membership changes take effect on the user's next request

## Prerequisites
- Twingate Identity Firewall enabled
- App published as a **Web App Resource** on the Gateway
- App must support header/JWT authentication natively (e.g., Grafana `auth.jwt`/`auth.proxy`, Jenkins Reverse Proxy Auth plugin)

## Common Pattern (3 Steps)

1. **Configure the app** — Enable header or JWT-based auth in the app's config
2. **Configure the Gateway** — Set headers using template variables
3. **Map Groups to permissions** — Use Twingate Group names as role inputs in the app

## Configuration Values

### Gateway Template Variables
| Variable | Description |
|----------|-------------|
| `{{jwt}}` | Signed JWT containing user identity |
| `{{username}}` | Plaintext username |
| `{{groups}}` | Twingate Group memberships |

### Headers
| Header | Usage |
|--------|-------|
| `Authorization: Bearer <token>` | Gateway Access Token for JWT validation |
| `X-Forwarded-User` | Plaintext username (Jenkins pattern) |

## Security Model
- **Preferred**: Validate the Gateway Access Token (Bearer JWT in `Authorization` header) — cryptographically verifiable
- **Fallback**: Trusted-header auth (plaintext) — only accept if traffic originates from the Gateway; do not expose the app directly to the internet

## Gotchas
- Plaintext header auth is only safe if the app cannot be reached except through the Gateway
- JWT validation is the more secure option but requires app support for token verification
- Guides here are for **apps you cannot modify** — if you own the code, use the Web App Developer Guides instead

## Available Integration Guides
- **Grafana** — `auth.jwt` or `auth.proxy` configuration
- **Jenkins** — Reverse Proxy Auth plugin + Role-Based Strategy, reads `X-Forwarded-User`

## Related Docs
- [Identity Firewall for Web Apps overview](#) — header reference and JWT payload schema
- [Web App Developer Guides](#) — verifying JWT in custom application code
- [Grafana integration guide](#)
- [Jenkins integration guide](#)
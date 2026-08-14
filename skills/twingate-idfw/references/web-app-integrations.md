---
source: https://www.twingate.com/docs/web-app-integrations
type: docs
fetched: 2026-08-14
source_version: 04cf4fb23348b2ccf3844c3843d8d1fd607bb73a5983866d873bd3c2105171c8
---

# Web App Integrations

## Page Title
Web App Integrations (Twingate Identity Firewall)

## Summary
Configure self-hosted web applications to authenticate users via Twingate Identity Firewall headers without modifying application code. The Twingate Gateway injects signed tokens or user fields into headers that apps already read natively. Supports apps like Grafana and Jenkins through their built-in proxy/header auth mechanisms.

## Key Information
- Target use case: Apps you **run but cannot modify** (vs. apps you own/develop)
- Gateway injects identity data into HTTP headers using template variables
- Users are provisioned automatically on first request — no pre-created accounts needed
- Twingate Group changes take effect on the user's next request
- Available template variables: `{{jwt}}`, `{{username}}`, `{{groups}}`

## Prerequisites
- App must be published as a **Web App Resource** on the Twingate Gateway
- App must support header-based or JWT-based authentication natively
- Twingate Groups configured and mapped to app permission roles

## Common Integration Pattern (3 Steps)
1. **Configure the app** — enable built-in header/JWT auth (e.g., `auth.proxy` in Grafana, Reverse Proxy Auth plugin in Jenkins)
2. **Configure the Gateway** — inject headers using template variables (`{{jwt}}`, `{{username}}`, `{{groups}}`)
3. **Map Groups to permissions** — use Twingate Group names as inputs to the app's role/permission system

## Configuration Values

| Template Variable | Description |
|---|---|
| `{{jwt}}` | Signed Gateway Access Token (Bearer token) |
| `{{username}}` | Authenticated user's username |
| `{{groups}}` | User's Twingate Group memberships |

- JWT is sent as Bearer token in the `Authorization` header
- `X-Forwarded-User` is the header used for Jenkins username injection

## Security Model
- **Preferred**: Validate the Twingate Gateway Access Token (JWT) — cryptographically verifiable
- **Fallback**: Trusted-header auth (plaintext) — **must** restrict header acceptance to traffic originating from the Gateway only
- Plain header values with no source restriction are a security risk

## Gotchas
- Trusted-header mode (non-JWT) requires network-level enforcement — app must only accept headers from the Gateway, not arbitrary clients
- JWT validation is not always practical for off-the-shelf apps; use trusted-header only when JWT isn't supported
- If you **own the app code**, use the Web App Developer Guides instead (direct JWT verification)

## Available Integration Guides
- **Grafana**: Uses `auth.jwt` or `auth.proxy` — no plugins required
- **Jenkins**: Uses Reverse Proxy Auth plugin + Role-Based Strategy plugin

## Related Docs
- [Grafana Integration Guide](https://www.twingate.com/docs/grafana)
- [Jenkins Integration Guide](https://www.twingate.com/docs/jenkins)
- [Identity Firewall for Web Apps Overview](https://www.twingate.com/docs/identity-firewall-web-apps) — header reference & JWT payload
- [Web App Developer Guides](https://www.twingate.com/docs/web-app-developer-guides) — JWT verification in custom app code
---
source: https://www.twingate.com/docs/web-app-grafana
type: docs
fetched: 2026-11-13
source_version: c638b04c3ea14a44bd4cff9e4797211db4a8db4baad36af80177aa7b76fd6f69
trust: official
---

# Grafana SSO with Identity Firewall Headers

## Summary
Grafana can authenticate Twingate users through headers injected by the Twingate Gateway. The recommended option is JWT validation (`auth.jwt`). A fallback is trusted-header authentication (`auth.proxy`), for Grafana instances that cannot reach the Twingate JWKS endpoint. In both cases, accounts are auto-provisioned on first request.

## Key Information
- **JWT integration (recommended):** Grafana validates the JWT cryptographically using the Twingate JWKS endpoint. It requires outbound connectivity from Grafana to Twingate.
- **Trusted-header integration (fallback):** Less secure. Use it only if Grafana cannot reach the JWKS endpoint.
- The Gateway overwrites any client-supplied `X-WEBAUTH-USER` on the Twingate path, so a forged header cannot arrive through Twingate.
- Grafana re-evaluates roles at each sign-in, so moving a user between Twingate Groups changes their Grafana role.
- Verified against Grafana 11.4.

## Prerequisites
- Grafana instance you administer, with access to `grafana.ini` or `GF_*` environment variables.
- A Twingate Web App Resource for Grafana, network-isolated so the Gateway is the only path to it.

## Step-by-Step (JWT)
1. Set the `auth.jwt` config (below) via env vars or `grafana.ini`.
2. On the Grafana Web App Resource, add a request header: key `X-JWT-Assertion`, value `{{jwt}}`.
3. Optionally set `role_attribute_path` to map Twingate Groups to Grafana roles.

## Step-by-Step (Trusted Header)
1. Set the `auth.proxy` config (below).
2. On the Web App Resource, add a request header: key `X-WEBAUTH-USER`, value `{{username}}`.

## Configuration Values

**JWT (`[auth.jwt]`):**
```
GF_AUTH_JWT_ENABLED=true
GF_AUTH_JWT_JWK_SET_URL=https://<your-tenant>.twingate.com/api/v1/jwk/ec
GF_AUTH_JWT_HEADER_NAME=X-JWT-Assertion
GF_AUTH_JWT_USERNAME_ATTRIBUTE_PATH=user.username
GF_AUTH_JWT_EMAIL_ATTRIBUTE_PATH=user.email
GF_AUTH_JWT_AUTO_SIGN_UP=true
GF_AUTH_DISABLE_LOGIN_FORM=true
```

**Group-to-role mapping (JMESPath):**
```
GF_AUTH_JWT_ROLE_ATTRIBUTE_PATH="contains(user.groups[*], 'grafana-admin') && 'Admin' || contains(user.groups[*], 'grafana-editor') && 'Editor' || 'Viewer'"
```
Replace the example group names with your own.

**Trusted header (`[auth.proxy]`):**
```
GF_AUTH_PROXY_ENABLED=true
GF_AUTH_PROXY_HEADER_NAME=X-WEBAUTH-USER
GF_AUTH_PROXY_HEADER_PROPERTY=username
GF_AUTH_PROXY_AUTO_SIGN_UP=true
GF_AUTH_PROXY_WHITELIST=<gateway-ip>
GF_AUTH_DISABLE_LOGIN_FORM=true
```

## Gotchas
- **JWT mode needs outbound access** from Grafana to `<your-tenant>.twingate.com` for JWKS.
- **Always set `auth.proxy.whitelist` to the Gateway IP.** Other internal services that can reach Grafana directly could otherwise forge the header.
- Only the Gateway should be allowed to send headers to Grafana in trusted-header mode.
- Without `role_attribute_path`, auto-provisioned users get Grafana's default role.
- `disable_login_form=true` hides local login, so confirm SSO works before enabling it.
- Replace `<your-tenant>` and `<gateway-ip>` placeholders.

## Related Docs
- Privileged Access for Web Apps overview (architecture and all header template variables)
- Web App Integrations (shared trusted-header pattern)
- Jenkins integration guide (another trusted-header example)
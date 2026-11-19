---
source: https://www.twingate.com/docs/web-app-grafana
type: docs
fetched: 2026-11-19
source_version: a1f20f5a0528918307b3e63cb56c32c60db1bdd74ced14d14b612f42d7c8cb08
trust: official
---

# Grafana SSO with Twingate Privileged Access

## Summary
Grafana can authenticate users from Twingate identity by validating a JWT (`auth.jwt`, recommended) or by trusting a header (`auth.proxy`, fallback). The Twingate Gateway injects the identity header on every request to the Grafana Web App Resource. Accounts are auto-provisioned on first request, so no manual user administration is needed in Grafana.

## Key Information
- **JWT integration (recommended):** Grafana validates the JWT cryptographically via the Twingate JWKS endpoint. Requires Grafana to have outbound access to that endpoint.
- **Trusted-header integration (fallback):** Use only if Grafana can't reach the JWKS endpoint. It is less secure because it trusts a header.
- The Gateway overwrites any client-supplied `X-WEBAUTH-USER`, so a forged header can't come through Twingate. Other internal services that reach Grafana directly could still forge it.
- Grafana re-evaluates roles at each sign-in, so moving a user between Twingate Groups changes their Grafana role.

## Prerequisites
- A Grafana instance you administer (verified on Grafana 11.4).
- Admin access to Grafana config (env vars or `grafana.ini`).
- A Twingate Web App Resource for Grafana, network-isolated so the Gateway is the only path to it.

## Step-by-Step (JWT)
1. Set the `auth.jwt` config values below (env vars or `grafana.ini`).
2. On the Grafana Web App Resource, add a request header: key `X-JWT-Assertion`, value `{{jwt}}`.
3. Optionally add `role_attribute_path` to map Twingate Groups to Grafana roles.

## Step-by-Step (Trusted Header)
1. Set the `auth.proxy` config values below.
2. Set `whitelist` to the Gateway IP.
3. On the Web App Resource, add a request header: key `X-WEBAUTH-USER`, value `{{username}}`.

## Configuration Values

**JWT (`[auth.jwt]`)**
```
GF_AUTH_JWT_ENABLED=true
GF_AUTH_JWT_JWK_SET_URL=https://<your-tenant>.twingate.com/api/v1/jwk/ec
GF_AUTH_JWT_HEADER_NAME=X-JWT-Assertion
GF_AUTH_JWT_USERNAME_ATTRIBUTE_PATH=user.username
GF_AUTH_JWT_EMAIL_ATTRIBUTE_PATH=user.email
GF_AUTH_JWT_AUTO_SIGN_UP=true
GF_AUTH_DISABLE_LOGIN_FORM=true
```

**Group-to-role mapping (JMESPath, uses `user.groups` claim)**
```
GF_AUTH_JWT_ROLE_ATTRIBUTE_PATH="contains(user.groups[*], 'grafana-admin') && 'Admin' || contains(user.groups[*], 'grafana-editor') && 'Editor' || 'Viewer'"
```
Replace the group names with your own.

**Trusted header (`[auth.proxy]`)**
```
GF_AUTH_PROXY_ENABLED=true
GF_AUTH_PROXY_HEADER_NAME=X-WEBAUTH-USER
GF_AUTH_PROXY_HEADER_PROPERTY=username
GF_AUTH_PROXY_AUTO_SIGN_UP=true
GF_AUTH_PROXY_WHITELIST=<gateway-ip>
GF_AUTH_DISABLE_LOGIN_FORM=true
```

## Gotchas
- JWT mode fails if Grafana can't make outbound connections to the Twingate JWKS endpoint.
- In trusted-header mode, always pin `whitelist` to the Gateway IP, and make sure only Gateway traffic can send headers to Grafana.
- Without `role_attribute_path`, auto-created users get Grafana's default role.
- `disable_login_form=true` hides the local login form, since auth now comes from Twingate.
- Replace `<your-tenant>` with your Twingate tenant name.

## Related Docs
- Privileged Access for Web Apps overview (architecture and header template variables)
- Web App Integrations (shared trusted-header pattern)
- Jenkins integration guide (another trusted-header example)
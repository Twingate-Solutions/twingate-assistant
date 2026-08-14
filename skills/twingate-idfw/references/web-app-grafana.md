---
source: https://www.twingate.com/docs/web-app-grafana
type: docs
fetched: 2026-08-14
source_version: 44782b20adff20625d50109d8b4141775efa834571a801f31af8fdd3b375cb59
---

# Grafana Integration

## Summary
Adds Twingate user identity to Grafana using either JWT validation (`auth.jwt`) or trusted-header proxy (`auth.proxy`) authentication. JWT method is preferred as it cryptographically validates tokens; trusted-header is a fallback for network-restricted environments.

## Key Information
- Two integration modes: JWT (recommended) and Trusted Header (fallback)
- Twingate Gateway injects identity headers on every request
- Both modes support auto-provisioning—no pre-created Grafana accounts needed
- Verified against Grafana 11.4

## Prerequisites
- Grafana instance with admin config access (env vars or `grafana.ini`)
- Twingate Web App Resource configured for Grafana
- Grafana network-isolated so Gateway is the only ingress path

## Configuration Values

### JWT Auth (Recommended)
| Env Var | Value |
|---|---|
| `GF_AUTH_JWT_ENABLED` | `true` |
| `GF_AUTH_JWT_JWK_SET_URL` | `https://<tenant>.twingate.com/api/v1/jwk/ec` |
| `GF_AUTH_JWT_HEADER_NAME` | `X-JWT-Assertion` |
| `GF_AUTH_JWT_USERNAME_ATTRIBUTE_PATH` | `user.username` |
| `GF_AUTH_JWT_EMAIL_ATTRIBUTE_PATH` | `user.email` |
| `GF_AUTH_JWT_AUTO_SIGN_UP` | `true` |
| `GF_AUTH_DISABLE_LOGIN_FORM` | `true` |

**Gateway Header to inject:**
- Key: `X-JWT-Assertion` → Value: `{{jwt}}`

### Trusted Header Auth (Fallback)
| Env Var | Value |
|---|---|
| `GF_AUTH_PROXY_ENABLED` | `true` |
| `GF_AUTH_PROXY_HEADER_NAME` | `X-WEBAUTH-USER` |
| `GF_AUTH_PROXY_HEADER_PROPERTY` | `username` |
| `GF_AUTH_PROXY_AUTO_SIGN_UP` | `true` |
| `GF_AUTH_DISABLE_LOGIN_FORM` | `true` |

Also set in `grafana.ini`: `whitelist = <gateway-ip>`

**Gateway Header to inject:**
- Key: `X-WEBAUTH-USER` → Value: `{{username}}`

## Step-by-Step

1. Choose integration mode (JWT if Grafana can reach `twingate.com`; trusted-header otherwise)
2. Apply env vars or `grafana.ini` config for chosen mode
3. In Twingate Admin Console, open the Grafana Web App Resource
4. Add the appropriate request header injection (`X-JWT-Assertion`/`{{jwt}}` or `X-WEBAUTH-USER`/`{{username}}`)
5. Restart Grafana; first user access auto-provisions the account

## Gotchas
- **JWT mode requires outbound access**: Grafana must reach `https://<tenant>.twingate.com/api/v1/jwk/ec` for JWKS validation
- **Trusted-header security**: Always set `auth.proxy.whitelist` to Gateway IP—other internal services that can reach Grafana directly could forge the header
- **Gateway overwrites client headers**: Forged `X-WEBAUTH-USER` headers are overwritten by the Gateway, but only for traffic flowing through it
- Disabling the login form (`GF_AUTH_DISABLE_LOGIN_FORM=true`) removes fallback local auth

## Related Docs
- [Identity Firewall for Web Apps overview](https://www.twingate.com/docs/web-app-overview) — full header template variable list
- [Web App Resource configuration](https://www.twingate.com/docs/web-app-resource)
- [Jenkins integration](https://www.twingate.com/docs/web-app-jenkins) — another trusted-header example
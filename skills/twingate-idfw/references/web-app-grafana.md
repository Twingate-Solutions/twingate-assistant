---
source: https://www.twingate.com/docs/web-app-grafana
type: docs
fetched: 2026-08-23
source_version: b76e8f354dc59630c14acf9535942c10098785beb499cf450bdeb8b656c21f1f
---

# Grafana SSO with Twingate Identity Firewall Headers

## Summary
Configure Grafana to authenticate users via Twingate-injected headers using either JWT validation (`auth.jwt`) or trusted-header (`auth.proxy`) methods. JWT method is preferred as it cryptographically validates tokens; trusted-header is a fallback for network-restricted environments.

## Key Information
- Two integration options: JWT Auth (recommended) or Trusted Header (fallback)
- Twingate Gateway injects identity headers on every request to the Grafana Resource
- Both methods support auto-provisioning—no pre-created Grafana accounts needed
- Verified against Grafana 11.4

## Prerequisites
- Grafana instance with admin config access (env vars or `grafana.ini`)
- Grafana configured as a Twingate Web App Resource, network-isolated so Gateway is only ingress path
- Outbound network access from Grafana to `<tenant>.twingate.com` (JWT method only)

## JWT Auth Integration (Recommended)

### Grafana Configuration
```ini
# Environment variables
GF_AUTH_JWT_ENABLED=true
GF_AUTH_JWT_JWK_SET_URL=https://<your-tenant>.twingate.com/api/v1/jwk/ec
GF_AUTH_JWT_HEADER_NAME=X-JWT-Assertion
GF_AUTH_JWT_USERNAME_ATTRIBUTE_PATH=user.username
GF_AUTH_JWT_EMAIL_ATTRIBUTE_PATH=user.email
GF_AUTH_JWT_AUTO_SIGN_UP=true
GF_AUTH_DISABLE_LOGIN_FORM=true
```

### Twingate Gateway Header
| Header Key | Value Template |
|---|---|
| `X-JWT-Assertion` | `{{jwt}}` |

## Trusted Header Integration (Fallback)

### Grafana Configuration
```ini
# Environment variables
GF_AUTH_PROXY_ENABLED=true
GF_AUTH_PROXY_HEADER_NAME=X-WEBAUTH-USER
GF_AUTH_PROXY_HEADER_PROPERTY=username
GF_AUTH_PROXY_AUTO_SIGN_UP=true
GF_AUTH_DISABLE_LOGIN_FORM=true
```

```ini
# grafana.ini equivalent (includes whitelist)
[auth.proxy]
enabled = true
header_name = X-WEBAUTH-USER
header_property = username
auto_sign_up = true
whitelist = <gateway-ip>
```

### Twingate Gateway Header
| Header Key | Value Template |
|---|---|
| `X-WEBAUTH-USER` | `{{username}}` |

## Configuration Values

| Setting | JWT Value | Trusted Header Value | Purpose |
|---|---|---|---|
| Auth header | `X-JWT-Assertion` | `X-WEBAUTH-USER` | Header Grafana reads |
| Token source | `{{jwt}}` | `{{username}}` | Gateway template variable |
| JWKS URL | `https://<tenant>.twingate.com/api/v1/jwk/ec` | N/A | JWT validation endpoint |
| `auto_sign_up` | `true` | `true` | Auto-provision accounts |
| `disable_login_form` | `true` | `true` | Disable local auth |

## Gotchas
- **JWT method requires outbound connectivity** from Grafana to Twingate JWKS endpoint—blocked firewalls require the trusted-header fallback
- **Trusted-header method**: Must set `auth.proxy.whitelist` to Gateway IP; without it, any internal service that can reach Grafana directly can forge the identity header
- Gateway overwrites client-supplied headers on its path, but does NOT protect direct-to-Grafana traffic—network isolation of the Resource is critical
- `disable_login_form=true` removes local login fallback; ensure Twingate auth works before enabling in production

## Related Docs
- [Identity Firewall for Web Apps overview](https://www.twingate.com/docs/web-app-overview) — full header template variable list
- [Web App Integrations](https://www.twingate.com/docs/web-app-integrations) — trusted-header security model
- [Jenkins integration guide](https://www.
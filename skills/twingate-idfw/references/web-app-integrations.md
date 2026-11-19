---
source: https://www.twingate.com/docs/web-app-integrations
type: docs
fetched: 2026-11-19
source_version: 62710287bd1bd75f576064834682941bbcf72f23adf1292ae6e66919e39f2009
trust: official
---

# Web App Integrations for Privileged Access Management

## Summary
Twingate Privileged Access Management (PAM) can act as a proxy that injects a signed JWT or individual identity fields into HTTP headers for self-hosted web apps. Apps that already support header- or JWT-based authentication (e.g., Grafana, Jenkins) can then authenticate and authorize users with no code changes and no OIDC integration. These guides target apps you run but cannot modify.

## Key Information
- Publish the app as a **Web App Resource**; configure the **Gateway** to write headers the app already reads.
- The app handles both authentication and authorization itself.
- Users are provisioned on first request, so there is no need to pre-create accounts.
- Moving a user between Twingate Groups changes their app permissions on their next request.
- Available guides: **Grafana** (`auth.jwt` or `auth.proxy`, no plugins) and **Jenkins** (Reverse Proxy Auth plugin + Role-Based Strategy, reads user from `X-Forwarded-User`, maps Twingate Groups to Jenkins roles).
- If you own the app code, use the Web App Developer Guides to verify the Gateway's signed JWT directly instead.

## Prerequisites
- A self-hosted app that supports JWT or trusted-header authentication.
- Twingate PAM with a Gateway and the app published as a Web App Resource.
- Admin access to the app's auth configuration.

## Step-by-Step (Common Pattern)
1. **Configure the app** to read identity (and Groups, if supported) from named headers or a signed JWT.
2. **Configure the Gateway** to inject those headers using template variables.
3. **Map Groups to permissions** in the app, using Twingate Group names as input.

## Configuration Values
Gateway header template variables:
- `{{jwt}}`: signed token
- `{{username}}`: user identity
- `{{groups}}`: Twingate Groups

Other values:
- `Authorization: Bearer <Gateway Access Token>`: preferred for validation
- `X-Forwarded-User`: used by the Jenkins guide
- Grafana: `auth.jwt` / `auth.proxy` settings

## Gotchas
- **Prefer JWT validation** (Bearer token in `Authorization`) because the app can cryptographically verify identity.
- Trusted-header values are plaintext. Ensure the app **only accepts these headers from traffic originating at the Gateway**; otherwise they can be spoofed.
- Group-to-role mapping depends on the exact Twingate Group names.

## Related Docs
- Grafana integration guide
- Jenkins integration guide
- Privileged Access for Web Apps overview (header reference, JWT payload)
- Web App Developer Guides (verify JWT in your own code)
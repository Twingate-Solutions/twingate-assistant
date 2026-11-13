---
source: https://www.twingate.com/docs/web-app-integrations
type: docs
fetched: 2026-11-13
source_version: e41a409912a656d5db36e8315e7decdc4b6506abdf4537bd3ecd59f2f0800b8e
trust: official
---

# Web App Integrations for Identity Firewall

## Summary
Twingate Identity Firewall (the Gateway) can inject a signed JWT or individual identity fields into HTTP headers for self-hosted web apps that already support header-based or JWT authentication. This lets you integrate apps you can't modify, with no code changes and no OIDC setup. The app handles authentication and authorization itself, using Twingate Groups as input.

## Key Information
- Applies to apps you run but cannot modify. If you own the code, use the Web App Developer Guides to verify the Gateway's signed JWT directly.
- Publish the app as a **Web App Resource**, then configure the Gateway to write headers the app already reads.
- Available guides:
  - **Grafana**: uses built-in `auth.jwt` or `auth.proxy`; no plugins or code.
  - **Jenkins**: uses the Reverse Proxy Auth plugin plus Role-Based Strategy; reads user from `X-Forwarded-User` and maps Twingate Groups to Jenkins roles.
- Users are provisioned on first request, so there's no need to pre-create accounts.
- Changing a user's Twingate Group membership changes their app permissions on their next request.

## Prerequisites
- A self-hosted app that supports JWT or trusted-header authentication.
- The app published as a Web App Resource behind the Twingate Gateway.

## Step-by-Step (Common Pattern)
1. **Configure the app** to read identity (and Groups, if supported) from named headers or a signed JWT.
2. **Configure the Gateway** to inject headers using template variables.
3. **Map Groups to permissions** in the app, using Twingate Group names as the input.

## Configuration Values
Gateway header template variables:
- `{{jwt}}`: the signed token
- `{{username}}`: user identity
- `{{groups}}`: Twingate Groups

Header/config references:
- `Authorization: Bearer <token>`: Gateway Access Token (preferred)
- `X-Forwarded-User`: used by the Jenkins integration
- Grafana: `auth.jwt`, `auth.proxy`

## Gotchas
- **Prefer JWT validation** (Bearer token in the `Authorization` header) because the app can cryptographically verify identity.
- Trusted-header authentication is a fallback only. Header values are plaintext, so ensure the app accepts these headers **only from traffic originating at the Gateway**. Otherwise they can be spoofed.
- Group-to-role mapping uses Twingate Group names, so names must match what the app expects.

## Related Docs
- Grafana integration guide
- Jenkins integration guide
- Privileged Access for Web Apps overview (full header reference and JWT payload)
- Web App Developer Guides (verifying the JWT in your own code)
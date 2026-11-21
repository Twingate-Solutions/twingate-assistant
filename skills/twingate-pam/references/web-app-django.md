---
source: https://www.twingate.com/docs/web-app-django
type: docs
fetched: 2026-11-19
source_version: 65a99dfbec2b877849fa0c62eb9fa2aa015ac6a60f85d03663f543647756745c
trust: official
---

# Django JWT Middleware (Twingate Privileged Access for Web Apps)

## Summary
Shows how to verify Twingate Privileged Access Management JWTs in a Django app using PyJWT. A custom middleware validates the Gateway-injected Bearer token, attaches claims to `request.gat`, and logs the user into Django's session.

## Key Information
- The Gateway injects no headers by default. You must configure a request header on the Web App Resource.
- Verification uses ES256 with keys fetched from the tenant JWKS endpoint (cached 24h, 5s timeout).
- `TwingateVerifier.verify()` flow:
  1. Decode unverified to read `iss` and `aud`.
  2. Reject if the issuer isn't `twingate` or the audience isn't allowed.
  3. Read `kid` from the header and fetch the signing key.
  4. Re-decode with full signature, issuer, audience and `exp` validation.
- Missing, malformed or invalid tokens fall through to the next middleware (the failure is logged), so it can coexist with other auth and public routes.
- On success, the middleware:
  - sets `request.gat` to the decoded claims;
  - calls `get_or_create` for a Django user keyed on `gat["user"]["username"]` (defaults: email, first_name, last_name);
  - logs out a different logged-in user first;
  - skips login if the same user is already authenticated.
- Group names are in `gat["user"]["groups"]`, used for authorization in views (return 401 if `request.gat` is None, 403 if the group is missing).

## Prerequisites
- Python 3.8+
- A Django project
- A Web App Resource with the Gateway configured to inject the JWT

## Step-by-Step
1. On the Web App Resource, add the request header: key `Authorization`, value `Bearer {{jwt}}`.
2. Install: `pip install pyjwt[crypto]` (the `crypto` extra provides `cryptography` for signature verification).
3. Create `twingate_middleware.py` in your app directory, with a `TwingateMiddleware` class and a `TwingateVerifier` class (the full code is on the source page).
4. Register in `settings.py` `MIDDLEWARE`, after `SessionMiddleware` and `AuthenticationMiddleware`:
   `"yourapp.twingate_middleware.TwingateMiddleware"`
5. In views, read `getattr(request, "gat", None)` and check `gat["user"]["groups"]` as needed.

## Configuration Values
| Setting | Value |
|---|---|
| `TWINGATE_JWKS_URL` | `https://<your-tenant>.twingate.com/api/v1/jwk/ec` (constant in `twingate_middleware.py`) |
| `AUDIENCE` | Your Twingate network name; must match the token's `aud` claim |
| `allowed_issuers` | `["twingate"]` |
| Algorithm | `ES256` |
| JWKS cache lifespan | 24 hours |
| JWKS timeout | 5 seconds |

## Gotchas
- Middleware order matters. It must come after the session and auth middleware, because it uses `request.user`, `login()` and `logout()`.
- Replace both `<your-tenant>` placeholders (JWKS URL and `AUDIENCE`).
- The header name and format are configurable at the Gateway/Resource level. The code assumes `Authorization: Bearer`, so change the middleware if you use a different header.
- Invalid tokens are not rejected by the middleware itself. Views must enforce access by checking `request.gat`.
- The middleware auto-provisions Django users on first sight.

## Related Docs
- Privileged Access for Web Apps overview
- JWT Payload Reference
- Request Headers (header options and template variables)
- Express.js, Next.js, and Next.js + Auth.js guides
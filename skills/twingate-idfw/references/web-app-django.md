---
source: https://www.twingate.com/docs/web-app-django
type: docs
fetched: 2026-11-13
source_version: 7a3765f63ba66e376190d68497c83943939ec8efed434cd9faeaf12e339df547
trust: official
---

# Django JWT Middleware for Identity Firewall

## Summary
Guide to verifying Twingate Identity Firewall JWTs in a Django app using PyJWT. A custom middleware validates the signed JWT injected by the Twingate Gateway, logs the user into a Django session, and exposes claims on `request.gat`.

## Key Information
- The Gateway injects **no headers by default**. You must configure a request header on the Web App Resource.
- Recommended header: key `Authorization`, value template `Bearer {{jwt}}`. Header name and format are configurable at the Gateway/Resource level.
- Verification uses **ES256** with keys from the tenant JWKS endpoint.
- `TwingateVerifier.verify()` flow:
  1. Decode unverified to read `iss` and `aud`.
  2. Reject if the issuer is not in the allowed list (`twingate`) or the audience is not allowed.
  3. Read `kid` from the header and fetch the signing key via `PyJWKClient`.
  4. Re-decode with full signature, issuer, audience, and `exp` validation.
- `PyJWKClient` caches the JWK set for 24 hours (timeout 5s).
- Missing, malformed, or invalid tokens pass through to the next middleware (the failure is logged as a warning), so it can coexist with other auth and public routes.
- On a valid token: claims are attached to `request.gat`, and a Django user is created via `get_or_create` (username, email, first_name, last_name). If a different user is logged in, they are logged out first. If the same user is logged in, the request passes straight through.
- Views read identity from `request.gat["user"]` (`username`, `groups`, etc.). Group authorization checks `gat["user"]["groups"]`.

## Prerequisites
- Python 3.8+
- A Django project
- Web App Resource with the request header configured

## Step-by-Step
1. On the Web App Resource, add header `Authorization` = `Bearer {{jwt}}`.
2. Install: `pip install pyjwt[crypto]` (the `[crypto]` extra installs `cryptography`, required for signature verification).
3. Create `twingate_middleware.py` in your Django app with `TwingateMiddleware` and `TwingateVerifier` classes (see the source page for the full code).
4. Register in `settings.py` `MIDDLEWARE`, after `SessionMiddleware` and `AuthenticationMiddleware`:
   `"yourapp.twingate_middleware.TwingateMiddleware"`
5. In views, use `getattr(request, "gat", None)`. Return 401 if `None`, and 403 if the required group is missing.

## Configuration Values
Constants at the top of `twingate_middleware.py`:
- `TWINGATE_JWKS_URL` = `https://<your-tenant>.twingate.com/api/v1/jwk/ec`
- `AUDIENCE` = your Twingate network name (tenant); must match the token's `aud` claim
- `allowed_issuers` = `["twingate"]`

## Gotchas
- Middleware order matters: it must come after the session and auth middleware because it uses `request.user`, `login()`, and `logout()`.
- The middleware does not reject unauthenticated requests. Views must check `request.gat` (or use other auth enforcement) themselves.
- Replace both `<your-tenant>` placeholders (JWKS URL and audience).
- The auto-provisioned Django user is created with defaults only on first sight. Later changes to email or name in Twingate are not synced.
- Group names are case-sensitive strings in `gat["user"]["groups"]`.

## Related Docs
- Identity Firewall for Web Apps overview (architecture and JWT reference)
- JWT Payload Reference
- Request Headers (header options and template variables)
- Express.js, Next.js, and Next.js + Auth.js guides
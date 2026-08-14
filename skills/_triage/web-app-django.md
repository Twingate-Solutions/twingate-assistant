---
source: https://www.twingate.com/docs/web-app-django
type: docs
fetched: 2026-08-14
source_version: 171a5bb573f41b15099f0a1073c706e26bc58e97e0ea50e609726ad86489f328
---

<!-- triage: unassigned -->

# Django Middleware for Twingate Identity Firewall JWTs

## Summary
Verifies Twingate Identity Firewall JWTs in Django using PyJWT. The middleware extracts Bearer tokens from the Authorization header, validates signatures via JWKS, and provisions/manages Django session users automatically.

## Key Information
- JWT algorithm: ES256
- JWKS keys cached for 24 hours to avoid per-request fetches
- Middleware passes through requests without valid tokens (doesn't block)
- Attaches decoded claims to `request.gat` for use in views
- Provisions Django users via `get_or_create` on first login
- Groups available at `gat["user"]["groups"]` for authorization

## Prerequisites
- Python 3.8+
- Django project with sessions and auth middleware enabled
- `pip install pyjwt[crypto]`
- Twingate Gateway configured to inject JWT header on Web App Resource

## Step-by-Step

1. **Configure Gateway header injection** on the Web App Resource:
   - Header Key: `Authorization`
   - Value Template: `Bearer {{jwt}}`

2. **Install dependency**: `pip install pyjwt[crypto]`

3. **Create `twingate_middleware.py`** in your Django app with `TwingateMiddleware` and `TwingateVerifier` classes

4. **Register in `settings.py`** after `SessionMiddleware` and `AuthenticationMiddleware`:
   ```python
   MIDDLEWARE = [
       "django.contrib.sessions.middleware.SessionMiddleware",
       "django.contrib.auth.middleware.AuthenticationMiddleware",
       "yourapp.twingate_middleware.TwingateMiddleware",
   ]
   ```

## Configuration Values

| Setting | Value |
|---|---|
| `TWINGATE_JWKS_URL` | `https://<your-tenant>.twingate.com/api/v1/jwk/ec` |
| `AUDIENCE` | Your Twingate network name (must match token `aud` claim) |
| `allowed_issuers` | `["twingate"]` |
| JWT algorithm | `ES256` |
| JWKS cache lifespan | 24 hours |
| JWKS fetch timeout | 5 seconds |

## Gotchas
- `TwingateMiddleware` **must** run after `SessionMiddleware` and `AuthenticationMiddleware`—it calls `login()`/`logout()` which depend on both
- The `[crypto]` extra for PyJWT is required; plain `pip install pyjwt` won't work for signature verification
- Middleware is **non-blocking**: invalid/missing tokens fall through to next middleware, not a 401 response—views must check `request.gat` themselves
- Two-pass JWT decode: first without signature to check `iss`/`aud`, then with full verification—prevents fetching JWKS for untrusted tokens
- `get_or_create` only sets `email`/`first_name`/`last_name` on creation, not on subsequent logins

## Related Docs
- Identity Firewall for Web Apps overview
- JWT Payload Reference (full token structure)
- Request Headers (Gateway injection options and template variables)
- Framework guides: Express.js, Next.js, Next.js + Auth.js
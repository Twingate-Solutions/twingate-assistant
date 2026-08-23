---
source: https://www.twingate.com/docs/web-app-django
type: docs
fetched: 2026-08-23
source_version: acc7242479398a67c6a121d13480a16a914065bba9c2df34d4f8b12a499c0ad0
---

# Django JWT Middleware for Twingate Identity Firewall

## Summary
Verifies Twingate Identity Firewall JWTs in Django applications using PyJWT. The middleware validates tokens injected by the Twingate Gateway, provisions Django users automatically, and attaches decoded claims to `request.gat` for use in views.

## Key Information
- Uses EC256 (ES256) signature verification via JWKS endpoint
- JWKS keys cached for 24 hours to avoid per-request fetches
- Middleware is non-blocking: invalid/missing tokens pass through to other auth middleware
- Auto-provisions Django users via `get_or_create` on first login
- Attaches decoded JWT claims to `request.gat`
- Twingate groups available at `gat["user"]["groups"]`

## Prerequisites
- Python 3.8+
- Django project with sessions and auth middleware configured
- `pip install pyjwt[crypto]` (requires `cryptography` package)
- Twingate Gateway configured to inject JWT header on the Web App Resource

## Step-by-Step

1. **Configure Gateway header injection** on the Web App Resource:
   - Header Key: `Authorization`
   - Value Template: `Bearer {{jwt}}`

2. **Install dependency**: `pip install pyjwt[crypto]`

3. **Create `twingate_middleware.py`** in your Django app with `TwingateMiddleware` and `TwingateVerifier` classes

4. **Register middleware** in `settings.py` — must appear after `SessionMiddleware` and `AuthenticationMiddleware`

5. **Access identity in views** via `request.gat`

## Configuration Values

| Setting | Value |
|---|---|
| `TWINGATE_JWKS_URL` | `https://<your-tenant>.twingate.com/api/v1/jwk/ec` |
| `AUDIENCE` | `<your-tenant>` (must match token `aud` claim) |
| Allowed issuer | `"twingate"` |
| Algorithm | `ES256` |
| JWKS cache lifespan | 24 hours |
| JWKS fetch timeout | 5 seconds |

**Required `settings.py` middleware order:**
```python
MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "yourapp.twingate_middleware.TwingateMiddleware",  # must be after both above
]
```

## Gotchas
- `TwingateMiddleware` **must** come after `SessionMiddleware` and `AuthenticationMiddleware` — it calls `login()`/`logout()` which depend on both
- If a different user is already authenticated, the middleware forces logout before logging in the JWT user
- Token verification decodes twice: once without signature to check `iss`/`aud` allow-lists, then fully with signature — both checks must pass
- Missing `kid` in token header raises `InvalidTokenError`
- `exp` claim validated automatically by PyJWT
- Gateway injects **no headers by default** — must explicitly configure header injection on the Resource

## Related Docs
- [Identity Firewall for Web Apps overview](#) — architecture and full JWT reference
- [JWT Payload Reference](#) — full token structure and claims
- [Request Headers](#) — configuring Gateway header injection options
- Other framework guides: Express.js, Next.js, Next.js + Auth.js
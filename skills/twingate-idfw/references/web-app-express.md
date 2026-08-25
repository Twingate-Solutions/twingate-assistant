---
source: https://www.twingate.com/docs/web-app-express
type: docs
fetched: 2026-08-23
source_version: 64643837049ef656a252d9cea9d31eb85106e564d9a366774f3c1a7f8172e144
---

# Express.js JWT Middleware for Twingate Identity Firewall

## Summary
Verifies Twingate Identity Firewall JWTs in Express.js using the `jose` library. The Gateway injects a signed JWT into request headers; this middleware validates the token and attaches the payload to `req.twingateIdentity` for use in route handlers.

## Key Information
- Uses ES256 algorithm with remote JWKS for signature verification
- `jose` handles JWKS caching and key rotation automatically
- Missing `Authorization` header sets `req.twingateIdentity = null` (allows public routes/health checks)
- Invalid/malformed tokens return HTTP 401 JSON response
- JWT payload contains `user`, `device`, `resource`, and `user.groups` fields

## Prerequisites
- Node.js (LTS)
- Express.js application
- Twingate Gateway configured to inject JWT header on the Web App Resource

## Step-by-Step

1. **Configure Gateway header injection** on the Web App Resource:
   - Header Key: `Authorization`
   - Value Template: `Bearer {{jwt}}`

2. **Install dependency:**
   ```bash
   npm install jose
   ```

3. **Create `twingate-middleware.js`** with `twingateAuth(jwksUrl)` factory function

4. **Wire up middleware:**
   ```js
   app.use(twingateAuth(process.env.TWINGATE_JWKS_URL));
   ```

## Configuration Values

| Variable | Value |
|---|---|
| `TWINGATE_JWKS_URL` | `https://<your-tenant>.twingate.com/api/v1/jwk/ec` |

**JWT verification settings (hardcoded in middleware):**
- `algorithms`: `["ES256"]`
- `requiredClaims`: `["exp", "iat"]`
- `clockTolerance`: `"30s"`

## Key Code Pattern

```js
import { createRemoteJWKSet, jwtVerify } from "jose";

export function twingateAuth(jwksUrl) {
  const jwks = createRemoteJWKSet(new URL(jwksUrl));
  return async (req, res, next) => {
    // Parse Bearer token, verify, attach payload to req.twingateIdentity
  };
}
```

**Group-based authorization:**
```js
const { groups } = req.twingateIdentity.user;
if (!groups.includes("admin")) return res.status(403).json({ error: "Forbidden" });
```

## Gotchas
- Gateway injects **no headers by default** — must explicitly configure header injection on the Resource
- Header name/format are configurable; middleware assumes `Authorization: Bearer <token>` scheme
- `twingateIdentity` is `null` (not absent) when no `Authorization` header present — always null-check before accessing payload fields
- JWKS URL must use your specific tenant subdomain

## Related Docs
- [Identity Firewall for Web Apps overview](#) — architecture and full JWT payload reference
- [Request Headers](#) — Gateway header injection options and template variables
- Django, Next.js, Next.js + Auth.js framework guides
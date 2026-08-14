---
source: https://www.twingate.com/docs/web-app-express
type: docs
fetched: 2026-08-14
source_version: 40b8fd91ce34624dcece89ccff3edf759af22d56117d7ae0439996808497717a
---

<!-- triage: unassigned -->

# Express.js Middleware for Twingate Identity Firewall JWTs

## Summary
Verifies Twingate Identity Firewall JWTs in Express.js using the `jose` library. The Gateway injects a signed JWT into request headers; this middleware fetches the JWKS, validates the token, and attaches the payload to `req.twingateIdentity`.

## Key Information
- JWT algorithm: **ES256**
- Required claims: `exp`, `iat`
- Clock tolerance: 30 seconds
- JWKS auto-cached and key rotation handled by `jose`
- Missing `Authorization` header sets `req.twingateIdentity = null` and calls `next()` (allows public routes/health checks)
- Invalid/malformed token returns `401 JSON`

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

3. **Create `twingate-middleware.js`:**
   ```js
   import { createRemoteJWKSet, jwtVerify } from "jose";
   
   export function twingateAuth(jwksUrl) {
     const jwks = createRemoteJWKSet(new URL(jwksUrl));
     return async (req, res, next) => {
       const auth = req.headers.authorization ?? "";
       if (!auth) { req.twingateIdentity = null; return next(); }
       const parts = auth.split(" ");
       if (parts.length !== 2 || parts[0].toLowerCase() !== "bearer")
         return res.status(401).json({ error: "Malformed Authorization header" });
       try {
         const { payload } = await jwtVerify(parts[1], jwks, {
           algorithms: ["ES256"],
           requiredClaims: ["exp", "iat"],
           clockTolerance: "30s",
         });
         req.twingateIdentity = payload;
         return next();
       } catch {
         return res.status(401).json({ error: "Invalid token" });
       }
     };
   }
   ```

4. **Register middleware:**
   ```js
   app.use(twingateAuth(process.env.TWINGATE_JWKS_URL));
   ```

## Configuration Values

| Variable | Value |
|---|---|
| `TWINGATE_JWKS_URL` | `https://<your-tenant>.twingate.com/api/v1/jwk/ec` |
| Gateway Header Key | `Authorization` |
| Gateway Value Template | `Bearer {{jwt}}` |

## Usage Patterns

**Read identity:**
```js
const { user, device, resource } = req.twingateIdentity;
```

**Group-based authorization:**
```js
if (!req.twingateIdentity?.user.groups.includes("admin"))
  return res.status(403).json({ error: "Forbidden" });
```

## Gotchas
- Gateway injects **no headers by default** — must explicitly configure the header on the Web App Resource
- Header name/format are configurable; this guide assumes standard `Authorization: Bearer` scheme
- Missing header results in `null` identity (not a 401) — routes must explicitly check `req.twingateIdentity`
- `createRemoteJWKSet` must be called **once at init**, not per-request

## Related Docs
- Identity Firewall for Web Apps overview
- JWT Payload Reference
- Request Headers (Gateway injection options)
- Framework guides: Django, Next.js, Next.js + Auth.js
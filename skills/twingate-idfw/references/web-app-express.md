---
source: https://www.twingate.com/docs/web-app-express
type: docs
fetched: 2026-11-19
source_version: f3efcf01bbe19bdd35ca379ab577744a08f4e34a0c54083c8ea1a7ba088fa664
trust: official
---

# Express.js JWT Middleware (Twingate Privileged Access for Web Apps)

## Summary
Shows how to verify Twingate Privileged Access Management JWTs in an Express.js app using the `jose` library. The Gateway injects a signed JWT into requests. The middleware validates it against the tenant's JWKS endpoint and exposes the identity on `req.twingateIdentity`.

## Key Information
- The Gateway injects **no headers by default**. You must add a request header on the Web App Resource.
- Recommended convention: `Authorization: Bearer {{jwt}}` (header name and format are configurable at the Gateway/Resource level).
- `jose` runs in Node.js, Deno, and edge runtimes.
- `createRemoteJWKSet` fetches and caches the Gateway public keys and handles rotation. Create it once, at middleware initialization.
- With no `Authorization` header, the middleware sets `req.twingateIdentity = null` and calls `next()`, so health checks and public routes still work. Routes that need identity must check for null themselves.
- A malformed header (not `Bearer <token>`) returns 401 `Malformed Authorization header`. A failed verification returns 401 `Invalid token`.
- On success, the full JWT payload is attached to `req.twingateIdentity`. It includes `user` (with `groups`), `device`, and `resource`.

## Prerequisites
- Node.js (LTS recommended)
- An Express.js application
- A Web App Resource with the request header configured

## Step-by-Step
1. On the Web App Resource, add the request header: key `Authorization`, value `Bearer {{jwt}}`.
2. Install the dependency: `npm install jose`
3. Create `twingate-middleware.js` exporting `twingateAuth(jwksUrl, audience)`. It:
   - builds the remote JWKS with `createRemoteJWKSet(new URL(jwksUrl))`
   - reads and parses the Bearer token
   - calls `jwtVerify(token, jwks, {...})` with the options below
   - sets `req.twingateIdentity` to the payload
4. Register it: `app.use(twingateAuth(process.env.TWINGATE_JWKS_URL, process.env.TWINGATE_AUDIENCE));`
5. Use the identity in routes:
   - `/me`: return 401 if `req.twingateIdentity` is null, otherwise return `{ user, device, resource }`.
   - `/admin`: return 401 if null, then 403 unless `req.twingateIdentity.user.groups.includes("admin")`.

## Configuration Values
| Variable | Description |
|---|---|
| `TWINGATE_JWKS_URL` | `https://<your-tenant>.twingate.com/api/v1/jwk/ec` |
| `TWINGATE_AUDIENCE` | Twingate network name, which must match the `aud` claim (e.g. `autoco` for `https://autoco.twingate.com`) |

`jwtVerify` options used:
- `algorithms: ["ES256"]`
- `issuer: "twingate"`
- `audience`: your network name
- `requiredClaims: ["exp", "iat"]`
- `clockTolerance: "30s"`

## Gotchas
- Without the Resource header configured, no JWT arrives and every request is treated as unauthenticated (`null` identity).
- The middleware lets unauthenticated requests through. Protected routes must explicitly reject a null identity.
- The audience is the network name only, not the full URL.
- The code uses ES module syntax (`import`/`export`), so the project needs ESM enabled.
- If you change the header name or format on the Gateway, update the parsing logic in the middleware to match.

## Related Docs
- Privileged Access for Web Apps overview
- JWT Payload Reference
- Request Headers (header options and template variables)
- Django, Next.js, and Next.js + Auth.js guides
---
source: https://www.twingate.com/docs/web-app-express
type: docs
fetched: 2026-11-13
source_version: fe71b98bafcca387785cdcee618229ba5b981a9e40434b09a3c5eecb9fef9307
trust: official
---

# Express.js JWT Middleware for Identity Firewall

## Summary
Guide for verifying Twingate Identity Firewall JWTs in an Express.js app using the `jose` library. The Gateway injects a signed JWT into a request header. Express middleware verifies it against the tenant's JWKS endpoint and exposes the identity on `req.twingateIdentity`.

## Key Information
- The Gateway injects **no headers by default**. You must add a request header on the Web App Resource.
- Recommended convention: `Authorization: Bearer {{jwt}}`. Header name and format are configurable at the Gateway/Resource level.
- `jose` runs in Node.js, Deno, and edge runtimes.
- `createRemoteJWKSet` fetches and caches the Gateway's public keys, and handles key rotation. Create it once at middleware init.
- With no `Authorization` header, the middleware sets `req.twingateIdentity = null` and calls `next()`, so health checks and public routes still work. Protected routes must check for null themselves.
- Verification settings: algorithm `ES256`, issuer `twingate`, audience = network name, required claims `exp` and `iat`, clock tolerance `30s`.
- On success the full payload is attached to `req.twingateIdentity` (includes `user`, `device`, `resource`; `user.groups`).
- On failure the middleware returns 401 JSON (`Malformed Authorization header` or `Invalid token`).

## Prerequisites
- Node.js (LTS recommended)
- An Express.js app
- Web App Resource configured with the JWT request header

## Step-by-Step
1. On the Web App Resource, add header key `Authorization` with value template `Bearer {{jwt}}`.
2. Install: `npm install jose`
3. Create `twingate-middleware.js` exporting `twingateAuth(jwksUrl, audience)`. It should:
   - build the JWKS with `createRemoteJWKSet(new URL(jwksUrl))`
   - return an async middleware that reads `req.headers.authorization`
   - set `twingateIdentity = null` if the header is absent
   - return 401 unless the header is exactly `Bearer <token>`
   - call `jwtVerify(token, jwks, { algorithms: ["ES256"], issuer: "twingate", audience, requiredClaims: ["exp","iat"], clockTolerance: "30s" })`
   - set `req.twingateIdentity = payload` and call `next()`, or return 401 on error
4. Wire it up: `app.use(twingateAuth(process.env.TWINGATE_JWKS_URL, process.env.TWINGATE_AUDIENCE));`
5. Use identity in routes:
   - `/me`: return 401 if `req.twingateIdentity` is null, else return `{ user, device, resource }`.
   - `/admin`: return 401 if null, 403 if `!req.twingateIdentity.user.groups.includes("admin")`.

## Configuration Values
| Variable | Description |
|---|---|
| `TWINGATE_JWKS_URL` | `https://<your-tenant>.twingate.com/api/v1/jwk/ec` |
| `TWINGATE_AUDIENCE` | Network name, must match the `aud` claim (e.g. `autoco` for `https://autoco.twingate.com`) |

## Gotchas
- A missing header is allowed through, so every protected route must reject a null identity.
- If you change the header name or format on the Gateway, update the middleware parsing to match.
- The audience is the network name, not the full URL.
- Only ES256 is accepted, and the JWKS path ends in `/jwk/ec`.
- Group names are compared as exact strings (`"admin"` in the example).

## Related Docs
- Identity Firewall for Web Apps overview
- JWT Payload Reference
- Request Headers (template variables and options)
- Django, Next.js, and Next.js + Auth.js guides
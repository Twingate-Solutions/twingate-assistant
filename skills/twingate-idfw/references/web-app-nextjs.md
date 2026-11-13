---
source: https://www.twingate.com/docs/web-app-nextjs
type: docs
fetched: 2026-11-13
source_version: 2d99d2c5c0ebbe1acaaf29d81c7577ac98d7bdbc397e435d696b36d34d504a5f
trust: official
---

# Next.js JWT Middleware for Identity Firewall

## Summary
Shows how to verify Twingate Identity Firewall JWTs in a Next.js app using the `jose` library. A thin Edge Middleware gates chosen routes (returns 401 on failure), and a shared helper verifies the JWT wherever user identity is needed (route handlers, Server Components).

## Key Information
- The Gateway injects **no headers by default**. You must configure a request header on the Web App Resource.
- Recommended convention: `Authorization: Bearer {{jwt}}`. The header name and format are configurable. If you change them, update the helper.
- `jose` runs in the Edge Runtime, as Next.js middleware requires.
- Middleware only gates (401 or `NextResponse.next()`). It does **not** forward identity downstream. Handlers and Server Components re-verify with the same helper. This is cheap because `createRemoteJWKSet` caches the JWKS.
- Verification settings: algorithm `ES256`, issuer `twingate`, audience = `TWINGATE_AUDIENCE`, required claims `exp` and `iat`, clock tolerance `30s`. The helper returns the identity or `null` on any failure.
- Identity shape: `user {id, username, email?, groups[]}`, `device? {id}`, `resource? {id, type, address, aliases[]}`.

## Prerequisites
- Next.js 14+ with App Router
- A Twingate Web App Resource with the request header configured
- `npm install jose`

## Step-by-Step
1. On the Web App Resource, add a header: key `Authorization`, value `Bearer {{jwt}}`.
2. Run `npm install jose`.
3. Create `src/twingate.ts` exporting `verifyTwingateJWT(authHeader)`. It parses the Bearer header, then calls `jwtVerify` with `createRemoteJWKSet(new URL(process.env.TWINGATE_JWKS_URL!))`.
4. Create `src/middleware.ts` (or `middleware.ts` at the project root). It calls the helper with `request.headers.get("authorization")` and returns `NextResponse.json({error:"Unauthorized"},{status:401})` if the result is null.
5. Set `config.matcher` (default example: `["/api/:path*"]`).
6. In route handlers, call the helper with the `authorization` header. In Server Components, use `await headers()` from `next/headers`.
7. For group authorization, check `identity.user.groups.includes("engineering")` and return 403 if absent.

## Configuration Values
Add to `.env.local`:
- `TWINGATE_JWKS_URL`: `https://<your-tenant>.twingate.com/api/v1/jwk/ec`
- `TWINGATE_AUDIENCE`: Twingate network name, which must match the `aud` claim (e.g. `autoco` for `https://autoco.twingate.com`)

Matcher options:
- Allowlist: `["/api/:path*", "/dashboard/:path*"]`
- Gate everything except public paths: `["/((?!health|_next/static|_next/image|favicon.ico).*)"]`
- Or branch on `request.nextUrl.pathname` inside the middleware and return early for public routes.

## Gotchas
- If you use a header other than `Authorization`/Bearer, the helper and the `headers.get(...)` calls must be changed to match.
- Routes outside `config.matcher` are not gated, but you can still verify the JWT in any handler.
- `TWINGATE_AUDIENCE` is the network name, not the full URL.
- Don't rely on middleware to pass identity along. Re-verify in each place.
- This approach is not session-based. For `useSession()`/`auth()` or session persistence, use the Auth.js guide.

## Related Docs
- Identity Firewall for Web Apps overview
- Next.js + Auth.js guide
- JWT Payload Reference
- Request Headers
- Express.js and Django guides
---
source: https://www.twingate.com/docs/web-app-nextjs
type: docs
fetched: 2026-11-19
source_version: 0c7a3149c093f5e036a8e3d9e5c10e658dbd90a3b986ae8f5d481a1fea93a9a7
trust: official
---

# Next.js JWT Middleware

## Summary
Guide to verifying Twingate Privileged Access Management JWTs in Next.js (App Router) using the `jose` library. A thin Edge Middleware gates chosen routes with a 401, while a shared helper (`verifyTwingateJWT`) re-verifies the JWT in route handlers and Server Components to read user identity.

## Key Information
- The Gateway injects no headers by default; you must configure a request header on the Web App Resource.
- Recommended convention: `Authorization: Bearer {{jwt}}`. If you use a different header, change the helper to read that header.
- `jose` runs in the Edge Runtime, as required for Next.js middleware.
- Verification: ES256 signature, issuer `twingate`, audience = Twingate network name, required claims `exp` and `iat`, 30s clock tolerance. Returns identity or `null` on any failure.
- `createRemoteJWKSet` caches the Gateway's public keys, so there is no network call after the first fetch.
- Middleware does NOT forward identity downstream. Handlers re-verify with the same helper, keeping the JWT the single source of truth.
- Identity shape: `user` (`id`, `username`, `email?`, `groups[]`), `device?` (`id`), `resource?` (`id`, `type`, `address`, `aliases[]`).

## Prerequisites
- Next.js 14+ with App Router
- Web App Resource behind the Twingate Gateway with the JWT request header configured
- `npm install jose`

## Step-by-Step
1. On the Web App Resource, add request header key `Authorization`, value `Bearer {{jwt}}`.
2. Install `jose`.
3. Create `src/twingate.ts` exporting `verifyTwingateJWT(authHeader)`. It splits on a space, requires the `bearer` scheme, then calls `jwtVerify(token, jwks, { algorithms: ["ES256"], issuer: "twingate", audience: TWINGATE_AUDIENCE, requiredClaims: ["exp","iat"], clockTolerance: "30s" })`.
4. Create `src/middleware.ts` (or `middleware.ts` at the project root). Call the helper with `request.headers.get("authorization")`, return `NextResponse.json({error:"Unauthorized"},{status:401})` on null, else `NextResponse.next()`.
5. Set `config.matcher` (default `["/api/:path*"]`).
6. In route handlers, call the helper with the request's `authorization` header. In Server Components, use `await headers()` from `next/headers`.
7. For group authorization, check `identity.user.groups.includes("engineering")` and return 403 if absent.

## Configuration Values
Add to `.env.local` in the project root:
- `TWINGATE_JWKS_URL`: `https://<your-tenant>.twingate.com/api/v1/jwk/ec`
- `TWINGATE_AUDIENCE`: Twingate network name matching the token's `aud` claim (e.g. `autoco` for `https://autoco.twingate.com`)

Matcher options:
- Specific paths: `["/api/:path*", "/dashboard/:path*"]`
- Invert to gate everything except public paths: `["/((?!health|_next/static|_next/image|favicon.ico).*)"]`
- Finer control: branch on `request.nextUrl.pathname` inside the middleware and return `NextResponse.next()` early.

## Gotchas
- Without the header configured on the Resource, no JWT arrives and every request returns 401.
- The middleware only protects matched routes; routes outside the matcher must verify in their own handler if they need identity.
- Audience is the network name only, not the full URL.
- The helper returns `null` for all failures (missing header, malformed, invalid token), so you cannot distinguish them.
- Use the Auth.js guide if you need `useSession()` in Client Components or session persistence.

## Related Docs
- Privileged Access for Web Apps overview
- JWT Payload Reference
- Request Headers
- Next.js + Auth.js guide
- Express.js and Django guides
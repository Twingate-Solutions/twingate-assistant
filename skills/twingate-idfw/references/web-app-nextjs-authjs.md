---
source: https://www.twingate.com/docs/web-app-nextjs-authjs
type: docs
fetched: 2026-11-19
source_version: 6d1be189356d64d489e0dfccce7494974d284b3300271552de46379109d98729
trust: official
---

# Next.js + Auth.js Session Integration

## Summary
Combines Twingate Privileged Access for web apps with Auth.js (NextAuth v5) in Next.js. Middleware verifies the Twingate JWT from the `Authorization` header and mints an Auth.js session cookie. This enables `auth()` in Server Components and `useSession()` in Client Components.

## Key Information
- Use this guide if you need `useSession()` in Client Components, session persistence across navigation, or already use Auth.js. Otherwise use the plain Next.js middleware guide.
- Auth.js is configured with no providers (`providers: []`) and `session.strategy: "jwt"`. The middleware creates the session.
- Middleware flow:
  1. If a valid, unexpired Auth.js session cookie exists, pass the request through.
  2. Otherwise verify the Twingate JWT with `jose` (`jwtVerify`) using remote JWKS.
  3. Encode a new session token (1-hour `maxAge`).
  4. Set the cookie on both the request (so `auth()` works in the same request) and the response (so the browser persists it).
- JWT verification: algorithm `ES256`, issuer `twingate`, audience `TWINGATE_AUDIENCE`, required claims `exp` and `iat`, clock tolerance 30s.
- Session mapping: `sub` = `user.id`, `email` and `name` = `user.username`, `twingateGroups` = `user.groups ?? []`.
- Missing auth header: request continues. Malformed header or invalid token/claims: 401 JSON.
- Matcher excludes `_next/static`, `_next/image`, `favicon.ico`, `api/health`.

## Prerequisites
- Next.js 14+ with App Router
- Auth.js v5 (`next-auth@beta`)
- Twingate Web App Resource configured to inject the JWT

## Step-by-Step
1. On the Web App Resource, add request header: key `Authorization`, value `Bearer {{jwt}}` (the Gateway injects no headers by default).
2. Install: `npm install next-auth@beta jose`
3. Generate the secret: `npx auth secret` (creates `.env.local` with `AUTH_SECRET`).
4. Create `src/middleware.ts` (verify the JWT, mint the session cookie).
5. Create `src/auth.ts` (export `auth` and `handlers`; add a `session` callback that maps `token.sub` to `session.user.id` and `token.twingateGroups` to `session.user.twingateGroups`; augment the `Session` type with `twingateGroups: string[]`).
6. Wrap the root layout in `<SessionProvider>` from `next-auth/react`.
7. Use `await auth()` in Server Components, `useSession()` in Client Components. For group authorization, check `session.user.twingateGroups.includes("admin")` and `redirect("/")` otherwise.

## Configuration Values
| Variable | Description |
|---|---|
| `TWINGATE_JWKS_URL` | `https://<your-tenant>.twingate.com/api/v1/jwk/ec` |
| `TWINGATE_AUDIENCE` | Twingate network name, must match the `aud` claim (e.g. `autoco` for `autoco.twingate.com`) |
| `AUTH_SECRET` | Random secret for encrypting session cookies |

All go in `.env.local`.

## Gotchas
- The cookie name differs by environment: `authjs.session-token` (dev) vs `__Secure-authjs.session-token` (production). The same value is used as the encode/decode `salt`.
- The cookie is set `secure` only when the request protocol is https.
- Existing-session check runs first, so the Twingate JWT is not re-verified until the session expires (1 hour). Group changes are reflected only after the session expires.
- Requests with no `Authorization` header pass through unauthenticated; check `auth()` results in pages.
- The header name and format are configurable at the Gateway/Resource level. The code assumes `Authorization: Bearer`.
- Stable Auth.js v4 will not work; v5 beta is required.

## Related Docs
- Privileged Access for Web Apps overview (architecture, JWT reference)
- Plain Next.js middleware guide
- JWT Payload Reference
- Request Headers
- Express.js and Django guides
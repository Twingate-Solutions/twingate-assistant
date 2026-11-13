---
source: https://www.twingate.com/docs/web-app-nextjs-authjs
type: docs
fetched: 2026-11-13
source_version: 1425bbc3a2d8210fa197dc71cea63e393c97c67bfbf55514a22647faf334da8e
trust: official
---

# Next.js + Auth.js Session Integration

## Summary
Combines Twingate Identity Firewall with Auth.js (NextAuth v5) in Next.js. Middleware verifies the Twingate JWT from the `Authorization` header and mints an Auth.js session cookie. This enables `auth()` in Server Components and `useSession()` in Client Components.

## Key Information
- Use this guide if you need `useSession()` in Client Components, session persistence across navigation, or already use Auth.js. For identity only in API routes or a few Server Components, use the plain Next.js middleware guide instead.
- Middleware flow:
  1. Check for an existing valid Auth.js session cookie. If valid, pass through without re-verifying.
  2. Otherwise verify the Twingate JWT (ES256, issuer `twingate`, audience from env, required claims `exp`/`iat`, 30s clock tolerance) via remote JWKS using `jose`.
  3. Encode a new Auth.js session token (1-hour `maxAge`) with `sub`, `email`, `name`, `twingateGroups`.
  4. Set the cookie on both the request (so `auth()` works in the same request) and the response (so the browser persists it).
- `auth.ts` uses no providers and `session: { strategy: "jwt" }`. The `session` callback maps `token.sub` and `twingateGroups` into the session. TypeScript module augmentation adds `twingateGroups` to `Session`.
- Cookie name: `authjs.session-token` in dev, `__Secure-authjs.session-token` in production. It is also used as the `salt`.
- Middleware matcher excludes `_next/static`, `_next/image`, `favicon.ico`, `api/health`.
- Wrap the root layout in `<SessionProvider>` (from `next-auth/react`) for client-side `useSession()`.
- Group authorization: `session.user.twingateGroups.includes("admin")`, with `redirect("/")` if it fails.

## Prerequisites
- Next.js 14+ with App Router
- Twingate Web App Resource with the Gateway configured to inject the JWT
- Auth.js v5 (`next-auth@beta`)

## Step-by-Step
1. On the Web App Resource, add request header: Key `Authorization`, Value `Bearer {{jwt}}`. (The Gateway injects no headers by default.)
2. Install: `npm install next-auth@beta jose`
3. Run `npx auth secret` to generate `AUTH_SECRET` in `.env.local`.
4. Create `src/middleware.ts` (verification and session minting as described above).
5. Create `src/auth.ts` exporting `{ auth, handlers }` from `NextAuth(...)`.
6. Wrap `src/app/layout.tsx` with `SessionProvider`.
7. Use `await auth()` in Server Components or `useSession()` in Client Components.

## Configuration Values
| Variable | Description |
|---|---|
| `TWINGATE_JWKS_URL` | `https://<your-tenant>.twingate.com/api/v1/jwk/ec` |
| `TWINGATE_AUDIENCE` | Twingate network name, must match the `aud` claim (e.g., `autoco` for `https://autoco.twingate.com`) |
| `AUTH_SECRET` | Random secret that encrypts session cookies |

All go in `.env.local`.

## Gotchas
- Auth.js v5 beta is required; v4 will not work.
- The header name and format are configurable at the Gateway level. The middleware assumes `Authorization: Bearer`, so change the code if you use a different header.
- A malformed `Authorization` header returns 401. A missing header passes the request through unauthenticated, so pages must check `auth()` themselves.
- Invalid or missing `user.id`/`user.username` claims return 401.
- The existing session is trusted until it expires (1 hour), so changes in Twingate group membership are not reflected until then.
- The cookie `salt` must match the cookie name between `encode` and `decode`.
- Verification errors on an existing cookie are swallowed and fall through to JWT re-verification.

## Related Docs
- Identity Firewall for Web Apps overview
- Plain Next.js middleware guide
- JWT Payload Reference
- Request Headers
- Express.js and Django guides
---
source: https://www.twingate.com/docs/web-app-nextjs-authjs
type: docs
fetched: 2026-08-23
source_version: a33f15577e7627d69dff5380af3c712d9824faebbcc61943bae019098c55c802
---

# Next.js + Auth.js Session Integration with Twingate

## Summary
Integrates Twingate Identity Firewall with Auth.js (NextAuth v5) in Next.js to provide session-based authentication. Middleware verifies Twingate JWTs and mints Auth.js session cookies, enabling `auth()` in Server Components and `useSession()` in Client Components.

## Key Information
- Use this over plain Next.js middleware when you need `useSession()` in Client Components, session persistence across navigation, or are already using Auth.js
- Session is created by middleware, not OAuth providers — no Auth.js providers are configured
- Cookie name differs by environment: `authjs.session-token` (dev) vs `__Secure-authjs.session-token` (prod)
- Session cookie has 1-hour (`MAX_SESSION_AGE = 3600`) lifetime
- JWT verified using ES256 algorithm with 30s clock tolerance

## Prerequisites
- Next.js 14+ with App Router
- Twingate Gateway configured to inject JWT via request header
- `npm install next-auth@beta jose`

## Configuration Values

| Variable | Value |
|---|---|
| `TWINGATE_JWKS_URL` | `https://<your-tenant>.twingate.com/api/v1/jwk/ec` |
| `AUTH_SECRET` | Generate with `npx auth secret` (auto-writes to `.env.local`) |

**Gateway Resource header:**
| Header Key | Value Template |
|---|---|
| `Authorization` | `Bearer {{jwt}}` |

## Step-by-Step

1. Configure Gateway Web App Resource to inject `Authorization: Bearer {{jwt}}` header
2. `npm install next-auth@beta jose`
3. `npx auth secret` → generates `AUTH_SECRET` in `.env.local`
4. Add `TWINGATE_JWKS_URL` to `.env.local`
5. Create `src/middleware.ts` (verifies JWT, mints session cookie)
6. Create `src/auth.ts` (Auth.js config with JWT strategy, no providers)
7. Wrap root layout with `<SessionProvider>` in `src/app/layout.tsx`
8. Use `auth()` in Server Components, `useSession()` in Client Components

## How Middleware Works
1. Check for existing valid Auth.js session cookie → pass through if valid
2. If no valid session, extract Bearer token from `Authorization` header
3. Verify JWT against JWKS endpoint (ES256)
4. Extract `user.id`, `user.username`, `user.groups` from payload
5. Encode Auth.js session token with user info + `twingateGroups`
6. Set cookie on **both** request (for same-request `auth()` reads) and response (browser persistence)

## JWT Claims Used
- `payload.user.id` → `token.sub`
- `payload.user.username` → `token.email`, `token.name`
- `payload.user.groups` → `token.twingateGroups`

## Gotchas
- Auth.js v5 (`next-auth@beta`) required — not v4
- Middleware skips static assets: `_next/static`, `_next/image`, `favicon.ico`, `api/health`
- If `Authorization` header is absent, middleware passes through (no 401) — unauthenticated access possible without additional route guards
- TypeScript module augmentation in `auth.ts` required to access `twingateGroups` on `Session` type
- `requiredClaims: ["exp", "iat"]` enforced during verification

## Related Docs
- [Identity Firewall for Web Apps overview](#) — architecture and JWT reference
- [Plain Next.js middleware](#) — simpler option without session management
- [Request Headers](#) — Gateway header injection options
- Express.js and Django guides for other frameworks
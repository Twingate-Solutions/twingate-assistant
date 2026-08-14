---
source: https://www.twingate.com/docs/web-app-nextjs-authjs
type: docs
fetched: 2026-08-14
source_version: 7a6858a05767b6d03a4670c41488a8fe1c43ffacbd3465cad7b1058c2bbb6f22
---

# Next.js + Auth.js (NextAuth v5) Twingate Integration

## Summary
Integrates Twingate Identity Firewall with Auth.js sessions in Next.js App Router. Middleware verifies the Twingate JWT and mints an Auth.js session cookie, enabling `auth()` in Server Components and `useSession()` in Client Components. Use this over plain middleware when Client Components need user identity or session persistence is required.

## Key Information
- Auth.js v5 (`next-auth@beta`) required — not compatible with v4
- Session cookie name differs by environment: `authjs.session-token` (dev) vs `__Secure-authjs.session-token` (prod)
- No OAuth providers configured — session is created entirely by middleware, not an OAuth flow
- Session lifetime: 1 hour (`MAX_SESSION_AGE = 3600`)
- JWT algorithm: `ES256` with 30-second clock tolerance
- Middleware skips re-verification if a valid session cookie already exists

## Prerequisites
- Next.js 14+ with App Router
- Twingate Gateway configured to inject JWT via `Authorization: Bearer {{jwt}}` header on the Web App Resource

## Step-by-Step

1. **Configure Gateway**: Add request header `Authorization: Bearer {{jwt}}` on the Web App Resource
2. **Install dependencies**: `npm install next-auth@beta jose`
3. **Generate AUTH_SECRET**: `npx auth secret` (writes to `.env.local`)
4. **Set env vars** in `.env.local`
5. **Create `src/middleware.ts`** — verifies Twingate JWT, mints Auth.js session cookie
6. **Create `src/auth.ts`** — configures NextAuth with JWT strategy, no providers, maps `twingateGroups` into session
7. **Wrap root layout** with `<SessionProvider>` from `next-auth/react`

## Configuration Values

| Variable | Description | Example |
|---|---|---|
| `TWINGATE_JWKS_URL` | Twingate tenant JWKS endpoint | `https://<tenant>.twingate.com/api/v1/jwk/ec` |
| `AUTH_SECRET` | Session cookie encryption secret | Generated via `npx auth secret` |

**Middleware matcher** (excludes from processing):
```
/((?!_next/static|_next/image|favicon.ico|api/health).*)
```

**Session cookie flags**: `httpOnly: true`, `secure` (on HTTPS), `sameSite: lax`, `path: /`

## Gotchas
- Cookie is set on **both** the request object (for same-request `auth()` reads) and the response (for browser persistence) — both are required
- `AUTH_SECRET` must match between middleware `encode`/`decode` calls and Auth.js config — they share the same secret and salt
- `twingateGroups` must be explicitly mapped in the `session` callback; it does not pass through automatically
- TypeScript module augmentation in `auth.ts` is required to expose `twingateGroups` on the `Session` type
- If no `Authorization` header is present, middleware passes through silently (unauthenticated state, not a 401)
- JWT claims `exp` and `iat` are required; missing claims cause verification failure

## Group-Based Authorization Pattern
```typescript
if (!session || !session.user.twingateGroups.includes("admin")) {
  redirect("/");
}
```

## Related Docs
- [Identity Firewall for Web Apps overview](https://www.twingate.com/docs/identity-firewall-web-apps) — architecture and JWT payload reference
- [Plain Next.js middleware](https://www.twingate.com/docs/web-app-nextjs) — simpler option without session management
- [Request Headers configuration](https://www.twingate.com/docs/request-headers)
- Express.js and Django guides for other frameworks
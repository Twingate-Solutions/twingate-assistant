---
source: https://www.twingate.com/docs/web-app-nextjs
type: docs
fetched: 2026-08-14
source_version: fd5d87a44a75cb317bd47c7f8aca186f0329dbfa8376f8c5c30e9fb85777845b
---

# Next.js Middleware - Twingate Identity Firewall JWT Verification

## Summary
Verifies Twingate Identity Firewall JWTs in Next.js Edge Middleware using the `jose` library. A middleware file gates specified routes, and a reusable helper verifies JWTs in both middleware and route handlers/Server Components. Does not use session-based auth (see Auth.js guide for that).

## Key Information
- JWT injected by Gateway as `Authorization: Bearer {{jwt}}` header (configurable)
- `jose` runs in Edge Runtime (required for Next.js middleware)
- JWKS keys are cached after first fetch — re-verification in handlers is cheap
- Helper returns `TwingateIdentity | null`; never throws
- Middleware gates routes with 401; handlers re-verify independently (no forwarded identity header)
- Any route handler or Server Component can verify JWT regardless of middleware matcher config

## Prerequisites
- Next.js 14+ with App Router
- Twingate Gateway configured to inject JWT header on Web App Resource
- `TWINGATE_JWKS_URL` environment variable set

## Configuration Values

| Variable | Value |
|---|---|
| `TWINGATE_JWKS_URL` | `https://<your-tenant>.twingate.com/api/v1/jwk/ec` |

**Gateway Header Config:**
| Header Key | Value Template |
|---|---|
| `Authorization` | `Bearer {{jwt}}` |

**JWT Verification params:**
- Algorithm: `ES256`
- Required claims: `exp`, `iat`
- Clock tolerance: `30s`

## Step-by-Step

1. Configure Gateway to inject `Authorization: Bearer {{jwt}}` header on the Web App Resource
2. Install dependency: `npm install jose`
3. Create `src/twingate.ts` with `verifyTwingateJWT()` helper and `TwingateIdentity` interface
4. Create `src/middleware.ts` calling helper, returning 401 on null
5. Set `config.matcher` to target protected routes
6. Add `TWINGATE_JWKS_URL` to `.env.local`
7. Call `verifyTwingateJWT()` directly in route handlers and Server Components as needed

## Gotchas
- **Re-verify in every handler**: Middleware gates routes but does not forward identity downstream; each handler/Server Component must call `verifyTwingateJWT()` again
- **Header name is configurable**: If Gateway is set to a different header than `Authorization`, update all calls to `request.headers.get()`
- **Server Components**: Use `headers()` from `next/headers` to access the authorization header
- **Matcher inversion**: Use negative lookahead in matcher to protect all routes except public ones (health checks, static assets)
- **Group auth is manual**: Check `identity.user.groups.includes("group-name")` in handlers; middleware does not enforce groups

## Identity Object Shape
```typescript
interface TwingateIdentity {
  user: { id: string; username: string; email?: string; groups: string[] };
  device?: { id: string };
  resource?: { id: string; type: string; address: string; aliases: string[] };
}
```

## Related Docs
- [Identity Firewall for Web Apps overview](#) — architecture and JWT reference
- [Next.js + Auth.js guide](#) — session-based integration with `useSession()`/`auth()`
- [Request Headers](#) — Gateway header injection configuration
- [JWT Payload Reference](#) — full token structure
- Express.js and Django guides for other frameworks
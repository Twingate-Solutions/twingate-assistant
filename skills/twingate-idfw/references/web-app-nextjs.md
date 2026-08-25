---
source: https://www.twingate.com/docs/web-app-nextjs
type: docs
fetched: 2026-08-23
source_version: eef083df9394190c06e95df23f975975fc8734e3b492572fe8f30feee93c645a
---

# Next.js JWT Middleware for Twingate Identity Firewall

## Summary
Verifies Twingate Identity Firewall JWTs in Next.js 14+ using Edge Middleware and the `jose` library. A reusable helper (`verifyTwingateJWT`) validates JWT signatures against cached JWKS keys and returns typed identity data for use in middleware, route handlers, and Server Components.

## Key Information
- JWT injected by Gateway via request header (not by default — must configure)
- `jose` runs in Edge Runtime (required for Next.js middleware)
- JWKS keys are cached after first fetch; re-verification in handlers is cheap
- Middleware gates routes with 401; identity is re-verified in handlers (no forwarded headers)
- JWT is the single source of truth — verify at each consumption point

## Prerequisites
- Next.js 14+ with App Router
- Twingate Gateway configured to inject JWT header on Web App Resource
- `npm install jose`

## Configuration Values

| Variable | Value |
|---|---|
| `TWINGATE_JWKS_URL` | `https://<your-tenant>.twingate.com/api/v1/jwk/ec` |

Add to `.env.local`. Configure Gateway header:
- **Header Key:** `Authorization`
- **Value Template:** `Bearer {{jwt}}`

## Step-by-Step

1. **Configure Gateway** — Add `Authorization: Bearer {{jwt}}` request header on the Web App Resource
2. **Install dependency** — `npm install jose`
3. **Create `src/twingate.ts`** — JWKS setup + `verifyTwingateJWT()` helper; uses `ES256`, requires `exp`/`iat` claims, 30s clock tolerance
4. **Create `src/middleware.ts`** — Calls helper, returns 401 if null; set `config.matcher` for protected routes
5. **Use in handlers/components** — Call `verifyTwingateJWT(request.headers.get("authorization"))` directly

## JWT Verification Parameters
```typescript
jwtVerify(token, jwks, {
  algorithms: ["ES256"],
  requiredClaims: ["exp", "iat"],
  clockTolerance: "30s",
})
```

## Identity Type Shape
```typescript
TwingateIdentity {
  user: { id, username, email?, groups[] }
  device?: { id }
  resource?: { id, type, address, aliases[] }
}
```

## Gotchas
- Gateway injects **no headers by default** — must explicitly configure the header on the resource
- Do **not** forward identity from middleware as a custom header; re-verify with helper in each handler
- `config.matcher` only controls middleware gating — any route can still call `verifyTwingateJWT` independently
- Server Components use `next/headers` → `headers()` to access the Authorization header
- Group authorization is manual: check `identity.user.groups.includes("group-name")`

## Related Docs
- [Identity Firewall for Web Apps overview](#) — architecture and JWT reference
- [Next.js + Auth.js guide](#) — for `useSession()` / `auth()` session-based integration
- [Request Headers](#) — Gateway header injection options and template variables
- [JWT Payload Reference](#) — full token structure
- Express.js and Django guides for other frameworks
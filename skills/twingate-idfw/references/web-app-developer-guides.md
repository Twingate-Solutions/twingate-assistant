---
source: https://www.twingate.com/docs/web-app-developer-guides
type: docs
fetched: 2026-08-14
source_version: 3fae5eceeeadd3a278e6705028b5b6c4d822b548759dadb8fd6c52c46a975f91
---

# Web App Developer Guides

## Summary
Drop-in middleware guides for verifying Twingate Identity Firewall JWTs in common web frameworks. Each guide follows a consistent pattern: verify ES256-signed JWTs from the `Authorization` header and expose user identity to application code.

## Key Information
- JWT signing algorithm: **ES256**
- JWT source: `Authorization` header
- Architecture reference: Identity Firewall for Web Apps overview

## Available Framework Guides

| Framework | Library | Identity Attachment |
|-----------|---------|-------------------|
| Express.js | `jose` | `req.twingateIdentity` |
| Django | `PyJWT` | `request.twingate_identity` |
| Next.js | `jose` | Route handlers & Server Components via helper |
| Next.js + Auth.js | `jose` + Auth.js (NextAuth v5) | `auth()` in Server Components, `useSession()` in Client Components |

## Pattern (All Guides)
1. Intercept incoming request via middleware
2. Extract JWT from `Authorization` header
3. Verify ES256 signature
4. Extract user identity claims
5. Attach identity to request object for downstream handlers

## Framework-Specific Notes

**Express.js**
- Uses Node.js middleware pattern
- Identity available as `req.twingateIdentity`

**Django**
- Python middleware class
- Identity available as `request.twingate_identity`

**Next.js**
- Edge Middleware targets App Router
- Thin middleware gates selected routes
- Reusable helper for reading identity in route handlers and Server Components

**Next.js + Auth.js**
- Combines Twingate JWT verification with Auth.js (NextAuth v5) session management
- Middleware verifies Twingate JWT → mints Auth.js session cookie
- Enables standard Auth.js APIs (`auth()`, `useSession()`) instead of header-based identity passing

## Prerequisites
- Twingate Identity Firewall configured for your web app
- Framework-specific JWT library (`jose` for Node.js, `PyJWT` for Python)

## Gotchas
- Next.js + Auth.js integration changes identity delivery mechanism from request headers to session cookies — different architecture from other guides
- All guides assume ES256; ensure your JWT verification library supports ES256 specifically

## Related Docs
- Identity Firewall for Web Apps overview (architecture details and full JWT reference)
- Express.js developer guide
- Django developer guide
- Next.js developer guide
- Next.js + Auth.js developer guide
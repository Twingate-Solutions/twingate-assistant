---
source: https://www.twingate.com/docs/web-app-developer-guides
type: docs
fetched: 2026-08-23
source_version: 7b6bfdb3d379b3c2f22a1757d40c33bf392ad777bc14c22e5ade5eb4b65e3f92
---

# Web App Middleware Developer Guides

## Summary
Drop-in middleware implementations for verifying Twingate Identity Firewall JWTs in common web frameworks. All guides follow the same pattern: verify an ES256-signed JWT from the `Authorization` header, extract user identity, and expose it to application code.

## Key Information
- JWT algorithm: **ES256**
- JWT source: `Authorization` header
- For architecture details and full JWT schema, see the Identity Firewall for Web Apps overview

## Available Guides

| Framework | Library | Identity Attachment |
|-----------|---------|-------------------|
| Express.js | `jose` (Node.js) | `req.twingateIdentity` |
| Django | `PyJWT` (Python) | `request.twingate_identity` |
| Next.js | `jose` (Edge Middleware) | Available in route handlers and Server Components |
| Next.js + Auth.js | `jose` + Auth.js (NextAuth v5) | `auth()` in Server Components, `useSession()` in Client Components |

## Pattern Per Guide
1. Intercept incoming request
2. Extract JWT from `Authorization` header
3. Verify ES256 signature using Twingate public key
4. Attach verified identity to request context
5. Pass to application handlers

## Next.js + Auth.js Notes
- Combines Twingate Identity Firewall with Auth.js (NextAuth v5) sessions
- Middleware verifies Twingate JWT, then mints an Auth.js session cookie
- Enables standard Auth.js APIs (`auth()`, `useSession()`) downstream

## Prerequisites
- Twingate Identity Firewall configured for your web app
- Appropriate JWT verification library installed per framework

## Related Docs
- Identity Firewall for Web Apps overview (architecture + full JWT reference)
- Express.js developer guide
- Django developer guide
- Next.js developer guide
- Next.js + Auth.js developer guide
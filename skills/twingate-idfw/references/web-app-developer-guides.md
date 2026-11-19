---
source: https://www.twingate.com/docs/web-app-developer-guides
type: docs
fetched: 2026-11-19
source_version: 1ea12abec91a44ec3f930919c5561eaf30485e5b4727af9340d1e0eeae487cc6
trust: official
---

# Page Title
Web App Middleware Developer Guides (Twingate Privileged Access)

## Summary
This page is an index of drop-in middleware guides for verifying Twingate Privileged Access Management JWTs in common web frameworks. Each guide follows the same pattern: verify the ES256-signed JWT in the `Authorization` header, extract the user's identity, and expose it to application code. The page itself has no code. Implementation details live in the per-framework guides.

## Key Information
- Common pattern across all guides:
  1. Read the JWT from the `Authorization` header.
  2. Verify the ES256 signature.
  3. Extract the user identity.
  4. Make the identity available to app code.
- Available guides:
  - **Express.js**: Node.js middleware using the `jose` library. Identity is attached to `req.twingateIdentity`.
  - **Django**: Python middleware using `PyJWT`. Identity is attached to `request.twingate_identity`.
  - **Next.js**: Edge Middleware for the App Router, using `jose`. A thin middleware gates chosen routes. A reusable helper verifies the JWT to read identity in route handlers and Server Components.
  - **Next.js + Auth.js**: Combines Twingate PAM with Auth.js (NextAuth v5) sessions. The middleware verifies the Twingate JWT and mints an Auth.js session cookie instead of passing identity by header. This gives `auth()` in Server Components and `useSession()` in Client Components.
- Architecture details and the full JWT reference are in the "Privileged Access for Web Apps" overview page.

## Prerequisites
Not specified on this page. Check the overview and individual guides. Expect a web app in one of the frameworks above, with Twingate Privileged Access configured to front it.

## Step-by-Step
Not on this page. Follow the framework-specific guide.

## Configuration Values
None listed here. Relevant identifiers:
- Header: `Authorization`
- JWT algorithm: ES256
- Libraries: `jose` (Express.js, Next.js), `PyJWT` (Django), Auth.js / NextAuth v5 (Next.js + Auth.js)
- Identity access points:
  - Express.js: `req.twingateIdentity`
  - Django: `request.twingate_identity`
  - Next.js + Auth.js: `auth()` and `useSession()`

## Gotchas
- Choose the guide by how you want identity exposed: a request property or header-derived helper (Express, Django, Next.js) versus a session cookie (Next.js + Auth.js).
- In plain Next.js, the middleware only gates the routes you configure. Use the helper to read identity in route handlers and Server Components.
- Verification must use ES256. Get the key and claim details from the JWT reference in the overview.

## Related Docs
- Privileged Access for Web Apps overview (architecture and JWT reference)
- Express.js developer guide
- Django developer guide
- Next.js developer guide
- Next.js + Auth.js developer guide
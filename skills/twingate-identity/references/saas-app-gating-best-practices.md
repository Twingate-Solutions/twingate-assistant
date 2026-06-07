# Best Practices for SaaS App Gating

## Summary
App Gating restricts access to SaaS applications using Twingate Resource Policies, treating the Identity Provider (IdP) itself as a protected resource. A catch-22 can occur where clients need to re-authenticate but cannot access the IdP sign-in page because it is also gated. Setting the Minimum Authentication Requirements to 31 days prevents lockouts.

## Key Information
- **Resource Policies**: Define access conditions for resources (MFA requirements, device encryption, re-auth frequency)
- **Admin Console Policy**: Separate policy protecting only the Twingate Admin Panel, applies only to Administrators
- **Minimum Authentication Requirements**: Controls how frequently a Twingate Client must re-register against the IdP — does **not** grant access to any resource
- When App Gating is configured, the IdP is simultaneously a **protected Resource** and the **authentication provider**
- Accessing any Resource resets the Minimum Authentication Requirements window

## Prerequisites
- Identity Provider configured for Twingate user authentication
- Device must meet Trusted Profiles or minimum OS requirements (see Device Security page)

## The Lockout Problem
A lockout occurs when **both** conditions are true:
1. User has not accessed any Twingate Resource for 31+ days
2. User has not restarted their device or Twingate Client for 31+ days

Workaround if locked out: restart the Twingate Client (not ideal UX).

## Configuration Values

| Setting | Recommended Value |
|---|---|
| Minimum Authentication Requirements period | **31 days** |

## Gotchas
- Short Minimum Authentication Requirements periods create catch-22 lockouts: client needs to re-register but IdP sign-in page is itself a gated resource
- Minimum Authentication Requirements provides **no security benefit** when set short — all actual security is enforced by Resource Policies
- Minimum Authentication Requirements and Resource Policies are distinct; do not conflate re-registration frequency with resource access control

## Related Docs
- Device Security (Trusted Profiles, minimum OS requirements)
- Resource Policies
- Admin Console Security
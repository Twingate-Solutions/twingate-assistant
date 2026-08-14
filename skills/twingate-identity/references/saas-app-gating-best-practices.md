---
source: https://www.twingate.com/docs/saas-app-gating-best-practices
type: docs
fetched: 2026-08-14
source_version: a9e74626418d50c46a455c22e94ee32ea8d3879e942546178826dfc32a6eacc8
---

# Best Practices for SaaS App Gating

## Summary
App Gating restricts access to SaaS applications using Twingate Resource Policies, treating the Identity Provider (IdP) itself as a protected resource. A catch-22 can occur when the IdP sign-in page is gated but the client needs to re-register. Setting a long Minimum Authentication Requirements period prevents lockouts.

## Key Information
- **Resource Policies**: Define conditions for access (MFA, device encryption, re-auth frequency); apply to all resources including SaaS apps
- **Admin Console Policy**: Separate policy protecting only the Twingate Admin Panel, applies only to administrators
- **Minimum Authentication Requirements**: Controls how frequently a Twingate Client must re-register against the IdP — does **not** grant access to any resource
- When App Gating is enabled, the **IdP is simultaneously a Resource and the authentication provider** — this dual role creates potential lockout risk
- Accessing any Resource **resets** the Minimum Authentication Requirements window

## Prerequisites
- Identity Provider configured with Twingate
- Twingate Client deployed on user devices
- Devices must meet Trusted Profiles or minimum OS requirements (see Device Security page)

## The Catch-22 Problem
Lockout occurs when both conditions are true simultaneously:
1. Client needs to re-register (Minimum Authentication Requirements expired)
2. IdP sign-in page is a protected resource requiring an already-registered client

Workaround: restart the Twingate Client (not user-friendly)

## Configuration Values

| Setting | Recommended Value |
|---|---|
| Minimum Authentication Requirements period | **31 days** |

## Step-by-Step: Avoid App Gating Lockouts
1. Set Minimum Authentication Requirements to **31 days**
2. Ensure Resource Policies are applied to the IdP resource as with other SaaS apps
3. Note: lockout only possible if user has **not accessed any resource** AND **not restarted device or client** for the full 31-day period

## Gotchas
- Short Minimum Authentication Requirements periods provide **no added security benefit** for App Gating but significantly increase lockout risk
- The Minimum Authentication Requirements clock **resets on any resource access**, so active users are rarely at risk
- Minimum Authentication Requirements and Resource Policies are independent — do not conflate re-registration frequency with resource access control
- Admin Console Policy is distinct from Resource Policies and cannot substitute for them

## Related Docs
- Device Security (Trusted Profiles, minimum OS requirements)
- Resource Policies
- Admin Console Security
- Identity Provider configuration
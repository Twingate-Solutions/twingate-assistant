# Best Practices for SaaS App Gating

## Summary
App Gating restricts access to SaaS applications using Twingate Resource Policies, treating the Identity Provider (IdP) itself as a protected resource. A catch-22 can occur where a client needs to re-authenticate but cannot reach the IdP sign-in page because it's also gated. Setting the Minimum Authentication Requirements to 31 days prevents this lockout scenario.

## Key Information
- **App Gating** = applying Resource Policies to SaaS/public resources, not just private infrastructure
- **Resource Policies** define conditions for access (MFA, device encryption, re-auth frequency)
- **Three distinct policy types:**
  - Resource Policies (protect all resources)
  - Admin Console Policy (protects only the Twingate Admin Panel, applies only to admins)
  - Minimum Authentication Requirements (defines client re-registration frequency, grants no resource access itself)
- When App Gating via IdP, the IdP is simultaneously a **Resource** and the **authentication provider**
- Devices must also meet Trusted Profile or minimum OS requirements from Device Security page

## Prerequisites
- Identity Provider configured with Twingate
- IdP sign-in page added as a Twingate Resource (when App Gating)
- Understanding of Resource Policy configuration

## The Catch-22 Problem
If Minimum Authentication Requirements window expires:
1. Client must re-register → needs to reach IdP sign-in page
2. IdP sign-in page is a protected Resource → requires registered Client
3. **Result:** Lockout (workaround: restart Twingate Client, but poor UX)

## Configuration Values

| Setting | Recommended Value | Notes |
|---|---|---|
| Minimum Authentication Requirements | **31 days** | Prevents IdP lockout catch-22 |

## Lockout Conditions
A lockout can **only** occur if **both** are true simultaneously:
- User has not accessed **any** Resource for 31 days (any resource access resets the auth window)
- User has not restarted their device or Twingate Client for 31 days

## Gotchas
- Minimum Authentication Requirements **does not** grant or protect resource access — it only controls re-registration frequency
- Short Minimum Authentication Requirements periods provide **no added security benefit** but increase lockout risk
- Accessing any resource (not just the IdP) resets the authentication window
- Admin Console Policy is separate and cannot substitute for Resource Policies on other resources
- Restarting the Twingate Client resolves lockouts but is not acceptable as a standard workflow

## Related Docs
- Device Security (Trusted Profiles, minimum OS requirements)
- Resource Policies
- Admin Console Security
- Identity Provider configuration
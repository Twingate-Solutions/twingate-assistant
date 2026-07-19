# Best Practices for SaaS App Gating

## Summary
App Gating restricts access to SaaS applications using Twingate Resource Policies, treating the Identity Provider (IdP) itself as a protected resource. A catch-22 can occur where clients need to re-authenticate but cannot access the IdP sign-in page because it's behind a policy. Setting Minimum Authentication Requirements to 31 days prevents lockout scenarios.

## Key Information
- **Resource Policies**: Define conditions for access (MFA, device encryption, re-auth frequency) — apply to all resources including SaaS apps
- **Admin Console Policy**: Separate policy protecting only the Twingate Admin Panel, applies only to Administrators
- **Minimum Authentication Requirements**: Controls how often a Twingate Client must re-register against the IdP — does NOT directly gate any resource itself
- When App Gating is enabled, the IdP serves dual roles: **authentication provider** AND **protected resource**
- Accessing any Resource resets the Minimum Authentication Requirements window

## Prerequisites
- Twingate client deployed on user devices
- Identity Provider configured for Twingate authentication
- Devices must meet Trusted Profiles or minimum OS requirements (see Device Security page)

## Gotchas
- **Lockout catch-22**: If Minimum Authentication Requirements period is too short, clients needing re-registration cannot reach the IdP sign-in page (which is itself a protected resource). Restarting the Twingate Client resolves it but degrades UX.
- Lockout only occurs when **both** conditions are true simultaneously:
  1. User has not accessed any Resource for 31+ days
  2. User has not restarted their device or Twingate Client for 31+ days
- Minimum Authentication Requirements alone provides **no security benefit** for resource access — resources are protected by Resource Policies

## Configuration Values

| Setting | Recommended Value | Notes |
|---|---|---|
| Minimum Authentication Requirements | **31 days** | Prevents IdP lockout in App Gating scenarios |

## Step-by-Step: Avoiding App Gating Lockout
1. Set Minimum Authentication Requirements to **31 days** (no security benefit to shorter periods)
2. Configure IdP as a Twingate Resource with appropriate Resource Policy
3. Ensure Resource Policies on IdP allow access for clients in re-registration states if needed
4. Advise users that accessing any resource resets the authentication window

## Related Docs
- Device Security (Trusted Profiles, minimum OS requirements)
- Resource Policies
- Admin Console Security
- Identity Provider configuration
# Best Practices for SaaS App Gating

## Summary
App Gating restricts access to SaaS applications using Twingate Resource Policies, treating the Identity Provider (IdP) as a protected resource. A catch-22 can occur when the IdP sign-in page is gated but the client needs to re-authenticate to access it. Setting a long Minimum Authentication Requirements period prevents lockouts.

## Key Information
- **Resource Policies**: Define conditions for accessing resources (MFA, device encryption, re-auth frequency)
- **Admin Console Policy**: Separate policy protecting only the Twingate Admin Panel, applies only to Administrators
- **Minimum Authentication Requirements**: Controls how often a Twingate Client must re-register against the IdP — does **not** grant resource access itself
- When App Gating, the IdP is simultaneously a **Resource** and the **authentication provider** — creates a potential circular dependency
- Accessing any Resource resets the Minimum Authentication Requirements authentication window

## Prerequisites
- Twingate configured with an Identity Provider
- IdP configured as a Twingate Resource for App Gating
- Devices must meet Trusted Profiles or minimum OS requirements (see Device Security page)

## Configuration Values
| Setting | Recommended Value |
|---|---|
| Minimum Authentication Requirements period | **31 days** |

## Gotchas
- **Lockout scenario**: If Minimum Authentication Requirements is too short, a client needing re-registration cannot reach the IdP sign-in page because the IdP is itself a gated resource
- Lockout only occurs when **both** conditions are true simultaneously:
  1. User has not accessed any Resource for 31+ days
  2. User has not restarted device or Twingate Client for 31+ days
- Workaround for lockout: restart the Twingate Client (not ideal for UX)
- Short Minimum Authentication Requirements periods provide **no additional security benefit** — avoid them
- Minimum Authentication Requirements does not protect resources; that is handled exclusively by Resource Policies

## Step-by-Step
1. Configure your IdP as a Twingate Resource with appropriate Resource Policy
2. Set Minimum Authentication Requirements to **31 days**
3. Apply Resource Policies to SaaS apps requiring conditions (MFA, device encryption, etc.)
4. Verify devices meet Trusted Profile or minimum OS requirements

## Related Docs
- Device Security (Trusted Profiles, minimum OS requirements)
- Resource Policies
- Admin Console Security
- Identity Provider configuration
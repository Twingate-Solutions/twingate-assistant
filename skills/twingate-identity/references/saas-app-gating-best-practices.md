# Best Practices for SaaS App Gating

## Summary
App Gating restricts access to SaaS applications using Twingate Resource Policies, treating the Identity Provider (IdP) itself as a protected resource. A catch-22 can occur when clients need to re-authenticate but cannot reach the IdP sign-in page because it is itself gated. Setting a long Minimum Authentication Requirements period prevents lockouts.

## Key Information
- **App Gating** = applying Resource Policies to SaaS/public resources, same as private resources
- **Three policy types** in Twingate:
  - **Resource Policies** – protect individual resources (MFA, device encryption, session duration)
  - **Admin Console Policy** – protects the Twingate Admin Panel for admins only
  - **Minimum Authentication Requirements** – defines how often the Twingate Client must re-register with the IdP; does **not** grant resource access
- When App Gating an IdP, the IdP is simultaneously a **Resource** and the **authentication provider**
- Accessing any Resource resets the Minimum Authentication Requirements window

## Prerequisites
- Twingate deployed with an Identity Provider configured
- IdP sign-in URL added as a Twingate Resource (for App Gating)
- Devices must meet Trusted Profiles or minimum OS requirements (see Device Security page)

## The Lockout Catch-22
A user gets locked out when **both** conditions are true:
1. User has not accessed **any** Twingate Resource for 31+ days (no window reset)
2. User has not restarted their device or Twingate Client for 31+ days

Workaround if locked out: **restart the Twingate Client** (not ideal for UX).

## Configuration Values

| Setting | Recommended Value | Notes |
|---|---|---|
| Minimum Authentication Requirements period | **31 days** | Prevents IdP lockout; no security benefit to shorter periods |

## Gotchas
- **Short re-authentication windows cause lockouts**: If Minimum Authentication Requirements is too short and the IdP is a gated resource, users cannot re-authenticate to reach the IdP sign-in page
- Minimum Authentication Requirements provides **no resource access control**—do not confuse it with Resource Policies
- The Admin Console Policy is **separate** from Resource Policies and only applies to admin users
- Restarting the Twingate Client resolves lockouts but is a poor user experience

## Step-by-Step: Avoid App Gating Lockout
1. Add IdP sign-in URL as a Twingate Resource with appropriate Resource Policy
2. Navigate to Minimum Authentication Requirements settings in Admin Console
3. Set the re-registration period to **31 days**
4. Ensure all users access at least one Twingate Resource within any 31-day window to keep their session active

## Related Docs
- Device Security (Trusted Profiles, minimum OS requirements)
- Resource Policies
- Admin Console Security Policy
- Identity Provider configuration
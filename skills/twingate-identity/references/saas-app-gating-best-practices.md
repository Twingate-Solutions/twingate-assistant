# Best Practices for SaaS App Gating

## Summary
App Gating restricts access to SaaS applications using Twingate Resource Policies, treating the Identity Provider (IdP) itself as a protected resource. A catch-22 can occur when the IdP sign-in page is gated but a client needs to re-authenticate to access it. Setting Minimum Authentication Requirements to 31 days prevents lockouts.

## Key Information
- **App Gating** = applying Resource Policies to SaaS apps (public resources), same as private resources
- **Three policy types** in Twingate:
  - **Resource Policies** — protect all resources (private + public/SaaS); define access conditions
  - **Admin Console Policy** — protects only the Twingate Admin Panel; applies only to Administrators
  - **Minimum Authentication Requirements** — controls how frequently a Client must re-register against the IdP; does NOT grant resource access itself
- When App Gating via IdP, the IdP is simultaneously a **Resource** and the **authentication provider**
- Devices must also meet Trusted Profiles or minimum OS requirements (see Device Security docs)

## The Catch-22 Problem
If Minimum Authentication Requirements period is too short:
1. Client needs to re-register (re-authenticate with IdP)
2. IdP sign-in page is itself a gated resource
3. Client cannot reach IdP to re-authenticate → lockout

**Workaround:** Restart the Twingate Client (poor UX)  
**Solution:** Set Minimum Authentication Requirements to 31 days

## Configuration Values

| Setting | Recommended Value |
|---|---|
| Minimum Authentication Requirements period | **31 days** |

## Lockout Conditions
A lockout can only occur if **both** are true simultaneously:
- User has not accessed **any** Resource for 31 days (any resource access resets the auth window)
- User has not restarted their device or Twingate Client for 31 days

## Gotchas
- Minimum Authentication Requirements has **no security benefit** when set short — no resource access is granted by it
- Accessing any Resource (not just the IdP) resets the authentication window
- Short re-registration intervals create lockout risk with no security upside
- Admin Console Policy is separate from Resource Policies — don't conflate them

## Related Docs
- Device Security (Trusted Profiles, minimum OS requirements)
- Resource Policies
- Admin Console Security
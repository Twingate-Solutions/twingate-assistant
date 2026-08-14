---
source: https://www.twingate.com/docs/admin-console-security
type: docs
fetched: 2026-08-14
source_version: 6906336e2bb599a928e5be98ba585173fd46f9f95462325dc351d3fa2fbcbf61
---

# Admin Console Security

## Summary
Twingate allows administrators to configure MFA requirements specifically for Admin Console access. This setting is separate from end-user authentication policies (Minimum Authentication Requirements and Device Security do not apply to admins). MFA options include biometrics or a security key.

## Key Information
- Setting location: **Settings tab** in the Admin Console
- Applies only to **Twingate administrators** signing into the Admin Console
- Admins do not sign into the Twingate Client to access the Admin Console, so user-facing auth policies are irrelevant here
- MFA options: **biometrics** or **security key**
- When MFA is set to "required," admins are prompted to configure one of these methods post-authentication

## Prerequisites
- Admin role with access to the Settings tab
- Identity provider authentication already configured (MFA is layered on top)

## Step-by-Step: Configuring MFA for Admin Console

1. Navigate to **Settings** tab in the Admin Console
2. Locate the **Admin Console Security** section
3. Set MFA to **"required"**
4. On next login, admins will be prompted to configure biometrics or a security key
5. Complete the setup flow, or select **"Don't ask me again"** to defer

**To configure MFA later:**
- Select **"Configure MFA"** from the account dropdown (upper right corner)

## Configuration Values

| Option | Description |
|--------|-------------|
| MFA: Required | Admins must configure biometrics or security key |
| MFA: Not Required | No additional MFA enforced for Console access |

## Gotchas
- **Biometric isolation**: Biometrics configured for Admin Console sign-in **cannot** be reused for the Twingate Client — but biometrics previously set up on the Client **can** be used for the Admin Console (one-way compatibility)
- **"Don't ask me again"** suppresses the MFA setup prompt on future logins — admins must manually configure via account dropdown if they opt out initially
- Admin Console Security is **independent** of Minimum Authentication Requirements and Device Security policies

## Related Docs
- Minimum Authentication Requirements
- Device Security policies
- Twingate Client authentication
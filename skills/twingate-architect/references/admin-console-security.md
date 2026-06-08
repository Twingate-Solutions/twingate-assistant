# Admin Console Security

## Summary
Twingate allows administrators to enforce MFA requirements specifically for Admin Console access. This setting is separate from user-facing authentication policies (Minimum Authentication Requirements and Device Security) which do not apply to admin console access.

## Key Information
- Configured under **Settings** tab in the Admin Console
- Applies **only to Twingate administrators** signing into the Admin Console
- MFA policy here is independent from end-user authentication requirements
- When MFA is set to "required," admins must configure **biometrics or a security key**

## Prerequisites
- Twingate Admin role
- Access to Settings tab in Admin Console

## Step-by-Step: Configuring MFA for Admin Console

1. Navigate to **Settings** tab in Admin Console
2. Locate Admin Console Security section
3. Set MFA to **"required"**
4. On next login, admins will be prompted to configure biometrics or a security key

## Configuration Options

| Option | Description |
|--------|-------------|
| MFA Required | Admins must authenticate with biometrics or security key |
| MFA Not Required | Standard authentication only |

## MFA Setup Behavior

- **"Don't ask me again"** — suppresses the MFA setup prompt on future logins (MFA not configured)
- **Configure MFA later** — accessible via account dropdown → **"Configure MFA"** (upper right corner)

## Gotchas

- **Biometric isolation**: Biometrics configured for Admin Console access **cannot** be reused for the Twingate Client, but the reverse is allowed — biometrics previously set up on the Twingate Client **can** be used for Admin Console login
- Admins do **not** need to sign into the Twingate Client to access the Admin Console, so Device Security and Minimum Authentication Requirements policies are bypassed entirely
- Dismissing the MFA setup prompt with "Don't ask me again" does not enforce MFA — admins can skip configuration indefinitely unless the policy enforcement mechanism prevents login without MFA

## Related Docs
- Minimum Authentication Requirements
- Device Security policies
- Twingate Client authentication configuration
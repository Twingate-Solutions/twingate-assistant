# Admin Console Security

## Summary
Twingate allows administrators to configure MFA requirements specifically for Admin Console access, separate from user-facing authentication policies. This setting applies only to Twingate administrators signing into the Admin Console, not to regular users.

## Key Information
- Located under **Settings tab** in the Admin Console
- Applies **only to Twingate administrators** accessing the Admin Console
- Admin Console auth is **independent** from Minimum Authentication Requirements and Device Security policies (those don't apply here)
- MFA options: **biometrics** or **security key**

## Prerequisites
- Twingate Admin account
- Access to Settings tab in Admin Console

## Configuration Steps
1. Navigate to **Settings** tab in the Admin Console
2. Locate Admin Console Security settings
3. Set MFA to **"required"** or leave optional
4. If required: admins will be prompted to configure biometrics or security key on next login

## MFA Setup Behavior
- When MFA is set to "required," admins are prompted to configure biometrics or security key **after** successful authentication
- Selecting **"Don't ask me again"** suppresses the setup modal on future logins
- MFA can be configured later via **account dropdown → "Configure MFA"** (upper right corner)

## Gotchas
- **Biometric isolation**: Biometrics configured for Admin Console **cannot** be reused for the Twingate Client
- **Reverse is allowed**: Biometrics previously configured on the Twingate Client **can** be used to sign into the Admin Console
- Admin Console Security is entirely separate from user-facing security policies — changes here don't affect end-user authentication requirements
- Admins do **not** need to sign into the Twingate Client to access the Admin Console

## Related Docs
- Minimum Authentication Requirements (user-facing policy)
- Device Security settings
- Twingate Client authentication configuration
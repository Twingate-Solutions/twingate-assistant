# Admin Console Security

## Summary
Twingate allows configuration of authentication requirements specifically for Admin Console access. This setting is separate from client-side authentication policies (Minimum Authentication Requirements and Device Security), as admins don't need to sign into the Twingate client to access the console.

## Key Information
- Located under **Settings tab** in the Admin Console
- Applies only to **Twingate administrators** accessing the Admin Console
- MFA can be set to **required** for Admin Console access
- When MFA is required, admins must configure **biometrics or a security key** after initial authentication
- "Don't ask me again" option suppresses the MFA setup prompt on future logins

## Prerequisites
- Admin role in Twingate
- Access to Settings tab

## Configuration Steps
1. Navigate to **Settings** tab in Admin Console
2. Locate Admin Console Security section
3. Set MFA requirement (optional or required)

## Gotchas
- **Biometric isolation**: Biometrics configured for Admin Console login **cannot** be reused for Twingate Client authentication — but the reverse works (client biometrics **can** be used for Admin Console login)
- **Policy scope**: Minimum Authentication Requirements and Device Security policies do **not** apply to Admin Console access — only Admin Console Security policy does
- **Deferred MFA setup**: If user dismisses MFA setup prompt, they must manually trigger it later via **account dropdown → Configure MFA** (upper right corner)

## Related Docs
- Minimum Authentication Requirements
- Device Security policies
- Twingate Client authentication
# Admin Console Security

## Summary
Twingate's Admin Console Security settings control authentication requirements for administrators accessing the Admin Console. MFA can be required for admin sign-in, separate from end-user authentication policies. Standard Minimum Authentication Requirements and Device Security policies do not apply to Admin Console access.

## Key Information
- Configured under **Settings** tab in the Admin Console
- Policy applies **only to Twingate administrators** signing into the Admin Console
- Admin Console access is independent of Twingate Client sign-in
- MFA options: **biometrics** or **security key**
- Minimum Authentication Requirements and Device Security requirements do **not** apply to admins

## Prerequisites
- Admin access to Twingate Admin Console
- If requiring MFA: admins must have biometrics or a security key available to configure

## Configuration Steps
1. Navigate to **Settings** tab in the Admin Console
2. Locate Admin Console Security section
3. Set MFA to **required** or optional
4. On next admin login (if required), admins are prompted to configure biometrics or a security key

## MFA Setup Behavior
- When MFA is set to "required," admins are prompted to configure biometrics or security key after successful authentication
- Selecting **"Don't ask me again"** suppresses the setup modal on future logins
- To configure MFA later: select **"Configure MFA"** from the account dropdown (upper right corner)

## Gotchas
- **Biometric isolation**: Biometrics configured for Admin Console sign-in **cannot** be reused for Twingate Client authentication
- **Reverse is allowed**: Biometrics previously configured on the Twingate Client **can** be used for Admin Console sign-in
- Admins do not need a Twingate Client session to access the Admin Console — this means device trust and session policies don't gate admin access
- Dismissing MFA setup with "Don't ask me again" does not prevent future configuration via the account dropdown

## Related Docs
- Minimum Authentication Requirements
- Device Security policies
- Twingate Client authentication
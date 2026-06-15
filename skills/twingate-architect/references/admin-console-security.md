# Admin Console Security

## Summary
Twingate allows administrators to configure MFA requirements specifically for Admin Console access. This setting is separate from end-user authentication policies and only applies to administrators signing into the Admin Console.

## Key Information
- Located under the **Settings** tab in the Admin Console
- Applies **only to Twingate administrators** accessing the Admin Console
- Minimum Authentication Requirements and Device Security policies do **not** apply to Admin Console access
- MFA can be set to "required" for Admin Console logins
- Supported MFA methods: **biometrics** or **security key**

## MFA Configuration
- When MFA is set to "required," admins are prompted to configure biometrics or a security key after first successful authentication
- Admins can skip setup by selecting "Don't ask me again"
- MFA can be configured later via **account dropdown → Configure MFA** (upper right corner)

## Gotchas
- **Biometric isolation**: Biometrics configured for the Admin Console cannot be reused for the Twingate Client, and vice versa — **exception**: biometrics previously configured on the Twingate Client *can* be used to sign into the Admin Console (one-way compatibility)
- Admin Console security is completely independent from network/resource access policies; changes here don't affect end-user Twingate Client authentication
- Admins do not need a Twingate Client session to access the Admin Console

## Step-by-Step: Enable MFA for Admin Console
1. Sign into the Admin Console
2. Navigate to **Settings** tab
3. Locate Admin Console Security section
4. Set MFA to **Required**
5. Admins will be prompted to configure biometrics or security key on next login

## Related Docs
- Minimum Authentication Requirements
- Device Security policies
- Twingate Client authentication
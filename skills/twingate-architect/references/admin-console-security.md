# Admin Console Security

## Summary
Twingate allows configuration of authentication requirements specifically for Admin Console access. This setting applies only to Twingate administrators signing into the Admin Console, separate from end-user authentication policies.

## Key Information
- Configured under **Settings tab** in the Admin Console
- Applies **only to administrators** accessing the Admin Console
- MFA can be set to "required" for Admin Console access
- Supported MFA methods: **biometrics** or **security key**
- Minimum Authentication Requirements and Device Security policies do **not** apply to Admin Console access (admins don't sign into the Twingate client to access the console)

## Prerequisites
- Admin role in Twingate
- Access to Settings tab in Admin Console

## Configuration Steps
1. Navigate to **Settings** tab in Admin Console
2. Locate Admin Console Security section
3. Set MFA requirement as desired (e.g., "required")
4. If MFA required: admins will be prompted to configure biometrics or security key on next login

## MFA Setup Behavior
- When MFA is set to "required," admins are prompted to configure biometrics or security key **after** successful authentication
- Selecting **"Don't ask me again"** suppresses the setup modal on future logins
- To configure MFA later: select **"Configure MFA"** from account dropdown (upper right corner)

## Gotchas
- **Biometric isolation**: Biometrics configured for Admin Console login **cannot** be reused for Twingate Client authentication — but the reverse is allowed (client biometrics **can** be used for Admin Console login)
- Admin Console security policy is entirely separate from end-user `Minimum Authentication Requirements` and `Device Security` settings — do not confuse the two
- Dismissing MFA setup with "Don't ask me again" does not permanently opt out — it can be configured later via account dropdown

## Configuration Values
| Setting | Location | Options |
|---|---|---|
| MFA Requirement | Settings → Admin Console Security | Required / Not Required |
| MFA Method | Per-admin setup | Biometrics, Security Key |

## Related Docs
- Minimum Authentication Requirements
- Device Security
- Twingate Client Authentication
# Admin Console Security

## Summary
Twingate allows administrators to enforce MFA requirements specifically for Admin Console access. This policy is separate from standard user authentication policies and applies only to Twingate administrators signing into the Admin Console.

## Key Information
- Configured under **Settings tab** in the Admin Console
- Applies **only to Twingate administrators** accessing the Admin Console
- Minimum Authentication Requirements and Device Security policies do **not** apply to Admin Console access
- MFA options: **biometrics** or **security key**

## Prerequisites
- Twingate Admin Console access
- Administrator role

## Configuration Steps
1. Navigate to **Settings** tab in the Admin Console
2. Locate Admin Console Security section
3. Set MFA requirement to **Required** or optional

## MFA Setup Behavior
- When MFA is set to **Required**: admins are prompted to configure biometrics or a security key after initial successful authentication
- **"Don't ask me again"** option skips the setup modal on subsequent logins
- To configure MFA later: select **"Configure MFA"** from the account dropdown (upper right corner)

## Biometrics Gotchas
- Biometric setup for Admin Console **cannot** be shared with the Twingate Client — they are separate configurations
- **Exception**: If biometrics were previously configured on the Twingate Client, they **can** be used to sign into the Admin Console (one-way reuse only)
- Direction matters: Client → Console reuse works; Console → Client reuse does **not**

## Configuration Values
| Setting | Options |
|---|---|
| MFA Requirement | Required / Not Required |
| MFA Methods | Biometrics, Security Key |

## Related Docs
- Minimum Authentication Requirements
- Device Security policies
- Twingate Client authentication
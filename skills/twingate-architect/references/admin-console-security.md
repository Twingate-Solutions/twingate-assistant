# Admin Console Security

## Summary
Twingate allows administrators to configure authentication requirements specifically for Admin Console access. MFA can be required for admin sign-in, independent of user-facing authentication policies. This setting applies only to Twingate administrators accessing the Admin Console.

## Key Information
- Located under the **Settings** tab in the Admin Console
- Policy applies **only to administrators** signing into the Admin Console
- Minimum Authentication Requirements and Device Security policies do **not** apply to Admin Console access
- MFA options: **biometrics** or **security key**
- Admins do not need a Twingate client session to access the Admin Console

## Prerequisites
- Admin access to the Twingate Admin Console
- MFA set to "required" to trigger biometric/security key setup prompts

## Configuration Steps
1. Navigate to **Settings** tab in the Admin Console
2. Locate Admin Console Security settings
3. Set MFA requirement (optional or required)
4. If required, admins will be prompted to configure biometrics or a security key on next login

## Configuration Values
| Setting | Options |
|---|---|
| MFA | Required / Not Required |
| MFA Methods | Biometrics, Security Key |

## Gotchas
- **Biometric separation**: Biometrics configured for the Admin Console **cannot** be reused for the Twingate Client. However, biometrics previously set up on the Twingate Client **can** be used for Admin Console sign-in (one-way compatibility).
- **"Don't ask me again"** dismisses the MFA setup modal permanently for that admin; setup can be re-initiated via **account dropdown → Configure MFA** (upper right corner).
- Admin Console authentication is independent — Minimum Authentication Requirements and Device Security policies have **no effect** here.

## Related Docs
- Minimum Authentication Requirements
- Device Security policies
- Twingate Client authentication
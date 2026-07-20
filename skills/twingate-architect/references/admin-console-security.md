# Admin Console Security

## Summary
Twingate allows administrators to configure MFA requirements specifically for Admin Console access. This setting is separate from end-user authentication policies (Minimum Authentication Requirements and Device Security). MFA can be enforced via biometrics or a security key.

## Key Information
- Located under **Settings** tab in Admin Console
- Applies **only to Twingate administrators** signing into the Admin Console
- Admins do not sign into the Twingate Client to access the Admin Console, so standard user auth policies do not apply
- MFA options: **biometrics** or **security key**
- "Don't ask me again" suppresses the MFA setup prompt on subsequent logins
- MFA setup can be initiated later via **account dropdown → Configure MFA** (upper right corner)

## Prerequisites
- Twingate Admin role
- Access to Settings tab in Admin Console

## Configuration Steps
1. Navigate to **Settings** tab in Admin Console
2. Locate **Admin Console Security** section
3. Set MFA to **Required** or optional (default)
4. Admins will be prompted to configure biometrics or security key on next login if Required is set

## Configuration Values
| Setting | Options |
|---|---|
| Admin Console MFA | Required / Not Required |
| MFA Methods | Biometrics, Security Key |

## Gotchas
- **Biometric isolation**: Biometrics configured *in* the Admin Console **cannot** be reused for the Twingate Client. The reverse is allowed — Client biometrics **can** authenticate into the Admin Console.
- "Don't ask me again" permanently suppresses the MFA setup modal until manually triggered via Configure MFA
- Minimum Authentication Requirements and Device Security policies have **no effect** on Admin Console access
- Admin Console security policy is entirely separate from end-user/client security policies

## Related Docs
- Minimum Authentication Requirements
- Device Security
- Twingate Client authentication
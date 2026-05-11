# Admin Console Security

## Summary
Twingate lets you require MFA for Admin Console access, configured under Settings. This policy applies only to Twingate administrators signing into the Admin Console, not to regular users. Standard Minimum Authentication Requirements and Device Security policies do not apply to Admin Console access.

## Key Information
- MFA requirement is configured under **Settings tab** in the Admin Console
- Policy applies **only to administrators** accessing the Admin Console
- Regular user authentication policies (Minimum Authentication Requirements, Device Security) do **not** apply here
- Supported MFA methods: **biometrics** or **security key**

## Prerequisites
- Twingate Admin role
- Access to Settings tab in Admin Console

## Step-by-Step: Configuring MFA Requirement
1. Navigate to **Settings** tab in the Admin Console
2. Locate Admin Console Security section
3. Set MFA to **"required"**
4. Admins will be prompted to configure biometrics or security key on next login

## Step-by-Step: Setting Up Biometrics/Security Key (Admin Flow)
1. Authenticate into the Admin Console
2. When prompted, configure biometrics or security key
3. Optionally select **"Don't ask me again"** to suppress future prompts
4. To configure later: select **"Configure MFA"** from account dropdown (upper right corner)

## Configuration Values
| Setting | Location | Options |
|---|---|---|
| MFA Requirement | Settings → Admin Console Security | Required / Not Required |
| MFA Methods | Per-admin setup | Biometrics, Security Key |

## Gotchas
- **Biometric isolation**: Biometrics configured for Admin Console **cannot** be reused for the Twingate Client — they are separate setups
- **Reverse is allowed**: Biometrics previously configured on the Twingate Client **can** be used to sign into the Admin Console
- Selecting "Don't ask me again" skips MFA setup prompts on future logins; must manually trigger via account dropdown to configure later
- Admins do not need a Twingate Client session to access the Admin Console, so client-side security policies are irrelevant here

## Related Docs
- Minimum Authentication Requirements
- Device Security policies
- Twingate Client authentication
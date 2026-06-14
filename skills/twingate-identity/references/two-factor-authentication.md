# Native MFA - Twingate

## Summary
Twingate provides native MFA independent of your identity provider, configurable at sign-in, per Resource Policy, or for Admin Console access. Supports TOTP, biometrics (WebAuthn), and physical security keys. MFA should be configured in either Twingate or your IdP, not both.

## Key Information
- MFA is policy-scoped, not globally toggled
- Authentication frequency is inherited from the associated policy's settings
- TOTP is always configured as a backup even when biometrics/security keys are primary
- WebAuthn compatibility varies by platform/browser

## Supported MFA Methods
| Method | Details |
|--------|---------|
| TOTP | Google Authenticator, Authy, 1Password, etc. |
| Biometrics (WebAuthn) | Touch ID, Windows Hello |
| Security Keys (WebAuthn) | FIDO2/CTAP2 keys only (e.g., YubiKey) |

## Configuration Locations
- **Sign In Policy** → MFA required on every Client sign-in; frequency tied to Sign In Policy
- **Resource Policies** → MFA required on first access to protected Resource; frequency tied to Resource Policy (e.g., once per 24 hours)
- **Settings → Admin Console Security** → MFA required for admin sign-ins

## Prerequisites
- Admin access to Twingate Admin Console
- Users must have a compatible authenticator app or WebAuthn-capable device/key

## Step-by-Step
1. Navigate to the target policy (Sign In Policy, Resource Policy, or Admin Console Security settings)
2. Enable MFA within that policy
3. Set authentication frequency as needed
4. Users complete MFA setup on next prompted sign-in or Resource access

## Gotchas
- **Double MFA**: If IdP already enforces MFA, enabling Twingate native MFA causes users to complete MFA twice — configure in one place only
- **FIDO2/CTAP2 only**: Non-FIDO2 security keys are not supported
- **TOTP always required as backup**: Users with biometrics/security keys must also configure TOTP
- **WebAuthn limitations**: Browser/platform compatibility is not universal; check [webauthn.me/browser-support](https://webauthn.me/browser-support)
- **Lost device recovery**: Admin must manually reset MFA from the user's detail page in Admin Console; user re-enrolls on next MFA prompt

## Admin Actions
- Reset/delete a user's MFA method: Admin Console → User detail page → select method → reset or delete

## Related Docs
- [Security Policies](https://www.twingate.com/docs/security-policies)
- [WebAuthn Browser Support](https://webauthn.me/browser-support)
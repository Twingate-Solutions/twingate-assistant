# Native MFA (Twingate)

## Summary
Twingate provides native MFA independent of your identity provider, configurable at sign-in, resource access, or Admin Console login. MFA is managed at the policy level with per-policy authentication frequency controls. Supports TOTP, biometrics (WebAuthn), and physical security keys.

## Key Information
- MFA scope is determined by where it's configured: Sign In Policy, Resource Policies, or Admin Console Settings
- Authentication frequency is inherited from the policy it's attached to (e.g., 24-hour frequency = MFA once per day)
- TOTP is always configured as a backup even when biometrics or security keys are the primary method
- Admins can reset individual user MFA methods from the user detail page in the Admin Console

## Prerequisites
- Admin access to Twingate Admin Console
- Users need a TOTP app (Google Authenticator, Authy, 1Password) or WebAuthn-compatible device/key

## Configuration Locations

| Scope | Location | Effect |
|---|---|---|
| Sign-in | Sign In Policy | MFA required every Client login |
| Resource access | Resource Policies | MFA required per-resource access |
| Admin Console | Settings → Security | MFA required for admin logins |

## Supported MFA Methods
- **TOTP**: Time-based codes via authenticator app
- **Biometrics (WebAuthn)**: Touch ID, Windows Hello
- **Security Keys (WebAuthn)**: YubiKey or other FIDO2/CTAP2 keys only — non-FIDO2 keys not supported

## Gotchas
- **Do not enable MFA in both Twingate and your IdP** — users will be prompted twice per authentication
- FIDO2/CTAP2 required for security keys; older key formats unsupported
- WebAuthn (biometrics/security keys) has variable browser/platform support — check [webauthn.me/browser-support](https://webauthn.me/browser-support)
- Biometric/security key users are still required to configure TOTP as backup

## Admin Actions
- **Reset lost MFA**: User detail page → select method → reset or delete → user re-enrolls on next MFA prompt

## Related Docs
- Security Policies (authentication frequency configuration)
- webauthn.me/browser-support (WebAuthn compatibility reference)
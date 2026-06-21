# Native MFA (Twingate)

## Summary
Twingate provides native MFA configurable independently of your identity provider, applicable at sign-in, on specific Resources, or for Admin Console access. MFA is managed at the policy level with per-scope authentication frequency settings.

## Key Information
- MFA can be enforced at three scopes: Sign In Policy, Resource Policies, Admin Console (Settings)
- Authentication frequency is inherited from the policy where MFA is enabled
- TOTP is always configured as a backup even when biometrics/security keys are primary method
- Admins can reset individual user MFA methods from the user detail page in Admin Console

## Prerequisites
- Admin access to Twingate Admin Console
- Security policies already configured (Sign In Policy and/or Resource Policies)

## Configuration Locations

| Scope | Location | Effect |
|-------|----------|--------|
| Sign-in | Sign In Policy | MFA required on every Client sign-in |
| Resource access | Resource Policy | MFA required when accessing specific Resources |
| Admin Console | Settings → Security | MFA required for admin console login |

## Supported MFA Methods
- **TOTP**: Google Authenticator, Authy, 1Password (always required as backup)
- **Biometrics (WebAuthn)**: Touch ID, Windows Hello
- **Security Keys (WebAuthn)**: YubiKey — FIDO2/CTAP2 only

## Gotchas
- **Do not enable MFA in both Twingate and your IdP** — users will be prompted twice per authentication
- WebAuthn support varies by platform/browser; some environments may not support biometrics or security keys (check [webauthn.me/browser-support](https://webauthn.me/browser-support))
- Only FIDO2/CTAP2 security keys are supported — older FIDO U2F-only keys will not work
- Users with biometrics/security key configured still must set up TOTP as fallback

## Managing MFA Resets
1. Navigate to the user's detail page in Admin Console
2. Select the MFA method to reset or delete
3. User is guided through MFA setup on next authentication prompt

## Related Docs
- Security Policies (linked in source)
- [WebAuthn browser compatibility](https://webauthn.me/browser-support)
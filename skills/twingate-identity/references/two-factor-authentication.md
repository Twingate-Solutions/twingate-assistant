# Two-Factor Authentication

## Summary
Twingate provides native 2FA configured at the Security Policy level, supporting TOTP, biometrics (WebAuthn), and hardware security keys. 2FA frequency is controlled by session lifetime settings. Using both Twingate 2FA and IdP 2FA simultaneously is not recommended as it forces double authentication.

## Key Information
- 2FA is configured per **Security Policy**, not globally per user
- Three enforcement scopes:
  - **Network Sign In Policy**: requires 2FA on every login
  - **Admin Console Security settings**: requires 2FA for admin console access
  - **Resource-specific Security Policies**: requires 2FA only when accessing specific resources
- Session lifetime determines 2FA frequency (e.g., 24-hour session = daily 2FA prompt)
- TOTP is always required as backup even when biometrics/security key is configured

## Supported 2FA Methods
| Method | Details |
|--------|---------|
| TOTP | Third-party authenticator app (time-based codes) |
| Biometrics (WebAuthn) | TouchID, Windows Hello |
| Security Keys (WebAuthn) | FIDO2/CTAP2 only (e.g., YubiKey) |

## Prerequisites
- Security Policy configured in Twingate admin
- Do **not** enable 2FA at both IdP and Twingate levels (causes double authentication)
- WebAuthn requires compatible platform/browser (support varies)

## Configuration
- Navigate to Security Policy settings to enable 2FA
- Admin Console 2FA: **Settings → Security**
- Resource 2FA: assign Security Policy with 2FA enabled to specific resources

## User Management
- Reset lost 2FA: navigate to user → select authentication option → reset or delete
- After reset, user goes through initial 2FA setup on next authentication prompt

## Gotchas
- Users with biometrics/security key **still must configure TOTP** as backup
- Only **FIDO2/CTAP2** security keys supported — older U2F keys may not work
- WebAuthn support varies by browser/platform — check [compatibility](https://webauthn.io) for edge cases
- Session lifetime setting directly controls 2FA prompt frequency, not login state
- Enabling IdP 2FA + Twingate 2FA simultaneously results in users completing 2FA twice per session

## Related Docs
- Security Policy configuration documentation (linked inline)
- WebAuthn browser/platform compatibility reference
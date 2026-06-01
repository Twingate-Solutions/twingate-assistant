# Two-Factor Authentication

## Summary
Twingate provides native 2FA configured at the Security Policy level, supporting TOTP, biometrics (WebAuthn), and hardware security keys. 2FA frequency is controlled by the Security Policy session lifetime. Do not combine Twingate 2FA with IdP 2FA, as users will be double-prompted.

## Key Information
- 2FA is configured per **Security Policy**, not globally per user
- Three enforcement scopes:
  - **Network Sign In Policy**: requires 2FA on every login
  - **Admin Console Security settings**: requires 2FA for admin console access
  - **Resource-specific Security Policies**: requires 2FA only when accessing specific resources
- Session lifetime controls 2FA frequency (e.g., 24-hour lifetime = daily 2FA prompt even if user stays logged in)
- TOTP is always required as backup even when biometrics/security key are configured

## Supported 2FA Methods
| Method | Notes |
|--------|-------|
| TOTP | Third-party authenticator app (e.g., Google Authenticator, Authy) |
| Biometrics (WebAuthn) | TouchID, Windows Hello |
| Security Keys (WebAuthn) | YubiKey; **FIDO2/CTAP2 only** |

## Prerequisites
- Security Policy configured in Twingate admin console
- Do **not** enable 2FA at both IdP and Twingate levels simultaneously

## Configuration
- Navigate to **Security Policy** settings to enable 2FA
- Admin console 2FA: **Settings → Security**
- Resource-level 2FA: assign a 2FA-enabled Security Policy to specific resources

## User 2FA Reset
1. Navigate to the affected user in Admin Console
2. Select **reset** or **delete** on the specific authentication option
3. User will be prompted through initial 2FA setup on next authentication attempt

## Gotchas
- Users with biometrics/security keys **must also configure TOTP** as a backup — no exceptions
- WebAuthn support varies by platform and browser; not universally supported
- Only **FIDO2/CTAP2** security keys are supported (older U2F-only keys will not work)
- Combining IdP 2FA + Twingate 2FA results in users completing 2FA twice per login
- Session lifetime governs re-prompt frequency, not login/logout state

## Related Docs
- Security Policy configuration documentation (linked inline)
- WebAuthn browser/platform support matrix (external link referenced in page)
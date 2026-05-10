# Two-Factor Authentication Overview

## Summary
Twingate provides native 2FA configured at the Security Policy level, supporting TOTP, biometrics (WebAuthn), and hardware security keys. 2FA frequency is controlled by session lifetime settings. Using both Twingate 2FA and IdP 2FA simultaneously is not recommended as it forces users to authenticate twice.

## Key Information
- 2FA is configured per **Security Policy**, not globally per user
- Three scopes for 2FA enforcement:
  - **Network Sign In Policy** – required every login
  - **Admin Console Security settings** – required for admin console access
  - **Resource-specific Security Policies** – required only when accessing specific resources
- Session lifetime on the Security Policy controls 2FA frequency (e.g., 24-hour session = daily 2FA prompt)
- Users with biometrics/security keys are **also required to configure TOTP** as a backup method

## Supported 2FA Methods
| Method | Details |
|--------|---------|
| TOTP | Third-party authenticator app (e.g., Google Authenticator, Authy) |
| Biometrics (WebAuthn) | TouchID, Windows Hello |
| Security Keys (WebAuthn) | FIDO2/CTAP2 keys only (e.g., YubiKey) |

## Prerequisites
- Security Policies must be configured before enabling 2FA
- Users must have a supported device/browser for WebAuthn options
- FIDO2/CTAP2 compliance required for hardware security keys (older FIDO U2F keys may not work)

## Configuration
- Navigate to **Security Policy** settings to enable 2FA
- For admin console 2FA: **Settings → Admin Console Security**
- Set session lifetime on the policy to control re-authentication frequency

## User Management
- To reset a user's 2FA: Navigate to the user → select reset or delete the specific authentication option
- After reset, user completes initial setup flow on next 2FA prompt
- Handles lost device or lost authenticator access scenarios

## Gotchas
- **Do not enable both IdP 2FA and Twingate 2FA** – users will be prompted twice per login
- TOTP setup is mandatory even when biometrics/security key is configured (backup requirement)
- WebAuthn support varies by platform and browser – verify environment compatibility before deploying
- Only **FIDO2/CTAP2** security keys are supported; older standards are not compatible
- Resource-level 2FA triggers on resource access, not on login – users may be logged in but still prompted when hitting a protected resource

## Related Docs
- Security Policy configuration documentation (linked in source)
- WebAuthn browser/platform compatibility: [webauthn.me](https://webauthn.me) or similar compatibility reference
- Twingate Security Policies overview
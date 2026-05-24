# Two-Factor Authentication Overview

## Summary
Twingate provides native 2FA configured at the Security Policy level, supporting TOTP, biometrics, and security keys. Session lifetime controls 2FA frequency. Twingate recommends using their native 2FA instead of IdP 2FA to avoid double authentication prompts.

## Key Information
- 2FA is configured per **Security Policy**, not globally per user
- Three enforcement contexts:
  - **Network Sign In Policy** – requires 2FA on every user login
  - **Admin Console Security settings** – requires 2FA for admin console access
  - **Resource-specific Security Policies** – requires 2FA only when accessing specific resources
- Session lifetime determines 2FA frequency (e.g., 24-hour session = daily 2FA prompt even if user stays logged in)
- Don't configure 2FA in both Twingate and your IdP — users will be prompted twice

## Supported 2FA Methods
| Method | Details |
|--------|---------|
| TOTP | Time-based one-time codes via authenticator app |
| Biometrics (WebAuthn) | TouchID, Windows Hello, device-based biometrics |
| Security Keys (WebAuthn) | YubiKey and other FIDO2/CTAP2 keys only |

## Prerequisites
- Security Policy configured in Twingate admin
- Users must always configure TOTP even if biometrics/security key is set (backup method requirement)
- WebAuthn requires supported platform/browser (check [compatibility](https://webauthn.me/browser-support))

## Configuration Notes
- **Security Keys**: Only FIDO2/CTAP2 keys supported (not older U2F-only keys)
- **WebAuthn**: Platform and browser support varies — not universally available

## User 2FA Reset (Admin Action)
1. Navigate to the user in Admin Console
2. Select the authentication option to reset or delete
3. User is prompted through initial 2FA setup flow on next authentication

## Gotchas
- Users with biometrics/security keys **still must configure TOTP** as a backup
- Session lifetime drives re-authentication frequency — short sessions = frequent 2FA prompts
- WebAuthn may not work in all environments; TOTP is the universal fallback
- Enabling 2FA at both IdP and Twingate levels causes duplicate 2FA challenges for end users

## Related Docs
- Security Policy configuration documentation (linked in page)
- WebAuthn browser compatibility reference
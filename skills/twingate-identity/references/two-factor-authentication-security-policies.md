# Two-Factor Authentication Security Policies

## Summary
Controls whether users are prompted for 2FA when accessing Resources, signing into a Network, or the Admin Console. Uses industry-standard TOTP format, with optional biometric or security key alternatives. Can be applied at multiple policy levels.

## Key Information
- **Applicability**: Resource Policies, Minimum Authentication Requirements, Admin Console Security
- **TOTP standard**: Compatible with any TOTP authenticator app (Google Authenticator, Authy, etc.)
- **Additional methods**: After TOTP setup, users can also register biometric (Touch ID, Windows Hello) or security keys (YubiKey)
- **Code delivery**: QR code scan or alphanumeric ID entry for mobile setup

## Prerequisites
- TOTP-based authenticator app installed on Android or iOS
- Admin must configure 2FA rule in either Resource Policy or Minimum Authentication Requirements

## Step-by-Step (User Setup)
1. Authenticate with credentials — notification appears if 2FA not yet configured
2. Open authenticator app → add new application
3. Scan QR code with camera, or enter alphanumeric ID manually (easier on mobile)
4. Enter generated TOTP code to confirm setup
5. Optionally enroll biometric method or security key via browser flow

## Configuration Values
| Setting | Options |
|---|---|
| Policy Scope | Resource Policies, Minimum Authentication Requirements, Admin Console Security |
| 2FA Method | TOTP (required first), then biometric or security key (optional additions) |

## Gotchas
- **Do not apply 2FA rules to both Minimum Authentication Requirements AND Resource Policies** — users will be prompted twice
- **Do not delete the authenticator app or Twingate entry** — losing access requires Admin to reset 2FA for that user
- If 2FA access is lost, only an Admin can reset it; user must reconfigure from scratch
- Biometric/security key enrollment happens through browser redirect after initial TOTP setup

## Related Docs
- [Two-Factor Authentication general documentation](#) (linked in source)
- [TOTP standard](https://en.wikipedia.org/wiki/Time-based_one-time_password)
- Resource Policies configuration
- Minimum Authentication Requirements configuration
- Admin Console Security settings
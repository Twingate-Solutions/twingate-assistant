# Two-Factor Authentication Security Policies

## Summary
Controls whether users are prompted for 2FA when accessing Resources, signing into Networks, or accessing the Admin Console. Uses industry-standard TOTP format with support for additional biometric/hardware key methods. Configuration applies at policy level, not per-user.

## Key Information
- Applies to: Resource Policies, Minimum Authentication Requirements, Admin Console Security
- TOTP-based; compatible with any TOTP authenticator app (Google Authenticator, etc.)
- After TOTP setup, users are prompted to optionally enroll biometric (Touch ID, Windows Hello) or security key (YubiKey)
- Biometric/security key enrollment routes through the browser to complete

## Prerequisites
- TOTP authenticator app installed on Android or iOS
- Admin must configure 2FA rule in at least one policy location

## Setup Steps (User-Facing)
1. Authenticate with credentials — notification appears if 2FA not yet configured
2. Open authenticator app, add new application
3. Scan QR code (or manually enter alphanumeric ID if setting up from phone)
4. Enter generated code to confirm setup
5. Optionally enroll biometric method or security key via browser flow

## Configuration Values
| Scope | Options |
|---|---|
| Resource Policies | Enable/require 2FA per resource |
| Minimum Authentication Requirements | Network-wide 2FA requirement |
| Admin Console Security | Admin login 2FA |

## Gotchas
- **Do not set 2FA on both Minimum Authentication Requirements AND Resource Policies** — users will be prompted twice
- **Do not delete the authenticator app or Twingate entry** — loss of access requires Admin to reset 2FA for the user
- If TOTP access is lost, the Twingate Admin must reset the user's 2FA before re-enrollment is possible

## Related Docs
- [Two-Factor Authentication general documentation](#) (linked inline)
- [TOTP standard](https://en.wikipedia.org/wiki/Time-based_one-time_password)
- Resource Policies configuration
- Minimum Authentication Requirements configuration
# Two-Factor Authentication Security Policies

## Summary
Controls whether users are prompted for 2FA when accessing Resources, signing into Networks, or accessing the Admin Console. Uses industry-standard TOTP format, with optional biometric or security key methods as alternatives.

## Key Information
- **Applicability**: Resource Policies, Minimum Authentication Requirements, Admin Console Security
- TOTP-based; compatible with any TOTP authenticator app (Google Authenticator, etc.)
- After TOTP setup, users can optionally enroll biometric (Touch ID, Windows Hello) or security key (YubiKey) as additional 2FA methods
- Biometric/security key enrollment is completed via browser flow

## Prerequisites
- A TOTP-compatible authenticator app installed on Android or iOS
- Admin must configure 2FA rule on either Resource Policies **or** Minimum Authentication Requirements (not both)

## Configuration Steps
1. Trigger 2FA setup by authenticating — a notification prompts setup if 2FA is required but not configured
2. Open authenticator app and add a new account
3. Scan the QR code (or enter alphanumeric ID manually if on mobile)
4. Confirm setup by entering the generated code
5. Optionally enroll a biometric method or security key via browser prompt

## Gotchas
- **Do not set 2FA on both Minimum Authentication Requirements AND Resource Policies** — users will be prompted twice
- **Do not delete the authenticator app or Twingate entry** — loss of access requires Admin to reset 2FA for the user
- If TOTP access is lost, only an Admin can reset; self-service recovery is not available

## Configuration Values
| Method | Details |
|--------|---------|
| TOTP | Industry-standard; any TOTP app supported |
| Biometric | Touch ID, Windows Hello (browser-enrolled) |
| Security Key | YubiKey and similar (browser-enrolled) |

## Related Docs
- [Two-Factor Authentication general documentation](https://www.twingate.com/docs/two-factor-authentication-security-policies)
- Resource Policies configuration
- Minimum Authentication Requirements configuration
- Admin Console Security settings
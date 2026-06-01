# Two-Factor Authentication Security Policies

## Summary
Twingate's 2FA rule controls whether users are prompted for two-factor authentication when accessing Resources, signing into a Network, or accessing the Admin Console. It uses TOTP-based authentication and supports biometric methods and security keys as alternatives.

## Key Information
- **Applicability**: Resource Policies, Minimum Authentication Requirements, Admin Console Security
- **TOTP standard**: Compatible with any TOTP authenticator app (Google Authenticator, Authy, etc.)
- **Additional methods after TOTP setup**: Biometric (Touch ID, Windows Hello) or hardware security keys (YubiKey)
- **Registration flow**: Browser-based for biometric/security key enrollment

## Prerequisites
- TOTP authenticator app installed on Android or iOS
- Initial TOTP setup must be completed before biometric/security key options are available

## Step-by-Step: TOTP Setup
1. Add new application in your authenticator app
2. Scan QR code with camera (or enter alphanumeric ID manually if on mobile)
3. Confirm setup by entering the generated code
4. Optionally enroll biometric method or security key via browser prompt

## Configuration Values
| Scope | Options |
|-------|---------|
| Resource Policies | Enable/disable 2FA requirement per resource |
| Minimum Authentication Requirements | Network-level 2FA enforcement |
| Admin Console Security | Admin access 2FA enforcement |

## Gotchas
- **Double-prompt risk**: Do not set 2FA on both Minimum Authentication Requirements AND Resource Policies simultaneously — users will be prompted twice
- **App deletion = lockout**: Deleting the authenticator app or Twingate TOTP entry locks the user out of all 2FA-protected resources and networks
- **Recovery requires admin**: Lost authenticator access requires Admin to reset the user's 2FA; no self-service recovery
- Biometric/security key enrollment is only available after TOTP is configured first

## Related Docs
- Two-Factor Authentication general documentation (linked internally)
- Resource Policies
- Minimum Authentication Requirements
- Admin Console Security settings
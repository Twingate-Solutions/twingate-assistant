# Two-Factor Authentication Security Policies

## Summary
Twingate's 2FA security rule controls whether users are prompted for two-factor authentication when accessing Resources, signing into Networks, or accessing the Admin Console. It uses TOTP-based authentication with optional biometric or hardware key alternatives.

## Key Information
- Applies to: Resource Policies, Minimum Authentication Requirements, Admin Console Security
- TOTP standard format used for code generation
- Biometric methods (Touch ID, Windows Hello) and security keys (YubiKey) are supported as additional options after TOTP setup
- Admin can reset a user's 2FA if access to authenticator app is lost

## Prerequisites
- TOTP-compatible authenticator app (e.g., Google Authenticator for Android/iOS)
- Admin must configure 2FA rule in at least one policy location
- Browser access required for biometric/security key registration

## Configuration Values
- **Policy locations**: Resource Policies, Minimum Authentication Requirements, Admin Console Security
- **Supported 2FA methods**:
  - TOTP (primary)
  - Biometric (Touch ID, Windows Hello)
  - Security key (YubiKey)

## Step-by-Step: User 2FA Setup
1. Authenticate with credentials — notification appears if 2FA not yet configured
2. Open authenticator app and add new application
3. Scan QR code (or manually enter alphanumeric ID if on mobile)
4. Enter generated code to confirm setup
5. Optionally register biometric method or security key via browser prompt

## Gotchas
- **Double-prompt risk**: Setting 2FA on both Minimum Authentication Requirements AND Resource Policies causes users to authenticate twice — use one or the other
- **Lost authenticator app**: User loses all access to 2FA-protected Resources/Networks; Admin must manually reset the user's 2FA
- **Do not delete** the Twingate TOTP entry from the authenticator app

## Related Docs
- [Two-Factor Authentication general documentation](https://www.twingate.com/docs/)
- [TOTP standard](https://en.wikipedia.org/wiki/Time-based_one-time_password)
- Google Authenticator: [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2), [iOS](https://apps.apple.com/app/google-authenticator/id388497605)
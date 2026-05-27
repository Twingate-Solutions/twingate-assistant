# Two-Factor Authentication Security Policies

## Summary
Controls whether users are prompted for 2FA when accessing Resources, signing into Networks, or the Admin Console. Uses TOTP standard with support for additional biometric/hardware key methods. Can be scoped to Resource Policies, Minimum Authentication Requirements, or Admin Console Security.

## Key Information
- **Applicability**: Resource Policies, Minimum Authentication Requirements, Admin Console Security
- **Protocol**: Industry-standard TOTP format
- **Additional methods supported**: Biometric (Touch ID, Windows Hello) and security keys (YubiKey) — registered after initial TOTP setup
- Do **not** apply 2FA rules to both Minimum Authentication Requirements and Resource Policies simultaneously — users will be prompted twice

## Prerequisites
- A TOTP-compatible authenticator app (e.g., Google Authenticator for [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2) or [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605))
- Admin access to configure security policies

## Setup Steps (End User)
1. Trigger 2FA setup by attempting to access a 2FA-protected Resource or Network
2. Open authenticator app → add new application
3. Scan QR code shown in Twingate (or manually enter alphanumeric ID if on mobile)
4. Confirm setup by entering the generated code
5. Optionally register a biometric method or security key via browser prompt

## Configuration Values
| Scope | Description |
|-------|-------------|
| Resource Policies | Apply 2FA requirement per Resource |
| Minimum Authentication Requirements | Apply 2FA at network sign-in level |
| Admin Console Security | Apply 2FA for Admin Console access |

## Gotchas
- **Never delete** the authenticator app or Twingate entry — loss of access requires Admin to reset 2FA for the user
- Setting 2FA on **both** Minimum Authentication Requirements and Resource Policies causes double prompting
- Biometric/security key enrollment only becomes available **after** TOTP is configured first
- If a user loses their authenticator app, an Admin must manually reset their 2FA before they can re-enroll

## Admin Recovery
- Admin must reset the affected user's 2FA via the Admin Console
- User must complete full 2FA setup again after reset

## Related Docs
- [Two-Factor Authentication overview](https://www.twingate.com/docs/two-factor-authentication)
- Resource Policies documentation
- Minimum Authentication Requirements documentation
- Admin Console Security documentation
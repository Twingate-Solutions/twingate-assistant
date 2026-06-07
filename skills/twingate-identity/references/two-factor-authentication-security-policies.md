# Two-Factor Authentication Security Policies

## Summary
Twingate's 2FA security rule controls whether users are prompted for two-factor authentication when accessing Resources, signing into Networks, or the Admin Console. It uses TOTP-based authentication and supports additional methods like biometrics and security keys after initial setup.

## Key Information
- Applicable to: Resource Policies, Minimum Authentication Requirements, and Admin Console Security
- Uses industry-standard TOTP format
- Supports biometric methods (Touch ID, Windows Hello) and hardware security keys (YubiKey) as additional options after TOTP enrollment
- 2FA prompt appears after credential authentication when not yet configured

## Prerequisites
- A TOTP-compatible authenticator app (e.g., Google Authenticator for Android/iOS)
- OR identity provider mobile app with TOTP support
- Admin must configure 2FA rule on either Minimum Authentication Requirements OR Resource Policies (not both)

## Configuration Steps
1. Trigger 2FA setup by accessing a 2FA-protected Resource or Network
2. Open authenticator app and add a new application
3. Scan the QR code shown (or manually enter the alphanumeric ID if on mobile)
4. Confirm setup by entering the generated code
5. After TOTP setup, optionally enroll biometric method or security key via browser flow

## Gotchas
- **Do not apply 2FA rules to both Minimum Authentication Requirements AND Resource Policies** — users will be prompted twice
- **Do not delete the authenticator app or Twingate entry** — losing access requires an Admin to reset 2FA for that user
- Lost authenticator access = locked out of all 2FA-protected Resources/Networks until Admin resets

## Admin Actions
- Admins can reset a user's 2FA if they lose access to their authenticator app

## Related Docs
- [Two-Factor Authentication (general)](https://www.twingate.com/docs/)
- Resource Policies configuration
- Minimum Authentication Requirements
- Admin Console Security settings
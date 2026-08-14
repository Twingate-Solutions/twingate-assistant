---
source: https://www.twingate.com/docs/two-factor-authentication-security-policies
type: docs
fetched: 2026-08-14
source_version: 7879f55661bea5576a4fd54b33336420adffe4d003592e69d76d85c2d3d602c1
---

# Two-Factor Authentication Security Policies

## Summary
Twingate's 2FA security rule controls whether users must complete two-factor authentication when accessing Resources, signing into Networks, or accessing the Admin Console. It uses industry-standard TOTP and supports biometric/hardware key alternatives after initial TOTP setup.

## Key Information
- Applicable to: Resource Policies, Minimum Authentication Requirements, Admin Console Security
- TOTP-based; compatible with any standard TOTP authenticator app
- After TOTP setup, users can additionally register biometric methods (Touch ID, Windows Hello) or security keys (YubiKey)
- 2FA reset requires an Admin or Helpdesk role admin

## Prerequisites
- TOTP-compatible authenticator app (e.g., Google Authenticator for Android/iOS)
- For biometric/security key: browser-based registration flow

## Configuration

### Placement Warning
- Set 2FA on **either** Minimum Authentication Requirements **or** Resource Policies — **not both**, or users will be prompted twice

### Setup Steps
1. Apply Two-Factor Authentication rule to desired policy scope
2. User authenticates with credentials; notification appears prompting 2FA setup
3. User adds new application in authenticator app and scans QR code (or enters alphanumeric ID manually on mobile)
4. User confirms setup by entering generated TOTP code
5. User is then prompted to optionally register a biometric method or security key via browser

## Gotchas
- **Do not delete the authenticator app or Twingate entry** — loss of access to the TOTP app locks the user out of all 2FA-protected Resources/Networks
- Recovery requires an Admin or Helpdesk role admin to reset the user's 2FA
- Double-prompting occurs if 2FA rules are set at both policy levels simultaneously

## Related Docs
- [Two-Factor Authentication general documentation](https://www.twingate.com/docs/two-factor-authentication)
- [Resource Policies](https://www.twingate.com/docs/resource-policies)
- [Minimum Authentication Requirements](https://www.twingate.com/docs/minimum-authentication-requirements)
- [Admin Console Security](https://www.twingate.com/docs/admin-console-security)
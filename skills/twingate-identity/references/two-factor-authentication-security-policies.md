# Two-Factor Authentication Security Policies

## Summary
Controls whether users are prompted for 2FA when accessing Resources, signing into Networks, or signing into the Admin Console. Uses TOTP standard with optional biometric/security key enrollment. Applies as a security policy rule across multiple policy types.

## Key Information
- **Applicability**: Resource Policies, Minimum Authentication Requirements, Admin Console Security
- **Protocol**: Industry-standard TOTP format
- **Additional methods after TOTP setup**: Biometric (Touch ID, Windows Hello) or security key (YubiKey) — registered via browser
- All enrolled methods (TOTP, biometric, security key) satisfy the 2FA requirement interchangeably

## Prerequisites
- TOTP-compatible authenticator app (Google Authenticator, or IdP's own app)
- Admin must configure the 2FA rule on desired policy type before enforcement begins

## Step-by-Step: User 2FA Enrollment
1. Trigger 2FA prompt by accessing a 2FA-protected Resource or Network
2. Open authenticator app → add new application
3. Scan QR code (or manually enter alphanumeric ID if on mobile)
4. Enter generated TOTP code to confirm setup
5. (Optional) Enroll biometric method or security key via browser flow

## Configuration Values
| Setting | Notes |
|---|---|
| Apply to Resource Policies | Controls per-resource access |
| Apply to Minimum Authentication Requirements | Network-wide sign-in enforcement |
| Apply to Admin Console Security | Admin portal protection |

## Gotchas
- **Do not apply 2FA rules to both Minimum Authentication Requirements AND Resource Policies** — users will be prompted for 2FA twice
- **Never delete the authenticator app or Twingate entry** — loss of access requires Admin to reset the user's 2FA
- Admin reset required if user loses access to their TOTP app; user must re-enroll from scratch
- Biometric/security key enrollment only becomes available after initial TOTP setup is complete

## Related Docs
- [Two-Factor Authentication general documentation](https://www.twingate.com/docs/two-factor-authentication)
- [Resource Policies](https://www.twingate.com/docs/resource-policies)
- [Minimum Authentication Requirements](https://www.twingate.com/docs/minimum-authentication-requirements)
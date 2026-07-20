# Two-Factor Authentication Security Policies

## Summary
Controls whether users are prompted for 2FA when accessing Resources, signing into Networks, or accessing the Admin Console. Uses industry-standard TOTP format, with optional biometric or security key alternatives. Applies as a security policy rule within Twingate's policy framework.

## Key Information
- **Applicability**: Resource Policies, Minimum Authentication Requirements, Admin Console Security
- **Protocol**: TOTP (Time-based One-Time Password)
- **Supported authenticators**: Any TOTP-compatible app (Google Authenticator, Authy, etc.) or identity provider mobile apps
- **Additional methods**: Biometric (Touch ID, Windows Hello) or hardware security key (YubiKey) — registered after initial TOTP setup
- **Code loss = lockout**: Lost authenticator app requires Admin to reset 2FA for the user

## Prerequisites
- A TOTP-compatible authenticator app installed on Android or iOS
- Admin must have 2FA rule configured in either Resource Policies OR Minimum Authentication Requirements (not both)

## Step-by-Step: Setting Up 2FA (User)
1. Trigger 2FA enrollment by accessing a protected Resource or Network
2. Open authenticator app → add new account
3. Scan the QR code (or manually enter the alphanumeric ID if on mobile)
4. Enter the generated code to confirm setup
5. Optionally enroll a biometric method or security key via browser prompt

## Configuration Values

| Setting | Notes |
|---|---|
| Apply to Resource Policy | Prompts 2FA per-resource access |
| Apply to Minimum Authentication Requirements | Network-level 2FA requirement |
| Apply to Admin Console Security | Protects admin login |

## Gotchas
- **Do not apply 2FA rules to both** Resource Policies and Minimum Authentication Requirements simultaneously — users will be prompted twice
- **Do not delete** the authenticator app or Twingate entry within it — no self-service recovery exists
- If authenticator access is lost, an Admin must manually reset the user's 2FA
- Biometric/security key enrollment occurs **after** TOTP setup is complete, not as a standalone replacement

## Related Docs
- [Twingate 2FA documentation](#) (referenced inline)
- [TOTP standard](https://en.wikipedia.org/wiki/Time-based_one-time_password)
- Resource Policies configuration
- Minimum Authentication Requirements
- Admin Console Security policies
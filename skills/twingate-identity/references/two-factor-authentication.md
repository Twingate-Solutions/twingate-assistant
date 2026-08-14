---
source: https://www.twingate.com/docs/two-factor-authentication
type: docs
fetched: 2026-08-14
source_version: 52d84e6f94f5474093a42eae093ec5119172fa16345822f9494447fe31134db7
---

# Twingate Native MFA

## Summary
Twingate provides native MFA independent of identity provider configuration, applicable at sign-in, resource access, or Admin Console login. MFA is configured at the policy level with configurable authentication frequency. Three MFA methods are supported: TOTP, biometrics (WebAuthn), and security keys (WebAuthn).

## Key Information
- MFA operates independently from IdP-level MFA — enabling both forces users to complete MFA twice
- MFA frequency is tied to the policy's authentication frequency setting (e.g., once per 24 hours)
- TOTP is always configured as a backup even when biometrics/security keys are primary method
- Admin or Helpdesk role required to reset user MFA methods

## Prerequisites
- Access to Twingate Admin Console
- Security policies configured (Sign In Policy or Resource Policies)
- Users must have a supported authenticator app, biometric-capable device, or FIDO2/CTAP2 security key

## Configuration Locations

| Scope | Location | Effect |
|---|---|---|
| Sign-in | Sign In Policy | MFA required every client sign-in |
| Resource access | Resource Policies | MFA required when accessing specific Resources |
| Admin Console | Settings → Admin Console Security | MFA required for admin logins |

## Supported MFA Methods
- **TOTP**: Google Authenticator, Authy, 1Password (always configured as backup)
- **Biometrics (WebAuthn)**: Touch ID, Windows Hello
- **Security Keys (WebAuthn)**: YubiKey — FIDO2/CTAP2 only

## Admin: Reset User MFA
1. Navigate to user's detail page in Admin Console
2. Select the authentication method to reset or delete
3. User completes setup flow on next MFA prompt

## Gotchas
- **Double MFA**: Do not enable native MFA if IdP already enforces MFA — users will authenticate twice
- **Security key compatibility**: Only FIDO2/CTAP2 keys supported; older U2F-only keys will not work
- **WebAuthn limitations**: Browser/platform support varies; check [webauthn.me/browser-support](https://webauthn.me/browser-support) for compatibility
- **Backup TOTP requirement**: Users registering biometrics or security keys must also configure TOTP — cannot skip backup method setup
- **New devices**: Biometric and security key credentials are device-bound; users will need TOTP backup on new devices

## Related Docs
- Security Policies (policy-level configuration)
- Sign In Policy (authentication frequency settings)
- Resource Policies (per-resource MFA configuration)
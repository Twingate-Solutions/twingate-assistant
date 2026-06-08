# Native MFA (Twingate)

## Summary
Twingate provides native MFA that operates independently of your identity provider, configurable at sign-in, per-resource, or for Admin Console access. MFA is managed at the policy level with configurable authentication frequency. Supports TOTP, biometrics (WebAuthn), and FIDO2 security keys.

## Key Information
- MFA configured at policy level, not globally
- Three distinct scopes: Sign In Policy, Resource Policies, Admin Console
- Authentication frequency tied to the respective policy's settings
- TOTP always configured as backup even when biometrics/security key is primary method
- Admins can reset individual MFA methods from user detail page in Admin Console

## Prerequisites
- Admin Console access
- Users must have compatible authenticator app (for TOTP) or WebAuthn-capable device/browser

## Configuration Locations

| Scope | Location | Effect |
|-------|----------|--------|
| Sign-in | Sign In Policy | MFA on every client sign-in |
| Per-resource | Resource Policies | MFA when accessing specific resources |
| Admin Console | Settings > Admin Console Security | MFA for admin logins |

## Supported MFA Methods
- **TOTP**: Google Authenticator, Authy, 1Password, etc.
- **Biometrics (WebAuthn)**: Touch ID, Windows Hello
- **Security Keys (WebAuthn)**: YubiKey; **FIDO2/CTAP2 only**

## Step-by-Step: Reset User MFA
1. Navigate to user's detail page in Admin Console
2. Select the authentication method to reset or delete
3. User completes setup flow on next MFA prompt

## Gotchas
- **Do not enable MFA in both Twingate and your IdP** — users will be prompted twice per authentication
- Biometric/security key users are still required to configure TOTP as backup
- WebAuthn support varies by browser/platform — check [webauthn.me/browser-support](https://webauthn.me/browser-support) for compatibility
- Only FIDO2/CTAP2 security keys are supported; older U2F-only keys may not work

## Related Docs
- Security Policies (policy-level configuration)
- Sign In Policy (authentication frequency settings)
- Resource Policies (per-resource MFA)
# Native MFA

## Summary
Twingate provides native MFA independent of your identity provider, configurable at sign-in, resource access, or Admin Console levels. Supports TOTP, biometrics (WebAuthn), and hardware security keys. MFA frequency is tied to the authentication frequency of the policy where it's enabled.

## Key Information
- MFA is policy-level configuration, not account-level
- Three enforcement scopes: Sign In Policy, Resource Policies, Admin Console Security (Settings)
- Resource Policy MFA useful for protecting only sensitive resources
- TOTP always configured as backup even when biometrics/security key is primary method
- Admin MFA reset available from user detail page in Admin Console

## Prerequisites
- Admin Console access
- Users need a TOTP app (Google Authenticator, Authy, 1Password) and/or WebAuthn-capable device/key

## Configuration Locations

| Scope | Location | Effect |
|-------|----------|--------|
| Sign-in | Sign In Policy | MFA required every client login |
| Resource access | Resource Policies | MFA required per resource access |
| Admin Console | Settings → Security | MFA required for admin login |

## Supported MFA Methods
- **TOTP**: Time-based codes via authenticator app
- **Biometrics (WebAuthn)**: Touch ID, Windows Hello
- **Security Keys (WebAuthn)**: YubiKey — FIDO2/CTAP2 only

## Gotchas
- **Do not enable MFA in both Twingate and your IdP** — users will be prompted twice per authentication
- Authentication frequency (how often MFA is re-prompted) is inherited from the policy's auth frequency setting, not separately configurable
- WebAuthn support varies by platform/browser — check [webauthn.me/browser-support](https://webauthn.me/browser-support)
- TOTP backup is always required when biometrics or security key is configured — cannot be skipped

## Admin Operations
- **Reset user MFA**: User detail page → select method → reset or delete
- User is re-prompted through setup flow on next MFA challenge after reset

## Related Docs
- Security Policies (linked in source)
- Sign In Policy configuration
- Resource Policy configuration
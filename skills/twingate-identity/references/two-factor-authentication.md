# Native MFA

## Summary
Twingate provides native MFA configurable independently of an identity provider. MFA can be required at sign-in, for specific Resources via policies, or for Admin Console access. Avoid enabling MFA in both Twingate and your IdP simultaneously to prevent double authentication prompts.

## Key Information
- MFA is configured at the **policy level**, not per-user
- Three scopes: Sign In Policy, Resource Policies, Admin Console Security (Settings)
- Authentication frequency is inherited from the policy's configured frequency
- Even when using biometrics/security keys, TOTP is always required as a backup method

## Supported MFA Methods
| Method | Details |
|--------|---------|
| TOTP | Google Authenticator, Authy, 1Password, etc. |
| Biometrics (WebAuthn) | Touch ID, Windows Hello |
| Security Keys (WebAuthn) | FIDO2/CTAP2 keys only (e.g., YubiKey) |

## Configuration Locations
- **Sign In Policy** → MFA on every client sign-in
- **Resource Policy** → MFA on access to specific Resources (useful for sensitive Resources)
- **Settings → Admin Console Security** → MFA for admin sign-ins

## Step-by-Step: Reset User MFA
1. Navigate to user's detail page in Admin Console
2. Select the authentication method to reset or delete
3. User is guided through setup flow on next MFA prompt

## Gotchas
- **Do not enable MFA in both Twingate and your IdP** — users will be prompted twice
- TOTP backup is always configured even when biometrics/security keys are primary method
- WebAuthn (biometrics/security keys) support varies by platform and browser — check [webauthn.me/browser-support](https://webauthn.me/browser-support)
- Only **FIDO2/CTAP2** security keys are supported; older FIDO U2F-only keys will not work

## Related Docs
- Security Policies
- Sign In Policy configuration
- Resource Policy configuration
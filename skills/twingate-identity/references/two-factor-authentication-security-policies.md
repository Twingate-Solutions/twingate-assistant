---
source: https://www.twingate.com/docs/two-factor-authentication-security-policies
type: docs
fetched: 2026-11-13
source_version: de1b0677e80f7c042d5649c6fa242237dd47e13780ad15e869d2a00711681377
trust: official
---

# Page Title
Two-Factor Authentication (Twingate Security Policies)

## Summary
This rule controls whether users are prompted for two-factor authentication (2FA) when accessing a Resource, signing in to the Network, or signing in to the Admin Console. Twingate 2FA uses standard TOTP codes, with biometrics and security keys available as additional methods after TOTP setup.

## Key Information
- **Applies to:** Resource Policies, the Sign In Policy, and Admin Console Security.
- **Recommendation:** Set a 2FA rule on either the Sign In Policy or Resource Policies, not both. Setting both makes users complete 2FA twice.
- **TOTP:** Any TOTP-based authenticator app works on Android or iOS (e.g., Google Authenticator). An identity provider's mobile app may also offer this.
- **Re-prompting:** Users must enter a 2FA code each time the authentication frequency of a 2FA-requiring policy expires.
- **Additional methods:** After TOTP setup, users are prompted to set up a biometric method (Touch ID, Windows Hello) or register a security key (YubiKey). Either can satisfy the 2FA requirement.

## Prerequisites
- A policy (Resource, Sign In, or Admin Console) with the 2FA rule enabled.
- A TOTP-capable authenticator app on the user's phone.
- For biometrics or security keys: a browser and device that support them.

## Step-by-Step (User Enrollment)
1. Authenticate with credentials. If 2FA is required and not yet set up, a notification appears.
2. In the authenticator app, add a new application.
3. Scan the QR code with the phone camera. If setting up from the phone itself, enter the alphanumeric ID instead.
4. Enter the code generated in the app to confirm setup.
5. Optionally, enroll a biometric method or security key when prompted. Registration completes in the browser.

## Configuration Values
- No env vars, CLI flags, or API parameters are listed on this page.
- Format: TOTP.
- Policy setting: the 2FA rule on the policy, combined with the policy's authentication frequency.

## Gotchas
- Enabling 2FA on both the Sign In Policy and Resource Policies causes double prompts.
- Do not delete the authenticator app or the Twingate entry in it. If access is lost, the user cannot reach 2FA-protected Resources or Networks.
- Recovery requires a Twingate admin with the Admin or Helpdesk role to reset the user's 2FA, after which the user must set up 2FA again.
- Biometric and security key enrollment happens through the browser.

## Related Docs
- Twingate general two-factor authentication documentation (linked from the page as "documentation")
- Resource Policies
- Sign In Policy
- Admin Console Security
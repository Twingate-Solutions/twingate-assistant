## Two-Factor Authentication (Policy Rule)

The 2FA rule controls whether users are prompted for **two-factor authentication** when accessing a Resource, signing in to the Twingate environment, or signing in to the Admin Console.

**Applicability:**
- Resource Policies
- Minimum Authentication Requirements (MAR)
- Admin Console Security

**Recommended Pattern:**
- **Set 2FA on Resource Policies** for sensitive Resources (focused enforcement)
- **OR** set 2FA on MAR (blanket enforcement)
- **NOT both** -- otherwise users complete 2FA twice on each access flow

Per /docs/security-policies-best-practices: enforce at Resource Policy layer for tighter scope and less prompt fatigue.

### Configuration & Setup Flow

When 2FA is required and not yet configured:
- After authenticating with credentials, user sees a 2FA setup notification
- Twingate uses **TOTP** (industry-standard time-based one-time passwords)
- Compatible with any TOTP authenticator app (Google Authenticator, Authy, 1Password, IdP-vendor mobile app, etc.)

**TOTP Setup:**
- Add a new application in the authenticator app
- Scan the QR code OR enter the alphanumeric ID manually (easier on mobile-only setup)
- Confirm with a generated code

**Additional 2FA Methods (after TOTP):**
After TOTP is set up, the user is prompted to enroll **either**:
- **Biometric** (Touch ID, Face ID, Windows Hello)
- **Security Key** (YubiKey or other FIDO2/CTAP2 hardware key)

Registration completes via the browser. Once registered, the user can use **any** of their enrolled methods to satisfy the 2FA requirement.

**Why TOTP is Always Required (Even with Biometric/SecKey):**
- TOTP serves as the **portable backup** -- the user can authenticate from a new device (e.g., replacement laptop) using only their phone's authenticator
- Biometric/security key are tied to specific hardware -- losing the device strands the user without TOTP

### Recovery -- "I Lost My Phone"

If a user loses their authenticator app or device:
- They cannot self-recover -- they will be locked out of 2FA-protected Resources
- A Twingate Admin must:
  - Navigate to the user in the Admin Console
  - Reset/delete the user's 2FA configuration
- The user goes through 2FA setup again on next access

**Critical Operational Note:**
- Tell users **never to delete** the Twingate code from their authenticator app
- Document the admin reset procedure in your runbook

**Decision Notes:**
- Apply 2FA at the Resource Policy level for the risk-tier model (High and Medium tiers; skip for Very Low)
- For headless/Service Account access: 2FA cannot be satisfied -- design these Resources without a 2FA requirement
- Don't double-enforce in Twingate + IdP -- pick one layer for 2FA

**Gotchas:**
- WebAuthn (biometric / security key) support varies by platform and browser -- verify your fleet's environment
- Only FIDO2/CTAP2 security keys are supported -- older U2F-only keys are not
- TOTP is mandatory; users will be prompted to set it up even after enrolling biometric

**Related Docs:**
- /docs/two-factor-authentication -- 2FA overview + supported methods
- /docs/authentication -- Re-auth frequency rule (companion)
- /docs/security-policies -- Policy types overview
- /docs/security-policies-best-practices -- Where to enforce 2FA in the risk model

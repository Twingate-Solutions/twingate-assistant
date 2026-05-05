## Two-Factor Authentication Overview

Twingate's native 2FA -- supports TOTP, biometrics (WebAuthn), and FIDO2 security keys. Recommended **instead of** IdP-provided 2FA for finer-grained Twingate-specific policy control.

**Why Use Twingate Native 2FA Instead of IdP 2FA:**
- More granular policy control (per-Resource enforcement)
- Avoids double-2FA UX if you also have IdP-level 2FA
- Recommendation: pick one layer (IdP **or** Twingate), not both

**Where 2FA Applies:**

| Layer | Effect |
|---|---|
| **MAR (Network Sign In)** | Required on every Twingate sign-in (blanket) |
| **Admin Console Security** | Required only for admins signing in to the Admin Console |
| **Resource Policy** | Required only when accessing the specific Resource |

Per /docs/security-policies-best-practices: prefer **Resource Policy** scope so users only do 2FA when actually needed.

**Session Lifetime Determines Frequency:**
- Set on the Security Policy
- Example: Resource Policy with 2FA + 24-hour session -> user does 2FA once a day on Resource access
- Even if logged in continuously, 2FA is required each time the session expires

### Supported 2FA Methods

| Method | Notes |
|---|---|
| **TOTP** | Time-based one-time password via authenticator app -- always required as a backup |
| **Biometrics (WebAuthn)** | Touch ID, Face ID, Windows Hello, fingerprint sensors |
| **Security Keys (WebAuthn)** | FIDO2/CTAP2 only (e.g., YubiKey) -- older U2F keys NOT supported |

**TOTP is Mandatory Backup:**
- Even after enrolling biometrics or a security key, TOTP setup is still required
- Reason: portable recovery -- users can authenticate on a new device with only their phone's authenticator
- Biometric/SecKey are bound to specific hardware; TOTP follows the user

**Setting Up TOTP:**
- Use any TOTP authenticator (Google Authenticator, Authy, 1Password, IdP mobile app)
- Scan QR code or enter alphanumeric ID
- Enter the generated code to confirm

### Recovery / Reset Flow

If a user loses access to their 2FA method:
- **The user cannot self-recover**
- A **Twingate Admin** resets the user's 2FA via the Admin Console:
  - Navigate to the user
  - Select to reset or delete the corresponding authentication option
- On the user's next 2FA prompt, they go through initial setup again

**Operational Notes:**
- Do **not** delete the authenticator app or the Twingate code inside the app -- causes lockout
- Document the admin reset SOP in your runbook
- For high-availability admin access: maintain at least 2 admins (per /docs/security-policies-best-practices) so a 2FA reset is always available

### WebAuthn Compatibility

- WebAuthn support varies by platform and browser
- Most modern browsers/platforms support it; some legacy or constrained environments may not
- Reference: caniuse.com WebAuthn support matrix (linked from this doc)

**Decision Notes:**
- For high-security Resources: enable both biometric and security key paths -- security key for resistance to malware, biometric for convenience
- For Service Accounts (machine identities): 2FA cannot apply -- design those Resource Policies without 2FA
- For BYOD/contractor users: TOTP-only is usually fine; security keys may not be available

**Related Docs:**
- /docs/two-factor-authentication-security-policies -- Configuring the 2FA policy rule
- /docs/security-policies -- Policy types overview
- /docs/security-policies-best-practices -- Where to enforce 2FA
- /docs/admins -- Admin role management
- /docs/authentication -- Re-auth frequency rule (companion)

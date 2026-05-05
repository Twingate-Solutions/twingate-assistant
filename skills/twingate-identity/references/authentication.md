## Authentication Rule (Re-Auth Frequency)

The Authentication rule controls **how often** users must re-authenticate. Applied to Resource Policies and Minimum Authentication Requirements (MAR). Cannot be edited on the Admin Console policy.

**How It Works:**
- Set a session length (e.g., 6 hours, 1 day, 30 days)
- When the user attempts to access a Resource, Twingate checks: has the user authenticated within this window?
- If yes -> proceed
- If no -> prompt for re-authentication via the IdP

**Important Caveat -- IdP Behavior:**
- Twingate cannot control how the **IdP** handles the re-authentication prompt
- Some IdPs may use a still-valid session and not actually prompt for password
- If you require **active re-authentication** (password re-entry), configure the IdP itself to require passwords on every authentication
- Examples: Okta "Require password" setting, Entra ID "Sign-in frequency" Conditional Access policy

**Cross-Policy Session Reuse:**
- Authentication is **shared across policies** within a single sign-in window
- If MAR is 1 day and a Resource Policy is 6 hours:
  - User signs in -> 1-day MAR session starts
  - User accesses a Resource -> 6-hour Resource auth used
  - User accesses again 4 hours later -> no re-auth needed (within both windows)
  - User accesses 7 hours later -> re-auth prompt (Resource Policy expired)
  - 25 hours after sign-in -> MAR also expired; full sign-in flow

**Recommended Frequencies (per /docs/security-policies-best-practices):**

| Risk Tier | Re-Auth Frequency |
|---|---|
| High | 2 hours |
| Medium | 1 day |
| Low | 1 week |
| Very Low | 1 week or longer |
| MAR | 31 days (no MFA at this layer) |

**Decision Notes:**
- Don't enforce re-auth at MAR if you also enforce it at Resource Policies -- choose one layer
- Prompts that don't actually require password entry frustrate users while providing no security benefit -- align IdP settings with policy intent
- Long MAR windows (31 days) are safe because Resource Policies do the actual gating

**Gotchas:**
- A user who logs out of the Twingate Client resets the session -- next access requires full re-auth regardless of policy windows
- Resource Policy sessions don't survive Twingate Client restart **except** for device-only policies (see /docs/device-only-resource-policies)

**Related Docs:**
- /docs/security-policies -- Policy types overview
- /docs/security-policies-best-practices -- Risk-tier recommendations
- /docs/two-factor-authentication-security-policies -- Companion MFA rule
- /docs/two-factor-authentication -- 2FA setup details

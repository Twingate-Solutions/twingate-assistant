## Policy Guides Index

Index page pointing to the per-rule configuration guides for Security Policies. Treat this as a navigation hub.

**Configurable Rule Types (each has its own deeper guide):**

| Rule | What It Controls | Detailed Guide |
|---|---|---|
| **Authentication** | Re-auth frequency + MFA requirement | /docs/authentication |
| **Two-Factor Authentication** | MFA enforcement specifics within auth requirements | /docs/two-factor-authentication-security-policies |
| **Device-only Resource Policies** | Evaluate only device requirements (no user auth check) | /docs/device-only-resource-policies |
| **Trusted Devices** | Whether devices must be trusted (manually or automatically via EDR/MDM) | /docs/trusted-devices |

### Quick Reference

**When to use Device-only Policy:**
- IdP login Resources (`*.okta.com`, `login.microsoftonline.com`) -- breaks the SaaS app gating auth loop
- AD/DC Resources for the Everyone Group -- allows pre-logon connectivity
- Any Resource where you want to gate purely on device, not on user-level auth

**When to use Trusted Devices:**
- Any sensitive Resource (default for most production deployments)
- Trusted Profile defines what "trusted" means (CrowdStrike, SentinelOne, manual verification, native posture, etc.)

**When to use MFA in a Resource Policy:**
- High and Medium risk Resources per the risk-tier model
- Avoid MFA in MAR -- enforce at Resource level instead (less prompt fatigue)

**Re-auth Frequency Guidance:**
- High risk: every 2 hours
- Medium risk: once a day
- Low risk: once a week
- Very Low risk: once a week (or longer)

**Related Docs:**
- /docs/security-policies -- Policy types overview
- /docs/security-policies-best-practices -- Worked example with risk tiers
- /docs/security-policies-migration-guide -- Migration from older policy model
- /docs/device-security-guide -- Trusted Profiles + device posture

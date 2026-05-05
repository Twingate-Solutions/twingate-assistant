## Security Policies

Reference doc for the three Twingate Security Policy types -- where they apply, what they gate, and how they layer.

**Three Policy Types (under Policies tab):**

| Type | Applied To | Gates |
|---|---|---|
| **Minimum Authentication Requirements** | All users at network login | Twingate environment access (does NOT grant Resource access) |
| **Resource Policies** | Specific Resources at access time | Access to those Resources (per-user evaluation) |
| **Application Control Policies** | Specific Resources, restricting browser | Browser-based Resource access (e.g., enterprise browsers only) |

Plus the **Admin Console Security Policy** (under Settings tab) -- gates Admin Console sign-in for users with Admin/DevOps/Support roles. See /docs/admin-console-security.

### Resource Policy Components

When creating or editing a Resource Policy, configurable rules:

| Rule | What It Controls |
|---|---|
| **Location Requirements** | Which countries can / cannot access (Enterprise plan only) |
| **Authentication Requirements** | Re-auth frequency, MFA enforcement -- layers on top of MAR |
| **Device Security** | Required device posture: All / Trusted Devices / Custom |

### Policy Application Model

**Default behavior:**
- Every Resource has the **Default Policy** unless changed
- Groups assigned to a Resource inherit the Resource's Policy

**Group-Level Overrides:**
- A Resource Policy can be **overridden per Group** for a specific Resource
- Example: a "staging environment" Resource has Default Policy, but the Contractor Group accessing it uses "Contractor Policy" instead, and the Normal Group uses "Secure Policy"

**Override Stickiness:**
- Once you override a Group's policy on a Resource, that override is independent
- If the Resource Policy changes (Default -> Secure), the overridden Groups keep their override
- To revert: explicitly reset the override for that Group on that Resource

### Additional Resource Configuration (per-Resource or per-Group)

- **Ephemeral access** -- expiry date; Group is auto-removed from the Resource at expiry
- **Usage-based auto-lock** -- per-user inactivity timer; lock individual users who haven't touched the Resource

### Recommended Pattern

- Keep **Minimum Authentication Requirements lenient** (e.g., 31 days, no MFA) -- MAR doesn't grant Resource access; security comes from Resource Policies
- Apply **strict controls in Resource Policies** for sensitive Resources
- Avoids excessive auth prompts when users are accessing low-risk Resources
- Concentrates security checks at the moment of accessing the actual sensitive Resource

**Why "less is more" at the MAR layer:**
- Long MAR avoids the SaaS app gating chicken-and-egg lockout (see /docs/saas-app-gating-best-practices)
- Resource Policies still enforce the actual security per-Resource
- Users get fewer prompts overall -- better UX without sacrificing security

### Group Override Use Cases

- "Default Policy applies broadly, but the Contractor Group on this Resource needs MFA every 4 hours"
- "IT admins on the POS Resource need MFA + 1-day re-auth, while regular Retail staff need only weekly re-auth"

**Gotchas:**
- The **Everyone Group** for Resources like IdP / AD-DC must use a no-auth + device-trust policy -- otherwise pre-logon DC access fails (see /docs/security-policies-best-practices)
- Override semantics: explicitly clear an override to re-inherit -- don't assume a Resource Policy change cascades
- Application Control Policies are separate from Resource Policies -- you can have both on the same Resource

**Related Docs:**
- /docs/security-policies-best-practices -- Worked example of mapping risk to policies
- /docs/security-policy-guides -- Per-rule configuration guides
- /docs/security-policies-migration-guide -- Migration from older Twingate policy model
- /docs/authentication, /docs/two-factor-authentication-security-policies -- Auth rule configuration
- /docs/trusted-devices, /docs/device-only-resource-policies -- Device rule configuration
- /docs/location-requirements -- Geo-based controls
- /docs/admin-console-security -- Admin Console policy
- /docs/ephemeral-access-to-resources, /docs/usage-based-auto-lock -- Time/usage controls
- /docs/browser-security -- Application Control Policies (browser restriction)

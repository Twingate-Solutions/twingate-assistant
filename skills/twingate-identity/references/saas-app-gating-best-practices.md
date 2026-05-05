## Best Practices for SaaS App Gating

App gating = restricting access to SaaS apps so they're reachable **only** through the Twingate Connector exit IP -- enforced at the IdP layer (Conditional Access / Context-Aware Access). This page is the conceptual best-practices doc; the per-IdP guides handle the mechanics.

**The Three Twingate Policy Types:**

| Policy Type | Protects | Notes |
|---|---|---|
| **Resource Policies** | Individual Resources (private and SaaS-as-Resource) | Most common; defines MFA, encryption, re-auth requirements per Resource |
| **Admin Console Policy** | The Twingate Admin Console itself | Applies only to administrators |
| **Minimum Authentication Requirements** (MAR) | Nothing directly -- just controls how often Clients re-register against the IdP | Critical for SaaS app gating; see below |

**The Catch-22 -- Why MAR Matters for App Gating:**

When you gate a SaaS Resource, the **IdP itself becomes a Twingate Resource** (because authenticated users hit the IdP via the Connector exit IP).

- If the **Minimum Authentication Requirements** period is **too short**, the Twingate Client may need to re-register against the IdP
- But the IdP login page is now a **protected Twingate Resource** -- only reachable through a registered Client
- Result: lockout. The user can't authenticate to the IdP because they can't reach the IdP login page until they authenticate.

Workaround at the time: restart the Twingate Client. Not acceptable as a regular flow.

**Recommendation:**
- Set **MAR to 31 days** (the doc's default-recommended value)
- Lockout requires BOTH:
  1. User has not accessed any Resource (of any type) for 31 days (any Resource access resets the MAR window)
  2. User has not restarted their device or Client for 31 days

**Why 31 Days Is Safe:**
- MAR provides **no security benefit on its own** -- it only forces IdP re-registration; the IdP still applies its own session policies
- Resource Policies (MFA, device posture, hourly re-auth) are where actual security controls live
- A long MAR window simply prevents the lockout edge case

**Device Security:**
- Devices must meet Trusted Profiles or minimum OS requirements (per /docs/device-security-guide) before they can connect to Twingate at all -- this is independent of MAR

**Mitigations Beyond MAR (also recommended):**
- Apply a **Device-only Resource Policy** to the IdP Resource (e.g., `*.google.com`, `console.jumpcloud.com`) -- per the IdP-specific guides
- Device-only allows the IdP login page to be reached without requiring full Twingate auth -- breaks the chicken-and-egg loop independently of MAR

**Related Docs:**
- /docs/entra-id-app-gating-office-365 -- Entra ID + Office 365
- /docs/saas-app-gating-with-google-workspace -- Google Workspace Context-Aware Access
- /docs/saas-app-gating-with-jumpcloud -- JumpCloud Conditional Lists
- /docs/saas-app-gating-with-okta -- Okta Network Zones
- /docs/saas-app-gating-with-onelogin -- OneLogin
- /docs/saas-app-gating -- Generic IP-based gating
- /docs/security-policies -- Resource Policy reference
- /docs/device-security-guide -- Trusted Profiles / minimum OS

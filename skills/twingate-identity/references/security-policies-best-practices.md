## Security Policies Best Practices

The reference doc for designing Twingate Security Policies. Three policy types exist; each plays a different role. The bulk of the doc is a worked example of mapping risk to policy definitions.

**Three Policy Types:**

| Type | Scope | Component |
|---|---|---|
| **Admin Console Security Policy** | Twingate Admin Console only; applies to Admin/DevOps/Support roles | Admin Console |
| **Minimum Authentication Requirements (MAR)** | All users connecting; gates the Twingate environment, **does not grant Resource access** | Client |
| **Resource Policy** | Per-Resource access; defines auth + MFA + device + re-auth requirements | Client |

**Admin Console Policy -- Recommended:**
- Authenticate every 1 hour (cannot be lengthened, by design)
- Enforce MFA
- Assign Admin role to **at least 2 Twingate users** (avoid lockout from departures)

**Minimum Authentication Requirements -- Recommended:**
- Keep it lengthy: **31 days** (default recommended)
- **Do NOT enforce MFA at the MAR level** -- enforce MFA via Resource Policies instead
- Reasoning: MAR doesn't grant Resource access; security comes from Resource Policies. Long MAR avoids the SaaS app gating lockout edge case.

**Resource Policy Design -- Four Questions Answered Per Policy:**
1. Does the user need to authenticate to access this Resource?
2. What device attributes are required (trusted device, EDR/MDM verified)?
3. Does the user need MFA?
4. How often does the user re-authenticate after first access?

### Worked Example -- Mapping Risk to Policy

**Step 1: Catalog Resources by Risk**

Quantify risk along dimensions like:
- Data type (PII, IP, public)
- Data volume (single record vs. full DB access)
- Business impact of modifications (Terraform prod vs. SIEM config)
- Method of access (UI, CLI, RDP, SSH)

Map to risk tiers:
- **High**: 2h re-auth, MFA, verified device
- **Medium**: 1d re-auth, MFA, verified device
- **Low**: 1w re-auth, MFA, verified device
- **Very Low**: 1w re-auth, no MFA, verified device

**Step 2: Determine Device Verification Per User Group**
- Employees on company devices: EDR/MDM (CrowdStrike, SentinelOne, Jamf, Kandji)
- Contractors with BYOD: Twingate Serial Number verification (no EDR available), or accept no device verification with strict auth/MFA compensating controls

**Step 3: Configure Trusted Profiles + Minimum OS**
- For groups without device verification (e.g., contractors): allow only macOS via native posture (e.g., Screen Lock + Biometric Configuration)
- For groups with verification: create Trusted Profiles per (OS, EDR vendor) combination

**Step 4: Define Policies with a Naming Convention**
Format: `<Re-auth>-<MFA>-<Verif>` -- e.g., `1D-MFA-Verif`, `2H-MFA-Verif`, `1W-NoMFA-Verif`

A typical environment ends up with **6-8 distinct policies**:
- `1D-MFA-Verif` (Medium-risk, default for most assets)
- `2H-MFA-Verif` (High-risk: prod infra, source code, IdP/AD admin)
- `1W-NoMFA-Verif` (Very Low-risk: e.g., POS terminals)
- `1W-MFA-Verif` (Low-risk)
- `1D-NoMFA-Verif` (e.g., AD/DC traffic for non-admin users)
- `1D-NoMFA-None` (e.g., IdP traffic for non-admin users -- the "Everyone" group)
- Plus exception policies as needed

**Step 5: Apply Override Policies for Group-Specific Exceptions**
- Example: IT users accessing the POS get tighter controls than Retail users
- Example: Contractors 2 cannot meet device verification -- override to a no-Verif policy with stricter MFA

### The "Everyone" Group

- The only Group that can't be deleted; contains all Twingate users
- **Use it for IdP and AD/DC infrastructure Resources**:
  - IdP login (e.g., `*.okta.com`) -- needed before user auth
  - AD/DC for Windows environments -- needed before user logon
- **Resource Policy for the Everyone Group**:
  - Does NOT require authentication (allows the Twingate Client to reach DCs before user logon)
  - Requires device trust (native or via EDR/MDM)
- This is what makes domain-joined Windows + Twingate work seamlessly

**Decision Notes:**
- Build the catalog in a spreadsheet first; create Twingate policies last
- Don't create policies per-Resource -- create policies per-risk-tier and apply many Resources to one policy
- Override policies (Group-specific) handle exceptions; primary policies cover the default

**Related Docs:**
- /docs/security-policies -- Resource Policy reference
- /docs/security-policy-guides -- Step-by-step policy creation
- /docs/security-policies-migration-guide -- Migrating from older Twingate policy model
- /docs/device-security-guide -- Trusted Profiles + minimum OS reference
- /docs/trusted-devices, /docs/device-posture-checks -- Device verification details
- /docs/admin-console-security -- Admin Console policy reference
- /docs/saas-app-gating-best-practices -- Companion doc focused on SaaS gating + MAR

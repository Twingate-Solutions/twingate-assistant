## Device-only Resource Policies

A Resource Policy variant that **disables user authentication requirements** and evaluates **only device requirements**. Useful for Resources that need pre-logon connectivity or where user friction matters more than per-Resource auth.

**Applicability:**
- Resource Policies only (cannot be applied to MAR or Admin Console policy)

**How It Works:**
- Standard Resource Policies evaluate user auth + device requirements
- Device-only mode: skip user auth check; just evaluate device requirements (Trusted Device, posture)
- Configured by selecting the **Disable** option next to "Authentication Requirements" in the policy editor

**MAR Still Applies:**
- Even with user auth disabled at the Resource layer, **MAR is always enforced**
- The user must have authenticated successfully within the MAR session window
- Example: MAR = 30 days -> user must have authenticated in the last 30 days, **and** the device must meet posture, for access to be granted

**Session Persistence -- The Key Difference:**

| Policy Type | Session Survives Restart / Re-launch? |
|---|---|
| Standard Resource Policy | **No** -- always re-auth after restart or Client re-launch |
| **Device-only Resource Policy** | **Yes** -- as long as MAR window is still valid |

This means Resources behind device-only policies are **immediately accessible** after machine restart or Twingate Client re-launch (no auth prompt blocking access).

**Primary Use Cases:**

### 1. Windows Start Before Logon (SBL)
- Domain-joined Windows machines need to reach Domain Controllers **before** the user logs in
- A device-only policy on AD/DC Resources allows the Twingate Client to connect at boot, hit the DC, and let the user log in normally
- See /docs/windows-sbl

### 2. SaaS App Gating IdP Resources
- IdP login pages (`*.okta.com`, `login.microsoftonline.com`) need to be reachable so the user can authenticate
- Without device-only policy: chicken-and-egg loop -- user can't reach IdP because reaching IdP requires Twingate auth, which requires IdP login
- Device-only policy on the IdP Resource breaks the loop
- See /docs/saas-app-gating-best-practices

### 3. Frictionless Access to Low-Risk Resources
- Internal docs, dashboards, low-sensitivity tools
- Trusted-device users can access without auth prompt fatigue

**Configuration:**
- Edit the Resource Policy
- Next to "Authentication Requirements", click **Disable**
- Configure Device Security requirements (Trusted Profile, posture checks)
- Re-enable user auth at any time via the same screen

**Gotchas:**
- Don't apply device-only to high-risk Resources -- you lose the per-access authentication checkpoint
- Device-only requires a strong device trust posture -- if all you have is "any device", you've effectively removed all gating
- Make sure the **Everyone Group's** Resource Policy on AD/DC and IdP Resources is device-only (per /docs/security-policies-best-practices) -- otherwise pre-logon DC access fails on Windows domain joins

**Related Docs:**
- /docs/security-policies -- Policy types
- /docs/security-policies-best-practices -- "Everyone Group" pattern + risk tiers
- /docs/saas-app-gating-best-practices -- Why device-only on IdP Resources
- /docs/windows-sbl -- Windows Start Before Logon (the primary SBL use case)
- /docs/trusted-devices, /docs/device-security-guide -- Device requirement reference

## SaaS App Gating: Google Workspace (Context-Aware Access)

How to require Twingate connection for Google Workspace (Gmail, Drive, Calendar, ...) and SAML-based third-party apps via Google's **Context-Aware Access**.

**Coverage:**
- **Core Google Workspace apps** (Gmail, Drive, Calendar): context is **continuously checked**
- **SAML-based third-party apps**: context is checked **at authentication time**

**Twingate Admin Console Prerequisites:**

**1. Create a Resource for Google IdP Domains**
- For Google Workspace core apps, a wildcard like `*.google.com` is the simplest
- The Resource forces traffic through the Connector exit IP

**2. Apply a Device-only Resource Policy to the IdP Resource**
- Critical: **without this you create an authentication loop**
- The user can't authenticate to Google because reaching `*.google.com` requires Twingate auth, but Twingate auth requires Google login...
- Device-only Policy lets the device reach the Google login page without full user authentication, breaking the loop

### Google Admin Console Setup

**Step 1 -- Create an Access Level**
- Sign in to https://admin.google.com
- **Security -> Access and data control -> Context-Aware Access**
- Click **Access levels** -> **CREATE ACCESS LEVEL**
- Settings:
  - **Access level name**: e.g., "Twingate Application Control"
  - **Context conditions** tab: **BASIC** mode, **Meets all attributes (AND)**
  - **Attribute**: **IP subnet**
  - Add the Connector(s) public IP(s) in CIDR form -- e.g., `8.8.8.8/32`
  - Multiple IPs become an OR list -- enter each as a separate IP subnet entry
- **CREATE**

**Step 2 -- Assign the Access Level to Apps**
- From Context-Aware Access main screen -> **Assign access levels**
- Tick the apps to gate (Gmail, Drive, Calendar, etc., or specific SAML SSO apps)
- **Selected x of y -> Assign**
- Tick the access level created in Step 1
- **CONTINUE**

**Step 3 -- Enforcement Settings**
- Choose whether to block:
  - Desktop applications (e.g., Gmail desktop) -- **recommended: block**
  - Mobile applications -- **recommended: block**
  - **API-based access** -- **recommended: do NOT block** (would break legitimate API automation)
- **CONTINUE -> ASSIGN**

### Test

- Without Twingate: try to log in to Gmail -- expect an "access blocked" message
- With Twingate (Client connected): same login should succeed
- If still blocked, verify:
  - Twingate Resources are routing the Google domains through the gating Connector
  - The Connector's egress IP matches what's configured in the access level

**Gotchas:**
- Context-Aware Access **continuously** checks core apps -- if the user disconnects from Twingate mid-session, Gmail / Drive may revoke the session
- Mobile apps and desktop clients see context checks too -- some workflows may break (e.g., Drive sync from a laptop without Twingate)
- API-based access blocking will break service accounts, third-party tools, and most SaaS-to-SaaS integrations -- leave it unblocked unless you have a specific reason
- If your Connector NAT gateway IP changes, all Google Workspace users are locked out until you update the access level -- pin static IPs

**Related Docs:**
- /docs/saas-app-gating-best-practices -- Device-only policy + MAR (essential)
- /docs/google-workspace-configuration -- Google Workspace as Twingate IdP
- /docs/entra-id-app-gating-office-365 -- Equivalent pattern for Microsoft
- /docs/saas-app-gating-with-jumpcloud -- JumpCloud equivalent

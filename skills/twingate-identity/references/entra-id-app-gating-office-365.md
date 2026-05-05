## SaaS App Gating: Office 365 with Entra ID

Practical recipe to lock Office 365 access behind a Twingate Connector exit IP using Microsoft Entra ID **Conditional Access**. Users can only reach Office 365 if they're connected to Twingate.

**Prerequisites:**
- Office 365 Business subscription
- License for **Entra ID Conditional Access** (P1 or higher)
- At least one Connector deployed with a known **public IP address** (record this IP per Connector)

**Architecture:**
- Twingate Resource for Office 365 domains -- routes user traffic through the Connector
- Entra ID Conditional Access -- denies Office 365 access from any source IP **except** the Connector's public IP

### Step 1 -- Create the Twingate Resource

In the Remote Network containing the gating Connector(s):
- Create a Resource for the Office 365 domains. Depending on which apps you protect, add separate Resources for:
  - `portal.office.com`
  - `*.sharepoint.com`
  - `*-my.sharepoint.com`
  - `admin.microsoft.com`
  - `*-admin.sharepoint.com`
  - `admin.teams.microsoft.com`
- Apply a **Device-only Policy** to these Resources (avoids the chicken-and-egg auth loop -- see /docs/saas-app-gating-best-practices)

### Step 2 -- Entra ID Conditional Access

**WARNING:** Misconfigured Conditional Access can lock all admins (including global admins) out of the Entra portal. Always test with **Report-only** mode first and have a break-glass admin account excluded from the policy.

#### 2.1 Add a Trusted Location (Named Location)
- Entra ID Conditional Access -> **Named locations** -> new
- Name: e.g., "Twingate Connectors"
- Enter the **public CIDR** of each Connector (e.g., `203.0.113.42/32`)

#### 2.2 Configure the Policy
- Conditional Access -> **Policies** -> **New policy**
- **Users**: scope to a single test user first; expand later
- **Cloud apps or actions**: select **Office 365**
- **Conditions** -> **Locations**:
  - Include: **Any location**
  - Exclude: **Twingate Connectors** (the trusted location from 2.1)
- **Access controls** -> **Grant**: **Block access**

**Logic recap:**
- "Any location except Twingate Connectors" -> **Block**
- Result: only requests coming from the Connector's public IP are allowed

#### 2.3 Enable as Report-Only First
- Set policy to **Report-only**
- Verify in Conditional Access logs that:
  - Twingate-routed requests are reported as "would have been allowed"
  - Direct requests are reported as "would have been blocked"
- Toggle to **On** when validated

### Result

Twingate users connect via Client -> Office 365 traffic exits through the Connector -> Entra ID sees the Connector's public IP -> Conditional Access allows. Users not on Twingate are blocked.

**Gotchas:**
- Excluding a break-glass admin account from the policy is **not optional** -- if the Connector goes down, the policy locks everyone out
- If the Connector's public IP changes (e.g., elastic IP not reserved, NAT gateway recreation), Conditional Access will start blocking users -- pin static IPs for production
- Multiple Connectors can share a NAT egress -- one CIDR usually suffices; if Connectors have separate IPs, list each
- Wildcard SharePoint domains (`*.sharepoint.com`) can match more than expected -- review which Microsoft domains you actually want gated

**Related Docs:**
- /docs/saas-app-gating-best-practices -- MAR + Device-only policy guidance (essential)
- /docs/saas-app-gating-with-google-workspace -- Same pattern, different IdP
- /docs/saas-app-gating-with-okta -- Okta Network Zones equivalent
- /docs/entra-id-configuration -- Entra ID as Twingate IdP

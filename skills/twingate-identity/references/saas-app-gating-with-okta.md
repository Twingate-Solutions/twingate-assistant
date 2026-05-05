## SaaS App Gating: Okta (Network Zones + Sign-On Policy)

How to require Twingate connection for SaaS apps fronted by Okta -- the IP check happens at Okta sign-on via **IP Network Zones** + **app sign-on / authentication policy**.

**Twingate Admin Console Prerequisites:**

**1. Create a Resource for the Okta Login Domain**
- `tenant.okta.com` (your Okta org URL)
- Associate with one or more Groups

**2. Apply a Device-only Resource Policy to the IdP Resource**
- Required to break the chicken-and-egg auth loop -- user can't reach Okta login if Twingate auth depends on Okta login
- Device-only Policy allows the IdP login page to be reached without full Twingate user auth

### Okta Setup -- Two Engines

Okta has two engines: **Classic Engine** and **Identity Engine (OIE)**. Steps differ slightly. (See Okta docs for engine differences and upgrade paths.)

#### Common Step -- Create an IP Network Zone

- **Security -> Networks -> Add Zone -> IP Zone**
- **Zone Name**: e.g., "Twingate Connector Exit IP"
- **Gateway IPs**: enter the Connector(s) public IP(s)
  - Multiple Connectors behind a NAT usually share a single egress IP
  - If not behind NAT (uncommon), list each Connector IP
- Save

#### Classic Engine -- App Sign-On Policy

- **Applications -> Applications -> select target app (e.g., Google Workspace, Salesforce)**
- **Sign On** tab -> **Sign On Policy** -> **+ Add Rule**

**Rule settings:**

| Field | Value |
|---|---|
| Rule Name | e.g., "Twingate-secured SaaS" |
| Who does this rule apply to? | Users assigned to this app |
| If the user is located | **Not in Zone** |
| Network Zones | The IP Zone from above |
| Client platform | Any client |
| Sign on to this application is | **Denied** |

**Logic**: deny if the user is **not** in the Twingate IP Zone.

#### Identity Engine (OIE) -- Authentication Policy

- **Security -> Authentication Policies -> Add a policy** -- name + description -> Save
- **Add rule**:
  - **AND User's IP is**: **Not in any of the following zones** -> select the Twingate IP Zone
  - **THEN Access is**: **Denied**
- Save the rule

**Apply the Policy to Apps:**
- Open the policy -> **Applications** tab -> **Add app**
- Select the target SaaS app -> **Add** -> **Done**
- Alternatively, from the app's **Sign On** tab, set the authentication policy directly

### Result

- Twingate user -> Connector NAT IP matches the Okta IP Zone -> sign-on allowed
- User not on Twingate -> Okta denies sign-on at the IdP layer

**Gotchas:**
- "Deny if NOT in zone" semantics are different from "allow if in zone" -- get this wrong and the policy either does nothing or locks everyone out. Test on a single user first.
- OIE authentication policies are different from Classic sign-on policies -- pick the right path based on your Okta engine
- Always exclude a break-glass admin user from the app's gated policies in case the Connector NAT IP changes or goes down
- Pin static NAT egress IPs in production

**Related Docs:**
- /docs/saas-app-gating-best-practices -- MAR + Device-only Policy (essential)
- /docs/okta-configuration -- Okta as Twingate IdP
- /docs/okta-app-configuration -- Twingate as Okta SAML/OIDC app
- /docs/saas-app-gating-with-google-workspace, /docs/saas-app-gating-with-jumpcloud, /docs/saas-app-gating-with-onelogin, /docs/saas-app-gating-with-entra-id -- Other IdPs

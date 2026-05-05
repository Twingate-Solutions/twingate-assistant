## SaaS App Gating: Microsoft Entra ID (Conditional Access)

How to require Twingate connection for SaaS apps fronted by Microsoft Entra ID -- the IP check happens at IdP authentication via **Named Locations** + **Conditional Access**.

**Twingate Admin Console Prerequisites:**

**1. Create a Resource for the Entra ID Login Domains**
- `tenant.office.com` (your tenant's portal)
- `login.microsoftonline.com` (the generic Microsoft login)
- Associate with one or more Groups

**2. Apply a Device-only Resource Policy to the IdP Resource**
- Required to break the chicken-and-egg auth loop
- Without it: user can't authenticate to Entra ID because reaching the IdP login page requires Twingate auth, but Twingate auth requires Entra ID login
- Device-only Policy lets users reach the IdP portal without full user authentication

### Entra ID Portal Setup

**Step 1 -- Create a Named Location (Trusted)**
- **Entra ID Portal -> Conditional Access -> Named locations**
- Add new -- IP ranges location (mark as **Trusted**)
- Enter the **public IP / CIDR** of the Connector(s) -- typically the NAT gateway egress IP

**Step 2 -- Create the Conditional Access Policy**
- **Conditional Access -> Policies -> New policy**
- **Cloud apps**: select the SaaS app(s) to gate (e.g., Office 365, individual SaaS SAML apps)
- **Conditions -> Locations**:
  - Configure: **Yes**
  - **Include**: **Selected locations** -> the trusted Named Location from Step 1
  - (Or use the equivalent "any except trusted" pattern -- see /docs/entra-id-app-gating-office-365)
- **Access controls -> Grant**: configure to allow only when in the trusted location, or block when not in it (per the doc's guidance)

**Result:**
- Users authenticated via Twingate exit through the Connector NAT IP -> Conditional Access matches -> Entra auth proceeds
- Users not on Twingate are blocked by Entra ID before SAML/OIDC token issuance

**For a Step-by-Step Walkthrough:**
- See /docs/entra-id-app-gating-office-365 -- specifically scoped to Office 365

**Gotchas:**
- Always exclude break-glass admin accounts from the Conditional Access policy -- if the Connector NAT IP changes or Connector is offline, you can still log in
- Test the policy as **Report-only** before turning it on
- Multiple Connectors usually share a NAT egress IP -- one Named Location entry suffices; if Connectors have separate IPs, list each
- Pin static NAT egress IPs for production -- IP changes lock everyone out

**Related Docs:**
- /docs/entra-id-app-gating-office-365 -- Step-by-step walkthrough for Office 365
- /docs/saas-app-gating-best-practices -- MAR + Device-only Policy guidance (essential)
- /docs/entra-id-configuration -- Entra ID as Twingate IdP
- /docs/saas-app-gating -- Generic IP-based gating overview

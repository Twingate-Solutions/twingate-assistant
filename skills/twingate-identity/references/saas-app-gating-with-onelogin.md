## SaaS App Gating: OneLogin (App Policies)

How to require Twingate connection for SaaS apps fronted by OneLogin -- the IP check happens at OneLogin authentication via an **App Policy** with **Allowed IP Addresses**.

**Twingate Admin Console Prerequisites:**

**1. Create a Resource for the OneLogin Login Domain**
- `tenant.onelogin.com`
- Associate with one or more Groups

**2. Apply a Device-only Resource Policy to the IdP Resource**
- Required to break the chicken-and-egg auth loop
- Allows the IdP portal to be reached without full Twingate user auth

### OneLogin Setup

#### Step 1 -- Create an App Policy

- OneLogin Admin Console -> **Security -> Policies -> New App Policy**
- **Policy Name**: e.g., "Twingate SaaS App Gate"
- **Allowed IP Addresses**: enter the public exit IP of the Connector(s) Remote Network
- Save

#### Step 2 -- Apply the Policy to an SSO App

- **Applications -> Applications** -> open target app (e.g., Google Workspace)
- **Access -> Policies** -> select the App Policy created in Step 1
- Save

**Result:**
- Twingate user -> Connector NAT IP matches Allowed IP -> OneLogin authentication proceeds
- User not on Twingate -> OneLogin blocks the auth

**Gotchas:**
- The IP check happens at **authentication time** -- once authenticated, OneLogin does not re-check IPs continuously; an established SSO session survives a Twingate disconnect until SSO session expiry
- For tighter enforcement, shorten OneLogin session lifetimes (consult OneLogin admin docs)
- Always exclude a break-glass admin from the gated policies
- NAT egress IPs should be pinned (static / elastic) in production -- IP changes lock everyone out

**Related Docs:**
- /docs/saas-app-gating-best-practices -- MAR + Device-only Policy (essential)
- /docs/onelogin-configuration, /docs/onelogin-configuration-scim -- OneLogin as Twingate IdP
- /docs/saas-app-gating-with-okta, /docs/saas-app-gating-with-jumpcloud, /docs/saas-app-gating-with-entra-id, /docs/saas-app-gating-with-google-workspace -- Other IdPs

## SaaS App Gating: JumpCloud (Conditional Access Policies)

How to require Twingate connection for SaaS apps fronted by JumpCloud SSO -- the IP check happens at JumpCloud authentication time.

**Twingate Admin Console Prerequisites:**

**1. Create a Resource for JumpCloud's Login Domain**
- Resource for `console.jumpcloud.com` (and any subdomains used by your JumpCloud SSO flow)
- Associate the Resource with one or more Groups

**2. Apply a Device-only Resource Policy to the IdP Resource**
- Required to break the chicken-and-egg auth loop
- Without this: user can't authenticate to JumpCloud because reaching `console.jumpcloud.com` requires Twingate auth, but Twingate auth requires JumpCloud login
- Device-only Policy allows reaching the IdP login portal without full user auth

### JumpCloud Admin Portal Setup

**Step 1 -- Create an IP List**
- Log in to JumpCloud Admin Portal
- **SECURITY MANAGEMENT -> Conditional Lists**
- **( + )** to create a new list
- **List Name**: e.g., "Twingate Connectors"
- Enter the public IP(s) of the Connector(s)
  - Mix of single IPs, CIDR notation, and ranges allowed in one list
- **Save**

**Step 2 -- Create a Conditional Access Policy**
- **SECURITY MANAGEMENT -> Conditional Policies**
- **( + )** -> **SSO Applications**
- **Policy Name**: descriptive
- **SSO Applications**: select the apps to gate
- **Users & Groups**: select target users / groups
- **Match logic**: select "all" if every condition must be met (recommended for IP-based gating)
- **Add Conditions** -> **IP List** -> select "Twingate Connectors"
- **Create policy**

### NAT Behavior

- Multiple Connectors usually share a single NAT public IP -- one entry in the IP list is enough
- If your Connectors are NOT behind NAT (uncommon), each Connector has a unique egress IP -- add each
- For cloud Connectors with elastic/static IPs, pin the IPs to avoid surprise lockouts on infrastructure changes

### Result

- User connects to Twingate Client
- User clicks an SSO link or visits a JumpCloud-protected SaaS app
- JumpCloud sees the request from the Twingate Connector NAT IP -> matches IP List -> auth proceeds
- Without Twingate: JumpCloud blocks auth at the IdP layer

**Gotchas:**
- The IP check happens at **authentication time** -- once authenticated, JumpCloud doesn't re-check IPs continuously (vs. Google Workspace Context-Aware Access for core apps)
- This means an already-authenticated session survives a Twingate disconnect until the SSO session expires -- tighten JumpCloud session lifetimes if you need stricter enforcement
- Always exclude a break-glass admin account from the policy -- if the Connector NAT IP changes or goes down, you can still log in
- Test the policy on a single account before enabling for all users

**Related Docs:**
- /docs/saas-app-gating-best-practices -- MAR + Device-only policy (essential)
- /docs/jumpcloud-configuration -- JumpCloud as Twingate IdP
- /docs/saas-app-gating-with-okta, /docs/saas-app-gating-with-onelogin, /docs/saas-app-gating-with-entra-id, /docs/saas-app-gating-with-google-workspace -- Equivalents for other IdPs

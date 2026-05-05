## Getting Started with SaaS App Gating

The generic playbook for using Twingate as an enforcement point for SaaS access -- conceptually equivalent to IP whitelisting, but the IP check moves up to the IdP layer.

**Why Use Twingate for App Gating:**
- Extend Twingate's authorization controls to SaaS as well as private apps
- Add IP whitelisting to SaaS apps that don't natively support it
- Consolidate IP whitelisting from per-app config into a single IdP+Twingate setup
- Apply consistent device posture / trust requirements across SaaS

**General Setup (IdP-agnostic):**

**1. Choose a Remote Network for IdP Auth Traffic**
- Auth traffic is small in volume but must egress to the internet -- ensure outbound is allowed for the Connector(s)
- Could be a dedicated Remote Network or share with existing infrastructure

**2. Determine the External Egress IP of That Remote Network**
- Practical trick: define a Resource for `*.whatsmyip.org` and visit it while connected -- shows the public exit IP
- This IP is what you'll add to your IdP's allow list

**3. Use NAT for Multiple Connectors**
- User traffic is load-balanced across all Connectors in a Remote Network
- Without NAT you'd have to add every Connector's IP to the IdP allow list -- cumbersome and brittle
- With NAT (cloud NAT gateway, etc.): all Connectors egress through a single static IP -- one entry in the IdP

**4. Add the IdP's Authentication FQDN as a Twingate Resource**
- Examples: `tenant.okta.com`, `login.microsoftonline.com`, `*.google.com`, `tenant.onelogin.com`, `console.jumpcloud.com`
- Associate with Group(s) -- this controls which Twingate users can route IdP auth via the Connector

**5. Apply a Device-only Policy to the IdP Resource**
- Critical -- without this you create an authentication loop
- User can't authenticate to the IdP because reaching the IdP login portal requires Twingate auth (which requires IdP login...)
- Device-only Policy lets the device reach the IdP login page without full user auth, breaking the loop

**6. Configure the IdP to Allow the App Only From the Connector Egress IP**
- IdP-specific: Conditional Access (Entra), Network Zones (Okta), App Policy (OneLogin), Conditional Lists (JumpCloud), Context-Aware Access (Google Workspace)

**Gotchas:**
- Pin the NAT egress IP -- elastic IPs / static reservations only; ephemeral cloud IPs will change and lock users out
- Always have a break-glass admin excluded from the IdP gating policy
- Test in Report-only / single-user mode before fleet rollout
- Set Twingate Minimum Authentication Requirements to **31 days** to avoid the lockout edge case (see /docs/saas-app-gating-best-practices)

**IdP-Specific Guides:**
- /docs/saas-app-gating-with-okta -- Okta Network Zones
- /docs/saas-app-gating-with-jumpcloud -- JumpCloud Conditional Lists
- /docs/saas-app-gating-with-onelogin -- OneLogin App Policy
- /docs/saas-app-gating-with-entra-id -- Entra ID Named Locations + Conditional Access
- /docs/saas-app-gating-with-google-workspace -- Google Context-Aware Access
- /docs/entra-id-app-gating-office-365 -- Office 365 specific walkthrough

**Related Docs:**
- /docs/saas-app-gating-best-practices -- Concepts: MAR, Device-only, lockout avoidance

## Managing Access for Vendors and Contractors

How Twingate's features map to the unique access challenges of contractor / vendor / third-party access -- transient relationships, narrow access scope, BYOD, unknown device posture.

**The Challenges:**

| Challenge | Why It's Different from Employees |
|---|---|
| Transient relationships | 3-month engagements, rotating team members -- onboard/offboard is constant |
| Need targeted access | Contractor doesn't need everything an employee can see -- least-privilege matters more |
| BYOD / unknown devices | Contractors use their own laptops -- no corporate EDR baseline |

**How Twingate Addresses Each:**

### Easy Onboarding/Offboarding
- Twingate delegates auth to the IdP (Okta, Entra ID, Google Workspace, JumpCloud, OneLogin)
- Disabling the contractor's IdP account immediately revokes Twingate access -- and therefore access to every Resource Twingate gates
- This holds **even for Resources that don't natively support SSO** -- Twingate is the SSO enforcement layer
- See /docs/identity-providers

### Granular Access Controls
- Twingate gates per-Resource, not per-network-segment
- Contractors join Groups; Groups get Resource access -- not entire subnets
- Provision/revoke in seconds via Admin Console or API
- Avoids the VPN trap of "full network access for expediency"
- See /docs/resources

### Device Visibility
- All network access is logged with device + location attribution
- Useful for monitoring contractor BYOD devices: which devices, where, what posture
- See /docs/network-overview

### Time-Based Ephemeral Access
- Resources can be configured with an expiry date
- After the date, access is automatically revoked -- no manual cleanup
- Perfect fit for short engagements ("contractor needs DB access for 6 weeks")
- See /docs/ephemeral-access-to-resources

### Usage-Based Auto-Lock
- Auto-revoke access if a user doesn't touch a Resource for N days
- Catches "forgotten" access from over-provisioning
- Per-user, not per-Group -- one inactive contractor doesn't affect others
- See /docs/usage-based-auto-lock

### Just-in-Time Access Requests
- Contractors can request access on demand; admins approve in the Admin Console or via Slack/etc.
- Reduces standing access; access only exists when actively needed
- See /docs/jit-access-requests

**Recommended Pattern for Contractor Access:**
1. Create a separate **"Contractors"** group (or one per vendor) in the IdP
2. Map to a Twingate Group with **Resource Policy that requires MFA + device trust**
3. Where device trust isn't possible (BYOD without EDR): use Twingate native posture checks (Screen Lock, Biometrics, Disk Encryption) or accept the risk and tighten auth (shorter re-auth, mandatory MFA)
4. Use **ephemeral access** with explicit expiry for time-bound engagements
5. Enable **usage-based auto-lock** as a backstop for forgotten access
6. Apply **JIT access requests** for sensitive Resources -- contractor requests, manager approves

**Gotchas:**
- Don't put contractors in the Everyone Group -- they get Resources scoped to "all Twingate users" (IdP, AD/DC) but should not get default access to all Resource policies
- BYOD devices won't satisfy a Trusted Profile that requires CrowdStrike -- design a separate Trusted Profile for contractor BYOD with native posture checks
- Vendors with multiple contractors: use Group nesting in the IdP and let Twingate inherit via SCIM

**Related Docs:**
- /docs/identity-providers -- IdP integration overview
- /docs/groups -- Group management
- /docs/ephemeral-access-to-resources -- Time-bound Resource access
- /docs/usage-based-auto-lock -- Inactivity-based revocation
- /docs/jit-access-requests -- Just-in-time access requests
- /docs/security-policies-best-practices -- Trusted Profile patterns for BYOD
- /docs/scim-provisioning-api -- IdP-driven user lifecycle

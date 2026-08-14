---
source: https://www.twingate.com/docs/saas-app-gating-with-okta
type: docs
fetched: 2026-08-14
source_version: d3260ffa77f8b4741f196680bcda43bf1f1ec9d35c7333b834888892faa52ab4
---

# SaaS App Gating with Okta

## Summary
Configure Twingate and Okta to enforce network-level access control for SaaS applications. Users must be connected to Twingate (routing through a Connector) before Okta will allow authentication to protected apps. This replaces IP whitelisting configured in the SaaS app itself, moving the check to the IdP layer.

## Key Information
- Access control works by routing Okta auth traffic through a Twingate Connector, making requests appear from a known Connector exit IP
- Okta denies app authentication if the request doesn't originate from the approved IP Zone
- Supports both Okta Classic Engine and Identity Engine (OIE)
- Multiple Connectors behind NAT typically share one public IP; without NAT, add each Connector IP separately

## Prerequisites
- Twingate Admin Console access
- Okta Admin Console access
- Connector exit IP address(es) known
- **Twingate setup required:**
  1. Create a Resource for `tenant.okta.com` and assign to appropriate Groups
  2. Apply a **Device-only Policy** to the Okta Resource (prevents auth loop where users can't reach Okta because Okta access requires prior auth)

## Step-by-Step

### Okta Classic Engine
1. **Security > Networks** → Add Zone > IP Zone
2. Set Zone Name (e.g., "Twingate Connector Exit IP"), enter Connector public IP in Gateway IPs → Save
3. **Applications > Applications** → select target app → Sign On tab → Sign On Policy → Add Rule:
   - Who: Users assigned to this app
   - Location: **Not in Zone** → select your IP Zone
   - Access: **Denied**

### Okta Identity Engine (OIE)
1. **Security > Networks** → Add Zone > IP Zone → same IP Zone config as above
2. **Security > Authentication Policies** → Add a policy → Save
3. Within policy → Add rule:
   - User's IP is: **Not in any of the following zones** → select IP Zone
   - Access is: **Denied**
4. Navigate to Applications tab within the policy → Add app → select target app

## Configuration Values

| Setting | Value |
|---|---|
| Resource to create | `tenant.okta.com` |
| Resource Policy | Device-only |
| Okta Zone type | IP Zone |
| Gateway IPs | Connector exit public IP(s) |
| Rule condition | NOT in zone |
| Rule action | Denied |

## Gotchas
- **Auth loop risk**: Without a Device-only policy on the Okta Resource, users can't reach Okta to authenticate, which Twingate requires — a chicken-and-egg deadlock
- The Okta rule must be a **deny** rule (deny if NOT in zone), not an allow rule
- Connectors not behind NAT require listing each Connector's public IP individually in the zone
- OIE uses "Authentication Policies" instead of "Sign On Policy" — different navigation path

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- [Okta Classic vs Identity Engine differences](https://help.okta.com)
- [Okta OIE upgrade instructions](https://help.okta.com)
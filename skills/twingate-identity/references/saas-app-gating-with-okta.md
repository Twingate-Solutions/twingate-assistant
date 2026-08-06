---
source: https://www.twingate.com/docs/saas-app-gating-with-okta
type: docs
fetched: 2026-08-05
source_version: 1aa51b667eb36dd76c23e75b7109ac35cb92731f3f945697443e0ce784103218
---

# SaaS App Gating with Okta

## Summary
Configure Twingate and Okta to restrict SaaS application access by requiring users to route through a Twingate Connector as a prerequisite for Okta authentication. Access is denied at the IdP auth stage if the user's IP doesn't match the Connector's exit IP, replacing traditional IP whitelisting in SaaS apps.

## Key Information
- Works by adding Connector exit IP(s) as an Okta Network Zone, then denying app sign-on from IPs outside that zone
- Supports both Okta Classic Engine and Okta Identity Engine (OIE)
- Multiple Connectors typically share one public IP via NAT; multiple IPs only needed if Connectors have direct internet access (uncommon)

## Prerequisites
- Twingate: Add IdP authentication FQDN (e.g., `tenant.okta.com`) as a Resource assigned to relevant Groups
- Twingate: Apply **Device-only Resource Policy** to the IdP Resource — prevents authentication loop where users can't reach Okta without being authenticated through Twingate first
- Okta: Admin console access with permissions to manage Networks and App Sign On Policies
- Know the public exit IP address(es) of your Twingate Connector(s)

## Step-by-Step

### Twingate Setup
1. Create a Resource for `tenant.okta.com`, assign to appropriate Groups
2. Apply Device-only Policy to that Resource

### Okta Classic Engine
1. **Security > Networks** → **Add Zone > IP Zone**
2. Set Zone Name (e.g., `Twingate Connector Exit IP`), enter Connector public IP in **Gateway IPs**, save
3. **Applications > Applications** → select target app → **Sign On** tab → **Sign On Policy** → **+ Add Rule**
4. Configure rule:
   - People: `Users assigned to this app`
   - Location: `Not in Zone` → select your IP Zone
   - Client: `Any client`
   - Access: `Denied`

### Okta Identity Engine (OIE)
1. **Security > Networks** → **Add Zone > IP Zone** → same IP Zone setup as Classic
2. **Security > Authentication Policies** → **Add a policy** → name and save
3. Within policy, **Add rule**:
   - `AND User's IP is` → `Not in any of the following zones` → select IP Zone
   - `THEN Access is` → `Denied`
4. Navigate to **Applications** tab within the policy → **Add app** → select target SaaS app
   - *Alternatively*: Open app in **Applications > Applications** → **Sign On** tab → set Authentication Policy

## Configuration Values

| Setting | Value |
|---|---|
| Okta Zone Type | IP Zone |
| Gateway IPs | Connector public exit IP(s) |
| Rule condition | NOT in zone |
| Rule action | Denied |
| Twingate Resource Policy | Device-only |

## Gotchas
- **Must use a DENY rule** (not allow) — deny access when user is *not* in the approved zone
- **Authentication loop risk**: Without Device-only Policy on the IdP Resource, users can't reach Okta to authenticate, creating a deadlock
- OIE uses "Authentication Policies" instead of "Sign On Policy" — found under Security menu, not Applications
- Applications can be assigned to OIE policy via the policy's Applications tab OR via the app's Sign On settings — both work

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- [Okta Classic vs Identity Engine differences](https://help.okta.com)
- [Okta OIE upgrade instructions](https://help.okta.com)
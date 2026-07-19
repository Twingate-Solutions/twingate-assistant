# SaaS App Gating with Okta

## Summary
Configure Twingate and Okta to require an active Twingate connection as a prerequisite for IdP authentication to SaaS apps. Traffic routes through a Twingate Connector's exit IP, which Okta uses as a network zone gate. Access is denied to SaaS apps if the user's request doesn't originate from the approved Connector IP.

## Key Information
- Works by routing Okta auth traffic through a Connector's public IP, then denying SaaS app access from any other IP
- Supports both Okta Classic Engine and Okta Identity Engine (OIE)
- Multiple Connectors behind NAT typically share one public IP; without NAT, add each Connector IP separately
- The gate enforces both Twingate authentication AND correct Group membership

## Prerequisites
- Twingate: Add `tenant.okta.com` as a Resource assigned to appropriate Groups
- Twingate: Apply a **Device-only Policy** to the Okta Resource to prevent authentication loops (users can reach Okta login without prior Twingate auth)
- Okta: Admin access to configure Network Zones and Sign On / Authentication Policies
- Know the public exit IP(s) of your Twingate Connector(s)

## Step-by-Step

### Twingate Setup
1. Create a Resource for `tenant.okta.com` and assign it to relevant Groups
2. Apply a Device-only Resource Policy to that Resource

### Okta Classic Engine
1. **Security > Networks** → **Add Zone > IP Zone**
2. Name the zone (e.g., "Twingate Connector Exit IP"), add Connector public IP(s) to **Gateway IPs**, click **Save**
3. **Applications > Applications** → select target app → **Sign On** tab → **Sign On Policy** → **+ Add Rule**
4. Configure rule:
   - **Who**: Users assigned to this app
   - **Location**: Not in Zone → select your IP Zone
   - **Access**: Denied

### Okta Identity Engine (OIE)
1. **Security > Networks** → **Add Zone > IP Zone** → same IP Zone setup as Classic
2. **Security > Authentication Policies** → **Add a policy** → name it → **Save**
3. **Add rule** inside policy:
   - **User's IP is**: Not in any of the following zones → select your IP Zone
   - **Access is**: Denied → **Save**
4. In the policy's **Applications** tab → **Add app** → select target app(s)
   - Alternatively: open app in **Applications > Applications** → **Sign On** tab → set Authentication Policy

## Configuration Values

| Field | Value |
|---|---|
| Okta Zone Type | IP Zone |
| Gateway IPs | Connector public exit IP(s) |
| Rule condition (Classic) | Not in Zone |
| Rule action | Denied |
| Resource Policy (Twingate) | Device-only |

## Gotchas
- **Auth loop risk**: Without a Device-only Policy on the Okta Resource, users can't authenticate with Okta to gain Twingate access, but can't get Twingate access without Okta auth
- Must use a **deny** rule (not allow), denying access when NOT in the approved zone
- Connectors not behind NAT may have multiple public IPs requiring multiple Gateway IP entries
- OIE uses "Authentication Policies" (Security menu); Classic uses "Sign On Policy" (per-app)

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- [Okta Classic vs OIE differences](https://help.okta.com)
- [Okta OIE upgrade instructions](https://help.okta.com)
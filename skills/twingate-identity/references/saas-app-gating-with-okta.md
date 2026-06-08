# SaaS App Gating with Okta

## Summary
Configure Twingate and Okta to enforce that users must be connected via a Twingate Connector before authenticating to SaaS applications. Access is gated by requiring traffic to originate from the Connector's exit IP address, configured as an Okta Network Zone. This replaces direct SaaS-level IP whitelisting with IdP-layer enforcement.

## Key Information
- Works by routing Okta authentication traffic through a Twingate Connector, making it appear from a known IP
- Deny-based rule: blocks authentication if user is **not** in the approved IP Zone
- Connectors behind NAT present a single public IP; multiple IPs needed only if Connectors have direct internet egress
- Supports both Okta Classic Engine and Identity Engine (OIE)

## Prerequisites
- Twingate: Add `tenant.okta.com` as a Resource assigned to appropriate Groups
- Twingate: Apply a **Device-only Policy** to the Okta Resource to prevent authentication loops
- Okta admin access to Security and Applications settings
- Know the public egress IP(s) of your Twingate Connector(s)

## Step-by-Step

### Twingate Setup
1. Create a Resource for your Okta tenant FQDN (e.g., `tenant.okta.com`)
2. Assign the Resource to relevant Groups
3. Apply a Device-only Resource Policy to `tenant.okta.com`

### Okta Classic Engine
1. **Security > Networks** → **Add Zone > IP Zone**
2. Set Zone Name (e.g., `Twingate Connector Exit IP`), enter Connector public IP in **Gateway IPs**, Save
3. **Applications > Applications** → select target app → **Sign On** tab → **Sign On Policy** → **+ Add Rule**
4. Configure rule: People = *Users assigned to this app*, Location = *Not in Zone* (select your zone), Access = **Denied**

### Okta Identity Engine (OIE)
1. **Security > Networks** → **Add Zone > IP Zone** → same IP zone setup as above
2. **Security > Authentication Policies** → **Add a policy**, name it, Save
3. Within policy → **Add rule**: set *User's IP is* = **Not in any of the following zones** (select your zone), *Access is* = **Denied**, Save
4. Navigate to **Applications** tab within the policy → **Add app** → select target app(s)

## Configuration Values
| Setting | Value |
|---|---|
| Twingate Resource | `tenant.okta.com` |
| Resource Policy | Device-only |
| Okta Zone type | IP Zone |
| Zone condition | NOT in zone (deny rule) |
| Access action | Denied |

## Gotchas
- **Must use a deny rule**, not an allow rule — deny if user is NOT in the zone
- Device-only policy on the Okta Resource is critical — omitting it causes an authentication loop where users can't reach Okta to authenticate for Twingate access
- Classic Engine uses "Sign On Policy" per app; OIE uses "Authentication Policies" applied to multiple apps
- If Connectors lack a shared NAT, multiple IPs may be required in the Zone

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- [Okta Classic vs Identity Engine differences](https://help.okta.com)
- [Okta OIE upgrade instructions](https://help.okta.com)
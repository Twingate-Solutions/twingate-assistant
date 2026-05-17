# SaaS App Gating with Okta

## Summary
Configures Okta to deny SaaS app authentication unless users are connecting through a Twingate Connector's exit IP. Works by creating an Okta Network Zone with the Connector's public IP, then applying a deny rule to app sign-on policies for users not in that zone.

## Key Information
- Replaces IP whitelisting in SaaS apps — IP check happens at IdP auth stage instead
- Connector exit IP must be static/predictable (typically behind NAT gateway = single public IP)
- Requires a **Device-only Policy** on the IdP Resource to prevent auth loops
- Works with both Okta Classic Engine and Okta Identity Engine (OIE)

## Prerequisites
- Twingate: Add `tenant.okta.com` as a Resource assigned to appropriate Groups
- Twingate: Apply **Device-only Resource Policy** to the Okta tenant Resource (prevents chicken-and-egg auth loop)
- Know the public exit IP address of your Twingate Connector(s)
- Okta admin access

## Step-by-Step

### Okta Classic Engine
1. **Security > Networks** → **Add Zone > IP Zone**
2. Name the zone (e.g., "Twingate Connector Exit IP"), enter Connector public IP in **Gateway IPs** → **Save**
3. **Applications > Applications** → select target app → **Sign On** tab → **Sign On Policy** → **+ Add Rule**
4. Configure rule:
   - People: Users assigned to this app
   - Location: **Not in Zone** → select your new IP Zone
   - Access: **Denied**

### Okta Identity Engine (OIE)
1. **Security > Networks** → **Add Zone > IP Zone** → enter Connector IP → **Save**
2. **Security > Authentication Policies** → **Add a policy** (name/describe) → **Save**
3. Within policy → **Add rule**:
   - **User's IP is**: Not in any of the following zones → select your IP Zone
   - **Access is**: Denied
4. **Applications** tab → **Add app** → select target app → **Done**

## Configuration Values

| Setting | Value |
|---|---|
| Twingate Resource | `tenant.okta.com` |
| Twingate Policy on IdP Resource | Device-only |
| Okta Zone type | IP Zone |
| Gateway IPs | Connector public exit IP(s) |
| Rule condition | NOT in zone |
| Rule action | Denied |

## Gotchas
- **Must use a deny rule** (not an allow rule) — deny access when user is NOT in the Connector IP zone
- Multiple Connectors without NAT may expose multiple public IPs — add each to the zone
- Skipping the Device-only policy on `tenant.okta.com` creates an auth loop: users can't reach Okta to authenticate because Twingate requires authentication first
- OIE uses "Authentication Policies" instead of "Sign On Policy" (different navigation path)

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- [Okta Classic vs Identity Engine differences](https://help.okta.com)
- [Okta OIE upgrade instructions](https://help.okta.com)
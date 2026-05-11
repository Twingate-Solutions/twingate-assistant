# SaaS App Gating with Okta

## Summary
Configure Twingate and Okta together to gate SaaS application access by requiring users to connect through a Twingate Connector before IdP authentication succeeds. Access control is enforced at the Okta sign-on policy level using the Connector's exit IP address rather than within the SaaS app itself.

## Key Information
- Twingate Connector's public IP becomes the "trusted IP" in Okta's network zone
- Multiple Connectors behind NAT typically share one public IP; multiple IPs needed only if Connectors have individual public IPs
- Works with both Okta Classic Engine and Identity Engine (OIE)
- Deny rules are used (not allow rules) — deny access if user is NOT in the approved zone

## Prerequisites
- Twingate Admin Console access
- Okta Admin Console access (Classic or OIE)
- Know the public exit IP of your Twingate Connector(s)
- Create a Twingate Resource for `tenant.okta.com` assigned to relevant Groups
- Apply a **Device-only Policy** to the Okta IdP Resource to prevent authentication loops

## Step-by-Step

### Twingate Setup
1. Create a Resource for `tenant.okta.com`, assign to appropriate Groups
2. Apply Device-only Resource Policy to that Resource (prevents chicken-and-egg auth loop)

### Okta Classic Engine
1. **Security > Networks** → **Add Zone > IP Zone**
2. Set Zone Name (e.g., "Twingate Connector Exit IP"), add Connector public IP to **Gateway IPs**, Save
3. **Applications > Applications** → select target app → **Sign On** tab
4. Scroll to **Sign On Policy** → **+ Add Rule**
5. Configure rule:

| Setting | Value |
|---|---|
| Who does this apply to | Users assigned to this app |
| Location | **Not in Zone** |
| Network Zones | (zone created above) |
| Platform | Any client |
| Access | **Denied** |

### Okta Identity Engine (OIE)
1. **Security > Networks** → **Add Zone > IP Zone** — same IP zone setup as Classic
2. **Security > Authentication Policies** → **Add a policy** (name + description) → Save
3. Within policy → **Add rule**:
   - **User's IP is**: Not in any of the following zones → select created zone
   - **Access is**: Denied
4. Save rule
5. Navigate to **Applications** tab within policy → **Add app** → select target app(s)
   - Alternatively: set policy via **Applications > Applications** → app → **Sign On** tab

## Configuration Values
- **Okta Network Zone type**: IP Zone
- **Gateway IPs**: Connector public egress IP(s)
- **Rule action**: Denied (not Allow — this is a deny-if-not-in-zone pattern)
- **Twingate Resource Policy**: Device-only (for IdP resource)

## Gotchas
- Must use a **deny rule** (deny if NOT in zone), not an allow rule
- Without Device-only Policy on the IdP Resource, users hit an auth loop — can't reach Okta to authenticate Twingate, can't reach Twingate without authenticating Okta
- If Connectors are not behind NAT, each Connector may have a distinct public IP — add all of them to the zone
- OIE uses "Authentication Policies" instead of "Sign On Policy" found in Classic

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- [Okta Classic vs OIE differences](https://help.okta.com)
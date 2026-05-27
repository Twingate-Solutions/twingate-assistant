# SaaS App Gating with Okta

## Summary
Configure Twingate and Okta to restrict SaaS application access by requiring users to connect through a Twingate Connector before IdP authentication succeeds. Works by whitelisting Connector exit IPs in Okta's network zones, then denying app sign-on from outside those zones.

## Key Information
- Replaces IP whitelisting in SaaS apps — enforcement happens at IdP auth stage instead
- Connector exit IP (usually a NAT gateway IP) is the trust anchor
- Works with both Okta Classic Engine and Okta Identity Engine (OIE)
- Requires a Device-only Policy on the IdP Resource to prevent auth loops

## Prerequisites
- Twingate Connector deployed with a known public exit IP
- Okta admin access (Classic Engine or OIE)
- Target SaaS app configured in Okta

## Step-by-Step

### Twingate Admin Console
1. Create a Resource for your Okta tenant URL (e.g., `tenant.okta.com`)
2. Assign Resource to appropriate Twingate Groups
3. Apply a **Device-only Policy** to the `tenant.okta.com` Resource (prevents auth loop)

### Okta Classic Engine
1. **Security > Networks > Add Zone > IP Zone**
2. Set Zone Name (e.g., `Twingate Connector Exit IP`), add Connector public IP to **Gateway IPs**, save
3. **Applications > [App] > Sign On > Sign On Policy > + Add Rule**
4. Configure rule: Users assigned to app, **Not in Zone** [your zone], **Access = Denied**

### Okta Identity Engine (OIE)
1. **Security > Networks > Add Zone > IP Zone** — same as Classic
2. **Security > Authentication Policies > Add a policy** — name and save
3. Within policy, **Add rule**: set `AND User's IP is` → `Not in any of the following zones` → [your zone]; set `THEN Access is` → `Denied`
4. In policy's **Applications** tab, click **Add app** and attach target SaaS app
   - Alternative: set policy directly via **Applications > [App] > Sign On**

## Configuration Values

| Setting | Value |
|---|---|
| Okta Zone Type | IP Zone |
| Gateway IPs | Connector public exit IP(s) |
| Rule condition | User's IP NOT in zone |
| Rule action | Access = Denied |
| Twingate Resource Policy | Device-only |

## Gotchas
- **Auth loop risk**: Without Device-only Policy on `tenant.okta.com`, users can't authenticate to reach Twingate, and can't reach Okta without Twingate
- **Multiple Connectors behind NAT**: Typically one IP; if Connectors have individual public IPs (no NAT), add each IP to the zone
- **Deny rule required**: Logic is "deny if NOT in zone" — not an allow rule
- Okta Classic uses "Sign On Policy"; OIE uses "Authentication Policies" — different navigation paths

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- [Okta Classic vs Identity Engine differences](https://help.okta.com)
- [Okta OIE upgrade instructions](https://help.okta.com)
# SaaS App Gating with Okta

## Summary
Configure Twingate and Okta to require an active Twingate connection as a prerequisite for IdP authentication to SaaS applications. Traffic routes through a Twingate Connector, presenting a known exit IP that Okta uses to allow/deny app sign-on. This replaces per-app IP whitelisting with IdP-level enforcement.

## Key Information
- Works by routing Okta auth traffic through a Twingate Connector with a known public IP
- Okta denies SaaS app access if auth request doesn't originate from the Connector's IP zone
- Supports both Okta Classic Engine and Okta Identity Engine (OIE)
- Multiple Connectors behind NAT = single public IP; otherwise add each Connector IP

## Prerequisites
**Twingate Admin Console:**
- Create a Resource for your Okta tenant FQDN (e.g., `tenant.okta.com`)
- Assign Resource to appropriate Group(s)
- Apply **Device-only Policy** to the Okta Resource (prevents auth loop where Twingate access requires Okta auth which requires Twingate access)

**Okta:**
- Admin Console access
- Know the public exit IP of your Twingate Connector(s)

## Step-by-Step

### Okta Classic Engine
1. **Security > Networks** → **Add Zone > IP Zone**
2. Set Zone Name (e.g., "Twingate Connector Exit IP"), enter Connector public IP in **Gateway IPs**, Save
3. **Applications > Applications** → select target app → **Sign On** tab → **Sign On Policy** → **+ Add Rule**
4. Configure rule: Users assigned to app | Location **Not in Zone** [your IP Zone] | Access = **Denied**

### Okta Identity Engine (OIE)
1. **Security > Networks** → **Add Zone > IP Zone** → enter Connector IP, Save
2. **Security > Authentication Policies** → **Add a policy** (name + description) → Save
3. Within policy → **Add rule**: set **User's IP is** = `Not in any of the following zones` [your IP Zone] | **Access is** = `Denied` → Save
4. Navigate to **Applications** tab within policy → **Add app** → select target app(s) → Done
   - *Alternatively:* Go to app directly → **Sign On** tab → specify Authentication Policy

## Configuration Values

| Setting | Value |
|---|---|
| Okta Zone Type | IP Zone |
| Rule logic | DENY when NOT in Connector IP Zone |
| Twingate Resource Policy | Device-only |
| Twingate Resource | `<tenant>.okta.com` |

## Gotchas
- **Must use a DENY rule** (deny access when NOT in zone) — not an allow rule
- **Device-only Policy is critical** on the Okta Resource: without it, users can't reach Okta to authenticate because Twingate requires auth first (circular dependency)
- Connectors not behind NAT require adding each Connector's IP individually to the zone
- OIE uses "Authentication Policies" instead of "Sign On Policy" — different navigation path

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- [Okta Classic vs Identity Engine differences](https://help.okta.com)
- [Okta OIE upgrade instructions](https://help.okta.com)
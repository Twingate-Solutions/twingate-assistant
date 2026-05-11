# SaaS App Gating with OneLogin

## Summary
Configure Twingate and OneLogin together to restrict SaaS application access based on IP address. Users must be connected to Twingate to authenticate through OneLogin, ensuring only authorized users on approved devices can reach protected apps.

## Key Information
- Uses Twingate Connector's exit IP as an allowlist in OneLogin App Policies
- Prevents direct SaaS app access without an active Twingate connection
- Requires a Device-only policy on the IdP Resource to avoid authentication loops
- Works per-app: each SaaS app gets the App Policy applied individually

## Prerequisites
- Twingate Admin Console access
- OneLogin Admin Console access
- Twingate Connectors deployed with a known public exit IP
- OneLogin tenant URL (e.g., `tenant.onelogin.com`)

## Step-by-Step

### Twingate Admin Console
1. **Create a Resource** for your OneLogin tenant FQDN (e.g., `tenant.onelogin.com`) and assign it to the appropriate Group(s)
2. **Apply a Device-only Policy** to that Resource — prevents auth loops where Twingate requires IdP login but IdP requires Twingate connectivity

### OneLogin Admin Console
3. Navigate to **Security → Policies** → **New App Policy**
4. Name the policy (e.g., `Twingate SaaS App Gate`)
5. In the **Allowed IP Addresses** field, enter the public exit IP of the Remote network where your Connectors are deployed
6. Navigate to **Applications → Applications** and select the target app (e.g., Google Workspace)
7. Go to **Access → Policies**, select your new App Policy, and **Save**

## Configuration Values
| Field | Value |
|---|---|
| Twingate Resource | `tenant.onelogin.com` (your OneLogin FQDN) |
| Twingate Resource Policy | Device-only |
| OneLogin Policy Type | App Policy |
| Allowed IP Addresses | Public exit IP of Twingate Remote network/Connector |

## Gotchas
- **Auth loop risk**: Without the Device-only policy on the IdP Resource, users can't reach OneLogin to authenticate, which blocks Twingate access — a circular dependency
- **IP specificity**: The allowed IP is tied to a specific Remote network; users must connect to the correct Twingate network with a Connector on that IP
- **Per-app configuration**: The App Policy must be applied to each SaaS application individually in OneLogin
- **Group scoping**: Only users in the correct Twingate Group have access to route through the Connector, enforcing both network and identity controls

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- SaaS App Gating (general concept)
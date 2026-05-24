# SaaS App Gating with OneLogin

## Summary
Configure OneLogin and Twingate to restrict SaaS application access by requiring users to route traffic through Twingate Connectors. OneLogin App Policies enforce IP-based access control, ensuring only users connected via Twingate can authenticate to protected apps.

## Key Information
- Access control is enforced via the public exit IP of Twingate Connectors
- Works for any SaaS app configured in OneLogin (e.g., Google Workspace)
- Prevents direct access to SaaS apps without an active Twingate connection

## Prerequisites
- Twingate Admin Console access
- OneLogin admin access
- At least one deployed Twingate Connector with a known public exit IP
- OneLogin tenant URL (format: `tenant.onelogin.com`)

## Step-by-Step

### Twingate Admin Console

1. **Create a Resource** for your OneLogin tenant FQDN (e.g., `tenant.onelogin.com`) and assign it to the appropriate Group(s)
2. **Apply a Device-only Policy** to the OneLogin IdP Resource — prevents authentication loop where users can't reach the IdP because Twingate requires IdP auth first

### OneLogin Admin Console

3. Navigate to **Security → Policies** → select **New App Policy**
4. Name the policy (e.g., `Twingate SaaS App Gate`)
5. In the **Allowed IP Addresses** field, enter the public exit IP of the Twingate Remote network/Connector
6. Navigate to **Applications → Applications** → select the target app (e.g., Google Workspace)
7. Go to **Access → Policies** → select your new App Policy → **Save**

## Configuration Values

| Field | Value |
|---|---|
| Resource FQDN | `tenant.onelogin.com` |
| Resource Policy type | Device-only |
| Allowed IP Addresses | Public exit IP of Twingate Connector(s) |

## Gotchas
- **Authentication loop risk**: Without a Device-only policy on the IdP Resource, users cannot reach OneLogin to authenticate, creating a deadlock. Device-only policy must be applied specifically to the IdP Resource.
- The exit IP used in OneLogin must match the specific Remote network where authorized Connectors are deployed
- Users must belong to the correct Twingate Group associated with the IdP Resource to route through the Connector

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
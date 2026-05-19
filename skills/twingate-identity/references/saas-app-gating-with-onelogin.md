# SaaS App Gating with OneLogin

## Summary
Configure Twingate and OneLogin together to restrict SaaS application access based on IP address. Users must connect through Twingate to authenticate via OneLogin, ensuring only authorized users from approved Connectors can access protected apps.

## Key Information
- Uses Twingate Connector's public exit IP as the allowed IP in OneLogin App Policies
- Protects any OneLogin-federated SaaS app (e.g., Google Workspace)
- Prevents authentication loops via Device-only Policy on the IdP Resource

## Prerequisites
- Twingate Admin Console access
- OneLogin Admin Console access
- Deployed Twingate Connector(s) with a known public exit IP
- OneLogin tenant URL (e.g., `tenant.onelogin.com`)

## Step-by-Step

### Twingate Admin Console

1. **Create a Resource** for your OneLogin tenant FQDN (e.g., `tenant.onelogin.com`) and assign it to relevant Groups
2. **Apply a Device-only Policy** to the OneLogin IdP Resource — prevents the auth loop where users can't reach the IdP because Twingate requires prior IdP authentication

### OneLogin Admin Console

3. Navigate to **Security → Policies** → select **New App Policy**
4. Name the policy (e.g., `Twingate SaaS App Gate`)
5. In the **Allowed IP Addresses** field, enter the public exit IP of the Twingate Remote network/Connector
6. Navigate to **Applications → Applications** → select the target app (e.g., Google Workspace)
7. Go to **Access → Policies** → select your new App Policy → **Save**

## Configuration Values

| Field | Value |
|---|---|
| OneLogin Resource URL | `tenant.onelogin.com` |
| Twingate Resource Policy | Device-only |
| OneLogin Allowed IP | Connector's public exit IP |

## Gotchas
- **Auth loop risk**: Without a Device-only Policy on the IdP Resource, users cannot reach OneLogin to authenticate because Twingate itself requires authentication — apply Device-only Policy to break this dependency
- The allowed IP must be the **exit IP of the Remote network** where Connectors are deployed, not the user's IP
- Access is enforced at both layers: Twingate Group membership AND OneLogin App Policy IP check

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- SaaS App Gating (general concept)
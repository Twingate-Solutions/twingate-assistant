# SaaS App Gating with JumpCloud

## Page Title
How to Configure SaaS App Gating with JumpCloud

## Summary
Twingate can gate SaaS application access by requiring users to route IdP authentication traffic through a Twingate Connector. JumpCloud's Conditional Access Policies then restrict SSO app access to the Connector's exit IP address, effectively replacing IP whitelisting at the SaaS layer with enforcement at the IdP authentication stage.

## Key Information
- Traffic routes through Connector, making JumpCloud see the Connector's public exit IP
- Multiple Connectors behind a NAT gateway share a single public IP (typical case)
- Multiple IPs needed only if Connectors have direct internet access without NAT (uncommon)
- IP List supports individual addresses, CIDR notation, and ranges

## Prerequisites
**Twingate Admin Console:**
- Create a Resource for `console.jumpcloud.com` assigned to appropriate Groups
- Apply a **Device-only Policy** to the JumpCloud Resource to prevent auth loops (users must reach IdP login without needing prior Twingate auth)

**JumpCloud:**
- Admin Portal access with permissions for Security Management

## Step-by-Step

### Create an IP List (JumpCloud)
1. Log in to JumpCloud Admin Portal
2. Navigate to **Security Management > Conditional Lists**
3. Click **( + )**
4. Set **List Name** (e.g., `Twingate Connectors`)
5. Enter public IP address(es) of Twingate Connectors
6. Click **Save**

### Create a Conditional Access Policy (JumpCloud)
1. Navigate to **Security Management > Conditional Policies**
2. Click **( + )** → select **SSO Applications**
3. Enter a unique **Policy Name**
4. Select target **SSO Applications**
5. Select target **Users & Groups**
6. Set condition matching (select "all" to require all conditions)
7. Click **Add Conditions** → select **IP List** → choose `Twingate Connectors`
8. Click **Create Policy**

## Configuration Values
| Item | Value/Notes |
|------|-------------|
| JumpCloud Resource FQDN | `console.jumpcloud.com` |
| Twingate Resource Policy | Device-only |
| IP source | Connector public exit IP(s) |
| JumpCloud policy type | SSO Applications |

## Gotchas
- **Auth loop risk**: Without a Device-only policy on the JumpCloud Resource, users cannot authenticate because Twingate access requires IdP auth — which requires Twingate access. Device-only policy breaks this cycle.
- **NAT assumption**: Most deployments use a single shared NAT IP. If Connectors have direct internet egress, multiple IPs must be added to the IP List.
- **Group assignment**: The JumpCloud Resource must be associated with Groups so users route through the Connector.

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- [JumpCloud: Managing IP Lists](https://jumpcloud.com/support)
- [JumpCloud: Access Policies for SSO Apps](https://jumpcloud.com/support)
# SaaS App Gating with JumpCloud

## Summary
Configure JumpCloud and Twingate so that IdP authentication to SaaS apps requires an active Twingate connection. Traffic routes through a Twingate Connector, presenting a known exit IP that JumpCloud's Conditional Access Policy validates before allowing SSO.

## Key Information
- Replaces IP whitelisting in individual SaaS apps — enforcement happens at the IdP auth stage
- Connector exit IP(s) are used as the trusted IP list in JumpCloud
- Multiple Connectors behind NAT = single public IP; without NAT, add each Connector IP individually

## Prerequisites
- Twingate Admin Console access
- JumpCloud Admin Portal access
- Public IP address(es) of Twingate Connector(s)
- JumpCloud SSO applications already configured

## Step-by-Step

### Twingate Admin Console
1. **Create a Resource** for `console.jumpcloud.com`, assign to relevant Groups
2. **Apply a Device-only Policy** to the `console.jumpcloud.com` Resource — prevents auth loop where users can't reach IdP without first authenticating via Twingate

### JumpCloud: Create IP List
1. Admin Portal → **Security Management > Conditional Lists**
2. Click **+**
3. Name: `Twingate Connectors` (or similar)
4. Enter Connector public IP(s) — supports individual IPs, CIDR, and ranges
5. Click **Save**

### JumpCloud: Create Conditional Access Policy
1. Admin Portal → **Security Management > Conditional Policies**
2. Click **+** → select **SSO Applications**
3. Enter a unique **Policy Name**
4. Select target **SSO Applications**
5. Select target **Users & Groups**
6. Set condition matching (all/any)
7. Click **Add Conditions** → select **IP List** → choose `Twingate Connectors`
8. Click **Create Policy**

## Configuration Values
| Item | Value |
|------|-------|
| Resource FQDN | `console.jumpcloud.com` |
| Resource Policy Type | Device-only |
| JumpCloud IP list scope | Connector public egress IP(s) |
| IP formats supported | Individual, CIDR, range |

## Gotchas
- **Auth loop risk**: Without the Device-only policy on the IdP Resource, users can't reach JumpCloud to authenticate, but Twingate requires authentication — apply Device-only policy to break this cycle
- **NAT**: Most Connectors share one public IP via NAT — verify before assuming multiple IPs are needed
- **Non-NAT deployments**: Each Connector's individual public IP must be added to the JumpCloud IP list

## Related Docs
- [Twingate: Create a Resource](https://www.twingate.com/docs)
- [Twingate: Device-only Resource Policy](https://www.twingate.com/docs)
- [JumpCloud: Managing IP Lists](https://jumpcloud.com/support)
- [JumpCloud: Access Policies for SSO Apps](https://jumpcloud.com/support)
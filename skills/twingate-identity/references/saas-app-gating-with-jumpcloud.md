# SaaS App Gating with JumpCloud

## Summary
Configures JumpCloud and Twingate to require an active Twingate Connector connection before users can authenticate to SSO/SaaS applications. Traffic routes through Twingate Connectors, presenting a known exit IP that JumpCloud's Conditional Access Policy validates before permitting IdP authentication.

## Key Information
- Twingate Connector exit IP acts as the trusted IP source for JumpCloud's Conditional Access Policy
- Multiple Connectors behind NAT share one public IP; Connectors without NAT require multiple IPs in the JumpCloud IP list
- IP list supports individual addresses, CIDR notation, and IP ranges

## Prerequisites
- Twingate Admin Console access
- JumpCloud Admin Portal access
- Public IP address(es) of Twingate Connector(s)
- JumpCloud SSO applications already configured

## Step-by-Step

### Twingate Configuration
1. Create a Twingate Resource for `console.jumpcloud.com`
2. Associate the Resource with appropriate Groups
3. Apply a **Device-only Policy** to the `console.jumpcloud.com` Resource (prevents auth loop: users need IdP to auth with Twingate, but need Twingate to reach IdP)

### JumpCloud: Create IP List
1. Admin Portal → **Security Management > Conditional Lists**
2. Click **+**
3. Set List Name (e.g., `Twingate Connectors`)
4. Enter Connector public IP(s)
5. Click **Save**

### JumpCloud: Create Conditional Access Policy
1. Admin Portal → **Security Management > Conditional Policies**
2. Click **+** → Select **SSO Applications**
3. Enter unique Policy Name
4. Select target SSO Applications
5. Select target Users & Groups
6. Configure condition matching (all/any)
7. Add condition: **IP List** → select `Twingate Connectors`
8. Click **Create Policy**

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Twingate Resource FQDN | `console.jumpcloud.com` |
| Resource Policy Type | Device-only |
| JumpCloud IP list source | Connector(s) public egress IP(s) |

## Gotchas
- **Auth loop**: Without a Device-only Policy on the JumpCloud Resource, users can't reach the IdP to authenticate with Twingate, and can't reach the IdP without Twingate — creating a deadlock
- **Multiple Connectors without NAT**: Each Connector presents its own public IP; all must be added to the JumpCloud IP list
- Conditional policy applies at **SSO authentication time**, not at the SaaS app level directly

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- [JumpCloud: Managing IP Lists](https://jumpcloud.com/support)
- [JumpCloud: Access Policies for SSO Apps](https://jumpcloud.com/support)
# SaaS App Gating with JumpCloud

## Summary
Configure JumpCloud and Twingate to gate SaaS application access by requiring users to route IdP authentication traffic through a Twingate Connector. Access approval occurs at the IdP authentication stage via JumpCloud Conditional Access Policies, using the Connector's exit IP as the trusted source.

## Key Information
- Traffic routed through Twingate Connector presents the Connector's public exit IP to JumpCloud
- Multiple Connectors behind NAT share one public IP; without NAT, each Connector IP must be added separately
- Device-only policy on the IdP resource prevents authentication loop (chicken-and-egg problem)
- IP lists support individual addresses, CIDR notation, and ranges

## Prerequisites
- Twingate Admin Console access
- JumpCloud Admin Portal access
- Public IP address(es) of Twingate Connector(s)
- JumpCloud SSO applications already configured

## Step-by-Step

### Twingate Admin Console
1. **Create a Resource** for `console.jumpcloud.com` and assign it to relevant Groups
2. **Apply a Device-only Policy** to that Resource (prevents auth loop where IdP access requires prior Twingate auth)

### JumpCloud — Create IP List
1. Navigate to **Security Management > Conditional Lists**
2. Click **+**
3. Set **List Name** (e.g., `Twingate Connectors`)
4. Enter Connector public IP(s) (individual, CIDR, or range)
5. Click **Save**

### JumpCloud — Create Conditional Access Policy
1. Navigate to **Security Management > Conditional Policies**
2. Click **+**, select **SSO Applications**
3. Enter a unique **Policy Name**
4. Select target **SSO Applications**
5. Select target **Users & Groups**
6. Set condition matching (all/any)
7. Click **Add Conditions** → select **IP List** → choose `Twingate Connectors`
8. Click **Create Policy**

## Configuration Values
| Setting | Value |
|---|---|
| JumpCloud Resource FQDN | `console.jumpcloud.com` |
| Twingate Policy Type | Device-only |
| IP List source | Connector public exit IP(s) |

## Gotchas
- **Auth loop risk**: Without a Device-only policy on the IdP resource, users cannot authenticate because reaching JumpCloud requires Twingate auth first
- **Multiple Connectors without NAT**: Each Connector's individual IP must be added to the IP list (uncommon scenario)
- **NAT assumption**: Most deployments share one public IP via NAT gateway — verify before adding IPs

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs/creating-resources)
- [Device-only Resource Policy](https://www.twingate.com/docs/resource-policies)
- [JumpCloud IP Lists Guide](https://jumpcloud.com/support/manage-ip-lists)
- [JumpCloud SSO Access Policies](https://jumpcloud.com/support/access-policies-for-sso-apps)
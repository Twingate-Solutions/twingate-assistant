# SaaS App Gating with JumpCloud

## Page Title
How to Configure SaaS App Gating with JumpCloud

## Summary
Forces JumpCloud IdP authentication traffic through a Twingate Connector, using the Connector's exit IP as the trusted IP in a JumpCloud Conditional Access Policy. This replaces SaaS-level IP whitelisting by enforcing the IP check at the IdP authentication stage.

## Key Information
- Twingate Connector's public IP becomes the "trusted IP" for JumpCloud SSO access
- Multiple Connectors behind NAT present a single public IP (most common case)
- Connectors not behind NAT may require multiple IPs in the JumpCloud IP list
- IP list supports individual addresses, CIDR notation, and ranges

## Prerequisites
- Twingate Admin Console access
- JumpCloud Admin Portal access
- Know the public IP(s) of your Twingate Connectors

## Step-by-Step

### Twingate Configuration
1. Create a Twingate Resource for `console.jumpcloud.com` and assign it to relevant Groups
2. Apply a **Device-only Policy** to that Resource (prevents auth loop where users can't reach IdP without first authenticating through Twingate)

### JumpCloud — Create IP List
1. Admin Portal → **Security Management > Conditional Lists**
2. Click **+**
3. Name: `Twingate Connectors` (or similar)
4. Enter Connector public IP(s)
5. Click **Save**

### JumpCloud — Create Conditional Access Policy
1. Admin Portal → **Security Management > Conditional Policies**
2. Click **+** → select **SSO Applications**
3. Enter a unique Policy Name
4. Select target SSO Applications
5. Select target Users & Groups
6. Set condition matching (all/any)
7. Click **Add Conditions** → select **IP List** → choose the Twingate Connectors list
8. Click **Create Policy**

## Configuration Values
| Parameter | Value |
|-----------|-------|
| JumpCloud FQDN (Resource) | `console.jumpcloud.com` |
| Twingate Resource Policy | Device-only |
| JumpCloud IP List name | `Twingate Connectors` (suggested) |
| Policy type | SSO Applications |

## Gotchas
- **Auth loop risk**: Without the Device-only Policy on the IdP Resource, users cannot authenticate with JumpCloud because accessing the IdP requires prior Twingate auth — apply Device-only Policy to break this dependency
- **Multi-Connector IPs**: If Connectors are NOT behind a shared NAT, each Connector's IP must be added individually to the IP list
- Conditional Access Policy scope applies per SSO application — ensure all intended apps are selected

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- [JumpCloud: Managing IP Lists](https://jumpcloud.com/support)
- [JumpCloud: Access Policies for SSO Apps](https://jumpcloud.com/support)
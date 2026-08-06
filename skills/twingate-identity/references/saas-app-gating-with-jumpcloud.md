---
source: https://www.twingate.com/docs/saas-app-gating-with-jumpcloud
type: docs
fetched: 2026-08-05
source_version: a3be6a244ec6852075e4a6cca43039e4b4e25461080f710d85834f9294b0b458
---

# SaaS App Gating with JumpCloud

## Summary
Configure JumpCloud Conditional Access Policies to require traffic routing through a Twingate Connector as a prerequisite for SSO authentication. This enforces network-level access control at the IdP authentication stage rather than within individual SaaS apps.

## Key Information
- Twingate Connector's exit IP acts as the trusted IP in JumpCloud's Conditional Access Policy
- Multiple Connectors behind NAT present a single public IP; without NAT, multiple IPs may be required
- Protects any SSO-connected SaaS app without configuring each app individually

## Prerequisites
- Twingate Admin Console access
- JumpCloud Admin Portal access
- Public IP address(es) of Twingate Connector(s)
- JumpCloud SSO applications already configured

## Step-by-Step

### Twingate Admin Console
1. **Add IdP FQDN as a Resource** — Create a Resource for `console.jumpcloud.com`, associate with relevant Groups
2. **Apply Device-only Policy** to the `console.jumpcloud.com` Resource — prevents authentication loop where users need IdP auth to reach the IdP

### JumpCloud Admin Portal — Create IP List
1. Navigate to **Security Management > Conditional Lists**
2. Click **+**
3. Set **List Name** (e.g., `Twingate Connectors`)
4. Enter Connector public IP(s) — supports individual IPs, CIDR notation, and ranges
5. Click **Save**

### JumpCloud Admin Portal — Create Conditional Access Policy
1. Navigate to **Security Management > Conditional Policies**
2. Click **+**, select **SSO Applications**
3. Enter a unique **Policy Name**
4. Select target **SSO Applications**
5. Select target **Users & Groups**
6. Set condition matching (all conditions or any)
7. Click **Add Conditions** → select **IP List** → choose `Twingate Connectors`
8. Click **Create Policy**

## Configuration Values
| Parameter | Value |
|---|---|
| Resource FQDN | `console.jumpcloud.com` |
| Resource Policy Type | Device-only |
| IP List source | Twingate Connector(s) public egress IP(s) |

## Gotchas
- **Auth loop risk**: Without a Device-only policy on the JumpCloud Resource, users cannot reach the IdP to authenticate, blocking all access
- **Multi-Connector IPs**: Connectors not behind a shared NAT gateway each have distinct public IPs — all must be added to the JumpCloud IP List
- **IP List flexibility**: JumpCloud accepts individual IPs, CIDR ranges, and IP ranges in the same list

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs/resources)
- [Device-only Resource Policy](https://www.twingate.com/docs/resource-policies)
- [JumpCloud IP Lists Guide](https://support.jumpcloud.com)
- [JumpCloud Access Policies for SSO Apps](https://support.jumpcloud.com)
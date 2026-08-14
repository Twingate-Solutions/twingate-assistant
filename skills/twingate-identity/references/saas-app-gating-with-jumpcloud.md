---
source: https://www.twingate.com/docs/saas-app-gating-with-jumpcloud
type: docs
fetched: 2026-08-14
source_version: 418062dc55e61de0ce6f8b68e9781da8722b67706965269dc935381b51092527
---

# SaaS App Gating with JumpCloud

## Summary
Configure JumpCloud Conditional Access Policies to require traffic routing through a Twingate Connector before IdP authentication succeeds. Access to SaaS apps is gated by the Connector's exit IP address rather than IP whitelisting in the SaaS app itself.

## Key Information
- Twingate Connector's public IP becomes the trusted IP for JumpCloud's Conditional Access Policy
- Multiple Connectors behind a NAT gateway present a single public IP (most common setup)
- Multiple Connectors **not** behind NAT require adding multiple IPs to the JumpCloud IP List
- Works by controlling the source IP of authentication requests, not application-level IP restrictions

## Prerequisites
- Twingate Admin Console access
- JumpCloud Admin Portal access
- Public IP address(es) of Twingate Connector(s)
- JumpCloud SSO applications already configured

## Step-by-Step

### Twingate Admin Console Setup
1. **Add IdP FQDN as a Resource** — Create a Resource for `console.jumpcloud.com` and assign it to the appropriate Groups
2. **Apply Device-only Policy** to the `console.jumpcloud.com` Resource — prevents authentication loop where users can't reach the IdP login portal without already being authenticated

### JumpCloud: Create an IP List
1. Log in to JumpCloud Admin Portal
2. Navigate to **SECURITY MANAGEMENT > Conditional Lists**
3. Click **+**
4. Set **List Name** (e.g., `Twingate Connectors`)
5. Enter Connector public IP(s) — supports individual IPs, CIDR notation, and ranges
6. Click **Save**

### JumpCloud: Create Conditional Access Policy
1. Navigate to **SECURITY MANAGEMENT > Conditional Policies**
2. Click **+**, select **SSO Applications**
3. Enter a unique **Policy Name**
4. Select target **SSO Applications**
5. Select target **Users & Groups**
6. Set condition matching (all conditions or any)
7. Click **Add Conditions**, select **IP List** → choose `Twingate Connectors`
8. Click **Create Policy**

## Configuration Values
| Parameter | Value |
|-----------|-------|
| JumpCloud Resource FQDN | `console.jumpcloud.com` |
| Twingate Policy Type | Device-only |
| JumpCloud Policy Scope | SSO Applications |

## Gotchas
- **Authentication loop risk**: Without a Device-only Policy on the IdP Resource, users cannot authenticate because reaching the IdP requires Twingate auth, which requires the IdP — apply Device-only Policy to break this cycle
- **NAT vs. non-NAT**: Confirm whether Connectors share a NAT gateway before configuring IP List; non-NAT setups need all individual Connector IPs added
- IP List supports mixed formats (individual, CIDR, range) in a single list

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- [JumpCloud IP Lists Guide](https://jumpcloud.com/support)
- [JumpCloud Access Policies for SSO Apps](https://jumpcloud.com/support)
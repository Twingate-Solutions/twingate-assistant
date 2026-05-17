# SaaS App Gating with JumpCloud

## Page Title
How to Configure SaaS App Gating with JumpCloud

## Summary
Requires users to route traffic through a Twingate Connector before JumpCloud IdP authentication succeeds. JumpCloud's Conditional Access Policy checks the source IP against a list of Twingate Connector exit IPs, blocking auth from non-Twingate connections. Replaces IP whitelisting at the SaaS app layer with enforcement at the IdP layer.

## Key Information
- Gate works by restricting JumpCloud SSO authentication to requests originating from Twingate Connector exit IPs
- Multiple Connectors behind NAT share one public IP; multiple IPs only needed if Connectors have direct internet egress (uncommon)
- IP list supports individual addresses, CIDR notation, and ranges

## Prerequisites

**Twingate Admin Console:**
1. **Add JumpCloud FQDN as a Resource** — Create a Resource for `console.jumpcloud.com`, assign to appropriate Groups
2. **Apply Device-only Policy** to that Resource — Prevents auth loop where users can't reach the IdP to authenticate with Twingate because Twingate requires IdP auth first

## Step-by-Step

### Create an IP List in JumpCloud
1. Log in to JumpCloud Admin Portal
2. Navigate to **SECURITY MANAGEMENT > Conditional Lists**
3. Click **+**
4. Set **List Name** (e.g., `Twingate Connectors`)
5. Enter Connector public IP address(es)
6. Click **Save**

### Create a Conditional Access Policy
1. Navigate to **SECURITY MANAGEMENT > Conditional Policies**
2. Click **+** → select **SSO Applications**
3. Enter a unique **Policy Name**
4. Select target **SSO Applications**
5. Select target **Users & Groups**
6. Set condition matching (all conditions must be met)
7. Click **Add Conditions** → select **IP List** → choose `Twingate Connectors`
8. Click **Create Policy**

## Configuration Values
| Field | Value |
|-------|-------|
| Resource FQDN | `console.jumpcloud.com` |
| Resource Policy Type | Device-only |
| JumpCloud Policy Type | SSO Applications |
| IP List Source | Twingate Connector public exit IP(s) |

## Gotchas
- **Auth loop risk**: Without a Device-only policy on the JumpCloud Resource, users cannot authenticate with JumpCloud (needed for Twingate) because they haven't authenticated with Twingate yet — circular dependency
- **NAT assumption**: Most deployments share one NAT IP; verify before assuming single-IP configuration is sufficient
- **Connector IP changes**: If Connector exit IPs change, the JumpCloud IP list must be updated manually

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- [JumpCloud: Managing IP Lists](https://jumpcloud.com/support)
- [JumpCloud: Access Policies for SSO Apps](https://jumpcloud.com/support)
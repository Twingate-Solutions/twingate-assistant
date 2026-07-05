# SaaS App Gating with OneLogin

## Summary
Restricts SaaS application access by requiring users to route through Twingate before authenticating with OneLogin. OneLogin App Policies enforce that only requests originating from Twingate Connector exit IPs are permitted to access protected applications.

## Key Information
- Uses Twingate Connector's public exit IP as an allowlist in OneLogin App Policy
- Protects any OneLogin-federated SaaS app (e.g., Google Workspace)
- Requires Device-only Policy on the IdP resource to prevent authentication loops

## Prerequisites
- Twingate admin access with ability to create Resources and Policies
- OneLogin admin access with ability to create App Policies
- Twingate Connector(s) deployed with known public exit IP address(es)

## Step-by-Step

### Twingate Admin Console
1. Create a Resource for your OneLogin tenant URL (e.g., `tenant.onelogin.com`)
2. Associate the Resource with the appropriate Group(s)
3. Apply a **Device-only Policy** to the `tenant.onelogin.com` Resource

### OneLogin Admin Console
4. Navigate to **Security → Policies** → **New App Policy**
5. Name the policy (e.g., "Twingate SaaS App Gate")
6. In **Allowed IP Addresses**, enter the public exit IP of the Twingate Remote network/Connector
7. Save the App Policy
8. Navigate to **Applications → Applications** → select target app
9. Go to **Access → Policies**, select the new App Policy, and save

## Configuration Values
| Value | Description |
|---|---|
| `tenant.onelogin.com` | OneLogin tenant FQDN to use as Twingate Resource |
| Connector exit IP | Public IP of Twingate Remote network; added to OneLogin Allowed IP Addresses |

## Gotchas
- **Authentication loop risk**: Without a Device-only Policy on the IdP Resource, users can't reach OneLogin to authenticate because Twingate requires authentication first — apply Device-only Policy to break this cycle
- The exit IP in OneLogin must match the Connector's public IP, not an internal/private IP
- All users requiring access to the gated app must belong to the Twingate Group associated with the `tenant.onelogin.com` Resource

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- SaaS App Gating general configuration
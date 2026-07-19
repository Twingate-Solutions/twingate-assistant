# SaaS App Gating with OneLogin

## Summary
Configure Twingate and OneLogin together to restrict SaaS application access so that only users connected through Twingate can authenticate. OneLogin's App Policy checks the source IP, which must match the Twingate Connector's exit IP.

## Key Information
- Twingate acts as a network gateway; OneLogin enforces IP-based app access policies
- Users must route through a Twingate Connector to reach the OneLogin tenant and downstream SaaS apps
- The Connector's public exit IP is the enforcement mechanism in OneLogin

## Prerequisites
- Twingate Admin Console access
- OneLogin Admin Console access
- At least one deployed Twingate Connector with a known public exit IP
- Target SaaS app already configured in OneLogin (e.g., Google Workspace)

## Step-by-Step

### Twingate Configuration
1. **Create a Resource** for your OneLogin tenant FQDN (e.g., `tenant.onelogin.com`) and assign it to the appropriate Group(s)
2. **Apply a Device-only Policy** to that Resource — this prevents authentication loops where Twingate requires IdP login to reach the IdP

### OneLogin Configuration
3. Navigate to **Security → Policies** → **New App Policy**
4. Name the policy (e.g., `Twingate SaaS App Gate`)
5. In **Allowed IP Addresses**, enter the public exit IP of the Twingate Remote Network's Connector(s)
6. Navigate to **Applications → Applications** → select the target app
7. Go to **Access → Policies**, select the new App Policy, and **Save**

## Configuration Values
| Field | Value |
|---|---|
| Twingate Resource | `tenant.onelogin.com` (your org's OneLogin URL) |
| Resource Policy Type | Device-only |
| OneLogin Allowed IP | Public exit IP of Twingate Connector(s) |

## Gotchas
- **Authentication loop risk**: Without a Device-only Policy on the IdP Resource, users can't authenticate with OneLogin because Twingate requires prior authentication — apply Device-only Policy to break this dependency
- **Multiple Connectors**: If multiple Connectors are deployed in the Remote Network, ensure all their exit IPs are added to OneLogin's Allowed IP Addresses field
- **Group scoping**: Only users in the correct Twingate Group will route through the Connector to the IdP Resource; others will be blocked at the OneLogin IP policy level

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- SaaS App Gating with other IdPs (Okta, Azure AD)
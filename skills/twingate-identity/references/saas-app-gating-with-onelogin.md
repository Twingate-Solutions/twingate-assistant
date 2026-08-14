---
source: https://www.twingate.com/docs/saas-app-gating-with-onelogin
type: docs
fetched: 2026-08-14
source_version: 8bb56b50c0e29c780083702af0d63b550416c72e16550504a2ffeff6697c4b34
---

# SaaS App Gating with OneLogin

## Summary
Configures OneLogin to restrict SaaS application access to users connected through Twingate by whitelisting Connector exit IPs in OneLogin App Policies. Users must route through Twingate to authenticate, ensuring only authorized Twingate Group members can access protected apps.

## Key Information
- Uses Twingate Connector's public exit IP as the trusted IP in OneLogin App Policies
- Protects SaaS apps (e.g., Google Workspace) by requiring Twingate connection for OneLogin authentication
- Applies a Device-only Policy to the IdP Resource to prevent authentication loops

## Prerequisites
- Twingate Admin Console access
- OneLogin admin access
- Twingate Connector(s) deployed with a known public exit IP
- OneLogin tenant URL (e.g., `tenant.onelogin.com`)

## Step-by-Step

### Twingate Configuration
1. **Create a Resource** for your OneLogin tenant URL (e.g., `tenant.onelogin.com`) and assign it to the appropriate Group(s)
2. **Apply a Device-only Policy** to the OneLogin Resource — prevents authentication loops where Twingate auth is required before reaching the IdP

### OneLogin Configuration
3. Navigate to **Security → Policies** → **New App Policy**
4. Name the policy (e.g., "Twingate SaaS App Gate")
5. In **Allowed IP Addresses**, enter the public exit IP of the Twingate Remote network/Connector
6. Navigate to **Applications → Applications**, select the target app (e.g., Google Workspace)
7. Go to **Access → Policies**, select your new App Policy, and save

## Configuration Values
| Field | Value |
|-------|-------|
| OneLogin Resource URL | `<tenant>.onelogin.com` |
| Allowed IP Address | Public exit IP of Twingate Connector |
| Twingate Policy on IdP Resource | Device-only |

## Gotchas
- **Authentication loop risk**: Without a Device-only Policy on the IdP Resource, users cannot reach OneLogin to authenticate because Twingate requires prior auth — apply Device-only to break the loop
- The allowed IP must be the **Connector's public exit IP**, not the user's IP — ensure Connectors have stable/static public IPs
- Users must belong to the correct **Twingate Group** that has access to the OneLogin Resource

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- SaaS App Gating general configuration
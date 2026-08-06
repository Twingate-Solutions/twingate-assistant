---
source: https://www.twingate.com/docs/saas-app-gating-with-onelogin
type: docs
fetched: 2026-08-05
source_version: 58265894f8b298e56e8e298a9cd5ed3897ac03e2f0077001a436054c3398f877
---

# SaaS App Gating with OneLogin

## Summary
Configures OneLogin to restrict SaaS application access by IP allowlist, where the allowed IP is the Twingate Connector's exit IP. Users must be connected to Twingate to authenticate through OneLogin and access protected apps.

## Key Information
- Traffic routed through Twingate Connector gives users a predictable exit IP
- OneLogin App Policy enforces IP-based access control to specific applications
- Device-only policy on the IdP Resource prevents authentication loops
- Access control is enforced at the OneLogin app level, not the network level

## Prerequisites
- Twingate Admin Console access
- OneLogin admin access
- One or more Twingate Connectors deployed with known public exit IPs
- Target SaaS app configured in OneLogin (e.g., Google Workspace)

## Step-by-Step

### Twingate Configuration
1. Create a Twingate Resource for your OneLogin tenant FQDN (e.g., `tenant.onelogin.com`)
2. Associate the Resource with the appropriate Twingate Group(s)
3. Apply a **Device-only Resource Policy** to the `tenant.onelogin.com` Resource

### OneLogin Configuration
4. Navigate to **Security → Policies → New App Policy**
5. Name the policy (e.g., "Twingate SaaS App Gate")
6. Enter the Connector's **public exit IP** in the **Allowed IP Addresses** field
7. Navigate to **Applications → Applications**, select target app
8. Go to **Access → Policies**, apply the new App Policy, and save

## Configuration Values

| Parameter | Value |
|---|---|
| Twingate Resource | `tenant.onelogin.com` (your org's OneLogin URL) |
| Resource Policy | Device-only |
| OneLogin Allowed IP | Public exit IP of Twingate Remote network Connector |

## Gotchas
- **Authentication loop risk**: Without Device-only policy on the IdP Resource, users cannot reach OneLogin to authenticate because Twingate itself requires authentication — apply Device-only policy to break the loop
- The exit IP must be the Connector's **public** IP, not internal/private IP
- If Connectors are deployed across multiple Remote networks, ensure the correct network's exit IP is used in the allowlist
- All users requiring access to gated apps must belong to the Twingate Group associated with the `tenant.onelogin.com` Resource

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- SaaS App Gating (general concept)
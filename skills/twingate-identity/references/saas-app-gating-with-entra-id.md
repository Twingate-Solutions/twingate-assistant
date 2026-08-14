---
source: https://www.twingate.com/docs/saas-app-gating-with-entra-id
type: docs
fetched: 2026-08-14
source_version: 4bcdc96c2f86c05e60d000f665f4fe28979bcc46b700e31ed8bd80b64fba8036
---

# SaaS App Gating with Microsoft Entra ID

## Summary
Configure Twingate and Microsoft Entra ID to gate SaaS application access by requiring an active Twingate Connector connection before IdP authentication succeeds. This uses Connector egress IP addresses as trusted Named Locations in Entra ID Conditional Access Policies instead of per-app IP allowlists.

## Key Information
- Traffic routed through Twingate Connector gives users a predictable egress IP used as the trust signal in Entra ID
- Works at IdP auth stage, not at the SaaS app level
- Applies to any app(s) assignable via Entra ID Conditional Access

## Prerequisites
- Twingate Admin Console access
- Microsoft Entra ID admin access with Conditional Access permissions
- Connector egress IP address (typically NAT gateway IP)

## Step-by-Step

### Twingate Admin Console
1. **Create a Resource** for your Entra ID tenant FQDN (e.g., `tenant.office.com` or `login.microsoftonline.com`) and assign it to appropriate Groups
2. **Apply a Device-only Policy** to the IdP Resource — prevents authentication loop where users need IdP auth to reach Twingate but need Twingate to reach IdP

### Entra ID Portal
3. **Create a Named Location** (Conditional Access > Named Locations) using the Connector's egress IP address; mark it as trusted
4. **Create a Conditional Access Policy** with:
   - **Apps**: Select the SaaS app(s) to restrict
   - **Location condition**: `Selected locations` → choose the trusted Named Location created above

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Resource FQDN | `tenant.office.com` or `login.microsoftonline.com` |
| Twingate Resource Policy | Device-only |
| Entra ID Named Location type | IP ranges (Conditional Access) |
| IP address to use | Connector NAT gateway egress IP |
| Location condition type | Selected locations (trusted) |

## Gotchas
- **Authentication loop**: Without a Device-only Policy on the IdP Resource, users cannot authenticate because reaching the IdP requires prior Twingate auth — apply Device-only policy to break this circular dependency
- **IP source**: Use the NAT gateway IP for egress, not the Connector's private IP
- **Multiple Connectors**: If multiple Connectors share the Remote Network, ensure all their egress IPs are included in the Named Location

## Related Docs
- [SaaS App Gating Office 365 with Entra ID](https://www.twingate.com/docs/saas-app-gating-office-365-with-entra-id) — step-by-step example
- Twingate: Create a Resource
- Twingate: Device-only Resource Policy
- Microsoft: Named Locations (Entra ID documentation)
- Microsoft: Location condition in Conditional Access
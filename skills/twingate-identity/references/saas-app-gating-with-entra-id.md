# SaaS App Gating with Microsoft Entra ID

## Summary
Configure Twingate and Microsoft Entra ID so that SaaS app access requires an active Twingate connection. Authentication attempts to Entra ID-protected apps must originate from a Twingate Connector's egress IP, enforced via Conditional Access Named Locations instead of SaaS-level IP whitelisting.

## Key Information
- Twingate Connector's egress IP (typically a NAT gateway IP) acts as the trusted IP for Entra ID Conditional Access
- Works at IdP authentication stage, not at the SaaS app level
- Requires a Device-only Policy on the IdP Resource to prevent authentication loops

## Prerequisites
- Twingate Admin Console access with ability to create Resources and Policies
- Microsoft Entra ID admin access with Conditional Access permissions
- Known egress IP address of Twingate Connector(s)/NAT gateway for the Remote Network

## Step-by-Step

### Twingate Configuration
1. **Create a Resource** for your Entra ID tenant authentication FQDN (e.g., `tenant.office.com` or `login.microsoftonline.com`)
2. **Associate the Resource** with the appropriate Twingate Group(s)
3. **Apply a Device-only Policy** to the IdP Resource — prevents the chicken-and-egg auth loop where Twingate requires IdP auth but IdP is only reachable through Twingate

### Entra ID Configuration
4. **Create a Named Location** in Entra ID Portal → Conditional Access using the Connector's egress IP address (NAT gateway IP)
5. **Mark the Named Location as trusted**
6. **Create a Conditional Access Policy**:
   - Select the target app(s) to restrict
   - Set location condition to **Selected locations**
   - Choose the trusted Named Location created in step 4

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Resource FQDN | `tenant.office.com` or `login.microsoftonline.com` |
| Resource Policy type | Device-only |
| Named Location IP | Connector NAT gateway egress IP |
| Conditional Access location type | Selected locations (trusted) |

## Gotchas
- **Auth loop risk**: Without a Device-only Policy on the IdP Resource, users can't authenticate with Entra ID because Twingate requires prior authentication — apply Device-only Policy to break this dependency
- **IP source**: Use the NAT gateway egress IP, not the Connector's internal IP
- **Multiple Connectors**: If multiple Connectors share a Remote Network, ensure all their egress IPs are included in the Named Location

## Related Docs
- [Device-only Resource Policy](https://www.twingate.com/docs) — Twingate docs
- [Create a Twingate Resource](https://www.twingate.com/docs) — Twingate docs
- [SaaS App Gating Office 365 with Entra ID](https://www.twingate.com/docs) — step-by-step example
- [Microsoft Named Locations documentation](https://learn.microsoft.com/en-us/entra/identity/conditional-access/location-condition) — Entra ID docs
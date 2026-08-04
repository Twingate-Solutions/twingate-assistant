# SaaS App Gating with Microsoft Entra ID

## Page Title
How to Configure SaaS App Gating with Microsoft Entra ID

## Summary
SaaS app gating uses Twingate Connectors as a network prerequisite for Entra ID authentication, replacing IP whitelisting in SaaS apps. Users must connect through an authorized Twingate Connector (with a known egress IP) before IdP authentication succeeds. The IP check occurs at the Entra ID Conditional Access layer, not within the SaaS application itself.

## Key Information
- Twingate Connector's egress IP becomes the trusted IP in Entra ID Named Locations
- Conditional Access Policy enforces that only traffic from the Connector IP can authenticate to target SaaS apps
- Twingate Group membership controls which users can reach the Connector/Resource

## Prerequisites
- Twingate Admin Console access
- Microsoft Entra ID admin access with Conditional Access permissions
- Known egress IP of Twingate Connector(s) (typically a NAT gateway IP)

## Step-by-Step

### Twingate Configuration
1. **Create a Resource** for your Entra ID authentication FQDN (e.g., `tenant.office.com` or `login.microsoftonline.com`); assign it to appropriate Groups
2. **Apply a Device-only Policy** to the IdP Resource — prevents authentication loops where Twingate auth requires IdP access but IdP access requires Twingate auth

### Entra ID Configuration
3. **Create a Named Location** in Entra ID Portal → Conditional Access using the Connector's egress IP address (NAT gateway IP)
4. **Create a Conditional Access Policy** with:
   - Target app(s) to restrict
   - Location condition: **Selected locations** → choose the trusted Named Location created above

## Configuration Values

| Item | Value/Notes |
|------|-------------|
| Resource FQDN | `tenant.office.com` or `login.microsoftonline.com` |
| Resource Policy | Device-only |
| Named Location IP | Connector egress/NAT gateway IP |
| Location condition type | Selected locations (trusted Named Location) |

## Gotchas
- **Authentication loop risk**: Without a Device-only policy on the IdP Resource, users cannot authenticate with Entra ID because Twingate requires prior auth — apply Device-only policy to break this circular dependency
- **NAT gateway IP**: Use the NAT gateway IP (not the Connector's private IP) as the Named Location address — this is the actual egress IP Entra ID sees
- Connector IP changes will break the Conditional Access Policy; update Named Location if Connector egress IP changes

## Related Docs
- [SaaS App Gating Office 365 with Entra ID](https://www.twingate.com/docs/saas-app-gating-office-365-with-entra-id) — step-by-step example
- Twingate: Create a Resource
- Twingate: Device-only Resource Policy
- Microsoft: Named Locations (Conditional Access)
- Microsoft: Location condition configuration
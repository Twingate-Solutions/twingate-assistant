# SaaS App Gating with Microsoft Entra ID

## Page Title
How to Configure SaaS App Gating with Microsoft Entra ID

## Summary
SaaS app gating with Twingate and Entra ID enforces an authorized Twingate Connector connection as a prerequisite for IdP authentication to SaaS apps. Instead of IP whitelisting inside the SaaS app, the IP check occurs at the Entra ID Conditional Access stage. Users must route through a Twingate Connector, whose egress IP is registered as a trusted Named Location in Entra ID.

## Key Information
- Traffic flows through Twingate Connector → Connector egress IP is registered in Entra ID as trusted Named Location → Conditional Access Policy enforces that SaaS app access only succeeds from that IP
- The Connector's egress IP (typically a NAT gateway IP) is the critical linking value between Twingate and Entra ID
- Only users in the correct Twingate Group with authorized accounts can reach the Connector exit IP

## Prerequisites
- Twingate admin access with ability to create Resources and Policies
- Entra ID admin access with Conditional Access licensing
- Known egress IP(s) for the Twingate Connector(s) / NAT gateway

## Step-by-Step

### Twingate Admin Console
1. **Create a Resource** for the Entra ID authentication FQDN (e.g., `tenant.office.com` or `login.microsoftonline.com`) and assign it to the appropriate Group(s)
2. **Apply a Device-only Policy** to that IdP Resource — prevents authentication loops where users can't reach the IdP because Twingate itself requires IdP auth first

### Entra ID Portal
3. **Create a Named Location** (Conditional Access → Named Locations) using the Connector egress IP address(es) — mark it as trusted
4. **Create a Conditional Access Policy** with:
   - Target app(s) to restrict
   - Location condition: **Selected locations** → choose the trusted Named Location created above

## Configuration Values

| Value | Description |
|-------|-------------|
| `tenant.office.com` | Example IdP Resource FQDN |
| `login.microsoftonline.com` | Alternative generic Entra ID login FQDN |
| Connector egress IP | NAT gateway IP used by Connectors; used in Named Location |
| Device-only Policy | Policy type applied to IdP Resource to break auth loops |
| Selected locations | Location condition type in Conditional Access Policy |

## Gotchas
- **Auth loop risk**: Without a Device-only Policy on the IdP Resource, users cannot authenticate with Entra ID because Twingate requires Entra ID auth first — always apply Device-only Policy to the IdP Resource
- The egress IP used in Named Location is typically the **NAT gateway IP**, not the Connector host IP directly
- Policy restricts by Group membership — ensure users are in the correct Twingate Group

## Related Docs
- [SaaS App Gating Office 365 with Entra ID](https://www.twingate.com/docs/saas-app-gating-office-365-with-entra-id) — step-by-step example
- Twingate: Create a Resource
- Twingate: Device-only Resource Policy
- Microsoft: Named Locations (Conditional Access)
- Microsoft: Location conditions in Conditional Access
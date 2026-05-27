# SaaS App Gating with Microsoft Entra ID

## Page Title
How to Configure SaaS App Gating with Microsoft Entra ID

## Summary
SaaS app gating forces users to connect through a Twingate Connector before IdP authentication succeeds, replacing IP whitelisting in SaaS apps with IP enforcement at the Entra ID Conditional Access layer. Access is approved/denied based on whether the user's traffic exits from a Connector-associated IP address.

## Key Information
- IP check occurs at IdP auth stage, not within the SaaS application itself
- Connector egress IP (typically a NAT gateway IP) is registered as a trusted Named Location in Entra ID
- Conditional Access Policy restricts app access to that Named Location only
- Users must be in the correct Twingate Group to route through the authorized Connector

## Prerequisites
- Twingate Admin Console access
- Microsoft Entra ID admin access with Conditional Access permissions
- Twingate Connector deployed with a known, stable egress IP (NAT gateway recommended)

## Step-by-Step

### Twingate Admin Console
1. **Create a Resource** for your Entra ID tenant URL (e.g., `tenant.office.com` or `login.microsoftonline.com`) and assign it to the relevant Group(s)
2. **Apply a Device-only Policy** to the IdP Resource — prevents authentication loops where users can't reach the IdP login portal because Twingate auth hasn't completed yet

### Microsoft Entra ID Portal
3. **Create a Named Location** (Conditional Access > Named Locations) using the Connector's egress IP address; mark it as trusted
4. **Create a Conditional Access Policy** with:
   - Target: selected SaaS app(s)
   - Location condition: `Selected locations` → choose the trusted Named Location created above

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Resource FQDN | `tenant.office.com` or `login.microsoftonline.com` |
| Resource Policy type | Device-only |
| Named Location IP | Connector NAT gateway egress IP |
| Conditional Access location type | Selected locations (trusted Named Location) |

## Gotchas
- **Authentication loop risk**: Without a Device-only policy on the IdP Resource, users cannot reach the login portal to authenticate — creating a circular dependency
- **IP must be static**: The Connector egress IP registered in Entra ID must be stable; dynamic IPs will break the Conditional Access Policy
- **NAT gateway IP, not Connector IP**: Use the NAT gateway egress IP, not the Connector's internal IP address

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- [Entra ID Named Locations documentation](https://learn.microsoft.com/en-us/entra/identity/conditional-access/location-condition)
- [SaaS App Gating Office 365 with Entra ID](https://www.twingate.com/docs/saas-app-gating-office-365-with-entra-id) — step-by-step walkthrough example
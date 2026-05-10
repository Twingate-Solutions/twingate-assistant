# SaaS App Gating with Microsoft Entra ID

## Page Title
How to Configure SaaS App Gating with Microsoft Entra ID

## Summary
SaaS app gating with Twingate and Entra ID enforces that users must be connected through a Twingate Connector before IdP authentication succeeds. This works by routing IdP auth traffic through a Connector's egress IP, then using Entra ID Conditional Access Named Locations to allowlist that IP. Replaces per-app IP whitelisting with network-level enforcement at auth time.

## Key Information
- Authentication check happens at IdP auth stage, not within individual SaaS apps
- Connector egress IP (typically a NAT gateway IP) is used as the trusted Named Location in Entra ID
- Applies to any SaaS app using Entra ID for SSO
- Chicken-and-egg problem is solved via Device-only Resource Policy on the IdP Resource

## Prerequisites
- Twingate Admin Console access
- Microsoft Entra ID admin access with Conditional Access permissions
- Known egress IP(s) for Twingate Connector(s) / NAT gateway

## Step-by-Step

### Twingate Configuration
1. **Create a Resource** for your Entra ID tenant URL (e.g., `tenant.office.com` or `login.microsoftonline.com`) and assign it to the appropriate Group(s)
2. **Apply a Device-only Policy** to the IdP Resource — prevents auth loops where accessing the IdP login requires prior Twingate auth

### Entra ID Configuration
3. **Create a Named Location** in Entra ID Portal → Conditional Access, using the Connector egress IP (NAT gateway IP)
4. **Create a Conditional Access Policy** with:
   - Target: selected SaaS app(s)
   - Location condition: `Selected locations` → the Named Location created above
   - Effect: block access from outside the trusted Named Location

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Resource FQDN examples | `tenant.office.com`, `login.microsoftonline.com` |
| Resource Policy type | Device-only |
| Entra Named Location IP | Connector NAT gateway egress IP |
| Conditional Access location type | Selected locations (trusted) |

## Gotchas
- **Auth loop risk**: Without Device-only Policy on the IdP Resource, users can't reach the IdP to authenticate, creating an unresolvable dependency
- **Egress IP accuracy**: Use the NAT gateway IP, not individual Connector IPs, if Connectors share a gateway for egress
- **Group assignment matters**: Only users in the correct Twingate Group will exit from the expected IP; misassigned users will fail Conditional Access

## Related Docs
- [Create a Twingate Resource](#) — initial Resource setup
- [Device-only Resource Policy](#) — policy type reference
- [Entra ID Named Locations documentation](https://learn.microsoft.com/en-us/entra/identity/conditional-access/location-condition)
- [SaaS App Gating Office 365 with Entra ID](#) — step-by-step example walkthrough
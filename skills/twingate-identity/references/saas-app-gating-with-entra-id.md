# SaaS App Gating with Microsoft Entra ID

## Summary
Configure Twingate and Microsoft Entra ID so that users must be connected through a Twingate Connector before IdP authentication is allowed for SaaS apps. This replaces IP whitelisting in individual SaaS apps by enforcing the IP check at the Entra ID Conditional Access layer.

## Key Information
- Traffic through Twingate Connector exits via a known IP (typically a NAT gateway), which is used as the trusted location in Entra ID
- Works by restricting Entra ID Conditional Access to only allow logins from the Connector egress IP
- Applies to any SaaS app using Entra ID for authentication

## Prerequisites
- Twingate admin access with ability to create Resources and Policies
- Entra ID admin access with Conditional Access permissions
- Known egress IP of the Twingate Connector(s) / NAT gateway for the Remote Network

## Step-by-Step

### Twingate Admin Console
1. **Create a Resource** for the Entra ID login FQDN (e.g., `tenant.office.com` or `login.microsoftonline.com`) and assign it to the appropriate Group(s)
2. **Apply a Device-only Policy** to the IdP Resource — prevents authentication loops where users can't reach the IdP because Twingate requires prior IdP auth

### Entra ID Portal
3. **Create a Named Location** (Conditional Access → Named locations) using the Connector egress IP address
4. **Create a Conditional Access Policy** with:
   - Target: the SaaS app(s) to restrict
   - Location condition: **Selected locations** → the Named location created above

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Twingate Resource FQDN | `tenant.office.com` or `login.microsoftonline.com` |
| Twingate Policy type | Device-only |
| Entra ID Named location IP | Connector NAT gateway egress IP |
| Entra ID location condition type | Selected locations (trusted) |

## Gotchas
- **Authentication loop risk**: Without a Device-only Policy on the IdP Resource, users cannot reach the Entra ID login page because Twingate itself requires authentication first — the Device-only Policy breaks this circular dependency
- **Use NAT gateway IP, not Connector IP directly**: The egress IP is typically the NAT gateway IP, not the individual Connector host IP
- **Group membership matters**: Users must belong to the correct Twingate Group that has access to the IdP Resource for the flow to work

## Related Docs
- [SaaS App Gating Office 365 with Entra ID](https://www.twingate.com/docs/saas-app-gating-office-365-with-entra-id) — step-by-step example
- [Create a Twingate Resource](https://www.twingate.com/docs/resources)
- [Device-only Resource Policy](https://www.twingate.com/docs/device-only-policy)
- [Entra ID Named Locations documentation](https://learn.microsoft.com/en-us/entra/identity/conditional-access/location-condition)
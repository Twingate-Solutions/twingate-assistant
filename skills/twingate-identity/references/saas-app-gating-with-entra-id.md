# SaaS App Gating with Microsoft Entra ID

## Summary
Configure Twingate and Microsoft Entra ID so that SaaS application access requires an active Twingate connection. Authentication traffic routes through a Twingate Connector's egress IP, which Entra ID Conditional Access validates via a Named Location policy.

## Key Information
- Replaces IP whitelisting in SaaS apps — IP enforcement happens at IdP auth stage instead
- Connector's egress IP (typically a NAT gateway IP) is the enforcement point
- Applies to any SaaS apps protected by Entra ID Conditional Access

## Prerequisites
- Twingate Admin Console access with ability to create Resources and Policies
- Microsoft Entra ID admin access with Conditional Access licensing
- Known egress IP of the Twingate Connector(s) / NAT gateway for the Remote Network

## Step-by-Step

### Twingate Admin Console
1. **Create a Resource** for the Entra ID authentication FQDN (e.g., `tenant.office.com` or `login.microsoftonline.com`) and assign it to the appropriate Group(s)
2. **Apply a Device-only Policy** to that IdP Resource — prevents authentication loop where users can't reach the IdP to authenticate because Twingate requires prior auth

### Microsoft Entra ID
3. **Create a Named Location** (Conditional Access → Named Locations) using the Connector's egress IP address
4. **Create a Conditional Access Policy** with:
   - Target: the SaaS app(s) to restrict
   - Location condition: `Selected locations` → choose the Named Location created above

## Configuration Values

| Field | Value |
|-------|-------|
| Twingate Resource FQDN | `tenant.office.com` or `login.microsoftonline.com` |
| Twingate Resource Policy | Device-only |
| Named Location IP | Connector NAT gateway egress IP |
| Conditional Access location type | Selected locations (trusted) |

## Gotchas
- **Auth loop risk**: Without a Device-only Policy on the IdP Resource, users cannot authenticate to reach Twingate, creating a deadlock. Device-only Policy breaks this dependency.
- **Egress IP accuracy**: Use the NAT gateway IP, not the Connector host IP, if Connectors share a NAT gateway for egress.
- **Group scoping**: Only users in the correct Twingate Group will route through the approved IP — others will fail Conditional Access.

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- [SaaS App Gating Office 365 with Entra ID](https://www.twingate.com/docs) — step-by-step walkthrough
- [Microsoft Entra ID Named Locations documentation](https://learn.microsoft.com/en-us/entra/identity/conditional-access/location-condition)
- [Entra ID Conditional Access location conditions](https://learn.microsoft.com/en-us/entra/identity/conditional-access/location-condition)
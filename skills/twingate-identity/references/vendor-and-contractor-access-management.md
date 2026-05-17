# Manage Access for Vendors and Contractors

## Page Title
How to Manage Access for Vendors and Contractors

## Summary
Twingate addresses vendor/contractor access challenges including frequent onboarding/offboarding, least-privilege access requirements, and unknown device security postures. It provides granular, time-limited access controls without requiring changes to underlying resources.

## Key Information
- Vendor access differs from employee access: more transient relationships, narrower resource needs, unmanaged devices
- Twingate overlays access controls on existing resources with no changes required to those resources
- SSO/IdP integration means disabling an IdP account disables all Twingate-secured resource access—even resources that don't natively support SSO
- Access is granted at the application level (not network level), enabling true least-privilege without VPN-style network segmentation

## Prerequisites
- Twingate deployed with at least one Connector
- Identity Provider configured (Okta, Google Workspace, etc.) for SSO delegation
- Resources defined in Twingate admin console

## Vendor Access Features

| Feature | Purpose | Config Reference |
|---|---|---|
| SSO/IdP Integration | Single offboarding point | [Identity Providers](https://www.twingate.com/docs/identity-providers) |
| Group-based permissions | Bulk access management for vendor teams | [Resources](https://www.twingate.com/docs/resources) |
| Ephemeral Access | Auto-revoke after set time period | [Ephemeral Access](https://www.twingate.com/docs/ephemeral-access) |
| Auto-lock | Revoke access after inactivity period | [Auto-lock](https://www.twingate.com/docs/auto-lock) |
| Network Traffic Logs | Visibility into contractor device activity, location, security posture | [Network Traffic](https://www.twingate.com/docs/network-traffic) |

## Recommended Implementation Pattern
1. Create dedicated Groups for each vendor/contractor org
2. Assign only required Resources to those Groups
3. Configure ephemeral access on Resources for fixed-duration engagements
4. Configure auto-lock for ongoing vendor relationships with sporadic access
5. Link vendor accounts to SSO/IdP — offboard by disabling IdP account only
6. Monitor network traffic logs for contractor device and location visibility

## Gotchas
- **Over-provisioning risk**: Without explicit least-privilege setup, contractors may inherit broader group access. Assign vendors to dedicated groups, not general employee groups.
- **Device visibility requires Twingate Client**: Contractor device security posture logging only works if the Twingate Client is installed on their device.
- **SSO offboarding only works if all access flows through Twingate**: Resources accessible outside Twingate won't be covered by IdP account disablement.
- **Ephemeral access must be configured per Resource**: It is not a global setting applied automatically to new resources.

## Related Docs
- [Identity Providers](https://www.twingate.com/docs/identity-providers)
- [Resources](https://www.twingate.com/docs/resources)
- [Ephemeral Access](https://www.twingate.com/docs/ephemeral-access)
- [Auto-lock](https://www.twingate.com/docs/auto-lock)
- [Network Traffic](https://www.twingate.com/docs/network-traffic)
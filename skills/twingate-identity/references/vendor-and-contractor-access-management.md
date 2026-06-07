# Vendor and Contractor Access Management

## Page Title
How to Manage Access for Vendors and Contractors

## Summary
Twingate provides tools to manage remote access for vendors and contractors, who present unique challenges compared to employees: higher turnover, need for targeted access, and use of unmanaged devices. Key features include SSO-delegated authentication, granular resource-level permissions, and time-based access controls.

## Key Information
- Vendor/contractor access problems differ from employee access: transient relationships, narrower access needs, unmanaged devices
- Twingate overlays access controls without modifying the underlying resource
- SSO integration means disabling a vendor's SSO account revokes all Twingate-secured resource access — including resources that don't natively support SSO
- Access is granted at the application level (not network level), enabling least-privilege without network segmentation
- Contractors can be grouped; permissions assigned to groups for easier bulk management
- Network traffic logging provides visibility into contractor devices: identity, location, security posture

## Prerequisites
- SSO/Identity Provider configured (Okta, Google Workspace, etc.) for authentication delegation
- Resources defined in Twingate
- Groups configured for contractor/vendor user management

## Features for Vendor Access Control

| Feature | Purpose | Docs |
|---|---|---|
| Identity Provider integration | Disabling SSO account revokes all access | Identity Providers guide |
| Resource-level permissions | Least-privilege, per-application access | Resources guide |
| Ephemeral Access | Time-limited access with automatic revocation | Ephemeral Access guide |
| Auto-lock | Revokes access after inactivity period | Auto-lock guide |
| Network Traffic logging | Monitors devices, locations, security posture | Network Traffic guide |

## Configuration Values
- **Ephemeral Access**: Set per-Resource time window after which access is auto-revoked
- **Auto-lock**: Configure inactivity threshold per Resource to trigger automatic lockout
- **Groups**: Assign contractors to groups; attach Resource permissions to groups

## Gotchas
- SSO deprovisioning only works if Twingate authentication is delegated to the identity provider — verify this is configured before relying on it for offboarding
- Traditional VPN network segmentation is not equivalent; Twingate's model requires resources to be explicitly defined and assigned
- Contractor devices are not managed by default — use traffic logging to monitor posture rather than assuming device compliance

## Related Docs
- Identity Providers
- Resources
- Network Traffic
- Ephemeral Access
- Auto-lock
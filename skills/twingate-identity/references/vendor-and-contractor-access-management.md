# Vendor and Contractor Access Management

## Page Title
How to Manage Access for Vendors and Contractors

## Summary
Twingate addresses vendor/contractor access challenges including frequent onboarding/offboarding, need for least-privilege access, and unknown device security posture. It provides granular resource-level controls, SSO integration for simplified lifecycle management, and visibility into contractor device activity without requiring changes to protected resources.

## Key Information
- Vendor access differs from employee access: more transient relationships, narrower resource needs, unmanaged personal devices
- Twingate overlays access controls without modifying underlying resources
- SSO account deactivation cascades to all Twingate-secured resources (including non-SSO-native systems)
- Access is managed at application level, not network segment level (unlike traditional VPN)
- Contractors can be assigned to Groups; permissions attach to Groups for bulk management

## Prerequisites
- Twingate deployed with at least one Connector
- Identity Provider (Okta, Google Workspace, etc.) configured for SSO delegation
- Resources defined in Twingate admin console

## Features for Vendor Access Control

| Feature | Purpose | Docs Reference |
|---|---|---|
| SSO/IdP Integration | Disable SSO account → revokes all Twingate access automatically | Identity Providers guide |
| Granular Resource Access | Grant least-privilege access per resource in seconds | Resources guide |
| Group-based Permissions | Assign contractors to groups; manage permissions at group level | Resources guide |
| Ephemeral Access | Set time-limited access on Resources; auto-revokes after period expires | Ephemeral Access guide |
| Auto-lock | Lock out users who haven't accessed a Resource after defined inactivity period | Auto-lock guide |
| Network Traffic Logging | Monitor device identity, location, security posture for contractor devices | Network Traffic guide |

## Gotchas
- Traditional VPNs require complex network segmentation to restrict vendor access; this is slow and often results in over-provisioning. Twingate eliminates this by operating at the application layer
- Ephemeral access and auto-lock are **distinct features**: ephemeral is time-based from grant; auto-lock is inactivity-based
- Vendors using personal devices are visible in logs but device posture enforcement requires Device Security Policy configuration (not covered on this page)
- Disabling access via SSO only works if the IdP is properly integrated — standalone Twingate local accounts would need separate deprovisioning

## Related Docs
- [Identity Providers](https://www.twingate.com/docs/identity-providers)
- [Resources](https://www.twingate.com/docs/resources)
- [Network Traffic](https://www.twingate.com/docs/network-traffic)
- [Ephemeral Access](https://www.twingate.com/docs/ephemeral-access)
- [Auto-lock](https://www.twingate.com/docs/auto-lock)
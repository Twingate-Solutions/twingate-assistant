---
source: https://www.twingate.com/docs/vendor-and-contractor-access-management
type: docs
fetched: 2026-08-14
source_version: c77d5576f18c3c3e487a160d624f438d8bf22a846ed6f544cb759d8bb23458c0
---

# Vendor and Contractor Access Management in Twingate

## Page Title
How to Manage Access for Vendors and Contractors

## Summary
Twingate addresses the unique challenges of vendor/contractor remote access—transient relationships, need for targeted resource access, and unmanaged devices—through granular access controls, SSO integration, and automated access lifecycle management. It provides a more flexible and secure alternative to traditional VPN-based approaches for external user access.

## Key Information
- Twingate overlays access controls on private resources without modifying the underlying resource
- SSO/IdP integration means disabling a contractor's SSO account revokes all Twingate-secured resource access automatically
- Access is granted at the application level (least privilege), not network segment level
- Contractors can be organized into Groups for bulk permission management
- Network access logs capture device info, location, and security posture for contractor-owned devices

## Prerequisites
- Twingate deployed with at least one Resource configured
- Identity Provider (Okta, Google Workspace, etc.) integrated for SSO delegation
- Groups configured for contractor/vendor organization

## Core Features for Vendor Management

| Feature | Use Case | Reference |
|---|---|---|
| SSO/IdP Integration | Auto-revoke access on account disable | Identity Providers guide |
| Granular Resource Access | Least-privilege per contractor/project | Resources guide |
| Group-based Permissions | Manage sets of contractors efficiently | Resources guide |
| Ephemeral Access | Auto-expire access after set time period | Ephemeral Access guide |
| Auto-lock | Revoke access after inactivity period | Auto-lock guide |
| Network Traffic Logging | Monitor contractor device/location/posture | Network Traffic guide |

## Configuration Values
- **Ephemeral Access**: Configure time-bounded access on individual Resources
- **Auto-lock**: Set inactivity threshold per Resource to trigger automatic lockout

## Gotchas
- Disabling access via SSO/IdP covers Twingate-secured resources but does **not** automatically revoke native credentials on resources that require separate accounts—Twingate bypasses the need to log into those resources but doesn't manage those credentials
- Contractor devices are unmanaged; use network traffic logging to assess security posture since you cannot enforce corporate device policies
- Traditional VPN segmentation is noted as inflexible; if migrating from VPN, audit existing contractor access levels as over-provisioning is common

## Related Docs
- [Identity Providers](https://www.twingate.com/docs/identity-providers)
- [Resources](https://www.twingate.com/docs/resources)
- [Network Traffic](https://www.twingate.com/docs/network-traffic)
- [Ephemeral Access](https://www.twingate.com/docs/ephemeral-access)
- [Auto-lock](https://www.twingate.com/docs/auto-lock)
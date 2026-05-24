# Vendor and Contractor Access Management

## Page Title
How to Manage Access for Vendors and Contractors

## Summary
Twingate addresses vendor/contractor remote access challenges including transient relationships, need for least-privilege access, and unmanaged devices. It provides controls for granular resource access, SSO-linked offboarding, device visibility, and time-limited access without requiring changes to underlying resources.

## Key Information
- Twingate overlays access controls on private resources without modifying those resources
- SSO/IdP integration means disabling a contractor's SSO account revokes all Twingate-secured resource access—including resources that don't natively support SSO
- Group-based permissions simplify contractor access management at scale
- Access can be scoped to specific applications (least-privilege), unlike VPN network segmentation

## Prerequisites
- Twingate deployed on network resources
- SSO/Identity Provider configured (Okta, Google Workspace, etc.) for offboarding automation

## Features for Vendor Access Management

| Feature | Purpose | Reference |
|---|---|---|
| IdP Integration | Disable SSO = disable all resource access | Identity Providers guide |
| Granular Resource Access | Per-application permissions, group assignments | Resources guide |
| Network Traffic Logging | Monitor devices, locations, security posture of contractor devices | Network Traffic guide |
| Ephemeral Access | Auto-revoke access after a configured time period | Ephemeral Access guide |
| Auto-lock | Lock users out after period of inactivity; prevents over-provisioning drift | Auto-lock guide |

## Configuration Values
- **Ephemeral Access**: Set time-bounded access on individual Resources
- **Auto-lock**: Configure inactivity threshold per Resource
- **Groups**: Assign contractors to groups; apply permissions at group level

## Gotchas
- Contractor offboarding only auto-propagates via Twingate if SSO/IdP is integrated—manual account management required otherwise
- Auto-lock and ephemeral access are configured per Resource; no network-wide default mentioned
- Vendor devices may have unknown security posture; network traffic logging provides visibility but does not enforce device compliance by itself

## Related Docs
- Identity Providers
- Resources
- Network Traffic
- Ephemeral Access
- Auto-lock
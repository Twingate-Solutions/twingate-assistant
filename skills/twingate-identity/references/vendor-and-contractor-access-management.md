# Manage Access for Vendors and Contractors

## Summary
Twingate addresses vendor/contractor access management challenges including transient relationships, need for scoped access, and unmanaged devices. It provides granular, time-limited access controls that integrate with existing identity providers without requiring changes to protected resources.

## Key Information
- Vendor access challenges differ from employee access: higher onboarding/offboarding frequency, more targeted resource needs, and unmanaged devices
- Twingate overlays access controls without modifying underlying resources
- Access can be provisioned at the application level (least privilege), not network level
- Group-based permissions simplify bulk management of contractor cohorts

## Prerequisites
- Twingate network with at least one Resource configured
- (Recommended) SSO/identity provider integration (Okta, Google Workspace, etc.) for centralized deprovisioning

## Core Features for Vendor Management

| Feature | Purpose | Docs |
|---|---|---|
| SSO/IdP Integration | Disabling SSO account revokes all Twingate-secured resource access | Identity Providers guide |
| Granular Resource Access | Assign specific resources to groups; contractors see only what they need | Resources guide |
| Network Traffic Logging | Monitor devices, locations, and security posture including contractor-owned devices | Network Traffic guide |
| Ephemeral Access | Set time-limited access on Resources; auto-revokes after period expires | Ephemeral Access guide |
| Auto-lock | Automatically lock users out after period of inactivity on a Resource | Auto-lock guide |

## Implementation Approach
1. Create a dedicated Group for vendor/contractor users
2. Assign only required Resources to that Group
3. Integrate with SSO/IdP so deprovisioning happens at the identity layer
4. Configure Ephemeral Access on Resources for fixed-term engagements
5. Enable Auto-lock to handle over-provisioning drift
6. Enable Network Traffic logging to audit contractor device activity

## Gotchas
- SSO deprovisioning disables Twingate access even for resources that don't natively support SSO — this is intentional and is the recommended offboarding path
- Traditional VPN cannot easily replicate application-level segmentation; Twingate removes the need for network segmentation projects to scope contractor access
- Contractor devices are unmanaged — use traffic logging to gain visibility since you cannot control device security posture directly
- Without Ephemeral Access or Auto-lock configured, contractor accounts may retain access after engagement ends

## Related Docs
- Identity Providers
- Resources
- Network Traffic
- Ephemeral Access
- Auto-lock
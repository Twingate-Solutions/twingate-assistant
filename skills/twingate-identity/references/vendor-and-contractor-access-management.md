# Vendor and Contractor Access Management

## Page Title
How to Manage Vendors and Contractors Access Management

## Summary
Twingate addresses the unique access control challenges posed by vendors and contractors—transient relationships, targeted access needs, and unmanaged devices—through granular controls, SSO integration, and automated access lifecycle features. It provides application-level access control without requiring changes to underlying resources.

## Key Information
- Vendor/contractor access differs from employee access in three ways: higher onboarding/offboarding frequency, need for more targeted (least-privilege) access, and use of unmanaged personal devices
- Twingate overlays access controls on any private resource without modifying the resource itself
- SSO integration means revoking an IdP account immediately cuts access to all Twingate-secured resources, even non-SSO-native systems
- Group-based permissions simplify bulk management of contractors
- Access activity logging covers contractor devices including device type, location, and security posture

## Prerequisites
- Twingate network with at least one Connector deployed
- Identity Provider (IdP) configured (e.g., Okta, Google Workspace) for SSO-delegated authentication
- Resources defined in Twingate admin console

## Configuration Options / Features

| Feature | Purpose | Reference |
|---|---|---|
| Identity Provider integration | Centralize auth; deprovisioning IdP account revokes all access | Identity Providers guide |
| Group-based permissions | Assign contractors to groups; manage permissions at group level | Resources guide |
| Ephemeral Access | Set time-limited access windows; auto-revokes after period expires | Ephemeral Access guide |
| Auto-lock | Lock users out after inactivity period; prevents over-provisioning drift | Auto-lock guide |
| Network Traffic logging | Monitor device identity, location, security posture for all users | Network Traffic guide |

## Step-by-Step (Recommended Pattern)
1. Connect IdP (Okta, Google Workspace, etc.) to Twingate
2. Create a dedicated Group for vendors/contractors
3. Assign only the specific Resources the vendor needs to that Group (least-privilege)
4. Configure Ephemeral Access on Resources if engagement is time-bounded
5. Enable Auto-lock on Resources to handle inactivity/over-provisioning
6. Monitor access via Network Traffic logs
7. Offboard: disable IdP account → access to all Twingate resources revoked automatically

## Gotchas
- Traditional VPNs require network segmentation to restrict contractor access; Twingate does this at application level—avoid conflating the two approaches during migration
- Vendors using personal devices bypass corporate MDM; use Twingate's device visibility/logging as compensating control
- Auto-lock and Ephemeral Access are separate features—configure both for comprehensive lifecycle management
- Revoking Twingate group membership does not revoke the underlying resource credentials (e.g., database passwords); handle those separately

## Related Docs
- Identity Providers
- Resources
- Network Traffic
- Ephemeral Access
- Auto-lock
# Managing Vendor and Contractor Access in Twingate

## Page Title
How to Manage Access for Vendors and Contractors

## Summary
Twingate addresses the unique access control challenges of vendor/contractor relationships—transient access needs, targeted resource permissions, and unmanaged devices—through granular controls, SSO integration, and automated access lifecycle management. It provides a more flexible alternative to VPN-based network segmentation for third-party access.

## Key Information
- Vendor access differs from employee access in three ways: higher onboarding/offboarding frequency, need for narrower resource access, and use of unmanaged personal devices
- Twingate overlays access controls without requiring changes to underlying resources
- SSO/IdP integration means disabling a contractor's SSO account revokes all Twingate-secured resource access—including resources that don't natively support SSO
- Group-based permissions simplify bulk contractor access management
- Access activity logging covers contractor-owned devices (device type, location, security posture)

## Prerequisites
- Twingate deployed with at least one Resource configured
- SSO/Identity Provider integration (Okta, Google Workspace, etc.) recommended for automated offboarding
- Resources, Groups, and Policies configured per your access model

## Key Features for Vendor Access

| Feature | Use Case | Reference |
|---|---|---|
| SSO/IdP Integration | Auto-revoke access on account disable | Identity Providers guide |
| Group-based permissions | Assign contractors to scoped groups | Resources guide |
| Ephemeral Access | Time-limited access with auto-expiry | Ephemeral Access guide |
| Auto-lock | Revoke access after inactivity period | Auto-lock guide |
| Network Traffic Logs | Monitor contractor device activity | Network Traffic guide |

## Configuration Approaches

**Least-privilege access:**
- Create dedicated Groups for contractor cohorts or individual vendors
- Assign only specific Resources needed for the engagement to those Groups

**Automated offboarding:**
- Integrate IdP so disabling the SSO account cascades to all Twingate resources
- Use Ephemeral Access to set a hard expiry date matching contract end date

**Inactivity lockout:**
- Configure Auto-lock on Resources to revoke access after a defined idle period—mitigates over-provisioning risk

## Gotchas
- Traditional VPN requires network segmentation projects to restrict vendor access; Twingate does this at the application layer without infrastructure changes
- Resources without native SSO support still benefit from Twingate's SSO-gated access—disabling the IdP account blocks entry even to legacy systems
- Vendor team composition changes (swapping individuals) require individual user management within the Group, not just Group-level changes
- Auto-lock and Ephemeral Access are complementary but distinct—set both for belt-and-suspenders access lifecycle control

## Related Docs
- Identity Providers
- Resources
- Network Traffic
- Ephemeral Access
- Auto-lock
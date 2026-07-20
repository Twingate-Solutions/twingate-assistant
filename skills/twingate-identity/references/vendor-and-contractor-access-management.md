# Vendor and Contractor Access Management

## Page Title
How to Manage Access for Vendors and Contractors

## Summary
Twingate addresses vendor/contractor remote access challenges including transient relationships, scoped resource needs, and unmanaged devices. It provides granular, time-limited access controls with full audit visibility without requiring changes to underlying resources.

## Key Information
- Vendor access differs from employee access in three ways: higher onboarding/offboarding frequency, need for narrower resource access, and use of unmanaged personal devices
- Twingate overlays access controls without modifying protected resources
- SSO integration means disabling a contractor's IdP account revokes all Twingate-secured resource access automatically—even resources without native SSO support
- Group-based permissions simplify bulk access management for contractor teams
- Access can be scoped per-resource at application level (vs. VPN network segmentation)

## Prerequisites
- Twingate network deployed with Resources configured
- Identity Provider (Okta, Google Workspace, etc.) integrated for SSO delegation
- Resources assigned to Groups for contractor access management

## Vendor Access Features

| Feature | Use Case | Docs Reference |
|---|---|---|
| SSO/IdP Integration | Instant offboarding via IdP account disable | Identity Providers guide |
| Granular Resource Access | Least-privilege scoping per contractor | Resources guide |
| Network Traffic Logging | Device visibility, location, security posture monitoring | Network Traffic guide |
| Ephemeral Access | Auto-revoke after defined time period | Ephemeral Access guide |
| Auto-lock | Auto-lockout after inactivity period | Auto-lock guide |

## Configuration Values
- **Ephemeral Access**: Set time-bound expiration on specific Resources
- **Auto-lock**: Configure inactivity threshold per Resource to prevent over-provisioning
- **Groups**: Assign contractors to groups; apply Resource permissions to groups

## Implementation Steps
1. Create a dedicated Group for each vendor/contractor team
2. Assign only required Resources to that Group
3. Configure ephemeral access expiration if engagement has a known end date
4. Enable auto-lock on Resources to handle over-provisioning drift
5. Connect IdP so offboarding is handled by disabling the IdP account
6. Monitor access via Network Traffic logs for device/location visibility

## Gotchas
- VPN-style network segmentation is not nimble—Twingate's application-level access avoids needing segmentation projects when scoping contractor access
- Resources without native SSO are still protected via Twingate's IdP delegation; disabling the IdP account blocks Twingate access even if the resource has a separate local credential
- Contractor device security posture is unknown by default—use Network Traffic logging to monitor device state

## Related Docs
- [Identity Providers](https://www.twingate.com/docs/identity-providers)
- [Resources](https://www.twingate.com/docs/resources)
- [Network Traffic](https://www.twingate.com/docs/network-traffic)
- [Ephemeral Access](https://www.twingate.com/docs/ephemeral-access)
- [Auto-lock](https://www.twingate.com/docs/auto-lock)
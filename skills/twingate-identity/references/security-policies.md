# Security Policies

## Summary
Twingate Security Policies control access to network resources through layered authentication, device, and location requirements. Policies are managed in the Admin Console under the **Policies** tab and can be applied at the network level, resource level, or per-group basis.

## Key Information
- **Four policy types**: Minimum Authentication Requirements, Resource Policies, Application Control Policies, Admin Console Security Policy
- **Default Policy** automatically applies to all new Resources; additional Resource Policies can be created
- Group-level policy overrides take precedence over Resource-level policies and persist even if the Resource Policy changes
- Enterprise customers get Location Requirements (country-based access control)

## Policy Types

| Policy | Applied To | Location |
|--------|-----------|----------|
| Minimum Authentication Requirements | All users at network login | Policies tab |
| Resource Policies | Resources at access time | Policies tab |
| Application Control | Resources (browser restriction) | Policies tab |
| Admin Console Security | Admins signing into Admin Console | Settings tab |

## Configuration Options Per Policy
- **Location Requirements**: Allowlist/blocklist countries (Enterprise only)
- **Authentication Requirements**: MFA enforcement, re-authentication frequency
- **Device Security**: All devices, Trusted Devices, or custom profile

## Policy Application Logic
1. User must satisfy **Minimum Authentication Requirements** first
2. Then satisfy the **Resource Policy** (or Group override) at access time
3. Group-level override persists independently — resetting required to re-inherit Resource Policy

## Additional Access Controls
- **Ephemeral Access**: Set expiration date on Resource or Group access → group auto-removed at expiry
- **Usage-based Auto-lock**: Lock individual user access after inactivity period; configurable per Resource or Group

## Gotchas
- Group policy overrides are "sticky" — changing the Resource Policy does NOT update overridden groups; must manually reset the override
- Minimum Authentication Requirements apply at login, not at resource access; Admin Console logins bypass these (use Admin Console Security Policy instead)
- Admins don't need Twingate client to access Admin Console, so network policies don't apply to them

## Prerequisites
- Admin Console access
- Enterprise plan required for Location Requirements

## Recommendations
- Keep Minimum Authentication Requirements **less strict** to reduce friction
- Apply stricter controls at the **Resource Policy level**, especially for sensitive resources

## Related Docs
- [Device Security Guide](#)
- [Browser Security / Application Control Policies](#)
- [Admin Console Security](#)
- [Ephemeral Access to Resources](#)
- [Usage-based Auto-lock](#)
# Security Policies

## Summary
Twingate Security Policies control access to network resources through authentication, device, and location requirements. Policies are configured in the Admin Console under the Policies tab and applied at the resource level with optional per-group overrides.

## Key Information
- **Three policy types**: Minimum Authentication Requirements, Resource Policies, Application Control Policies
- **Fourth policy**: Admin Console Security Policy (Settings tab, separate from network policies)
- Minimum Authentication Requirements apply to all users at login, before any resource access
- One **Default Policy** always exists and applies to all new resources automatically
- Resource Policies can be overridden per Group on the Resource page
- Group-level overrides persist even if the Resource's base policy changes
- Location Requirements (country-based) available for **Enterprise customers only**

## Policy Rule Types
- **Location Requirements**: Allowlist/blocklist by country
- **Authentication Requirements**: Auth frequency, MFA requirement (layers on top of Minimum Auth)
- **Device Security**: All devices, Trusted Devices, or custom profile

## Policy Application Logic
1. User must pass **Minimum Authentication Requirements** first
2. Device must meet minimum OS requirements or Trusted Profile
3. At resource access time, **Resource Policy** is evaluated
4. If Group has a policy override, that override applies instead of the resource's base policy
5. Group overrides must be manually reset to re-inherit the resource policy

## Additional Access Controls
- **Ephemeral Access**: Set expiration date at resource or group level; group is removed from resource at expiry
- **Usage-based Auto-lock**: Lock individual user access after inactivity period; configured per resource or group

## Configuration Location
| Policy Type | Admin Console Location |
|---|---|
| Minimum Auth Requirements | Policies tab |
| Resource Policies | Policies tab |
| Application Control Policies | Policies tab |
| Admin Console Security | Settings tab |

## Gotchas
- Admins do **not** use Minimum Authentication Requirements when signing into the Admin Console (separate policy applies)
- Group-level policy overrides are "sticky" — changing the resource's base policy does **not** update overridden groups
- To remove a group override, explicitly reset it on the Resource page
- Ephemeral and usage-based access are additive controls alongside policy selection, not part of the policy definition itself

## Recommendations
- Keep **Minimum Authentication Requirements** less strict to reduce user friction
- Apply stricter controls via **Resource Policies** on sensitive resources
- Use Group overrides for contractor/third-party access with elevated requirements

## Related Docs
- Device Security Guide
- Browser Security (Application Control Policies)
- Admin Console Security
- Ephemeral Access to Resources
- Usage-based Auto-lock
- MFA configuration
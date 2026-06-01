# Security Policies

## Summary
Twingate Security Policies control access at both the network login level and individual Resource level. Policies are configured in the Admin Console under the **Policies** tab, with a separate Admin Console Security Policy under **Settings**.

## Key Information
- **Three policy types**: Minimum Authentication Requirements, Resource Policies, Application Control Policies
- One **Default Policy** always exists and applies to all new Resources automatically
- Resource Policies can be **overridden per Group** on the Resource page
- Group-level overrides persist even if the parent Resource Policy changes (must be manually reset)
- Location Requirements (country-based) are **Enterprise tier only**

## Policy Types

| Type | Applied When | Configured Under |
|------|-------------|-----------------|
| Minimum Authentication Requirements | User logs into network | Policies tab |
| Resource Policies | Resource is accessed | Policies tab |
| Application Control Policies | Resource accessed via browser | Policies tab |
| Admin Console Security Policy | Admin signs into Admin Console | Settings tab |

## Policy Rules Available
- **Location Requirements** – allowlist/blocklist countries (Enterprise only)
- **Authentication Requirements** – MFA requirement, re-authentication frequency
- **Device Security** – all devices, Trusted Devices, or custom profile

## Policy Application Logic
1. User must satisfy **Minimum Authentication Requirements** first
2. When accessing a Resource, user must also satisfy the **Resource Policy**
3. Group-level policy overrides take precedence over the Resource's default policy
4. Overrides are sticky — reset manually to re-inherit the Resource Policy

## Additional Access Controls
- **Ephemeral Access**: Set expiration date on Resource or per-Group access
- **Usage-based Auto-lock**: Lock individual user access after inactivity period
- Both configurable at Resource level or Group-override level

## Configuration Steps
1. Navigate to **Admin Console → Policies tab**
2. Click **Create Policy** under Resource Policies
3. Add rules: Location, Authentication, Device Security
4. Assign policy to a Resource by editing the Resource
5. Override per Group via the Resource page; reset override to re-inherit

## Gotchas
- Minimum Authentication Requirements apply to **all users/resources** — overly strict settings here create friction for every login
- Admin Console Security Policy is **separate** from Minimum Authentication Requirements (admins don't go through network login)
- Group policy overrides **do not auto-update** when the Resource Policy changes
- Device must also meet minimum OS requirements or a Trusted Profile (separate from policy rules)

## Recommendations
- Keep **Minimum Authentication Requirements** loose to reduce friction
- Apply strict controls at the **Resource Policy level**, especially for sensitive resources

## Related Docs
- [Device Security Guide](#)
- [Browser Security / Application Control Policies](#)
- [Admin Console Security](#)
- [Ephemeral Access to Resources](#)
- [Usage-based Auto-lock](#)
# Security Policies

## Summary
Twingate Security Policies control access at multiple levels: network login, individual resource access, and Admin Console access. Policies define authentication frequency, MFA requirements, device trust, and location restrictions. Resource policies can be overridden per-Group with independent lifecycle controls.

## Key Information
- **Four policy scopes**: Minimum Authentication Requirements, Resource Policies, Application Control Policies, Admin Console Security Policy
- **Minimum Auth Requirements**: Applied at network login; all users must satisfy before accessing any resource
- **Resource Policies**: Applied at resource access time; one Default Policy always exists
- **Application Control Policies**: Restrict resource access to specific browsers
- **Admin Console Security Policy**: Only for admins signing into Admin Console (separate from network auth); managed under Settings tab
- **Group-level policy overrides**: A specific Group's policy on a Resource can differ from the Resource's default policy
- **Overrides persist**: If Resource Policy changes, overridden Group policies do NOT update automatically — must be manually reset

## Prerequisites
- Admin Console access
- Enterprise plan required for Location Requirements feature

## Policy Configuration Options
| Rule Type | Description |
|-----------|-------------|
| Location Requirements | Allowlist/denylist by country |
| Authentication Requirements | Auth frequency + MFA enforcement |
| Device Security | All devices, Trusted Devices, or custom profile |

## Step-by-Step: Create/Edit Resource Policy
1. Navigate to Admin Console → **Policies** tab
2. Click **Create Policy** under Resource Policies
3. Add rules: Location Requirements, Authentication Requirements, Device Security
4. Assign policy to a Resource by editing the Resource

## Step-by-Step: Override Policy for Specific Group
1. Navigate to the Resource page
2. Find the Group assignment
3. Set a different policy for that Group
4. To revert: reset the override for that Group (restores Resource Policy inheritance)

## Additional Access Controls
- **Ephemeral Access**: Set expiration date on Resource or Group-level access → see *Ephemeral Access to Resources*
- **Usage-based Auto-lock**: Lock user access after inactivity period; applied per-user → see *Usage-based Auto-lock*

## Gotchas
- Minimum Auth Requirements layer beneath Resource Policies — users must satisfy both
- Group-level policy overrides are sticky: changing the Resource's policy does not cascade to overridden Groups
- Admins accessing Admin Console bypass Minimum Authentication Requirements (separate policy applies)
- Location Requirements are Enterprise-only

## Recommendations
- Keep Minimum Authentication Requirements **less strict** to reduce friction
- Apply stricter controls at the **Resource Policy level**, especially for sensitive resources

## Related Docs
- Device Security Guide
- Browser Security (Application Control Policies)
- Admin Console Security
- Ephemeral Access to Resources
- Usage-based Auto-lock
- MFA configuration
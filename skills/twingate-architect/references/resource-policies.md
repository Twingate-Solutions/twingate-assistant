# Resource Policies

## Summary
Resource Policies define security requirements (authentication, device, location) applied at the Resource level in Twingate. Each policy can combine up to three requirement types and is assigned to Resources via the Admin Console. Group-level overrides allow per-team policy variation on the same Resource.

## Key Information
- Managed under **Policies → Resource Policies** tab in Admin Console
- A **Default Policy** is auto-assigned to all new Resources; editable but not deletable
- Three requirement types: Authentication, Device Security, Location (all optional)
- Least permissive policy applies when a user belongs to multiple Groups with different Group-level policies
- Session prompt appears ~10 minutes before expiry if user is actively accessing the Resource

## Prerequisites
- Enterprise plan required for Location Requirements (geoblocking)
- Trusted Profiles and Approved OS configurations must be defined before using Custom/Only Trusted Devices modes

## Policy Requirements

### Authentication
| Setting | Range/Options |
|---|---|
| Authentication frequency | 1 hour to 31 days |
| MFA | Enabled/Disabled (uses Twingate native MFA) |

- Timer is **rolling**: any successful auth resets timer across **all** Resources, not just one
- Can disable entirely for device-only policies

### Device Security Modes
- **Any Device** (default): Any device meeting Approved OS requirements or Trusted Profile
- **Only Trusted Devices**: Must meet a Trusted Profile; Approved OS alone is insufficient
- **Custom**: Select specific Trusted Profiles and Approved OS configurations

### Location Requirements
- Configure allowlist (only specified countries) or denylist (block specified countries)
- **Always blocked (cannot override):** Cuba, Iran, North Korea, Syria

## Configuration Steps

1. Navigate to **Admin Console → Policies → Resource Policies**
2. Click **Create** → name the policy
3. Configure Authentication, Device, and/or Location requirements as needed
4. Assign to a Resource via the Resource's detail page
5. Optionally set Group-level overrides on the Resource detail page

## Assigning and Overrides

- Policy assigned on Resource detail page; applies to all Groups by default
- **Group-level override:** Change policy per-Group on the Resource detail page
- Overrides persist even if Resource-level policy changes; must be manually reset to inherit Resource policy again

## Gotchas
- Group-level overrides **stick** after being set — changing the Resource-level policy won't affect overridden Groups
- Ignoring/dismissing the session expiry prompt cuts off access immediately at expiry; user must re-authenticate to restore access
- If IdP session is still valid at re-auth check, user is not redirected; if expired, redirect occurs and all timers reset after
- Embargoed countries (Cuba, Iran, North Korea, Syria) cannot be unblocked via allowlist

## Related Docs
- [Device Profiles](https://www.twingate.com/docs/device-profiles)
- [Location Requirements](https://www.twingate.com/docs/location-requirements)
- [Multi-Factor Authentication](https://www.twingate.com/docs/mfa)
- [Device-only Resource Policies](https://www.twingate.com/docs/device-only-resource-policies)
- [How Sessions Work](https://www.twingate.com/docs/sessions)
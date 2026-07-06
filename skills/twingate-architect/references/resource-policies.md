# Resource Policies

## Summary
Resource Policies define security requirements (authentication, device security, location) applied at the Resource level in Twingate. Policies can be assigned per-Resource and overridden per-Group. A Default Policy is auto-assigned to all new Resources.

## Key Information
- Managed under **Policies → Resource Policies** tab in Admin Console
- Each policy combines up to 3 optional requirement types: Authentication, Device Security, Location
- Default Policy is auto-assigned to new Resources; editable but not deletable
- When user is in multiple Groups with different policies on same Resource, **least permissive policy wins**
- Successful authentication resets timer across **all** Resources (rolling window), not just the accessed one

## Prerequisites
- Admin Console access
- Enterprise plan required for Location Requirements (geoblocking)
- Device Profiles/Trusted Profiles configured if using device security requirements

## Configuration Values

### Authentication Requirements
| Setting | Range/Options |
|---|---|
| Authentication frequency | 1 hour – 31 days |
| MFA | Enabled / Disabled |

### Device Security Modes
| Mode | Description |
|---|---|
| `Any Device` | Any device meeting Approved OS requirements or Trusted Profile (default) |
| `Only Trusted Devices` | Must match a Trusted Profile; Approved OS alone insufficient |
| `Custom` | Select specific Trusted Profiles and/or Approved OS configurations |

### Location Requirements
- **Allowlist**: Only specified countries permitted
- **Denylist**: Specified countries blocked
- **Always blocked (non-overridable)**: Cuba, Iran, North Korea, Syria

## Step-by-Step

### Create a Policy
1. Navigate to **Policies → Resource Policies**
2. Click **Create**
3. Name the policy
4. Configure Authentication, Device Security, and/or Location requirements (all optional)
5. Save

### Assign to a Resource
1. Open the Resource in Admin Console
2. Select desired policy from available options on Resource detail page

### Override Policy for a Specific Group
1. Open Resource detail page
2. Change the policy assignment for an individual Group
3. To revert, explicitly reset the override for that Group

## Gotchas
- Group-level overrides **persist** even if the Resource-level policy changes later; must be manually reset to re-inherit
- Authentication timer expiry triggers IdP session check first — user may not see a prompt if IdP session is still valid
- Session expiry prompt appears ~10 minutes before timer expires **only if user is actively accessing the Resource**; ignored/dismissed prompt = access cut off immediately at expiry
- Disabling authentication requirements creates a device-only policy (authentication section can be fully disabled)
- Device-only policies have different session behavior — see sessions guide

## Related Docs
- [Device Profiles](https://www.twingate.com/docs/device-profiles)
- [Location Requirements](https://www.twingate.com/docs/location-requirements)
- [Device-only Resource Policies](https://www.twingate.com/docs/device-only-resource-policies)
- [How Sessions Work](https://www.twingate.com/docs/how-sessions-work)
- [Multi-Factor Authentication](https://www.twingate.com/docs/mfa)
# Resource Policies

## Summary
Resource Policies define authentication, device security, and location requirements for accessing specific Twingate Resources. Policies are assigned at the Resource level and can be overridden per Group. A Default Policy exists on every network and is auto-assigned to new Resources.

## Key Information
- Managed under **Policies → Resource Policies** tab in Admin Console
- Each policy combines up to three optional requirement types: Authentication, Device Security, Location
- Default Policy cannot be deleted but can be edited
- Successful authentication resets timer across **all** Resources (rolling window)
- When multiple Group-level policies conflict, **least permissive** policy applies
- Group-level overrides persist even if Resource-level policy changes

## Prerequisites
- Twingate Admin Console access
- Enterprise plan required for Location (geoblocking) requirements
- Device Profiles/Trusted Profiles configured if using device security requirements

## Configuration Options

### Authentication Requirements
| Setting | Range/Options |
|---|---|
| Authentication frequency | 1 hour to 31 days |
| MFA | Enabled/Disabled (uses Twingate native MFA) |
| Disable auth entirely | Enables device-only policy mode |

### Device Security Modes
- **Any Device** – meets Approved OS requirements or Trusted Profile (default)
- **Only Trusted Devices** – must match a Trusted Profile (OS approval alone insufficient)
- **Custom** – select specific Trusted Profiles and Approved OS configurations

### Location Requirements
- Configure as allowlist or denylist by country
- Permanently blocked (non-overridable): **Cuba, Iran, North Korea, Syria**

## Step-by-Step: Create and Assign a Policy
1. Navigate to **Policies → Resource Policies** → click **Create**
2. Name the policy; add Authentication, Device, and/or Location requirements
3. Open target Resource in Admin Console
4. Select the policy from available options on the Resource detail page
5. Optionally override policy per Group on the same Resource detail page

## Session Behavior
- ~10 minutes before expiry: prompt shown **only if user is actively accessing** the Resource
- If IdP session still valid: re-authentication is seamless, all timers reset
- If IdP session expired: user redirected to IdP, then timers reset
- If prompt ignored/dismissed: session expires, access cut off until next auth

## Gotchas
- Group-level overrides **do not automatically revert** when Resource policy changes; must be manually reset
- MFA frequency shares the same timer as authentication frequency (not separate)
- Embargoed countries cannot be allowlisted regardless of policy configuration
- Device-only policies require explicitly disabling authentication requirements

## Related Docs
- [Device-only Resource Policies](#)
- [Device Profiles](#)
- [Location Requirements](#)
- [Multi-Factor Authentication](#)
- [How Sessions Work](#)
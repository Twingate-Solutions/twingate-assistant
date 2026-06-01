# Resource Policies

## Summary
Resource Policies define authentication, device security, and location requirements for accessing specific Twingate Resources. Policies are assigned at the Resource level with optional Group-level overrides. A Default Policy is auto-assigned to all new Resources.

## Key Information
- Managed under **Policies > Resource Policies** tab in Admin Console
- Each policy combines up to three requirement types: Authentication, Device Security, Location
- All requirement types are optional
- Default Policy applies to all new Resources; editable but not deletable
- Location restrictions (geoblocking) require **Enterprise plan**
- Permanently blocked countries (non-overridable): Cuba, Iran, North Korea, Syria

## Policy Requirement Types

### Authentication
- **Frequency**: Re-auth interval from 1 hour to 31 days
- **MFA**: Twingate native MFA toggle (triggers at frequency interval)
- **Rolling window**: Any successful auth resets timer across ALL Resources in session
- Can be disabled entirely for device-only policies

### Device Security
| Mode | Description |
|------|-------------|
| Any Device | Meets Approved OS requirements OR Trusted Profile (default) |
| Only Trusted Devices | Must match a Trusted Profile specifically |
| Custom | Select specific Trusted Profiles and/or Approved OS configs |

### Location
- Configure as allowlist or denylist by country
- Enterprise plan only

## Assignment & Overrides

**Resource-level**: Set policy on Resource detail page; applies to all Groups by default.

**Group-level overrides**:
- Override per-Group on the Resource detail page
- Overrides persist even if Resource-level policy changes
- Must manually reset to restore inheritance
- When user is in multiple Groups with different policies → **least permissive policy wins**

## Session Behavior
- ~10 min before expiry: prompt shown if user is actively accessing Resource
- If IdP session still valid: re-auth is seamless, all timers reset
- If IdP session expired: user redirected to IdP, timers reset after completion
- If prompt dismissed/ignored: session expires, access cut off until next auth attempt

## Gotchas
- Group-level policy overrides are "sticky" — they don't follow Resource-level policy changes; must be manually reset
- Rolling auth window affects all Resources simultaneously, not just the one accessed
- Only Trusted Devices mode excludes devices that only meet Approved OS requirements
- Geoblocking is Enterprise-only; attempting on lower plans unavailable

## Related Docs
- [Device-only Resource Policies](#)
- [Multi-Factor Authentication](#)
- [Device Profiles](#)
- [Location Requirements](#)
- [How Sessions Work](#)
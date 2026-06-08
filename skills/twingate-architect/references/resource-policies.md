# Resource Policies

## Summary
Resource Policies define security requirements (authentication, device, location) applied at the Resource level in Twingate. Each policy is assigned to a Resource and can be overridden per Group. A Default Policy exists on every network and is auto-assigned to new Resources.

## Key Information
- Managed under **Policies → Resource Policies** tab in Admin Console
- Three requirement types: Authentication, Device Security, Location (all optional)
- Default Policy: editable, cannot be deleted, auto-assigned to new Resources
- Least permissive policy applies when a user belongs to multiple Groups with conflicting policies
- Location restrictions (geoblocking) are **Enterprise plan only**
- Permanently blocked countries (non-overridable): Cuba, Iran, North Korea, Syria

## Prerequisites
- Admin Console access
- Enterprise plan required for Location Requirements
- Device Profiles/Trusted Profiles configured if using device security requirements

## Configuration Options

### Authentication Requirements
| Setting | Range/Options |
|---|---|
| Authentication frequency | 1 hour to 31 days |
| MFA | Enabled/Disabled (uses Twingate native MFA) |
| Disable auth entirely | Creates device-only policy |

- Timer is **rolling**: any successful auth resets timer across **all** Resources, not just one

### Device Security Modes
- **Any Device** – meets Approved OS requirements or Trusted Profile (default)
- **Only Trusted Devices** – must match a Trusted Profile (Approved OS alone insufficient)
- **Custom** – select specific Trusted Profiles and Approved OS configurations

### Location Requirements
- Configure allowlist (permitted countries) or denylist (blocked countries)

## Assignment & Overrides
1. Open Resource in Admin Console → select policy from available options
2. To override per Group: change policy on individual Group assignment within the Resource detail page
3. Group overrides **persist** even if Resource-level policy changes — must be manually reset
4. To revert: reset the override on the Group assignment

## Session Behavior
- ~10 min before expiry: prompt shown **only if user is actively accessing** the Resource
- On re-auth: Twingate checks stored IdP session first (no redirect if valid); redirects to IdP if expired
- If prompt dismissed/ignored: session expires, access cut off until next explicit auth
- All session timers reset on successful re-authentication

## Gotchas
- Group-level overrides are sticky — changing the Resource-level policy does NOT update overridden Groups
- MFA frequency shares the same timer as auth frequency (not a separate interval)
- "Only Trusted Devices" excludes devices that only meet Approved OS requirements — stricter than it may appear
- Device-only policies require disabling authentication requirements entirely

## Related Docs
- [Device Profiles](https://www.twingate.com/docs/device-profiles)
- [Location Requirements](https://www.twingate.com/docs/location-requirements)
- [Device-only Resource Policies](https://www.twingate.com/docs/device-only-resource-policies)
- [Multi-Factor Authentication](https://www.twingate.com/docs/mfa)
- [How Sessions Work](https://www.twingate.com/docs/sessions)
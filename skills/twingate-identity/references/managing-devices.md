# Device Administration

## Summary
Twingate tracks devices connecting to the network, displaying attributes like hardware info, OS details, and security posture. Admins can manage device states (active/archived/blocked) and incorporate verification status into Security Policies.

## Key Information
- Device info visible in both individual user detail pages and the **Devices** tab
- Device attributes vary by platform (Windows, macOS, Linux, iOS)
- Verified devices can be marked automatically via EDR/MDM integrations or manually by admins
- Devices auto-archive after 90 days of inactivity

## Device Attributes by Platform

| Attribute | Windows | macOS | Linux | iOS |
|-----------|---------|-------|-------|-----|
| Name (friendly) | ✓ | ✓ | — | ✓ |
| Hostname | ✓ | ✓ | ✓ | — |
| Make/Model | — | ✓ | ✓ | ✓ |
| Serial Number | ✓ | ✓ | ✓ | — |
| Local Username | ✓ | ✓ | ✓ | — |
| OS name/version | ✓ | ✓ | ✓ | ✓ |
| Internet Security | ✓ | ✓ | ✓ | — |

## Device States

| State | Access | Admin Console | Auto-Trigger |
|-------|--------|---------------|--------------|
| **Active** | Allowed (per policy) | Visible | Default for new devices |
| **Archived** | Requires re-auth | Filtered out | 90 days inactivity |
| **Blocked** | No access | Filtered out | Manual only |

## State Behavior Details
- **Archived**: Auto-signs out user; re-authentication restores device to active state
- **Blocked**: Auto-signs out user; user **cannot** sign back in on that device
- States can be set via Admin Console or API

## Device Verification
- Supported via EDR/MDM integrations (automatic) or manual admin designation
- Verification status can be used as a condition in Security Policies
- Applies to all platforms and locations

## Gotchas
- Archived devices are filtered from default Admin Console view — must adjust filters to see them
- Re-authenticating on an archived device automatically reactivates it (cannot keep it archived if user logs back in)
- Blocked state is irreversible from the user side — only admins can change it
- `Internet Security` status not available on iOS
- `Name` (friendly name) not available on Linux; use `Hostname` instead

## Related Docs
- [Device Security Guide](https://www.twingate.com/docs/device-security) — Trusted Profiles, Security Policies, verification integration setup
- Twingate API — for programmatic device state management
# Device Administration

## Summary
Twingate tracks and displays device information for users connecting to the network, including hardware details, OS info, and security posture. Admins can manage device lifecycle through three states (active, archived, blocked) and integrate with EDR/MDM tools for automated device verification.

## Key Information
- Device details visible in both the **user detail page** and the **Devices tab**
- Verified device status can be incorporated into Security Policies
- Devices auto-archive after **90 days** of no sign-in or Resource access
- Device states manageable via Admin Console or API

## Device Attributes by Platform

| Attribute | Windows | macOS | Linux | iOS |
|-----------|---------|-------|-------|-----|
| Name (friendly) | ✓ | ✓ | — | ✓ |
| Hostname | ✓ | ✓ | ✓ | — |
| Make/Model | — | ✓ | ✓ | ✓ |
| OS name/version | ✓ | ✓ | ✓ | ✓ |
| Serial number | ✓ | ✓ | ✓ | — |
| Local username | ✓ | ✓ | ✓ | — |
| Internet Security status | ✓ | ✓ | ✓ | — |

## Device States

| State | Access | Admin Console | Auto-triggered |
|-------|--------|---------------|----------------|
| **Active** | Allowed (per policy) | Visible | Default for new devices |
| **Archived** | Requires re-auth | Filtered out | 90 days inactive |
| **Blocked** | No access | Filtered out | Manual only |

## State Behavior Details
- **Archived**: Auto-signs out user; re-authentication restores device to active state
- **Blocked**: Auto-signs out user; user **cannot sign back in** on that device; use for lost/stolen devices
- States can be set manually via Admin Console or API

## Device Verification
- Supported via integrations with **EDR and MDM** software (automated)
- **Manual verification** available for individual devices
- Verified status usable as a condition in Security Policies

## Gotchas
- Archived devices are filtered from the Admin Console view by default — they still exist but require filtering to find
- Re-authenticating on an archived device automatically re-activates it (no admin action needed)
- Blocked state is irreversible from the device side — user cannot self-recover
- `Name` attribute (friendly name) is user-set; `Hostname` is system-assigned — these may differ
- Internet Security status not available on iOS

## Related Docs
- [Device Security Guide](https://www.twingate.com/docs/device-security) — Trusted Profiles, Security Policies, device verification integration
- Twingate API — for programmatic device state management
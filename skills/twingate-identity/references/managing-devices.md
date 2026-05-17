# Device Administration

## Summary
Twingate tracks devices used to connect to the network, displaying attributes like hardware info, OS version, and posture data. Admins can manage device states (active/archived/blocked) and mark devices as verified for use in Security Policies.

## Key Information
- Device details visible in both individual user pages and the **Devices** tab
- Verified devices integrate with EDR/MDM software or can be manually verified by admins
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
| Client version | ✓ | ✓ | ✓ | ✓ |
| Internet Security status | ✓ | ✓ | ✓ | — |

## Device States

| State | Access | Admin Console | Auto-trigger |
|-------|--------|---------------|--------------|
| **Active** | Allowed (per policy) | Visible | Default for new devices |
| **Archived** | Requires re-auth | Filtered out | 90 days of inactivity |
| **Blocked** | No access | Filtered out | Manual only |

## State Behaviors
- **Archived**: Auto-signs out user; re-authentication restores device to active state automatically
- **Blocked**: Auto-signs out user; user **cannot** sign back in on that device
- States set via Admin Console or API

## Verified Devices
- Supports EDR/MDM integrations for automatic verification
- Manual verification available for individual devices
- Verified status can be used as a condition in Security Policies
- Applies to all platforms and locations

## Gotchas
- `Name` (friendly name) is **not** collected on Linux — only `Hostname`
- iOS devices do not report `Hostname`, `Serial number`, or `Local username`
- Archived devices still technically allow access after re-authentication — use **Blocked** for lost/stolen devices
- 90-day inactivity archival is automatic and cannot be disabled per-device
- Archived → Active transition happens automatically on re-auth (no manual intervention needed)

## Related Docs
- [Device Security Guide](https://www.twingate.com/docs/device-security) — Trusted Profiles, Security Policies, device verification integration
- Twingate API — for programmatic device state management
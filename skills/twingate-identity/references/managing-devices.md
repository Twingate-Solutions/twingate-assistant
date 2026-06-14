# Device Administration

## Summary
Twingate tracks devices connecting to the network, displaying attributes like device name, OS, and posture information. Admins can manage device verification status and control access through three device states: active, archived, and blocked.

## Key Information

- Device data visible in both **User Detail page** and **Devices tab** in Admin Console
- Devices automatically archived after **90 days** of no sign-in or Resource access
- Device states configurable via **Admin Console or API**
- Verified device status can be incorporated into Security Policies

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
| **Active** | Full (per policy) | Visible | Default for new devices |
| **Archived** | Requires re-auth | Filtered out | 90 days inactive |
| **Blocked** | No access | Filtered out | Manual only |

## Device Verification

- Supports automatic verification via **EDR/MDM integrations**
- Admins can **manually verify** specific devices
- Verified status enforceable across all platforms and locations via Security Policies

## Gotchas

- **Archived → Active**: Re-authenticating on an archived device automatically restores active state
- **Blocked devices**: User cannot sign back in; state must be manually changed by admin
- **Archived devices**: User is automatically signed out but can regain access by re-authenticating
- **Blocked devices**: User is automatically signed out with no self-service recovery path
- iOS does not report hostname, serial number, or local username — relevant for posture policies targeting mobile

## Related Docs

- [Device Security Guide](https://www.twingate.com/docs/device-security) — Trusted Profiles, Security Policies, device verification integration
- Twingate API — for programmatic device state management
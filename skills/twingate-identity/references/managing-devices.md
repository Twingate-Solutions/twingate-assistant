# Device Administration

## Summary
Twingate tracks devices used to connect to the network, displaying attributes like hardware info, OS details, and posture data. Admins can manage device states (active/archived/blocked) and verification status through the Admin Console or API.

## Key Information
- Device details visible in both the **User Detail page** and the **Devices tab**
- Displays posture information and which Trusted Profiles are met
- Verified device status integrates with EDR/MDM software or can be set manually
- Device verification can be enforced regardless of platform or location

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

## Gotchas
- **Archived ≠ Blocked**: Archived devices can regain access by re-authenticating; blocked devices cannot sign in at all
- Archiving automatically signs out the user; re-authentication restores active state
- Blocking permanently prevents sign-in on that device — use for lost/stolen devices
- Devices auto-archive after **90 days** without sign-in or Resource access
- iOS does not report hostname, serial number, local username, or Internet Security status

## Configuration Options
- Device states settable via **Admin Console** or **API**
- Verification: automatic via EDR/MDM integrations, or manual admin designation
- Verified status incorporated into Security Policies

## Related Docs
- [Device Security Guide](https://www.twingate.com/docs/device-security) — Trusted Profiles, Security Policies, device verification enforcement
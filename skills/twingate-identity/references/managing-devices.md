---
source: https://www.twingate.com/docs/managing-devices
type: docs
fetched: 2026-08-14
source_version: 1eb067e8906dc0c50f62e006a887834ba020145c226c1fb16dcae58b341c34ec
---

# Device Administration

## Summary
Twingate tracks device information for all users connecting through the network, displaying attributes like device name, OS, and posture data in the Admin Console. Admins can manage device states (active/archived/blocked) and configure verification status through EDR/MDM integrations or manual designation.

## Key Information
- Device details visible in both the user detail page and the **Devices** tab
- Not all attributes supported across all platforms (see table below)
- Verified device status can be incorporated into Security Policies

## Device Attributes by Platform

| Attribute | Windows | macOS | Linux | iOS |
|---|---|---|---|---|
| Name (friendly) | ✓ | ✓ | — | ✓ |
| Hostname | ✓ | ✓ | ✓ | — |
| Make/Model | — | ✓ | ✓ | ✓ |
| OS name/version | ✓ | ✓ | ✓ | ✓ |
| Serial number | ✓ | ✓ | ✓ | — |
| Local username | ✓ | ✓ | ✓ | — |
| Internet Security | ✓ | ✓ | ✓ | — |
| Client version / Active state | ✓ | ✓ | ✓ | ✓ |

## Device States

| State | Access | Admin Console | Auto-trigger |
|---|---|---|---|
| **Active** | Requires sign-in | Visible | Default for new devices |
| **Archived** | Requires re-auth | Filtered out | No activity for 90 days |
| **Blocked** | No access | Filtered out | Manual only |

- States configurable via **Admin Console** or **API**
- Archiving auto-signs out the user; re-authentication restores to Active
- Blocking permanently prevents sign-in on that device

## Device Verification

- **Automatic**: Integrations with EDR/MDM software
- **Manual**: Admins with **Admin** or **Helpdesk** role can manually verify devices
- Verification status usable as a condition in Security Policies
- Applies to all platforms and locations

## Gotchas
- iOS devices do **not** report hostname, serial number, or local username — plan policies accordingly
- Archived devices appear "filtered out" in console by default — use filters to find them
- Re-authenticating on an archived device automatically reactivates it (cannot stay archived after login)
- Blocked devices cannot be recovered by the user — requires admin intervention
- 90-day auto-archive timer applies to both sign-in activity **and** Resource access

## Prerequisites
- Admin or Helpdesk role required to manually verify devices or change device states
- EDR/MDM integration required for automatic device verification

## Related Docs
- [Device Security Guide](https://www.twingate.com/docs/device-security) — Trusted Profiles, Security Policies, verification integration setup
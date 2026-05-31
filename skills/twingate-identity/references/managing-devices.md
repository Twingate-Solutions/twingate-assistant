# Device Administration

## Summary
Twingate tracks devices used to connect to the network, displaying attributes like hardware info, OS details, and security posture. Admins can manage device states (active/archived/blocked) and mark devices as verified for use in Security Policies.

## Key Information
- Device info visible in user detail pages and the **Devices** tab in Admin Console
- Verified devices can integrate with EDR/MDM software or be manually verified by admins
- Device verification status can be incorporated into Security Policies
- Archived devices auto-sign-out users; re-authentication restores active state
- Blocked devices permanently lose access until unblocked

## Device Attributes by Platform

| Attribute | Windows | macOS | Linux | iOS |
|-----------|---------|-------|-------|-----|
| Name | ✓ | ✓ | — | ✓ |
| Hostname | ✓ | ✓ | ✓ | — |
| Make/Model | — | ✓ | ✓ | ✓ |
| OS name/version | ✓ | ✓ | ✓ | ✓ |
| Serial number | ✓ | ✓ | ✓ | — |
| Local username | ✓ | ✓ | ✓ | — |
| Client version | ✓ | ✓ | ✓ | ✓ |
| Internet Security | ✓ | ✓ | ✓ | — |

## Device States

| State | Access | Admin Console | Auto-trigger |
|-------|--------|---------------|--------------|
| **Active** | Requires sign-in | Visible | Default for new devices |
| **Archived** | Requires re-authentication | Filtered out | 90 days of inactivity |
| **Blocked** | No access (cannot sign in) | Filtered out | Manual only |

## Configuration
- States set via **Admin Console** or **API**
- Verified status configured via EDR/MDM integrations or manual designation

## Gotchas
- Archiving a device **immediately signs out** the current user
- Re-authenticating on an archived device automatically restores it to **active** state
- Blocking is **permanent until manually changed**; user cannot re-authenticate on that device
- Devices inactive for **90 days** are automatically archived (not blocked)
- iOS does not report hostname, serial number, or local username
- Internet Security status not available on iOS

## Related Docs
- [Device Security Guide](https://www.twingate.com/docs/device-security-guide) — Trusted Profiles, Security Policies, device verification integration
# Device Administration

## Summary
Twingate tracks devices that users connect from, displaying attributes like hardware info, OS version, and posture data. Admins can manage device lifecycle through three states (active/archived/blocked) and integrate with EDR/MDM for verification.

## Key Information
- Device info visible in both **User Detail page** and **Devices tab** in Admin Console
- Device states manageable via Admin Console or API
- Devices auto-archive after **90 days** of no sign-in or Resource access
- Verified device status integrates with Security Policies

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
| Internet Security | ✓ | ✓ | ✓ | — |

## Device States

| State | Access | Admin Console | Auto-trigger |
|-------|--------|---------------|--------------|
| **Active** | Requires sign-in | Visible | Default for new devices |
| **Archived** | Requires re-auth | Filtered out | 90 days inactive |
| **Blocked** | No access | Filtered out | Manual only |

## State Behaviors
- **Archived**: Signs out user automatically; re-authentication restores to active state
- **Blocked**: Signs out user automatically; user **cannot sign in again** on that device; permanent loss of Resource access
- States set via Admin Console or API

## Device Verification
- Supports automatic verification via **EDR/MDM integrations**
- Manual verification available for individual devices
- Verified status can be required in **Security Policies**
- Enforcement applies to all platforms and locations

## Gotchas
- iOS does not report hostname, serial number, or local username
- Linux does not report a friendly device name
- Archived devices still require sign-in to access Resources (not fully locked out)
- Blocked state is not reversible for sign-in (device permanently loses access)
- Green connection dot indicates active login session, not just enrollment

## Related Docs
- [Device Security Guide](https://www.twingate.com/docs/device-security) — Trusted Profiles, verification in Security Policies
- Manual device verification
- EDR/MDM integration setup
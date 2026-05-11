# Device Administration

## Summary
Twingate tracks device attributes and states for all user devices connecting to the network. Admins can view device details, manage verification status, and control access through three device states (active, archived, blocked). Device verification integrates with EDR/MDM tools or can be set manually for use in Security Policies.

## Key Information
- Device info visible in both user detail page and the **Devices** tab in Admin Console
- Tracked attributes include: name, hostname, make/model, OS, serial number, local username, client version, active state, internet security status
- Verified devices can be used as conditions in Security Policies
- Devices auto-archive after **90 days** of no sign-in or resource access

## Device Attribute Platform Support

| Attribute | Windows | macOS | Linux | iOS |
|-----------|---------|-------|-------|-----|
| Name | ✓ | ✓ | — | ✓ |
| Hostname | ✓ | ✓ | ✓ | — |
| Make/Model | — | ✓ | ✓ | ✓ |
| Serial Number | ✓ | ✓ | ✓ | — |
| Local Username | ✓ | ✓ | ✓ | — |
| Internet Security | ✓ | ✓ | ✓ | — |
| OS, Client Version, Active State | All | All | All | All |

## Device States

| State | Resource Access | Admin Console | Auto-set |
|-------|----------------|---------------|----------|
| **Active** | Yes (per policy) | Visible | Default for new devices |
| **Archived** | Requires re-auth | Filtered out | After 90 days inactive |
| **Blocked** | No access | Filtered out | Manual only |

## State Behaviors
- **Archived**: Auto-signs out user; re-authentication restores device to active state
- **Blocked**: Auto-signs out user; user **cannot** sign back in on that device
- States can be set via Admin Console or API

## Device Verification
- Supports EDR/MDM integrations for automatic verification
- Manual verification available per device
- Verification status usable as condition in Security Policies
- Applies to all platforms and locations

## Gotchas
- Archived devices are filtered from default Admin Console view — not deleted
- Re-authenticating on an archived device automatically reactivates it (not true for blocked)
- Blocked devices permanently lose access — cannot be recovered by the user
- iOS does not report hostname, make/model not available on Windows

## Related Docs
- [Device Security Guide](https://www.twingate.com/docs/device-security) — Trusted Profiles, Security Policies, verification integration setup
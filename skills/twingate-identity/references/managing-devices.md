# Device Administration

## Summary
Twingate tracks devices that users connect from, displaying attributes like name, OS, and posture information in the Admin Console. Admins can manage device verification status and control access via three device states: active, archived, and blocked.

## Key Information

- Device info visible in both **User Detail page** and the **Devices tab**
- Displays: name, make/model, Client version, posture info, Trusted Profiles met
- Verified devices can be integrated into Security Policies

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
| **Archived** | Requires re-auth | Filtered out | No activity for 90 days |
| **Blocked** | No access | Filtered out | Manual only |

- States can be set via **Admin Console** or **API**
- Re-authenticating on an archived device automatically returns it to **active**
- Blocking a device signs out the user and **permanently prevents re-login** on that device

## Verified Devices

- Supports EDR/MDM integrations for automatic verification
- Manual verification available via Admin Console
- Verification status enforceable in Security Policies across all platforms/locations

## Gotchas

- Blocked devices cannot be re-signed into — use for lost/stolen/permanently deprecated devices only
- Archiving auto-signs out the user; they must re-authenticate to regain access
- Archived devices are filtered from default Admin Console view (not deleted)
- `Name` attribute (friendly name) is user-set and differs from `Hostname` (DNS-assigned)
- Internet Security status not available on iOS

## Related Docs

- [Device Security Guide](https://www.twingate.com/docs/device-security-guide) — Trusted Profiles, Security Policies, device verification integration
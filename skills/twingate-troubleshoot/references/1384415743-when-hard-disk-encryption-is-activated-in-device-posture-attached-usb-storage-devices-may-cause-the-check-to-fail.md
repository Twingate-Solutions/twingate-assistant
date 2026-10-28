---
source: https://help.twingate.com/articles/1384415743-when-hard-disk-encryption-is-activated-in-device-posture-attached-usb-storage-devices-may-cause-the-check-to-fail
type: help
fetched: 2026-10-28
source_version: 64a1c7e18daab848517f9218885a3f6bda83d3eb2a4e520923e6ee75517ab635
trust: official
---

# [Windows Client] Disk Encryption Posture Check Fails with External Drive Connected

## Summary
When a Device Security policy requires disk encryption, the Windows Twingate Client evaluates all drives Windows classifies as "local (non-removable)" disks. External SSDs and HDDs may be classified as local disks by Windows, causing the BitLocker check to fail if they are unencrypted, even when the system drive is fully encrypted.

## Key Information
- Only **BitLocker** encryption is recognized; third-party encryption products do not satisfy the check
- **External SSDs/HDDs** may be classified by Windows as local disks → evaluated by posture check
- **USB flash drives** are typically classified as removable → not evaluated
- **Locked BitLocker drives** on Client versions prior to 2026.239 report unknown protection status, which was treated as "not encrypted"
- Client **2026.239+** correctly passes locked-but-encrypted drives

## Symptoms
- Connection blocked with: *"Authentication Blocked – Device security not met"*
- Troubleshoot panel shows: `Block reason: Device posture`
- Client logs contain: `{"IsHardDriveEncryptionEnabled":false, ...}`
- Failure correlates with connecting/disconnecting an external drive

## Prerequisites
- Windows platform
- Twingate Device Security policy with disk encryption required
- External drive connected (SSD or HDD, not USB flash drive)

## Resolution Steps
1. **Encrypt the external drive** with BitLocker, OR **disconnect** it while using Twingate
2. If the drive is BitLocker-encrypted but locked: upgrade Client to **2026.239 or later**, or manually unlock the drive
3. After resolving, quit and relaunch the Twingate Client, then retry the connection
4. If still failing, collect Client logs and contact Twingate Support

## Configuration Values
| Item | Value |
|------|-------|
| Minimum Client version (locked drive fix) | `2026.239` |
| Affected component | Windows Client / Device Security posture |
| Required encryption type | BitLocker only |

## Gotchas
- Not all external drives behave the same — Windows drive classification determines whether a device is evaluated, not whether it is physically external
- Upgrading the Client is required to handle locked-but-encrypted drives; there is no workaround on older versions short of unlocking the drive
- Third-party full-disk encryption (e.g., VeraCrypt, manufacturer encryption) will **not** satisfy the check

## Related Docs
- [Device Security Posture Checks](https://help.twingate.com/articles/device-security-posture-checks)
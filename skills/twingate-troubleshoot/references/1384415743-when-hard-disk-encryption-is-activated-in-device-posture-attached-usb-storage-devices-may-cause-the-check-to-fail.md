---
source: https://help.twingate.com/articles/1384415743-when-hard-disk-encryption-is-activated-in-device-posture-attached-usb-storage-devices-may-cause-the-check-to-fail
type: help
fetched: 2026-10-25
source_version: b9edcffb2e2688c8db4fdf0d7f557b948651a0abaeae5dac91166ba0305026b1
trust: official
---

# [Windows Client] Disk Encryption Posture Check Fails with Unencrypted External Drive

## Summary
When a Device Security policy requires disk encryption, the Windows Twingate Client checks BitLocker status on all drives Windows classifies as "local (non-removable)." External SSDs and HDDs are sometimes classified as local disks by Windows, causing the posture check to fail if they are unencrypted, even when the system drive is fully encrypted.

## Key Information
- Only **BitLocker** encryption is recognized; third-party encryption products do not satisfy the check
- Check evaluates **system drive + all non-removable drives** — not removable/flash drives
- External SSDs/HDDs may be classified as **local disks** by Windows, making them subject to the check
- USB flash drives are typically classified as removable and are **not evaluated**
- Client versions **before 2026.239**: locked (but encrypted) BitLocker drives report unknown status and fail the check
- Client **2026.239+**: locked encrypted drives correctly pass the check

## Symptoms
- Auth blocked: `"Device security not met. This device does not meet the minimum security requirements to access this Network."`
- Troubleshoot panel shows: `Block reason: Device posture`
- Client logs contain: `{"IsHardDriveEncryptionEnabled":false, ...}`
- Failure appears when external drive is connected; clears when disconnected

## Prerequisites
- Windows platform
- Twingate Client installed
- Device Security policy with disk encryption requirement enabled

## Resolution Steps
1. **Identify** whether an external SSD or HDD is connected when the failure occurs
2. **Choose one**:
   - Encrypt the external drive with BitLocker, **or**
   - Disconnect the external drive while using Twingate
3. If drive **is** BitLocker-encrypted but locked:
   - Update Twingate Client to **2026.239 or later**, or unlock the drive manually
4. If check doesn't clear after resolving: quit and relaunch the Twingate Client, then retry
5. If still failing: contact Support with Client logs

## Configuration Values
| Item | Value |
|------|-------|
| Affected component | Windows Client — Device Security posture check |
| Fixed-in version | 2026.239 |
| Encryption required | BitLocker only |
| Drive types evaluated | Local (non-removable) disks |
| Drive types excluded | Removable drives (USB flash drives) |

## Gotchas
- Third-party full-disk encryption (e.g., VeraCrypt, FileVault equivalents) **will not** pass the check
- External SSDs behave differently from USB flash drives — they are frequently misidentified as local disks
- Older clients treat locked-but-encrypted drives as unencrypted; upgrade to 2026.239+ to fix this without unlocking

## Related Docs
- [Device Security Posture Checks](https://help.twingate.com) (referenced in source)
- Twingate Client release notes for version 2026.239
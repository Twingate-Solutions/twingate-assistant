---
source: https://help.twingate.com/articles/1384415743-when-hard-disk-encryption-is-activated-in-device-posture-attached-usb-storage-devices-may-cause-the-check-to-fail
type: help
fetched: 2026-10-18
source_version: 9d11efe1e3375105c711bde7861620fe45bb494de899fd2f5bec4e2262354833
trust: official
---

# [Windows Client] Disk Encryption Posture Check Fails with Unencrypted External Drive

## Summary
When a Device Security policy requires disk encryption, the Windows Twingate Client checks BitLocker status on all drives Windows classifies as "local (non-removable)" disks. External SSDs and HDDs may be classified as local disks, causing the posture check to fail if they are unencrypted, even when the system drive is fully encrypted.

## Key Information
- Only **BitLocker** encryption is recognized; third-party encryption tools do not satisfy the check
- **External SSDs/HDDs** may be classified by Windows as local (non-removable) disks → evaluated by posture check
- **USB flash drives** are typically classified as removable → not evaluated
- **Locked BitLocker drives** (encrypted but not yet unlocked) reported unknown protection status in Client versions before 2026.239, causing false failures
- Client **2026.239+** correctly passes locked-but-encrypted drives

## Symptoms
- Auth blocked: *"Device security not met. This device does not meet the minimum security requirements to access this Network."*
- Troubleshoot panel shows: `Block reason: Device posture`
- Client logs show: `"IsHardDriveEncryptionEnabled":false`
- Failure appears on external drive connection; clears on disconnection

## Prerequisites
- Windows Twingate Client
- Device Security policy with disk encryption requirement enabled

## Resolution Steps
1. **Identify** whether an external SSD or HDD is connected when the failure occurs
2. **Choose one**:
   - Encrypt the external drive with BitLocker, **or**
   - Disconnect the external drive while using Twingate
3. If the drive is **encrypted but locked**: upgrade Client to **2026.239+**, or manually unlock the drive
4. After resolving, **quit and relaunch** the Twingate Client, then retry connection
5. If check still fails, contact Support with Client logs

## Configuration Values
| Item | Value |
|------|-------|
| Minimum Client version for locked-drive fix | `2026.239` |
| Log field to check | `IsHardDriveEncryptionEnabled` |
| Required encryption technology | BitLocker only |

## Gotchas
- Third-party full-disk encryption (e.g., VeraCrypt, hardware encryption) does **not** satisfy the check
- The Windows drive classification (local vs. removable) is determined by Windows, not Twingate — the same physical device may behave differently across machines
- Client versions **before 2026.239** will fail on any locked BitLocker drive, even if correctly encrypted

## Related Docs
- [Device Security Posture Checks](https://help.twingate.com/articles/device-security-posture-checks)
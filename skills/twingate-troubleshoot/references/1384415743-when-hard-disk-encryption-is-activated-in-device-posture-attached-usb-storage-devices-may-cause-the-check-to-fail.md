---
source: https://help.twingate.com/articles/1384415743-when-hard-disk-encryption-is-activated-in-device-posture-attached-usb-storage-devices-may-cause-the-check-to-fail
type: help
fetched: 2026-11-08
source_version: 6f90dee90713bda2b2383fa3995a926051e336cb515b45baae21af8fb6208800
trust: official
---

# [Windows Client] Disk Encryption Posture Check Fails with Unencrypted External Drive

## Summary
When a Device Security policy requires disk encryption, the Windows Twingate Client checks all drives classified by Windows as "local (non-removable)" disks for BitLocker encryption. External SSDs and HDDs connected via USB may be classified as local disks, causing the posture check to fail even if the system drive is fully encrypted.

## Key Information
- Only **BitLocker** encryption is recognized; third-party encryption products do not satisfy the check
- **External SSDs/HDDs** can be misclassified by Windows as local (non-removable) disks → evaluated by posture check
- **USB flash drives** are typically classified as removable → not evaluated
- System drive + all non-removable drives must be BitLocker-encrypted to pass
- Client versions before **2026.239**: locked (but encrypted) BitLocker drives report unknown status and fail the check
- Client **2026.239+**: locked encrypted drives correctly pass the check

## Symptoms
- Auth error: `"Authentication Blocked – Device security not met."`
- Troubleshoot panel shows: `Block reason: Device posture`
- Client logs show: `{"IsHardDriveEncryptionEnabled":false, ...}`
- Failure correlates with connecting/disconnecting external drive

## Prerequisites
- Windows platform
- Twingate Client installed
- Device Security policy with disk encryption requirement enabled

## Resolution Steps
1. **Identify** whether an external SSD or HDD is connected when the check fails
2. **Choose one option** for the external drive:
   - Encrypt it with BitLocker, **or**
   - Disconnect it while using Twingate
3. **If drive is BitLocker-encrypted but locked**: upgrade Twingate Client to **2026.239 or later**, or manually unlock the drive
4. After resolving, **quit and relaunch** the Twingate Client, then retry connection
5. If still failing, contact Support with Client logs

## Gotchas
- USB flash drives usually escape the check; external SSDs/HDDs do not — the distinction is Windows' drive classification, not the connection interface
- Non-BitLocker encryption (e.g., VeraCrypt, third-party tools) will **not** satisfy the posture check regardless of encryption state
- Locked BitLocker drives fail on Client versions < 2026.239 even though the drive is actually encrypted
- Reconnecting the drive after disconnecting may require a client restart to re-evaluate posture

## Configuration Values
| Item | Value |
|------|-------|
| Affected component | Twingate Windows Client |
| Fixed-in version (locked drive bug) | 2026.239 |
| Encryption required | BitLocker only |

## Related Docs
- [Device Security Posture Checks](https://help.twingate.com/articles/device-security-posture-checks)
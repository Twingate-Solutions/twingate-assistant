---
source: https://help.twingate.com/articles/1384415743-when-hard-disk-encryption-is-activated-in-device-posture-attached-usb-storage-devices-may-cause-the-check-to-fail
type: help
fetched: 2026-11-01
source_version: d51d263cafd520b6c6fb4c152975171f3884d8ce70cb050974683ff3cdb447cb
trust: official
---

# [Windows Client] Disk Encryption Posture Check Fails with Unencrypted External Drive

## Summary
When a Device Security policy requires disk encryption, the Windows Twingate Client checks BitLocker status on all drives classified by Windows as local (non-removable) disks. External SSDs and hard drives may be classified as local disks, causing the posture check to fail if they are unencrypted, even when the system drive is fully encrypted.

## Key Information
- Only **BitLocker encryption** is recognized; third-party encryption tools do not satisfy the check
- Windows classifies drives as local or removable — external SSDs/HDDs often classify as **local disks** and are evaluated
- USB flash drives typically classify as **removable** and are **not** evaluated
- Locked BitLocker drives report unknown protection status on Client versions before 2026.239, causing them to fail the check
- Client **2026.239+** correctly passes locked-but-encrypted drives

## Affected Components
- **Component:** Twingate Client, Device Security posture checks
- **Platform:** Windows only

## Symptoms
- Connection blocked with: `"Authentication Blocked – Device security not met."`
- Troubleshoot panel shows: `Block reason: Device posture`
- Client logs show: `{"IsHardDriveEncryptionEnabled":false, ...}`
- Failure correlates with external drive connect/disconnect events

## Resolution Steps
1. Identify any connected external SSDs or hard drives (not USB flash drives)
2. Either:
   - Encrypt the external drive with BitLocker, **or**
   - Disconnect the external drive while using Twingate
3. If the drive is BitLocker-encrypted but locked:
   - Upgrade Twingate Client to **2026.239 or later**, or unlock the drive manually
4. After resolving, quit and relaunch the Twingate Client, then retry connection
5. If check still fails, contact Support with Client logs

## Gotchas
- Third-party full-disk encryption (non-BitLocker) will **not** satisfy the check regardless of encryption status
- External drives that appear as "removable" in Windows Explorer may still be classified as local disks internally
- Pre-2026.239 clients treat locked BitLocker drives as unencrypted — upgrade resolves this without needing to unlock the drive
- Posture check may not clear immediately after disconnecting the drive; client restart is required

## Related Docs
- [Device Security Posture Checks](https://help.twingate.com/articles/device-security-posture-checks)
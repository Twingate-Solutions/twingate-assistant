---
source: https://help.twingate.com/articles/1384415743-when-hard-disk-encryption-is-activated-in-device-posture-attached-usb-storage-devices-may-cause-the-check-to-fail
type: help
fetched: 2026-11-13
source_version: c1c24d3c6b3dd06073a7ad300fe9be552a8ecd6d6514a0d805d07a01adb8764d
trust: official
---

# Page Title
[Windows Client] Disk encryption posture check fails when an unencrypted external drive is connected

## Summary
When a Device Security policy requires disk encryption, the Twingate Windows Client checks that the system drive and all other non-removable drives are BitLocker-encrypted. An unencrypted external SSD or hard drive that Windows classifies as a local disk can make the check fail even if the system drive is encrypted. Fix it by encrypting or disconnecting the drive, or by updating the Client for locked drives.

## Key Information
- Applies to: Twingate Client / Device Security, Windows.
- The check evaluates every drive Windows classifies as a **local (non-removable) disk**.
- External SSDs and hard drives are often classified as local disks, so they are evaluated.
- USB flash drives are usually classified as removable, so they are not evaluated.
- Only BitLocker encryption is recognised. Drives encrypted with non-BitLocker products fail the check.
- Client versions earlier than 2026.239 treated a locked BitLocker drive as unencrypted, because its protection status reports as unknown. Version 2026.239 fixes this.

## Prerequisites
- Device Security policy with disk encryption required.
- Windows Client; version 2026.239 or later if locked encrypted drives are involved.

## Symptoms / Diagnosis
- Connection fails with "Authentication Blocked – Device security not met. This device does not meet the minimum security requirements to access this Network."
- Client Troubleshoot info shows `Block reason: Device posture`.
- Client logs show: `Service posture data collected. {"IsHardDriveEncryptionEnabled":false, ...}`
- The failure starts when an external drive is connected and clears when it is disconnected.

## Step-by-Step Resolution
1. Identify any connected external SSD or hard drive (not a USB flash drive).
2. Either encrypt it with BitLocker, or disconnect it while using Twingate.
3. If the drive is already encrypted but locked, update the Client to 2026.239 or later, or unlock the drive.
4. If the check doesn't clear, quit and relaunch the Twingate Client, then retry.
5. If it still fails, contact Support with your Client logs.

## Configuration Values
- Log field: `IsHardDriveEncryptionEnabled` (false indicates failed check)
- Troubleshoot field: `Block reason: Device posture`
- Fixed Client version: 2026.239

## Gotchas
- The system drive being encrypted is not sufficient; other non-removable drives count too.
- Third-party (non-BitLocker) encryption is not recognised.
- Locked BitLocker drives fail on Client versions before 2026.239.
- Symptoms are intermittent, tied to connecting or disconnecting the drive.

## Related Docs
- Device Security Posture Checks (Twingate Help Center)
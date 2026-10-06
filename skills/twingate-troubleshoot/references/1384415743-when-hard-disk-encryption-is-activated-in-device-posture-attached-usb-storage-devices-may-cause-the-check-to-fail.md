---
source: https://help.twingate.com/articles/1384415743-when-hard-disk-encryption-is-activated-in-device-posture-attached-usb-storage-devices-may-cause-the-check-to-fail
type: help
fetched: 2026-10-04
source_version: cc139ee0644c459782b8633e7216ffce9131dbc65ff0fc99d5716054f1617c6b
trust: official
---

# When Hard Disk Encryption Device Posture Check Fails Due to USB Storage Devices

## Summary
On Windows, enabling hard disk encryption as a device posture condition can cause false failures when USB storage devices are connected. Windows incorrectly identifies the USB device as a local disk and flags it as unencrypted, blocking Twingate access.

## Key Information
- **Component:** Twingate Client, Device Security
- **Platform:** Windows only
- **Trigger:** USB flash drives or other USB storage devices connected while encryption posture check is active
- **Error message:** "Device security not met" / "Device security error"

## Cause
Windows detects attached USB storage devices as local disks. Since USB drives typically lack encryption, the posture check fails even if the actual system disk is properly encrypted.

## Resolution
**Current workaround:** Disconnect the USB storage device. The posture check should pass once the USB device is removed.

> **Note:** Twingate is evaluating filtering mechanisms to exclude USB drives from the encrypted disk check. No ETA provided.

## Gotchas
- This is a false positive — the actual local disk may be fully encrypted
- Any USB storage device can trigger this, not just flash drives
- No configuration option currently exists to exclude removable media from the check
- Users may be unexpectedly blocked from Twingate access after plugging in USB peripherals

## Related Topics
- Device Posture checks (encryption condition)
- Twingate Client troubleshooting on Windows
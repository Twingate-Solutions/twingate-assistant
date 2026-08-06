---
source: https://help.twingate.com/articles/1384415743-when-hard-disk-encryption-is-activated-in-device-posture-attached-usb-storage-devices-may-cause-the-check-to-fail
type: help
fetched: 2026-08-06
source_version: 48243c7c6aea407ecf02766a64b978df0245cdf6c64c3b8d2cd2734411280bde
---

# When Hard Disk Encryption Device Posture Check Fails with USB Storage Devices

## Summary
On Windows, enabling hard disk encryption as a device posture condition can cause Twingate connection failures when USB storage devices are attached. Windows incorrectly identifies the USB device as a local disk, which typically lacks encryption, triggering a posture check failure.

## Key Information
- **Component**: Twingate Client / Device Security
- **Platform**: Windows only
- **Trigger**: USB flash drives or other USB storage devices connected when encryption posture check is active
- **Known issue**: Twingate is evaluating filtering USB drives from encryption checks (fix not yet available)

## Symptoms
- Connection to Twingate fails with error: `"Device security not met"` or `"Device security error"`

## Cause
Windows incorrectly detects attached USB storage devices as local disks. Since USB drives typically do not have encryption enabled, the device posture encryption check fails.

## Resolution
**Immediate workaround**: Disconnect the USB storage device before connecting to Twingate.

No configuration-based fix is currently available. A platform-level fix to filter USB drives from encryption detection is under evaluation.

## Gotchas
- This is a false positive — the USB device is not a local disk, but Windows reports it as one
- Simply having the USB device plugged in (even if not actively used) is enough to trigger the failure
- No client-side or admin-side configuration can currently bypass this without disconnecting the device

## Related Docs
- Twingate Device Posture configuration
- Device Security policy settings
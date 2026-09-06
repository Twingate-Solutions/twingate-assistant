---
source: https://help.twingate.com/articles/1384415743-when-hard-disk-encryption-is-activated-in-device-posture-attached-usb-storage-devices-may-cause-the-check-to-fail
type: help
fetched: 2026-09-06
source_version: 936e1fc500c0750994bec12085ff454643bae5241d220f1b65522595caaca5fd
---

# When Hard Disk Encryption Check Fails Due to USB Storage Devices

## Page Title
When hard disk encryption is activated in device posture, attached USB storage devices may cause the check to fail

## Summary
On Windows, enabling disk encryption as a device posture condition can cause false failures when USB storage devices are connected. Windows incorrectly identifies the USB device as a local disk, which then fails the encryption check since USB drives typically aren't encrypted.

## Key Information
- **Component**: Twingate Client / Device Security
- **Platform**: Windows only
- **Trigger**: USB flash drives or other USB storage devices connected during posture check
- **Behavior**: Windows misidentifies USB device as local disk, checks it for encryption, finds none, fails posture check
- **Status**: Twingate is evaluating filtering mechanisms to exclude USB drives; no permanent fix currently available

## Symptoms
- Connection to Twingate fails with error: `"Device security not met"`
- Error occurs specifically when disk encryption is a configured posture condition
- Issue appears/disappears correlating with USB device connection state

## Prerequisites
- Device posture policy with hard disk encryption condition enabled
- Windows client
- USB storage device connected to the machine

## Resolution (Workaround)
1. Disconnect the USB storage device
2. Retry Twingate connection

No configuration-side workaround is currently available.

## Gotchas
- This is a false positive — the USB device is not actually a system disk
- The issue is non-deterministic ("in some cases") — not all USB devices trigger the failure
- No registry, policy, or Twingate setting currently resolves this without removing the USB device
- Encryption requirement cannot be scoped to exclude removable media at this time

## Related Docs
- Twingate Device Posture configuration (device security conditions)
- Twingate Client troubleshooting (Windows)
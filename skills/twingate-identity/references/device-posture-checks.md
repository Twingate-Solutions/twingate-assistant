---
source: https://www.twingate.com/docs/device-posture-checks
type: docs
fetched: 2026-11-08
source_version: 5a627bbd08b2d0c342cc0c0a472318f6c8a003589cc936c145f266e579fe9720
trust: official
---

# Device Posture Checks

## Page Title
Device Posture Checks

## Summary
Twingate's Device Profiles use native posture checks collected by the Twingate Client to evaluate device compliance against Approved Operating Systems or Trusted Profiles. Available checks vary by platform (Windows, macOS, Linux, iOS, Android).

## Key Information

### Windows Checks
| Check | Reports |
|---|---|
| HD encryption | BitLocker status on system and other disks |
| Screen lock | Password required on screen saver return |
| Firewall | Windows or third-party firewall state via Windows Security Center |
| Antivirus | Windows or third-party AV state via Windows Security Center |
| Minimum OS version | Windows 10, 11, Windows Server 2022 |

### macOS Checks
| Check | Reports |
|---|---|
| Screen lock | Password required after sleep/screen saver |
| Biometric configuration | Touch ID or Face ID configured |
| Firewall | Native firewall enabled (**standalone Client only**) |
| HD encryption | FileVault state (**standalone Client only**) |
| Minimum OS version | macOS 14–26 |

### Linux Checks
| Check | Reports |
|---|---|
| Firewall | UFW, firewalld, or iptables enabled |
| HD encryption | All non-`/boot` partitions encrypted via LUKS (`libcryptsetup`) |

### iOS Checks
| Check | Reports |
|---|---|
| Screen lock | Passcode required |
| Biometric configuration | Touch ID or Face ID configured |
| Minimum OS version | iOS 18–26 |

### Android Checks
| Check | Reports |
|---|---|
| Screen lock | Any screen lock configured |
| Biometric configuration | Fingerprint or facial recognition configured |
| HD encryption | File-Based Encryption enabled |

## Gotchas
- **macOS clamshell mode**: Device always reports biometric configuration as **disabled** when lid is closed, regardless of actual setting
- **macOS Firewall**: If "Block all incoming connections" is enabled, firewall is reported as **disabled**
- **macOS Firewall & FileVault**: Only available with the **macOS standalone Client**, not the browser extension
- **Linux HD encryption**: Uses `libcryptsetup`; only LUKS encryption is detected; `/boot` partition is excluded from check
- **Linux Firewall**: Supported distros are Debian/Ubuntu, CentOS/Fedora, and Arch Linux only

## Prerequisites
- Twingate Client installed on target device
- Device Profiles feature enabled in Twingate admin console
- macOS standalone Client required for Firewall and HD encryption checks on macOS

## Related Docs
- Approved Operating Systems
- Trusted Profiles
- Device Profiles
- macOS standalone Client setup
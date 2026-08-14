---
source: https://www.twingate.com/docs/device-posture-checks
type: docs
fetched: 2026-08-14
source_version: 0e7fffe7a8f7fcdc5a0b2dc1be11b7473b2bd1af3c7d82d2a4a9a46afd6541af
---

# Device Posture Checks

## Page Title
Device Posture Checks

## Summary
Twingate Clients collect native device posture data used by Device Profiles to evaluate compliance via Approved Operating Systems or Trusted Profiles. Available checks vary by platform (Windows, macOS, Linux, iOS, Android).

## Key Information

### Windows
| Check | Reports |
|-------|---------|
| HD encryption | BitLocker status on system and other disks |
| Screen lock | Password required after screen saver |
| Firewall | Windows or third-party firewall via Windows Security Center |
| Antivirus | Windows or third-party AV via Windows Security Center |
| Minimum OS version | Windows 10, 11, Windows Server 2022 |

### macOS
| Check | Reports |
|-------|---------|
| Screen lock | Password required after sleep/screen saver |
| Biometric | Touch ID/Face ID configured (clamshell mode always reports disabled) |
| Firewall | Native firewall enabled (**standalone Client only**) |
| HD encryption | FileVault status (**standalone Client only**) |
| Minimum OS version | macOS 14–26 |

### Linux
| Check | Reports |
|-------|---------|
| Firewall | UFW, firewalld, or iptables (Debian/Ubuntu, CentOS/Fedora, Arch) |
| HD encryption | LUKS encryption on all partitions except `/boot` via `libcryptsetup` |

### iOS
| Check | Reports |
|-------|---------|
| Screen lock | Passcode required |
| Biometric | Touch ID/Face ID configured |
| Minimum OS version | iOS 18–26 |

### Android
| Check | Reports |
|-------|---------|
| Screen lock | Any screen lock type configured |
| Biometric | Fingerprint or facial recognition configured |
| HD encryption | File-Based Encryption status |

## Prerequisites
- Twingate Client installed on target devices
- macOS Firewall and FileVault checks require **macOS standalone Client** (not browser extension or other variants)

## Gotchas
- **macOS clamshell mode**: Biometric always reports as disabled when device lid is closed, regardless of actual configuration
- **macOS firewall**: Reports as disabled if "Block all incoming connections" is enabled
- **Linux HD encryption**: Only checks non-`/boot` partitions; requires `libcryptsetup` library
- **Linux firewall**: Limited to specific distro families (Debian/Ubuntu, CentOS/Fedora, Arch)
- **Android screen lock**: Reports any lock type as compliant (no differentiation by lock strength)
- Posture checks feed into **Device Profiles** → used by **Approved Operating Systems** or **Trusted Profiles** configurations

## Related Docs
- Device Profiles
- Approved Operating Systems
- Trusted Profiles
- macOS standalone Client documentation
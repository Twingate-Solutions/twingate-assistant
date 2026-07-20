# Device Posture Checks

## Page Title
Device Posture Checks

## Summary
Twingate Client collects native device posture data to evaluate devices against Approved Operating Systems or Trusted Profiles. Available checks vary by platform (Windows, macOS, Linux, iOS, Android). These checks feed into Device Profiles for access control decisions.

## Key Information

### Windows Checks
| Check | Reports |
|-------|---------|
| HD encryption | BitLocker status on system and other disks |
| Screen lock | Password required on screen saver return |
| Firewall | Windows or third-party firewall via Windows Security Center |
| Antivirus | Windows or third-party AV via Windows Security Center |
| Minimum OS version | Windows 10, 11, Windows Server 2022 |

### macOS Checks
| Check | Reports |
|-------|---------|
| Screen lock | Password required after sleep/screen saver |
| Biometric | Touch ID/Face ID configured (disabled in clamshell mode) |
| Firewall | Native firewall only; standalone Client required |
| HD encryption | FileVault status; standalone Client required |
| Minimum OS version | macOS 14–26 |

### Linux Checks
| Check | Reports |
|-------|---------|
| Firewall | UFW, firewalld, or iptables on Debian/Ubuntu, CentOS/Fedora, Arch |
| HD encryption | LUKS encryption on all non-`/boot` partitions via `libcryptsetup` |

### iOS Checks
| Check | Reports |
|-------|---------|
| Screen lock | Passcode required |
| Biometric | Touch ID/Face ID configured |
| Minimum OS version | iOS 18–26 |

### Android Checks
| Check | Reports |
|-------|---------|
| Screen lock | Any screen lock type configured |
| Biometric | Fingerprint or facial recognition configured |
| HD encryption | File-Based Encryption status |

## Gotchas
- **macOS clamshell mode**: Biometric always reports as disabled when lid is closed, regardless of actual setting
- **macOS Firewall**: Only available with macOS standalone Client (not browser extension); "Block all incoming connections" causes firewall to report as **disabled**
- **macOS HD encryption (FileVault)**: Requires macOS standalone Client
- **Linux HD encryption**: Only `/boot` partition excluded from LUKS check; all other partitions must be encrypted
- **Linux Firewall**: Limited to specific distros — Debian/Ubuntu, CentOS/Fedora, Arch Linux

## Prerequisites
- Twingate Client installed on devices
- macOS standalone Client required for Firewall and FileVault checks
- Linux requires `libcryptsetup` library for encryption checks
- Device Profiles configured with Approved Operating Systems or Trusted Profiles

## Related Docs
- Device Profiles
- Approved Operating Systems
- Trusted Profiles
- macOS standalone Client documentation
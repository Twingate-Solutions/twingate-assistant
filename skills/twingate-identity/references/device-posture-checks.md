# Device Posture Checks

## Summary
Twingate Client collects native device posture data to evaluate devices against Device Profiles (Approved Operating Systems or Trusted Profiles). Available checks vary by platform and OS version.

## Key Information

- Posture checks are collected automatically by the Twingate Client
- Used within **Device Profiles** to enforce access policies
- Platform support varies; some checks require specific client types (e.g., macOS standalone Client)

## Posture Checks by Platform

### Windows
| Check | Reports |
|-------|---------|
| HD Encryption | BitLocker status on system and other disks |
| Screen Lock | Password required after screen saver |
| Firewall | Windows or third-party firewall via Windows Security Center |
| Antivirus | Windows or third-party AV via Windows Security Center |
| Minimum OS Version | Windows 10, 11, Windows Server 2022 |

### macOS
| Check | Reports |
|-------|---------|
| Screen Lock | Password required after sleep/screen saver |
| Biometric | Touch ID/Face ID configured (reports disabled in clamshell mode) |
| Firewall | Native firewall enabled — **standalone Client only** |
| HD Encryption | FileVault status — **standalone Client only** |
| Minimum OS Version | macOS 14–26 |

### Linux
| Check | Reports |
|-------|---------|
| Firewall | UFW, firewalld, or iptables (Debian/Ubuntu, CentOS/Fedora, Arch) |
| HD Encryption | LUKS encryption via `libcryptsetup` (all partitions except `/boot`) |

### iOS
| Check | Reports |
|-------|---------|
| Screen Lock | Passcode required |
| Biometric | Touch ID/Face ID configured |
| Minimum OS Version | iOS 18–26 |

### Android
| Check | Reports |
|-------|---------|
| Screen Lock | Any screen lock configured |
| Biometric | Fingerprint or facial recognition configured |
| HD Encryption | File-Based Encryption enabled |

## Gotchas

- **macOS clamshell mode**: Biometric always reports as disabled when lid is closed, regardless of actual configuration
- **macOS Firewall/FileVault**: Only available with the macOS standalone Client, not the browser extension or other client types
- **macOS Firewall**: If "Block all incoming connections" is enabled, firewall reports as **disabled**
- **Linux HD Encryption**: Uses `libcryptsetup`; only LUKS encryption detected; `/boot` partition excluded from check
- **Windows Antivirus/Firewall**: Detection relies on Windows Security Center reporting — third-party tools must register with Security Center

## Prerequisites

- Twingate Client installed on devices
- macOS Firewall and HD Encryption checks require **macOS standalone Client**
- Linux firewall checks supported only on Debian/Ubuntu, CentOS/Fedora, and Arch Linux distributions

## Related Docs

- Device Profiles
- Approved Operating Systems
- Trusted Profiles
- macOS standalone Client setup
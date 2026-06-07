# Device Posture Checks

## Summary
Twingate Client collects native device posture data to evaluate devices against Device Profile requirements. Checks vary by platform and feed into Approved Operating Systems or Trusted Profiles configurations.

## Key Information

- Posture checks are collected automatically by the Twingate Client — no separate agent required
- Results feed into **Device Profiles** → **Approved Operating Systems** or **Trusted Profiles**
- Check availability varies significantly by platform and client type

## Posture Checks by Platform

### Windows
| Check | Details |
|-------|---------|
| HD Encryption | BitLocker (system + other disks) |
| Screen Lock | Password required after screen saver |
| Firewall | Windows or third-party, via Windows Security Center |
| Antivirus | Windows or third-party, via Windows Security Center |
| Min OS Version | Windows 10, 11, Server 2022 |

### macOS
| Check | Details |
|-------|---------|
| Screen Lock | Password after sleep/screen saver |
| Biometric | Touch ID/Face ID (disabled in clamshell mode) |
| Firewall | Native only; **standalone Client only** |
| HD Encryption | FileVault; **standalone Client only** |
| Min OS Version | macOS 14–26 |

### Linux
| Check | Details |
|-------|---------|
| Firewall | UFW, firewalld, or iptables (Debian/Ubuntu, CentOS/Fedora, Arch) |
| HD Encryption | LUKS via `libcryptsetup` (all partitions except `/boot`) |

### iOS
| Check | Details |
|-------|---------|
| Screen Lock | Passcode required |
| Biometric | Touch ID/Face ID |
| Min OS Version | iOS 18–26 |

### Android
| Check | Details |
|-------|---------|
| Screen Lock | Any screen lock type |
| Biometric | Fingerprint or facial recognition |
| HD Encryption | File-Based Encryption |

## Gotchas

- **macOS clamshell mode**: Biometric always reports as disabled when lid is closed, regardless of actual configuration
- **macOS Firewall/FileVault**: Only available with the **standalone Client** — not the browser extension or other variants
- **macOS Firewall**: If "Block all incoming connections" is enabled, firewall reports as **disabled**
- **Linux HD Encryption**: Only checks LUKS encryption via `libcryptsetup`; `/boot` partition is excluded from check
- **Android Screen Lock**: Reports any lock type as passing — does not distinguish PIN, pattern, password, etc.
- **No Windows Server support** beyond Server 2022 listed; verify compatibility for other Server versions

## Prerequisites

- Twingate Client installed on endpoint devices
- macOS Firewall/FileVault checks require **macOS standalone Client** specifically
- Linux encryption check requires `libcryptsetup` library present on system

## Related Docs

- Device Profiles
- Approved Operating Systems
- Trusted Profiles
- macOS standalone Client setup
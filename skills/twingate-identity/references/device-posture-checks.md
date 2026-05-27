# Device Security Posture Checks

## Summary
Twingate desktop and client applications perform device posture checks to define trusted devices and enforce Security Policies at the network or individual Resource level. Supported checks vary by platform and are reported by the Twingate client application.

## Key Information
- Posture check results feed into Security Policies applied to Networks or individual Resources
- Each platform supports a different subset of posture checks
- Some checks are client-type specific (e.g., macOS standalone Client required for HD Encryption and Firewall)

## Posture Checks by Platform

### Windows
| Check | Details |
|-------|---------|
| Hard drive encryption | BitLocker (system + other disks) |
| Screen lock | Password required on screen saver return (WinAPI `LogonUser`) |
| Firewall | Windows or third-party, via Windows Security Center |
| Antivirus | Windows or third-party, via Windows Security Center |
| Minimum OS version | Windows 10, 11, Windows Server 2022 |

### macOS
| Check | Details |
|-------|---------|
| Screen lock | Password required after sleep/screen saver |
| Biometric | Touch ID or Face ID configured |
| Firewall | Native firewall only; **standalone Client only** |
| HD Encryption | FileVault; **standalone Client only** |
| Minimum OS version | macOS 12–15 |

### Linux
| Check | Details |
|-------|---------|
| Firewall | UFW, firewalld, or iptables (Debian/Ubuntu, CentOS/Fedora, Arch) |
| Hard drive encryption | All non-`/boot` partitions via LUKS (`libcryptsetup`) |

### iOS
| Check | Details |
|-------|---------|
| Screen lock | Password required |
| Biometric | Touch ID or Face ID |
| Minimum OS version | iOS 15–18 |

### Android
| Check | Details |
|-------|---------|
| Screen lock | Any screen lock type |
| Biometric | Fingerprint or facial recognition |
| Hard drive encryption | File-Based Encryption |

## Gotchas
- **macOS clamshell mode**: Closed lid always reports biometric as **disabled**, regardless of actual configuration
- **macOS "Block all incoming connections"**: Device reports firewall as **disabled** even when firewall is on
- **macOS Firewall + HD Encryption**: Only available with the macOS standalone Client, not the browser extension
- **Linux encryption**: Uses `libcryptsetup`; only LUKS-encrypted partitions qualify; `/boot` partition exempted
- **Linux firewall**: Limited to specific distro families — verify compatibility before enforcing

## Prerequisites
- Twingate desktop/mobile client installed on managed devices
- macOS standalone Client required for Firewall and HD Encryption checks on macOS
- Security Policies must be configured to use posture check results

## Related Docs
- macOS Standalone Client
- Security Policies
- Device Security configuration
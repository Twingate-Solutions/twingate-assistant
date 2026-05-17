# Device Security Posture Checks

## Summary
Twingate desktop and client applications perform device posture checks to enforce trust definitions as part of Device Security policies. These checks can be applied to Security Policies for Networks or individual Resources. Supported checks vary by platform.

## Key Information
- Posture checks integrate with Security Policies at Network or Resource level
- Checks are performed by Twingate desktop/client applications automatically
- Platform support varies — not all checks available on all OS versions

## Supported Checks by Platform

### Windows (10, 11, Server 2022)
| Check | Details |
|-------|---------|
| Hard drive encryption | BitLocker on system + other disks |
| Screen lock | Password required on screen saver return (WinAPI `LogonUser`) |
| Firewall | Windows or third-party, via Windows Security Center |
| Antivirus | Windows or third-party, via Windows Security Center |
| Minimum OS version | Configurable version requirement |

### macOS (12–15)
| Check | Details |
|-------|---------|
| Screen lock | Password required after sleep/screen saver |
| Biometric | Touch ID or Face ID configured |
| Firewall | Native macOS firewall only |
| HD Encryption | FileVault status |
| Minimum OS version | Configurable version requirement |

> **Note:** HD Encryption and Firewall checks available only in macOS standalone Client

### Linux
| Check | Details |
|-------|---------|
| Firewall | UFW, firewalld, or iptables (Debian/Ubuntu, CentOS/Fedora, Arch) |
| Hard drive encryption | All non-`/boot` partitions encrypted via LUKS (`libcryptsetup`) |

### iOS (15–18)
| Check | Details |
|-------|---------|
| Screen lock | Password required |
| Biometric | Touch ID or Face ID configured |
| Minimum OS version | Configurable version requirement |

### Android
| Check | Details |
|-------|---------|
| Screen lock | Any screen lock type configured |
| Biometric | Fingerprint or facial recognition configured |
| Hard drive encryption | File-Based Encryption enabled |

## Gotchas
- **macOS clamshell mode**: Closed lid always reports biometric as **disabled**, regardless of actual configuration
- **macOS firewall**: If "Block all incoming connections" is enabled, firewall reports as **disabled**
- **macOS firewall/encryption**: Only available in the macOS standalone Client, not the browser extension
- **Linux encryption**: Uses `libcryptsetup` — only LUKS encryption detected; `/boot` partition exempted
- **Linux firewall**: Limited to specific distro families; other distros may not report correctly
- **Android screen lock**: Any lock type counts (PIN, pattern, password — not differentiated)

## Prerequisites
- Twingate desktop or mobile client installed on endpoint devices
- Device Security feature enabled in Twingate admin console
- Security Policies configured to use posture check criteria

## Related Docs
- macOS standalone Client documentation
- Security Policies configuration
- Device Security overview
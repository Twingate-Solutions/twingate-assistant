# Device Security Posture Checks

## Summary
Twingate desktop and client applications perform device posture checks to enforce trust definitions used in Security Policies. Checks are platform-specific and report security configuration states to determine device trustworthiness. Results feed into Network-level or Resource-level Security Policies.

## Key Information
- Posture checks are performed by Twingate desktop/client applications automatically
- Results are used in **Security Policies** applied to Networks or individual Resources
- Each platform supports a different subset of posture checks

## Platform-Specific Checks

### Windows (10, 11, Server 2022)
| Check | Reports |
|-------|---------|
| Hard drive encryption | BitLocker status on system and other disks |
| Screen lock | Password required on screen saver return (WinAPI `LogonUser`) |
| Firewall | Windows or third-party firewall via Windows Security Center |
| Antivirus | Windows or third-party AV via Windows Security Center |
| Minimum OS version | OS meets configured requirement |

### macOS (12–15)
| Check | Reports |
|-------|---------|
| Screen lock | Password required after sleep/screen saver |
| Biometric configuration | Touch ID or Face ID configured |
| Firewall | Native firewall only |
| HD Encryption | FileVault status |
| Minimum OS version | OS meets configured requirement |

> **Note:** HD Encryption and Firewall checks available only in the **macOS standalone Client**

### Linux
| Check | Reports |
|-------|---------|
| Firewall | UFW, firewalld, or iptables enabled |
| Hard drive encryption | All non-`/boot` partitions encrypted via LUKS (`libcryptsetup`) |

### iOS (15–18)
| Check | Reports |
|-------|---------|
| Screen lock | Password required on device |
| Biometric configuration | Touch ID or Face ID configured |
| Minimum OS version | OS meets configured requirement |

### Android
| Check | Reports |
|-------|---------|
| Screen lock | Any screen lock configured |
| Biometric configuration | Fingerprint or facial recognition configured |
| Hard drive encryption | File-Based Encryption enabled |

## Gotchas
- **macOS clamshell mode**: Closed lid always reports biometric as **disabled**, regardless of actual config
- **macOS firewall**: "Block all incoming connections" causes firewall to report as **disabled**
- **macOS HD Encryption and Firewall**: Only available in the standalone Client app, not the browser extension or other clients
- **Linux firewall**: Limited to UFW/firewalld/iptables on specific distros (Debian/Ubuntu, CentOS/Fedora, Arch)
- **Linux encryption**: Uses `libcryptsetup`; only LUKS encryption is detected; `/boot` partition is excluded from check

## Related Docs
- macOS standalone Client
- Security Policies
- Device Security configuration
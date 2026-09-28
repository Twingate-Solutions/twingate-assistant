---
source: https://help.twingate.com/articles/1900346829-twingate-client-system-requirements-and-supported-operating-systems
type: help
fetched: 2026-09-27
source_version: d9d73d202583c1acc52bde99284eb486b449e53f16f3a72434b551d26cc225e9
---

# Twingate Client System Requirements and Supported Operating Systems

## Summary
Defines minimum OS versions and platforms supported by the Twingate Client across desktop and mobile. Twingate drops support for OS versions that reach end-of-life; the client may continue functioning temporarily but updates will cease.

## Key Information

### Desktop Clients
| Platform | Minimum Version |
|----------|----------------|
| Windows | Windows 10 21H2 (LTS) |
| macOS | macOS 14 (Sequoia) |
| Linux | Varies by distro |

### Supported Linux Distributions (x86/AMD64 and ARM64 unless noted)
- **Ubuntu**: 20.04 LTS, 22.04 LTS, 24.04 LTS
- **Debian**: 9+
- **Fedora**: 40+
- **CentOS**: Stream 9+
- **Oracle Linux**: 8+
- **Arch Linux, ThinPro, NixOS**: x64/AMD64 only

### Mobile Clients
| Platform | Minimum Version |
|----------|----------------|
| iOS | iOS 18 |
| Android | Android 14 (Upside Down Cake) |

## Prerequisites
- **Windows**: .NET 8 Desktop Runtime (bundled with `.exe` installer)
- **Admin rights**: Required for initial installation on Windows and macOS
- **macOS**: System Extension framework must be available
- **DNS**: Twingate configures a local DNS resolver for private resource resolution

## Gotchas
- Windows 7/8 are **not supported**
- Older macOS versions (e.g., Monterey) may install older client versions but are **not officially supported**
- Android custom ROMs or restricted devices may be unsupported
- Arch Linux, ThinPro, and NixOS are **x64/AMD64 only** — no ARM64 support
- EOL OS versions may work temporarily but receive no support or updates

## Related Docs
- Twingate Client installation guides (Windows, macOS, Linux)
- Twingate Connector system requirements
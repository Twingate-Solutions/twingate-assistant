---
source: https://help.twingate.com/articles/1900346829-twingate-client-system-requirements-and-supported-operating-systems
type: help
fetched: 2026-10-11
source_version: f0dd1b168f67a8cd8f55804fe7722369ed9e9e65dbf2d107dbd4e56c345f1a3c
trust: official
---

# Twingate Client System Requirements and Supported Operating Systems

## Summary
Documents minimum OS versions and platforms supported by the Twingate Client across desktop, mobile, and Linux distributions. EOL OS versions are not supported; Twingate may still function temporarily but receives no updates or support on those platforms.

## Key Information

### Desktop Clients
| Platform | Minimum Version | Notes |
|----------|----------------|-------|
| Windows | Windows 10 21H2 (LTS) | Requires .NET 8 Desktop Runtime |
| macOS | macOS 14 (Sequoia) | Older versions may install older client builds, unsupported |
| Linux | Varies by distro | See below |

### Supported Linux Distributions (x86/AMD64 and ARM64 unless noted)
- **Ubuntu**: 20.04 LTS, 22.04 LTS, 24.04 LTS
- **Debian**: 9 or later
- **Fedora**: 40 or later
- **CentOS**: Stream 9 or later
- **Oracle Linux**: 8 or later
- **Arch Linux, ThinPro, NixOS**: x64/AMD64 only

### Mobile Clients
| Platform | Minimum Version |
|----------|----------------|
| iOS | iOS 18 (App Store) |
| Android | Android 14 / Upside Down Cake (Google Play) |

## Prerequisites
- **Windows**: .NET 8 Desktop Runtime (bundled with `.exe` installer)
- **Admin rights**: Required for initial installation on Windows and macOS
- **macOS**: System Extension framework must be available (used by network extension)

## Additional Requirements
- **DNS**: Twingate configures a local DNS resolver for private resource resolution — be aware this modifies system DNS settings
- **macOS System Extension**: Must not be blocked by MDM or security policy

## Gotchas
- Windows 7 and 8 are explicitly **not supported**
- Android custom ROMs or restricted devices may not work even if Android version meets minimum
- Arch Linux, ThinPro, and NixOS are **x64/AMD64 only** — no ARM64 support for these distros
- Older macOS versions (e.g., Monterey) may install an older client version silently — this is not officially supported
- EOL OS versions: Twingate may continue functioning temporarily post-EOL but client updates will eventually stop being available

## Related Docs
- Twingate Client installation guides (Windows, macOS, Linux)
- Twingate Connector system requirements (separate page)
- MDM deployment documentation for managed device rollouts
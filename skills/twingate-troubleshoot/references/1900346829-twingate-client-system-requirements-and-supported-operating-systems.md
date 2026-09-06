---
source: https://help.twingate.com/articles/1900346829-twingate-client-system-requirements-and-supported-operating-systems
type: help
fetched: 2026-09-06
source_version: 3aa0df401d8da794cd628cd451acfadc8f2d924718d8496cc7b95d63d1501f2d
---

# Twingate Client System Requirements and Supported Operating Systems

## Summary
Defines minimum OS versions and platforms for the Twingate Client across desktop, mobile, and Linux distributions. Requirements vary by platform with specific runtime dependencies for Windows.

## Key Information

### Desktop Clients
| Platform | Minimum Version | Notes |
|----------|----------------|-------|
| Windows | Windows 10 (Build 1809) | Requires .NET 8 Desktop Runtime |
| macOS | macOS 13 (Ventura) | Older versions unsupported |
| Linux | Varies by distro | See below |

### Supported Linux Distributions (x86/AMD64 and ARM64 unless noted)
- **Ubuntu**: 20.04 LTS, 22.04 LTS, 24.04 LTS
- **Debian**: 9 or later
- **Fedora**: 40 or later
- **CentOS**: Stream 9 or later
- **Oracle Linux**: 8 or later
- **x64/AMD64 only**: Arch Linux, ThinPro, NixOS

### Mobile Clients
| Platform | Minimum Version |
|----------|----------------|
| iOS | iOS 15 |
| Android | Android 9 (Pie) |

## Prerequisites
- Admin/root rights required for initial installation on Windows and macOS
- .NET 8 Desktop Runtime (bundled with `.exe` installer on Windows)
- macOS requires System Extension framework support

## Additional Requirements
- **DNS**: Twingate configures a local DNS resolver for private resource resolution
- **macOS**: Uses System Extension framework (not legacy kernel extensions)
- **Android**: Custom ROMs or restricted devices may not be supported

## Gotchas
- Windows 7/8 are explicitly **not supported**
- macOS Monterey and older may install older client versions but are **not officially supported**
- Arch Linux, ThinPro, and NixOS are **x64/AMD64 only** — no ARM64 support for these distros
- .NET 8 Desktop Runtime is bundled with the `.exe` installer but may need manual installation in enterprise/MSI deployments
- Android custom ROMs may have compatibility issues

## Related Docs
- Twingate Client installation guides (Windows, macOS, Linux)
- Twingate Connector system requirements
- Enterprise deployment / MDM documentation

---
*Last updated: May 2025*
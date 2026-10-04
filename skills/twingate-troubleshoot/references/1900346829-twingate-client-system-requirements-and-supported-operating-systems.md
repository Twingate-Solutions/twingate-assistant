---
source: https://help.twingate.com/articles/1900346829-twingate-client-system-requirements-and-supported-operating-systems
type: help
fetched: 2026-10-04
source_version: 856c67e3671cdc9b2458cf85d34bde337a6a99b947f28b296b26de3f2b9f9986
trust: official
---

# Twingate Client System Requirements and Supported Operating Systems

## Summary
Documents minimum OS versions and platforms supported by the Twingate Client across desktop, mobile, and Linux distributions. Twingate drops support for OS versions that reach end-of-life; the client may continue functioning temporarily but receives no further updates.

## Key Information

### Desktop Clients
| Platform | Minimum Version | Notes |
|----------|----------------|-------|
| Windows | Windows 10 21H2 (LTS) | Requires .NET 8 Desktop Runtime |
| macOS | macOS 14 (Sequoia) | Older versions may run older client builds, unsupported |
| Linux | Varies by distro | See below |

### Supported Linux Distributions (x86/AMD64 and ARM64 unless noted)
- **Ubuntu**: 20.04 LTS, 22.04 LTS, 24.04 LTS
- **Debian**: 9 or later
- **Fedora**: 40 or later
- **CentOS**: Stream 9 or later
- **Oracle Linux**: 8 or later
- **Arch Linux, ThinPro, NixOS**: x64/AMD64 only

### Mobile Clients
| Platform | Minimum Version | Notes |
|----------|----------------|-------|
| iOS | iOS 18 | App Store |
| Android | Android 14 (Upside Down Cake) | Google Play; custom ROMs may be unsupported |

## Prerequisites / Additional Requirements
- **.NET 8 Desktop Runtime** — Windows only; bundled with `.exe` installer
- **Admin/root rights** — Required for initial installation on Windows and macOS
- **macOS System Extension framework** — Used by the macOS client for network extensions
- **Local DNS resolver** — Twingate configures system DNS for private resource resolution

## Gotchas
- Windows 7 and 8 are explicitly **not supported**
- macOS versions older than Sequoia (e.g., Monterey) may install older client versions but receive **no official support**
- Android custom ROMs or restricted devices may be unsupported
- Arch Linux, ThinPro, and NixOS are **x64/AMD64 only** — no ARM64 support for these distros
- End-of-life OS versions may lose access to client updates even if the client continues to function temporarily

## Related Docs
- Twingate Client installation guides (Windows, macOS, Linux)
- Twingate Connector system requirements
- Network extension and DNS configuration documentation
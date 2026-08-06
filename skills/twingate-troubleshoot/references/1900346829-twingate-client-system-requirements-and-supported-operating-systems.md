---
source: https://help.twingate.com/articles/1900346829-twingate-client-system-requirements-and-supported-operating-systems
type: help
fetched: 2026-08-06
source_version: b49127d85b16d10eac5d851f6a88edc746d0907afba4803a49205aa0307b54b4
---

# Twingate Client System Requirements and Supported Operating Systems

## Summary
Defines minimum OS versions and platforms supported by the Twingate Client across desktop, mobile, and Linux distributions. Requirements apply to end-user devices running the Twingate Client software.

## Key Information

### Desktop Clients
| Platform | Minimum Version | Notes |
|----------|----------------|-------|
| Windows | Windows 10 Build 1809 | Requires .NET 8 Desktop Runtime |
| macOS | macOS 13 (Ventura) | Older versions may install but unsupported |
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
| iOS | iOS 15 |
| Android | Android 9 (Pie) |

## Prerequisites
- Admin/elevated rights required for initial installation on Windows and macOS
- .NET 8 Desktop Runtime (bundled with `.exe` installer on Windows)
- macOS requires System Extension framework support
- Network must allow Twingate to configure a local DNS resolver

## Gotchas
- Windows 7 and 8 are **not supported**
- macOS Monterey and older: may install an older client version but officially unsupported
- Android custom ROMs or restricted devices may be unsupported
- Arch Linux, ThinPro, and NixOS are **x64/AMD64 only** — no ARM64 support
- macOS client uses System Extensions (not Network Kernel Extensions) — relevant for MDM/security policy configuration
- Twingate modifies system DNS configuration to resolve private resources; may conflict with existing local DNS setups

## Additional Requirements
- **DNS**: Twingate installs a local DNS resolver on the client device for private resource resolution
- **macOS**: System Extension must be allowed (may require MDM approval or manual user approval in Security & Privacy settings)

## Related Docs
- Twingate Client installation guides (Windows, macOS, Linux)
- MDM deployment documentation
- Network and firewall requirements

---
*Last updated: May 2025*
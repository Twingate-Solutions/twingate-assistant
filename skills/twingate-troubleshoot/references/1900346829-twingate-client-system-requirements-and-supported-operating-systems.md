---
source: https://help.twingate.com/articles/1900346829-twingate-client-system-requirements-and-supported-operating-systems
type: help
fetched: 2026-10-25
source_version: 5ec3b5e2bd4b6caaa39c5bb3c8cce6ede1c079cc6fdbeb889081235923d7ddf8
trust: official
---

# Twingate Client System Requirements and Supported Operating Systems

## Summary
Documents minimum supported OS versions for Twingate Client across desktop and mobile platforms. Twingate drops support for OS versions that reach end-of-life; the client may continue functioning temporarily but receives no updates or official support.

## Key Information

### Desktop Clients
| Platform | Minimum Version | Notes |
|----------|----------------|-------|
| Windows | Windows 10 21H2 (LTS) | Requires .NET 8 Desktop Runtime |
| macOS | macOS 14 (Sequoia) | Older versions may run older client builds, unsupported |
| Linux | Varies by distro | See below |

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
| iOS | iOS 18 (App Store) |
| Android | Android 14 / "Upside Down Cake" (Google Play) |

## Additional Requirements
- **.NET 8 Desktop Runtime**: Required on Windows; bundled with `.exe` installer
- **Admin Rights**: Required for initial installation on Windows and macOS
- **Network Extensions**: macOS client uses the System Extension framework
- **DNS**: Twingate installs a local DNS resolver for private resource name resolution

## Gotchas
- Windows 7 and 8 are explicitly unsupported
- Android custom ROMs or restricted devices may not work even on Android 14+
- macOS versions older than Sequoia (14) may install an older client version but are not officially supported — no guarantee of parity or updates
- End-of-life OS versions may continue working temporarily but will eventually stop receiving client updates

## Related Docs
- Twingate Client installation guides (Windows, macOS, Linux, iOS, Android)
- Twingate Connector system requirements (separate page)
---
source: https://help.twingate.com/articles/1900346829-twingate-client-system-requirements-and-supported-operating-systems
type: help
fetched: 2026-10-18
source_version: f5bb686b9407181ed7f9ffcf67f30dff4d1696149c55d34d7e3ca5ee587f42f8
trust: official
---

# Twingate Client System Requirements and Supported Operating Systems

## Summary
Defines minimum supported OS versions for Twingate Client across desktop and mobile platforms. Twingate drops support for OS versions at their end-of-life; the client may still function temporarily but receives no further updates on unsupported versions.

---

## Key Information

### Desktop Clients

| Platform | Minimum Version |
|----------|----------------|
| Windows | Windows 10 21H2 (LTS) |
| macOS | macOS 14 (Sequoia) |
| Linux | Varies by distro (see below) |

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

---

## Prerequisites / Additional Requirements

- **Windows**: .NET 8 Desktop Runtime (bundled with `.exe` installer)
- **Admin rights**: Required for initial installation on Windows and macOS
- **macOS**: Relies on System Extension framework (not legacy kernel extensions)
- **DNS**: Twingate installs a local DNS resolver for private resource name resolution

---

## Gotchas

- Windows 7/8 are **not supported**
- macOS versions older than Sequoia (e.g., Monterey) may install an older Twingate client version but are **not officially supported**
- Android custom ROMs or restricted devices may be unsupported
- Arch Linux, ThinPro, and NixOS support is **x64/AMD64 only** — no ARM64
- End-of-life OS versions may lose access to client updates even if the client continues to function temporarily

---

## Related Docs
- Twingate Client installation guides (Windows, macOS, Linux)
- Twingate Connector system requirements (separate from client requirements)
- [Twingate Help Center](https://help.twingate.com)
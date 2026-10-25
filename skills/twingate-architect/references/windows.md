---
source: https://www.twingate.com/docs/windows
type: docs
fetched: 2026-10-25
source_version: c7d5c3a5d2b214e806f5d6ca7085eaeb0d2ab1041ce186a82c479f4366aed57e
trust: official
---

# Twingate Windows Client

## Summary
Installs the Twingate client on Windows 10/11 and Windows Server 2022/2025. The client runs from the system tray and intercepts only private Resource traffic. Windows Server is supported only in headless mode.

## Key Information
- Download installer from `get.twingate.com`
- Supported OS: Windows 10, Windows 11, Windows Server 2022, Windows Server 2025
- Windows Server: headless mode only (no posture checks support)
- Two tunnel driver options: **TunTap** (default, recommended) or **Wintun** (experimental, potentially higher throughput)
- Switching drivers requires reinstalling the client

## Prerequisites
- Local admin rights on the machine
- .NET Desktop Runtime (x64):
  - Versions from Nov 2024–Oct 22, 2026: .NET Desktop Runtime **8.0**
  - Versions from Oct 22, 2026 onward: .NET Desktop Runtime **10.0**
  - Recommendation: install .NET 10 to cover all current versions
- EXE/update installs handle .NET automatically; **MSI installs require manual .NET installation**

## Step-by-Step

1. Download installer from `get.twingate.com`
2. Run installer with local admin rights
3. Select tunnel driver (TunTap or Wintun) from install dialog
4. Launch Twingate from desktop shortcut or Start menu
5. Enter your Twingate network name (e.g., `Beamreach`)
6. Click **Join Network** → redirected to your org's identity provider
7. Authenticate with normal credentials; client runs from Notification Area (system tray)

## Configuration Values
| Item | Value/Notes |
|------|-------------|
| Installer source | `get.twingate.com` |
| Default tunnel driver | TunTap |
| Alternative tunnel driver | Wintun |
| .NET runtime (current) | 10.0 Desktop Runtime x64 |
| .NET runtime (legacy) | 8.0 Desktop Runtime x64 |
| .NET download source | Microsoft official site |

## Gotchas
- **MSI installs**: .NET runtime is NOT auto-installed — must be done manually before or alongside client install
- **Windows Server**: posture check packages are absent; only headless mode is supported
- **Intel Ethernet on Windows 10**: may cause slow speeds; Windows 10 does not auto-update Intel Ethernet drivers — download latest from Intel's website manually
- Switching tunnel drivers requires full reinstallation of the client
- Client only intercepts traffic for configured private Resources; normal internet browsing is unaffected

## Related Docs
- [Windows Client Migration to .NET 10](https://www.twingate.com/docs/) *(see Twingate docs site)*
- Twingate headless/service mode documentation (for Windows Server deployments)
- Twingate posture checks documentation
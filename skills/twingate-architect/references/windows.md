# Twingate Windows Client

## Summary
Installation guide for the Twingate Windows desktop client. Covers supported OS versions, tunnel driver selection, first-time setup, and common troubleshooting issues. Windows Server is supported only in headless mode.

## Key Information
- Supported platforms: Windows 10, Windows 11, Windows Server 2022, Windows Server 2025
- Windows Server **requires headless mode** (no posture checks supported)
- Installer requires **local admin rights**
- Two tunnel drivers available: **TunTap** (default, recommended) and **Wintun** (experimental, potentially higher throughput)
- Client runs from the **Notification Area** (system tray) after installation
- Only intercepts traffic for private Resources; does not affect general internet browsing

## Prerequisites
- Local admin rights on the machine
- .NET Desktop Runtime (x64):
  - Client versions **before November 2024**: .NET Desktop Runtime **6.0+**
  - Client versions **from November 2024 onward**: .NET Desktop Runtime **8.0+**
- EXE/update installer auto-installs .NET; **MSI installer requires manual .NET installation**

## Installation Steps
1. Download installer from `get.twingate.com`
2. Run installer with local admin rights
3. Select tunnel driver (TunTap or Wintun) from install dialog
4. Launch Twingate from desktop shortcut or Start menu
5. Enter your Twingate network name (e.g., `Beamreach`)
6. Click **Join Network** → redirected to your identity provider
7. Authenticate with your organizational credentials

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Download URL | `get.twingate.com` |
| Default tunnel driver | TunTap |
| Alternative tunnel driver | Wintun |
| .NET requirement (current) | .NET Desktop Runtime 8.0 x64 |

## Gotchas
- **Switching tunnel drivers requires a full reinstall** of the client
- **MSI installs**: must manually install .NET Desktop Runtime — not automatic
- **Intel Ethernet adapters on Windows 10**: may cause slow speeds; Windows 10 won't auto-update the driver — must manually update from Intel's website
- Windows Server posture checks are **not available**; headless mode only

## Related Docs
- Twingate headless/service mode (for Windows Server deployments)
- Posture checks documentation
- Client download: `get.twingate.com`
- [.NET 8.0 Desktop Runtime x64 (Microsoft)](https://dotnet.microsoft.com)
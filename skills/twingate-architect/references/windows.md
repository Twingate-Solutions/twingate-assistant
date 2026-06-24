# Twingate Windows Client

## Summary
Installation and configuration guide for the Twingate Windows desktop client. Covers installer download, tunnel driver selection, first-time setup, and common troubleshooting issues.

## Key Information
- Supported OS: Windows 10, Windows 11, Windows Server 2022, Windows Server 2025
- Windows Server only supports **headless mode** (no posture checks)
- Client runs from the Windows Taskbar Notification Area after install
- Two tunnel driver options: **TunTap** (default, recommended) and **Wintun** (experimental, potentially higher throughput)

## Prerequisites
- Local admin rights on the machine
- .NET Desktop Runtime (x64):
  - Client versions before November 2024: .NET 6.0+
  - Client versions November 2024+: .NET 8.0+
- EXE/update installer auto-installs .NET; **MSI installer requires manual .NET installation**

## Step-by-Step

1. Download installer from `get.twingate.com`
2. Run installer (requires local admin)
3. Select tunnel driver: choose **TunTap** (default) or Wintun
4. Launch Twingate from desktop shortcut or Start menu
5. Enter your Twingate network name (e.g., `Beamreach`)
6. Click **Join Network** → redirected to org identity provider
7. Authenticate with normal credentials

## Configuration Values
| Setting | Value |
|---|---|
| Installer download | `get.twingate.com` |
| Default tunnel driver | TunTap |
| Alternative tunnel driver | Wintun |
| Required .NET runtime | Desktop Runtime x64 (8.0+ for Nov 2024+ clients) |

## Gotchas
- **Switching tunnel drivers requires full reinstall** — select preferred driver during install dialog
- **MSI installs**: must manually install .NET Desktop Runtime; EXE installs handle this automatically
- **Windows Server**: posture checks are unsupported; use headless mode only
- **Intel Ethernet on Windows 10**: may cause slow speeds — update driver manually from Intel's website (Windows Update may not provide latest version)
- Twingate only intercepts traffic for configured private Resources; normal internet browsing is unaffected

## Related Docs
- Headless mode (Windows Server usage)
- Posture checks
- Twingate network configuration / identity provider setup
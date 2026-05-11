# Twingate Windows Client

## Summary
Twingate Windows client installs via an EXE or MSI installer and runs from the system tray. Supports Windows 10, 11, Server 2022, and Server 2025, with Windows Server limited to headless mode only.

## Key Information
- Download from `get.twingate.com`
- Supported OS: Windows 10, Windows 11, Windows Server 2022, Windows Server 2025
- Windows Server must use **headless mode** (no posture checks supported)
- Two tunnel driver options: **TunTap** (default, recommended) and **Wintun** (experimental, potentially higher throughput)
- To switch tunnel drivers, reinstall the client and select the preferred driver

## Prerequisites
- Local admin rights on the machine
- .NET Desktop Runtime (x64):
  - Client versions **before November 2024**: .NET Desktop Runtime 6.0+
  - Client versions **from November 2024 onward**: .NET Desktop Runtime 8.0+
- EXE installer auto-installs .NET runtime; **MSI installer requires manual .NET installation**

## Step-by-Step Installation
1. Download installer from `get.twingate.com`
2. Run installer (requires local admin)
3. Select tunnel driver (TunTap or Wintun) from install dialog
4. Launch Twingate from desktop shortcut or Start menu
5. Enter your Twingate network name (e.g., `Beamreach`)
6. Click **Join Network** → redirected to configured identity provider
7. Authenticate with normal credentials

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Download URL | `get.twingate.com` |
| Default tunnel driver | TunTap |
| Alternative tunnel driver | Wintun |
| .NET runtime (current) | 8.0 Desktop Runtime x64 |

## Gotchas
- **MSI installs**: Must manually install .NET Desktop Runtime — not bundled automatically
- **Windows Server**: Posture checks are unsupported; headless mode is the only supported method
- **Intel Ethernet adapters on Windows 10**: May experience slow speeds due to outdated drivers; update manually from Intel's website (Windows Update may not provide latest version)
- Switching tunnel drivers requires a full reinstall — no in-app toggle

## Related Docs
- Headless mode (Windows Server usage)
- Twingate Client posture checks
- Identity provider configuration
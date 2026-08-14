---
source: https://www.twingate.com/docs/windows
type: docs
fetched: 2026-08-14
source_version: 7e90ceb4a17e8785a854aa70979658ac11888cb402ec208266c28270b5253cbe
---

# Twingate Windows Client

## Summary
Twingate Windows Client installs via an EXE or MSI installer and runs from the system tray. Supports Windows 10, 11, Server 2022, and Server 2025, with Windows Server limited to headless mode only due to missing posture check dependencies.

## Key Information
- Download from `get.twingate.com`
- Supported OS: Windows 10, Windows 11, Windows Server 2022, Windows Server 2025
- Windows Server: **headless mode only** (no posture checks supported)
- Two tunnel driver options: **TunTap** (default, recommended) and **Wintun** (experimental, potentially higher throughput)
- To switch tunnel drivers, reinstall the client and select from install dialog

## Prerequisites
- Local admin rights on the machine
- .NET Desktop Runtime (x64):
  - Client versions **before November 2024**: .NET Desktop Runtime 6.0+
  - Client versions **from November 2024 onward**: .NET Desktop Runtime 8.0+
- EXE/update installer installs .NET automatically; **MSI installer requires manual .NET installation**

## Step-by-Step

1. Download installer from `get.twingate.com`
2. Run installer (requires local admin)
3. Select tunnel driver: TunTap (default) or Wintun
4. Launch Twingate from desktop shortcut or Start menu
5. Enter your Twingate network name (e.g., `Beamreach`)
6. Click **Join Network** → redirected to configured identity provider
7. Authenticate with normal credentials
8. Client runs from Notification Area (system tray); only intercepts traffic for private Resources

## Configuration Values
| Parameter | Options | Notes |
|-----------|---------|-------|
| Tunnel Driver | `TunTap` (default), `Wintun` | Selected at install time; requires reinstall to change |
| Network Name | Your org's Twingate network name | Entered on first launch |

## Gotchas
- **MSI installs**: Must manually install .NET 8.0 Desktop Runtime x64 — not bundled
- **Windows Server**: Posture checks not supported; headless mode only
- **Intel Ethernet adapters on Windows 10**: May cause slow speeds; Windows 10 does not auto-update Intel NIC drivers — update manually from Intel's website
- Tunnel driver changes require full reinstall

## Related Docs
- Twingate headless mode (for Windows Server deployments)
- Posture checks documentation
- `.NET 8.0 Desktop Runtime x64` — download directly from Microsoft
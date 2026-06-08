# Twingate Windows Client

## Summary
Twingate Windows Client installs via an EXE or MSI installer and runs from the system tray. Supports Windows 10, 11, Server 2022, and Server 2025, with Windows Server limited to headless mode only.

## Key Information
- Download from: `get.twingate.com`
- Supported OS: Windows 10, Windows 11, Windows Server 2022, Windows Server 2025
- Windows Server: headless mode only (no posture checks supported)
- Two tunnel driver options: **TunTap** (default, recommended) and **Wintun** (experimental, potentially higher throughput)
- Runs from Windows Notification Area (system tray) after install

## Prerequisites
- Local admin rights on the machine
- .NET Desktop Runtime (x64):
  - Client versions before November 2024 → .NET 6.0+
  - Client versions from November 2024 onward → .NET 8.0+
- EXE installer auto-installs .NET runtime; **MSI installer does not** — manual .NET install required

## Step-by-Step

1. Download installer from `get.twingate.com`
2. Run installer (requires local admin)
3. Select tunnel driver: **TunTap** (default) or Wintun
4. Launch Twingate from desktop shortcut or Start menu
5. Enter your Twingate network name (e.g., `Beamreach`)
6. Click **Join Network** → redirected to org identity provider
7. Authenticate with normal credentials

## Configuration Values
| Setting | Value |
|---|---|
| Tunnel driver (default) | TunTap |
| Tunnel driver (alternative) | Wintun |
| Driver switching method | Reinstall and reselect |

## Gotchas
- **MSI installs**: Must manually install .NET Desktop Runtime 8.0 x64 — not auto-installed
- **Windows Server**: Posture checks not supported; headless mode only
- **Driver switching**: No in-app toggle; must fully reinstall to change tunnel driver
- **Intel Ethernet adapters on Windows 10**: May cause slow speeds; update driver manually from Intel's website (Windows Update may not provide latest version)
- Only intercepts traffic for configured private Resources — does not affect general internet traffic

## Related Docs
- Headless mode (Windows Server usage)
- Posture checks
- Client installation via MSI (enterprise deployment)
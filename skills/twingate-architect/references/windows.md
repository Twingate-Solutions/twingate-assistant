# Twingate Windows Client

## Summary
Installation guide for the Twingate Windows desktop client. Covers supported OS versions, tunnel driver selection, first-time configuration, and common troubleshooting issues. Windows Server is supported only in headless mode.

## Key Information
- Download from `get.twingate.com`
- Supported OS: Windows 10, Windows 11, Windows Server 2022, Windows Server 2025
- Windows Server **must** use headless mode (no posture checks supported)
- Runs from system tray (Notification Area) after installation
- Only intercepts traffic for configured private Resources; does not affect general internet browsing

## Prerequisites
- Local admin rights on the machine
- .NET Desktop Runtime (x64):
  - Client versions **before** November 2024: .NET Desktop Runtime 6.0+
  - Client versions **from** November 2024 onward: .NET Desktop Runtime 8.0+
- EXE/update installer installs .NET automatically; **MSI installer requires manual .NET installation**

## Step-by-Step Installation
1. Download installer from `get.twingate.com`
2. Run installer (requires local admin)
3. Select tunnel driver: **TunTap** (default, recommended) or **Wintun** (alternative, potentially higher throughput)
4. Launch via desktop shortcut or Start menu
5. Enter your Twingate network name (e.g., `Beamreach`)
6. Click **Join Network** → redirected to configured identity provider
7. Authenticate with organizational credentials

## Configuration Values
| Setting | Options | Notes |
|---|---|---|
| Tunnel Driver | `TunTap` (default), `Wintun` | Switch by reinstalling and selecting at install dialog |
| Network Name | Your org's Twingate subdomain | Required on first run |

## Gotchas
- **Switching tunnel drivers requires a full reinstall** — no in-app toggle
- **MSI installs require manual .NET installation** — not handled automatically unlike EXE installs
- **Windows Server posture checks are unsupported** — headless mode only
- **Intel Ethernet adapters on Windows 10** may cause slow speeds; Windows 10 won't auto-update the driver — manually update from Intel's website
- .NET requirement jumped from 6.0 to 8.0 in November 2024 — old installs may need runtime upgrade

## Related Docs
- Headless mode (Windows Server usage)
- Twingate Client posture checks
- Network Resource configuration
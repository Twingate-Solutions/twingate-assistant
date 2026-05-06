# Twingate Windows Client

## Summary
Installation guide for the Twingate Windows desktop client. Covers download, installation with tunnel driver selection, first-time network configuration, and common troubleshooting issues.

## Key Information
- Download from `get.twingate.com`
- Supported platforms: Windows 10, Windows 11, Windows Server 2022, Windows Server 2025
- Windows Server only supports **headless mode** (no posture checks)
- Client runs from the system tray (Notification Area) after install
- Only intercepts traffic for configured private Resources; does not affect general internet traffic

## Prerequisites
- Local admin rights on the machine
- .NET Desktop Runtime (x64):
  - Client < November 2024: .NET Desktop Runtime **6.0+**
  - Client ≥ November 2024: .NET Desktop Runtime **8.0+**
- EXE installer auto-installs .NET; **MSI installer requires manual .NET installation**

## Step-by-Step

1. Download installer from `get.twingate.com`
2. Run installer (requires local admin)
3. Select tunnel driver: **TunTap** (default, recommended) or **Wintun** (alternative, potentially higher throughput)
4. Launch Twingate from desktop shortcut or Start menu
5. Enter your Twingate network name (e.g., `Beamreach`)
6. Click **Join Network** → redirected to configured identity provider
7. Authenticate with org credentials

## Configuration Values

| Parameter | Options | Notes |
|-----------|---------|-------|
| Tunnel Driver | `TunTap` (default), `Wintun` | Selected at install time; change requires reinstall |
| Network Name | Your org's Twingate subdomain | Provided during first-run setup |

## Gotchas
- **Switching tunnel drivers requires a full reinstall** — no in-place driver swap
- **MSI installs**: Must manually install .NET Desktop Runtime; EXE installs handle this automatically
- **Intel Ethernet on Windows 10**: May experience slow speeds; Windows 10 won't auto-update Intel NIC drivers — update manually from Intel's website
- **Windows Server**: Posture check packages unavailable; headless mode only

## Related Docs
- Headless mode (Windows Server usage)
- Twingate Client posture checks
- Identity provider configuration
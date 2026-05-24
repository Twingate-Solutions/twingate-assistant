# Twingate Windows Client

## Summary
Installation guide for the Twingate Windows desktop client. Covers supported OS versions, tunnel driver selection, first-time setup, and common troubleshooting issues. Windows Server is supported only in headless mode.

## Key Information
- Download from `get.twingate.com`
- Supported platforms: Windows 10, Windows 11, Windows Server 2022, Windows Server 2025
- Windows Server **only** supports headless mode (no posture checks)
- Runs from Windows Taskbar Notification Area after install

## Prerequisites
- Local admin rights on the machine
- .NET Desktop Runtime (x64):
  - Client versions before November 2024: .NET 6.0+
  - Client versions from November 2024 onward: .NET 8.0+
- EXE/update installer auto-installs .NET; **MSI installer requires manual .NET installation**

## Step-by-Step

1. Download installer from `get.twingate.com`
2. Run installer (requires local admin)
3. Select tunnel driver: **TunTap** (default, recommended) or **Wintun** (experimental, potentially higher throughput)
4. Launch Twingate from desktop shortcut or Start menu
5. Enter your Twingate network name (e.g., `Beamreach`)
6. Click **Join Network** → redirected to identity provider
7. Authenticate with organizational credentials
8. Client connects; only intercepts traffic for defined private Resources

## Configuration Values

| Option | Values | Notes |
|--------|--------|-------|
| Tunnel Driver | `TunTap` / `Wintun` | Set at install time; requires reinstall to change |
| Network Name | Your org's network name | Entered on first launch |

## Gotchas
- **Switching tunnel drivers requires full reinstall** — no in-app toggle
- **MSI installs**: Must manually install .NET Desktop Runtime x64 separately
- **Windows Server**: Posture checks not supported; headless mode only
- **Intel Ethernet on Windows 10**: May cause slow speeds; update driver manually from Intel's website (not via Windows Update)
- .NET version requirement changed in November 2024 — older clients need 6.0, newer need 8.0

## Related Docs
- Twingate headless/service mode (for Windows Server deployments)
- Posture checks documentation
- [.NET 8.0 Desktop Runtime x64 (Microsoft)](https://dotnet.microsoft.com/download/dotnet/8.0)
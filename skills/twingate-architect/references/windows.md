# Windows Client Installation

## Summary
Twingate Windows client supports Windows 10, Windows 11, Windows Server 2022, and Windows Server 2025. Installation requires local admin rights and offers two tunnel driver options. Windows Server is only supported in headless mode due to missing posture check dependencies.

## Key Information
- Download from `get.twingate.com`
- Requires local admin rights to install
- Two tunnel drivers available: **TunTap** (default, recommended) and **Wintun** (experimental, potentially higher throughput)
- Runs from Windows Taskbar Notification Area after installation
- Only intercepts traffic for configured private Resources; does not affect regular internet browsing
- Windows Server: headless mode only (no posture checks supported)

## Prerequisites
- Windows 10, 11, Server 2022, or Server 2025
- Local administrator rights
- **.NET Desktop Runtime (x64)**:
  - Client versions before November 2024: .NET Desktop Runtime 6.0+
  - Client versions from November 2024 onward: .NET Desktop Runtime 8.0+
  - EXE installer auto-installs .NET; **MSI installer requires manual .NET installation**

## Step-by-Step Installation
1. Download installer from `get.twingate.com`
2. Run installer with local admin rights
3. Select tunnel driver (TunTap recommended; Wintun optional)
4. Launch Twingate via desktop shortcut or Start menu
5. Enter your Twingate network name (e.g., `Beamreach`)
6. Click **Join Network** → redirected to identity provider
7. Authenticate with organizational credentials

## Configuration Values
| Setting | Value |
|---|---|
| Default tunnel driver | TunTap |
| Alternative tunnel driver | Wintun |
| .NET requirement (pre-Nov 2024) | Desktop Runtime 6.0 x64 |
| .NET requirement (Nov 2024+) | Desktop Runtime 8.0 x64 |

## Gotchas
- **MSI installs**: Must manually install .NET Desktop Runtime — it is NOT auto-installed (unlike EXE installer)
- **Driver switching**: Requires full reinstall; cannot switch drivers in-place
- **Windows Server**: Posture checks are unsupported; headless mode is the only option
- **Intel Ethernet on Windows 10**: May cause slow speeds; Windows 10 does not auto-update Intel adapter drivers — manually update from Intel's website if experiencing slow network throughput

## Related Docs
- Headless mode (for Windows Server deployments)
- Posture checks
- Client troubleshooting
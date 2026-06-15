# Twingate Windows Client

## Summary
Twingate Windows Client installs as a system tray application for accessing private Resources. Supports Windows 10, Windows 11, Windows Server 2022, and Windows Server 2025, with Windows Server limited to headless mode only.

## Key Information
- Download from `get.twingate.com`
- Runs from Windows Notification Area (system tray)
- Only intercepts traffic for configured private Resources; does not affect general internet browsing
- Two tunnel driver options: **TunTap** (default, recommended) and **Wintun** (experimental, potentially higher throughput)
- To switch drivers, reinstall and select at the install dialog

## Prerequisites
- Local admin rights required for installation
- **.NET Desktop Runtime (x64)**:
  - Client versions before November 2024: .NET Desktop Runtime 6.0+
  - Client versions from November 2024 onward: .NET Desktop Runtime 8.0+
  - EXE installer auto-installs .NET; **MSI installer requires manual .NET installation**

## Step-by-Step

1. Download installer from `get.twingate.com`
2. Run installer (requires local admin)
3. Select tunnel driver (TunTap recommended)
4. Launch from desktop shortcut or Start menu
5. Enter your Twingate network name when prompted
6. Click **Join Network** → redirected to your identity provider
7. Authenticate with org credentials

## Configuration Values
| Setting | Options | Notes |
|---|---|---|
| Tunnel Driver | `TunTap` (default), `Wintun` | Selected at install; change requires reinstall |
| Windows Server mode | Headless only | GUI/posture checks not supported |

## Gotchas
- **Windows Server**: Posture checks are unsupported; headless mode is the only supported deployment method
- **MSI installs**: .NET Desktop Runtime must be manually installed; EXE/update handles this automatically
- **Intel Ethernet on Windows 10**: May experience slow speeds due to outdated drivers; update manually from Intel's website (Windows 10 does not auto-update these)
- Switching tunnel drivers requires full reinstall

## Related Docs
- Headless mode configuration (for Windows Server deployments)
- Twingate Client posture checks
- Network Resources configuration
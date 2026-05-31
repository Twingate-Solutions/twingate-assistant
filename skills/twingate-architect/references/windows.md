# Twingate Windows Client

## Summary
Twingate Windows Client installer for desktop and server environments. Supports Windows 10/11 and Windows Server 2022/2025. Windows Server requires headless mode only due to missing posture check dependencies.

## Key Information
- Download from `get.twingate.com`
- Installation requires local admin rights
- Two tunnel driver options: **TunTap** (default, recommended) and **Wintun** (experimental, potentially higher throughput)
- Client runs from system tray (Notification Area) after installation
- Only intercepts traffic for private Resources; does not affect general internet traffic

## Prerequisites
- Local administrator rights on the machine
- **.NET Desktop Runtime (x64)**:
  - Client versions before November 2024: .NET Desktop Runtime 6.0+
  - Client versions November 2024+: .NET Desktop Runtime 8.0+
- EXE installer auto-installs .NET; **MSI installer requires manual .NET installation**

## Step-by-Step

1. Download installer from `get.twingate.com`
2. Run installer (local admin required)
3. Select tunnel driver: **TunTap** (default) or **Wintun**
4. Launch Twingate from desktop shortcut or Start menu
5. Enter your Twingate network name (e.g., `Beamreach`)
6. Click **Join Network** → redirected to configured identity provider
7. Authenticate with org credentials

## Configuration Values
| Option | Values | Notes |
|--------|--------|-------|
| Tunnel Driver | `TunTap` / `Wintun` | Set during install; switch by reinstalling |
| Network Name | `<your-org-name>` | Subdomain of your Twingate network |

## Gotchas
- **Windows Server**: Posture checks are unsupported; use headless mode only
- **MSI installs**: Must manually install .NET Desktop Runtime — not bundled automatically
- **Driver switching**: Requires full reinstall to change tunnel driver
- **Intel Ethernet on Windows 10**: May cause slow speeds; update driver manually from Intel's website (Windows Update may not provide latest version)
- .NET requirement changed in November 2024 (6.0 → 8.0); ensure correct runtime version for your client version

## Related Docs
- Twingate headless mode (Windows Server usage)
- Client posture checks
- [.NET 8.0 Desktop Runtime x64 (Microsoft)](https://dotnet.microsoft.com/download/dotnet/8.0)
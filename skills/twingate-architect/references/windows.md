## Windows Client

Install and setup guide for the Twingate Windows Client. Supports Windows 10, 11, Server 2022, and Server 2025; Windows Server only supports headless mode.

**Key Information:**
- Supported: Windows 10, Windows 11, Windows Server 2022, Windows Server 2025
- Windows Server does NOT support the interactive Client (no posture check packages) -- headless mode only
- Two tunnel drivers: TunTap (default, recommended) and Wintun (alternative, potentially higher throughput) -- switch by reinstalling
- Runs from the Windows Notification Area (system tray)
- EXE installer automatically installs .NET 8 Desktop Runtime; MSI requires manual .NET 8 installation
- Requires local admin rights to install

**Step-by-Step:**
1. Download installer from get.twingate.com
2. Run installer (admin rights required); select tunnel driver (TunTap recommended)
3. Launch Twingate from desktop shortcut or Start menu
4. Enter Twingate Network name on first run
5. Authenticate via IdP -- Client connects and runs from system tray

**Gotchas:**
- Windows Server: posture checks unavailable; use headless mode only
- Intel Ethernet adapter users on Windows 10 may experience slow speeds -- update driver directly from Intel's website
- MSI deployments require .NET 8 Desktop Runtime (x64) pre-installed separately

**Related Docs:**
- /docs/windows-headless -- Headless/service mode for Windows Server and CI/CD
- /docs/windows-client-dotnet-8 -- .NET 8 migration details for managed deployments
- /docs/endpoint-requirements -- Required firewall ports

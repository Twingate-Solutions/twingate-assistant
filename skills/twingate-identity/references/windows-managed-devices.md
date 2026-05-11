# Windows Managed Devices

## Summary
Twingate Windows Client supports EXE and MSI deployment formats for MDM distribution. EXE is recommended as it bundles the .NET Runtime prerequisite; MSI requires manual .NET 8 Desktop Runtime installation. Both formats support identical command-line parameters for automated deployment.

## Key Information
- EXE package: includes .NET Runtime, recommended for MDM deployment
- MSI package: requires separate .NET Desktop Runtime 8.0 (x64) installation
- Chocolatey support exists but updates may lag behind official releases
- Clients older than 12 months are unsupported and cannot connect

## Prerequisites
- .NET Desktop Runtime 8.0 (x64) if using MSI installer
- MDM solution (Intune, Endpoint Manager, or third-party)
- Download: EXE or MSI from Twingate downloads page

## Command-Line Configuration Values

| Parameter | Values | Description |
|-----------|--------|-------------|
| `/qn` | flag | Silent install, auto-accepts ToS |
| `network=` | `<name>.twingate.com` | Pre-configures network name |
| `auto_update=` | `true/false` | Reconnect automatically after update |
| `no_optional_updates=` | `true/false` | Disables user-triggered updates |
| `ncsi_global_dns=` | `true/false` | Fix false "No internet" NCSI warnings |
| `TUN_DRIVER=` | `TunTap` (default) / `Wintun` | Tunnel driver selection |

## Step-by-Step: Basic Deployment

1. Download EXE installer (recommended) or MSI
2. If MSI: separately deploy .NET Desktop Runtime 8.0 x64
3. Configure command-line parameters for your environment
4. Deploy via MDM (Intune guide available separately)
5. Run installer with parameters

**Example command:**
```
TwingateWindowsInstaller.exe /qn network=beamreach.twingate.com no_optional_updates=true auto_update=true
```

Running this on a system with existing installation performs in-place update; `auto_update=true` restores existing session.

## Gotchas
- **`no_optional_updates` decision depends on local admin rights:**
  - Users WITH local admin: leave enabled (default), users self-update
  - Users WITHOUT local admin: set `no_optional_updates=true`, push updates via MDM — otherwise users see prompts they cannot action
- MSI does NOT bundle .NET; missing runtime will cause installation failure
- Chocolatey packages are **not** on automated release pipeline — updates may be delayed
- Must maintain update cadence: clients >12 months old cannot connect to service
- `ncsi_global_dns=true` only needed if users report false "No internet" status while Twingate is running

## Related Docs
- Microsoft Intune & Endpoint Manager deployment guide
- Microsoft Intune custom PowerShell script guide (includes .NET + MSI install script)
- Twingate Windows Client public changelog
- Chocolatey installation instructions
# Windows Managed Devices

## Summary
Twingate Windows Client supports EXE and MSI deployment formats for MDM-managed environments. EXE is recommended as it bundles the .NET Runtime prerequisite; MSI requires separate .NET 8 Desktop Runtime installation. Both formats support command-line parameters for silent, pre-configured deployments.

## Key Information
- EXE includes .NET Runtime automatically; MSI does not
- Clients older than 12 months are unsupported and cannot connect
- Chocolatey package updates may be delayed (Early Access)
- Both EXE and MSI support identical command-line parameters

## Prerequisites
- .NET Desktop Runtime 8.0 (x64) or higher (MSI deployments only)
- MDM solution (Intune, Endpoint Manager, or third-party)

## Configuration Values

| Parameter | Description | Example |
|-----------|-------------|---------|
| `/qn` | Silent install, auto-accepts ToS | `/qn` |
| `network=` | Pre-configure network name | `network=beamreach.twingate.com` |
| `auto_update=` | Reconnect after update without re-login | `auto_update=true` |
| `no_optional_updates=` | Disable user-triggered updates | `no_optional_updates=true` |
| `ncsi_global_dns=` | Fix false "No internet" NCSI warnings | `ncsi_global_dns=true` |
| `TUN_DRIVER=` | Tunnel driver selection (`Wintun` or default TunTap) | `TUN_DRIVER=Wintun` |

## Step-by-Step (MDM Deployment)

1. Download [EXE installer](https://www.twingate.com/docs/windows-managed-devices) (recommended) or [MSI installer](https://www.twingate.com/docs/windows-managed-devices)
2. If using MSI, download [.NET 8.0 Desktop Runtime x64](https://dotnet.microsoft.com/download/dotnet/8.0)
3. Configure deployment command with required parameters
4. Upload package to MDM solution
5. Deploy to target device groups

**Example command:**
```bash
TwingateWindowsInstaller.exe /qn network=beamreach.twingate.com no_optional_updates=true auto_update=true
```
Running on an existing installation performs an in-place upgrade.

## `no_optional_updates` Decision Guide

| User Has Local Admin? | Recommendation |
|----------------------|----------------|
| Yes | Leave default (updates enabled) |
| No | Set `no_optional_updates=true`; push updates via MDM |

## Gotchas
- MSI requires manual .NET 8 Desktop Runtime installation — omitting it breaks the install
- If `no_optional_updates=true` is set, you **must** have an MDM process to push updates; clients older than 12 months stop working entirely
- Chocolatey packages are not on automated release pipeline — may lag behind current version
- Running install command on existing installation triggers in-place upgrade

## Related Docs
- [Microsoft Intune & Endpoint Manager Guide](https://www.twingate.com/docs/intune)
- [Microsoft Intune Custom Script Guide](https://www.twingate.com/docs/intune-custom-script)
- [Public Changelog](https://www.twingate.com/docs/changelog)
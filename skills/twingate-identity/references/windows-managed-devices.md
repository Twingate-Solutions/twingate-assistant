# Windows Managed Devices - Twingate

## Summary
Twingate Windows Client is distributed as EXE (recommended) or MSI packages for MDM deployment. The EXE includes .NET Runtime automatically; MSI requires manual .NET 8 Desktop Runtime installation. Both support identical command-line parameters for automated deployment.

## Key Information
- EXE package: self-contained, includes .NET Runtime, recommended for most deployments
- MSI package: requires separate .NET Desktop Runtime 8.0 (x64) installation
- Clients older than 12 months will not connect to Twingate service
- Chocolatey package available but not on automated release pipeline (delayed updates)

## Prerequisites
- For MSI: .NET Desktop Runtime 8.0 (x64) installed separately
- Download links: [EXE](https://www.twingate.com/docs/windows-managed-devices) | [MSI](https://www.twingate.com/docs/windows-managed-devices)

## Configuration Values (CLI Parameters)

| Parameter | Description | Example |
|-----------|-------------|---------|
| `/qn` | Silent install, auto-accepts ToS | `/qn` |
| `network=` | Pre-configure Twingate network name | `network=company.twingate.com` |
| `auto_update=` | Reconnect automatically after update | `auto_update=true` |
| `no_optional_updates=` | Disable user-triggered updates | `no_optional_updates=true` |
| `ncsi_global_dns=` | Fix false "No internet" NCSI warning | `ncsi_global_dns=true` |
| `TUN_DRIVER=` | Select tunnel driver (default: TunTap) | `TUN_DRIVER=Wintun` |

## Step-by-Step: Silent Deployment Example

```powershell
TwingateWindowsInstaller.exe /qn network=beamreach.twingate.com no_optional_updates=true auto_update=true
```

This command also performs in-place upgrades on existing installations and restores the user session via `auto_update=true`.

## Gotchas
- **`no_optional_updates` decision**: 
  - Users **with** local admin: leave enabled (default); users get update prompts and can self-update
  - Users **without** local admin: set `no_optional_updates=true`; otherwise users see prompts they cannot act on — you must push updates via MDM
- MSI installer silently fails if .NET 8 Desktop Runtime is absent — install runtime first
- Chocolatey packages lag behind official releases; not suitable for environments requiring current versions
- Running installer on existing installation performs in-place upgrade, not a fresh install

## Related Docs
- [Microsoft Intune & Endpoint Manager guide](https://www.twingate.com/docs/intune)
- [Microsoft Intune custom PowerShell script guide](https://www.twingate.com/docs/windows-managed-devices)
- [Public changelog](https://www.twingate.com/docs/windows-managed-devices)
- [.NET 8.0 Desktop Runtime x64 (Microsoft)](https://dotnet.microsoft.com/download/dotnet/8.0)
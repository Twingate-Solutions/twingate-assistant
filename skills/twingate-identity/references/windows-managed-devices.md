# Windows Managed Devices

## Summary
Twingate Windows Client is distributed as EXE or MSI packages for MDM deployment. EXE is recommended as it bundles the .NET Runtime prerequisite automatically; MSI requires manual .NET 8 Desktop Runtime installation. Both support identical command-line parameters for silent/automated deployment.

## Key Information
- EXE package: includes .NET Runtime, recommended for MDM distribution
- MSI package: requires separate .NET Desktop Runtime 8.0 (x64) installation
- Clients older than 12 months are unsupported and cannot connect to Twingate service
- Chocolatey package available but not part of automated release pipeline (delayed updates)

## Prerequisites
- .NET Desktop Runtime 8.0 (x64) — required for MSI installs (November 2024+ clients)
- MDM solution (e.g., Microsoft Intune) or manual deployment capability
- Local admin rights required for user-triggered updates

## Configuration Values (Command Line Parameters)

| Parameter | Description |
|---|---|
| `/qn` | Silent install, suppresses dialog, auto-accepts ToS |
| `network=<name>` | Pre-configures Twingate network name (e.g., `beamreach.twingate.com`) |
| `auto_update=true` | Reconnects existing session after update (no re-login required) |
| `no_optional_updates=true` | Disables user-triggered updates |
| `ncsi_global_dns=true` | Enables NCSI GlobalDns; fixes false "No internet" warnings |
| `TUN_DRIVER=Wintun` | Use Wintun driver instead of default TunTap |

## Step-by-Step: Silent Deployment Example

```bash
TwingateWindowsInstaller.exe /qn network=beamreach.twingate.com no_optional_updates=true auto_update=true
```

Running on an existing installation performs an in-place upgrade and restores the existing session (when `auto_update=true`).

## Gotchas
- **MSI missing .NET**: MSI does not bundle .NET — deployment will fail without pre-installing .NET 8.0 Desktop Runtime (x64)
- **`no_optional_updates` required for non-admins**: Users without local admin rights receive update prompts but cannot act on them — disable optional updates and push updates via MDM instead
- **12-month support window**: If disabling user-triggered updates, establish an MDM update process; outdated clients lose connectivity
- **Chocolatey delays**: Package updates lag behind official releases; not suitable for production environments requiring current versions

## Related Docs
- [Microsoft Intune & Endpoint Manager guide](https://www.twingate.com/docs/intune)
- [Microsoft Intune custom PowerShell script guide](https://www.twingate.com/docs/intune-custom-script)
- [Public changelog](https://www.twingate.com/docs/changelog)
- [.NET 8.0 Desktop Runtime x64 (Microsoft)](https://dotnet.microsoft.com/download/dotnet/8.0)
- [Chocolatey](https://chocolatey.org)
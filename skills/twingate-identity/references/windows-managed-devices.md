# Windows Managed Devices

## Summary
Twingate Windows Client is distributed as EXE (recommended, includes .NET Runtime) or MSI (requires separate .NET 8 Desktop Runtime). Both formats support command-line parameters for automated MDM deployment including silent install, network pre-configuration, and update control.

## Key Information
- EXE installer bundles .NET Desktop Runtime automatically — preferred for MDM deployment
- MSI requires .NET Desktop Runtime 8.0 (x64) separately if not present
- Clients older than 12 months are unsupported and cannot connect to the service
- Chocolatey package available but not on automated release pipeline (may lag behind)

## Prerequisites
- For MSI: [.NET 8.0 Desktop Runtime x64](https://dotnet.microsoft.com/download/dotnet/8.0) must be pre-installed
- MDM solution (Intune, Endpoint Manager, or third-party)
- Download: EXE or MSI from Twingate downloads page

## Command Line Parameters

| Option | Description |
|--------|-------------|
| `/qn` | Silent install, auto-accepts ToS |
| `network=` | Pre-configure Twingate network name |
| `auto_update=true` | Reconnect existing session after update |
| `no_optional_updates=true` | Disable user-triggered updates |
| `ncsi_global_dns=true` | Fix false "No internet" NCSI warnings |
| `TUN_DRIVER=Wintun` | Use Wintun driver (default: TunTap) |

## Example Command
```bash
TwingateWindowsInstaller.exe /qn network=beamreach.twingate.com no_optional_updates=true auto_update=true
```
Running on existing installation performs in-place upgrade; `auto_update=true` restores session automatically.

## Chocolatey Install
```bash
choco install twingate
```

## Gotchas
- **`no_optional_updates` decision depends on admin rights**: Users without local admin will see update prompts but cannot act on them — disable optional updates for non-admin users and push updates via MDM instead
- MSI missing .NET Runtime will cause install failure — distribute runtime alongside MSI
- Chocolatey packages may be delayed from latest release
- Must maintain update cadence; 12-month-old clients lose connectivity

## Related Docs
- Microsoft Intune & Endpoint Manager deployment guide
- Microsoft Intune custom PowerShell script guide
- Twingate public changelog
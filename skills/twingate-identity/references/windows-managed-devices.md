# Windows Managed Devices

## Summary
Twingate Windows Client supports EXE and MSI deployment formats for MDM-based distribution. EXE is recommended as it bundles .NET Runtime automatically; MSI requires manual .NET 8 Desktop Runtime installation. Both formats support identical command-line parameters for automated deployment.

## Key Information
- EXE package includes .NET Runtime prerequisite (recommended)
- MSI package requires separate .NET Desktop Runtime 8.0 (x64) installation
- Clients older than 12 months are unsupported and cannot connect
- Chocolatey support exists but has delayed release pipeline updates

## Prerequisites
- .NET Desktop Runtime 8.0 (x64) — required for MSI installs (November 2024+ clients)
- MDM solution (Intune, Endpoint Manager, or third-party)
- Admin rights for deployment

## Command-Line Parameters

| Parameter | Description |
|-----------|-------------|
| `/qn` | Silent install, auto-accepts ToS |
| `network=` | Pre-configure Twingate network name (e.g., `beamreach.twingate.com`) |
| `auto_update=true` | Reconnect existing session after update |
| `no_optional_updates=true` | Disable user-triggered updates |
| `ncsi_global_dns=true` | Fix false "No internet" NCSI detection |
| `TUN_DRIVER=Wintun` | Use Wintun driver (default: TunTap) |

## Example Command
```bash
TwingateWindowsInstaller.exe /qn network=beamreach.twingate.com no_optional_updates=true auto_update=true
```
Run on existing installations performs in-place update and restores session.

## Chocolatey Install
```bash
choco install twingate
```

## Gotchas
- **`no_optional_updates` decision**: Use `true` if users lack local admin rights — users will see update prompts but cannot act on them without admin. Leave default if users have admin rights.
- **MSI + .NET**: Must deploy .NET 8.0 Desktop Runtime separately before or alongside MSI
- **Stale clients**: Disabling user-triggered updates requires an MDM-based update process; 12-month-old clients lose connectivity entirely
- **Chocolatey**: Not on automated release pipeline — updates may lag behind official releases

## Related Docs
- Microsoft Intune & Endpoint Manager deployment guide
- Microsoft Intune custom PowerShell script guide
- Twingate Windows Client changelog
- .NET 8.0 Desktop Runtime x64 (Microsoft download)
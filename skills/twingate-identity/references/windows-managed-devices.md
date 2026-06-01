# Windows Managed Devices

## Summary
Twingate Windows Client is available as EXE (recommended, includes .NET Runtime) or MSI (requires separate .NET 8 Desktop Runtime). Both formats support command-line parameters for MDM/automated deployments. Clients older than 12 months cannot connect to Twingate services.

## Key Information
- **EXE**: Bundles .NET Runtime, recommended for most deployments
- **MSI**: Requires separate .NET Desktop Runtime 8.0 (x64) installation
- November 2024+ client versions require .NET Desktop Runtime 8.0 (x64) minimum
- Chocolatey package available but not auto-updated with releases (Early Access)

## Prerequisites
- For MSI deployments: [.NET 8.0 Desktop Runtime x64](https://dotnet.microsoft.com/download/dotnet/8.0) installed separately
- MDM solution (Intune, Endpoint Manager, or third-party) for managed deployments

## Configuration Values (Command Line Parameters)

| Parameter | Description |
|-----------|-------------|
| `/qn` | Silent install, suppresses dialog, auto-accepts ToS |
| `network=<name>` | Pre-configure Twingate network name (e.g., `beamreach.twingate.com`) |
| `auto_update=true` | Auto-reconnect existing session after update |
| `no_optional_updates=true` | Disable user-triggered updates |
| `ncsi_global_dns=true` | Fix false "No internet" NCSI indicator |
| `TUN_DRIVER=Wintun` | Use Wintun driver (default: TunTap) |

## Step-by-Step: Basic Deployment

```bash
# Silent install with pre-configured network, managed updates
TwingateWindowsInstaller.exe /qn network=beamreach.twingate.com no_optional_updates=true auto_update=true
```

Running installer on existing installation performs in-place upgrade; `auto_update=true` restores the existing session automatically.

## Chocolatey Install
```bash
choco install twingate
```

## Gotchas
- **`no_optional_updates` decision**: Use `true` if users lack local admin rights (they'd see update prompts but cannot install); leave default if users have admin rights
- **Client expiry**: Clients >12 months old cannot connect — if disabling user updates, implement MDM push process to keep clients current
- MSI deployments via PowerShell can reference the Intune custom script guide for downloading both .NET Runtime and MSI together
- Chocolatey packages may lag behind official releases (not in automated release pipeline)

## Related Docs
- [Microsoft Intune & Endpoint Manager guide](https://www.twingate.com/docs/intune)
- [Microsoft Intune custom PowerShell script guide](https://www.twingate.com/docs/intune-custom-script)
- [Public changelog](https://www.twingate.com/docs/windows-release-notes)
- [User terms of service](https://www.twingate.com/legal/terms)
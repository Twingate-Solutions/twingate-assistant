# Windows Managed Devices

## Summary
Twingate Windows Client is distributed as EXE (recommended, includes .NET Runtime) or MSI (requires separate .NET 8 Desktop Runtime). Both support command-line parameters for silent/automated MDM deployment. EXE is preferred for most deployments.

## Key Information
- EXE package bundles .NET Desktop Runtime automatically; MSI does not
- MSI requires .NET Desktop Runtime 8.0 (x64) minimum (clients from November 2024+)
- Chocolatey package available but **not** on automated release pipeline—updates may lag
- Clients older than 12 months will not connect to Twingate service

## Prerequisites
- For MSI: manually install [.NET 8.0 Desktop Runtime x64](https://dotnet.microsoft.com/download/dotnet/8.0) if not present
- MDM solution (Intune, Endpoint Manager, or third-party) for enterprise deployment

## Configuration Values (Command Line Parameters)

| Parameter | Description |
|---|---|
| `/qn` | Silent install, auto-accepts ToS |
| `network=<name>` | Pre-configure Twingate network (e.g., `beamreach.twingate.com`) |
| `auto_update=true` | Reconnect existing session after update |
| `no_optional_updates=true` | Disable user-triggered updates |
| `ncsi_global_dns=true` | Fix false "No internet" NCSI indicator |
| `TUN_DRIVER=Wintun` | Use Wintun driver (default: TunTap) |

## Step-by-Step: Basic Deployment

1. Download [EXE installer](https://www.twingate.com/docs/windows-managed-devices) (recommended) or MSI
2. If using MSI, deploy .NET 8.0 Desktop Runtime x64 first
3. Run installer with appropriate flags:
   ```
   TwingateWindowsInstaller.exe /qn network=yournet.twingate.com no_optional_updates=true auto_update=true
   ```
4. For Intune: follow [Intune & Endpoint Manager guide](https://www.twingate.com/docs/microsoft-intune)
5. For Chocolatey: `choco install twingate`

## Gotchas
- Running the installer on an existing installation performs an **in-place upgrade** (use `auto_update=true` to preserve session)
- `no_optional_updates=true` is required when users **lack local admin rights**—otherwise users see update prompts they cannot action
- If `no_optional_updates=true` is set, you **must** have an MDM-push process to keep clients under 12 months old
- Chocolatey packages may not reflect latest release immediately

## Decision: `no_optional_updates`
- **Allow local admin** → leave default (users self-update)
- **No local admin** → set `no_optional_updates=true`, push updates via MDM

## Related Docs
- [Microsoft Intune & Endpoint Manager guide](https://www.twingate.com/docs/microsoft-intune)
- [Intune custom PowerShell script guide](https://www.twingate.com/docs/microsoft-intune)
- [Public changelog](https://www.twingate.com/docs/windows-changelog)
# Windows Managed Devices

## Summary
Twingate Windows Client is distributed as EXE (recommended, includes .NET Runtime) or MSI (requires separate .NET 8 Desktop Runtime). Both support command-line parameters for MDM deployment. EXE is preferred for automated deployments.

## Key Information
- EXE package bundles .NET Runtime; MSI does not
- MSI requires .NET Desktop Runtime 8.0 (x64) minimum (for clients from November 2024+)
- Clients older than 12 months are unsupported and cannot connect
- Chocolatey package available but not on automated release pipeline (delayed updates)

## Prerequisites
- MSI deployments: Install [.NET 8.0 Desktop Runtime x64](https://dotnet.microsoft.com/download) separately
- MDM solution (Intune, Endpoint Manager, or third-party)

## Configuration Values (CLI Flags)

| Option | Description |
|--------|-------------|
| `/qn` | Silent install, auto-accepts ToS |
| `network=<name>` | Pre-configure Twingate network (e.g., `beamreach.twingate.com`) |
| `auto_update=true` | Reconnect existing session after update |
| `no_optional_updates=true` | Disable user-triggered updates |
| `ncsi_global_dns=true` | Fix false "No internet" NCSI indicator |
| `TUN_DRIVER=Wintun` | Use Wintun driver (default: TunTap) |

## Step-by-Step: Silent Deployment

```bash
TwingateWindowsInstaller.exe /qn network=beamreach.twingate.com no_optional_updates=true auto_update=true
```

Running on existing installation performs in-place upgrade; `auto_update=true` restores session.

## Gotchas
- **`no_optional_updates`**: Use when users lack local admin rights—users get update prompts but can't install without admin. Without this flag, non-admins will see prompts they cannot act on
- **Local admin allowed** → leave user-triggered updates enabled (default)
- **No local admin** → set `no_optional_updates=true` and push updates via MDM
- If disabling user updates, establish a regular MDM push process to avoid 12-month client expiry
- Chocolatey packages may lag behind official releases

## Deployment Methods
- **Microsoft Intune/Endpoint Manager**: Follow dedicated [Intune guide](https://www.twingate.com/docs/intune)
- **Third-party MDM**: Use EXE/MSI with CLI options above; PowerShell script available via Intune custom script guide
- **Chocolatey**: `choco install twingate`

## Related Docs
- Microsoft Intune & Endpoint Manager guide
- Microsoft Intune custom script guide (PowerShell for MSI + .NET install)
- Windows Client changelog
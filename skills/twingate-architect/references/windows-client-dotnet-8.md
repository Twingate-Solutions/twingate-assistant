# Windows Client Migration to .NET 8

## Summary
The Twingate Windows Client migrated to .NET 8 in November 2024 following Microsoft's end of .NET 6 support. EXE installer handles the dependency automatically; MSI deployments require manual .NET 8 Desktop Runtime installation.

## Key Information
- Migration occurred in **early November 2024** (November 12, 2024 was Microsoft's .NET 6 EOL date)
- **EXE installer**: automatically installs .NET 8 runtime — no admin action required
- **MSI installer**: admins must pre-install .NET 8 Desktop Runtime on each device
- Without .NET 8 Desktop Runtime, future client versions will not run

## Prerequisites
- .NET 8 Desktop Runtime x64 (for MSI deployments)
- Download from Microsoft website
- Local or domain admin permissions for deployment

## Step-by-Step (MSI Deployment)

1. Download .NET 8 Desktop Runtime x64 from Microsoft
2. Push runtime to devices via MDM or install manually
3. Use silent install flags (see below)
4. Verify installation on each device
5. Deploy Twingate Windows Client MSI as usual

## Configuration Values

**Silent install command:**
```
c:\path\to\windowsdesktop-runtime-8.0.10-win-x64.exe /install /quiet /norestart
```

**Flags:**
- `/install` — install the runtime
- `/quiet` — silent install, no UI
- `/norestart` — suppress automatic reboot

**Verify installation (PowerShell):**
```powershell
Get-WmiObject -Query "SELECT * FROM Win32_Product WHERE Name LIKE '%.NET%Runtime%8.%.%'"
```

**Manual verification:** Control Panel → Programs → Programs and Features → look for ".NET 8 Desktop Runtime"

## Gotchas
- MSI deployments have **no automatic dependency handling** — runtime must be present before deploying updated client versions
- Filename in silent install example (`8.0.10`) may differ from current runtime version — adjust path accordingly
- Runtime must be installed **before** upgrading the Twingate client, not after
- Failure to install runtime = client stops functioning after upgrade

## Related Docs
- [Windows Client Deployment Documentation](https://www.twingate.com/docs/) — managing remote Windows devices
- [Twingate Client Download Page](https://www.twingate.com/docs/)
- [Microsoft .NET 8 Desktop Runtime](https://dotnet.microsoft.com/download/dotnet/8.0)
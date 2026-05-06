# Windows Client Migration to .NET 8

## Summary
Twingate Windows Client migrated to .NET 8 in November 2024 following Microsoft's end of .NET 6 support. EXE installer handles the dependency automatically; MSI deployments require manual .NET 8 Desktop Runtime installation.

## Key Information
- Migration occurred in **early November 2024** (release date: November 12, 2024)
- .NET 8 Desktop Runtime (x64) is required for all future Windows Client versions
- EXE installer: automatically installs .NET 8 — no admin action needed
- MSI installer: admins must separately deploy .NET 8 Desktop Runtime

## Prerequisites
- .NET 8 Desktop Runtime x64 installed on each target device
- Download from [Microsoft website](https://dotnet.microsoft.com)
- MSI deployments only — EXE handles this automatically

## Step-by-Step (MSI Deployment)

1. Download .NET 8 Desktop Runtime x64 from Microsoft
2. Push runtime to devices via MDM or install manually
3. Use silent install flags (see below)
4. Verify installation on each device
5. Continue deploying Twingate Windows Client MSI as normal

## Configuration Values

**Silent Install Command:**
```cmd
c:\path\to\windowsdesktop-runtime-8.0.10-win-x64.exe /install /quiet /norestart
```

**Flags:**
| Flag | Purpose |
|------|---------|
| `/install` | Install the runtime |
| `/quiet` | Silent install, no UI |
| `/norestart` | Suppress automatic reboot |

**Verify Installation (PowerShell):**
```powershell
Get-WmiObject -Query "SELECT * FROM Win32_Product WHERE Name LIKE '%.NET%Runtime%8.%.%'"
```

**Manual Verification:** Control Panel → Programs → Programs and Features → look for ".NET 8 Desktop Runtime"

## Gotchas
- **MSI deployments will break** if .NET 8 Runtime is not pre-installed before upgrading the client
- Runtime must be x64 architecture — ensure correct package is deployed
- Future client versions will **fail to launch** entirely without the runtime, not degrade gracefully
- EXE installer path requires no changes to existing deployment workflows

## Related Docs
- [Windows Client Deployment Documentation](https://www.twingate.com/docs/windows-deployment)
- [Client Download Page](https://www.twingate.com/download)
- [Microsoft .NET 8 Desktop Runtime Download](https://dotnet.microsoft.com/download/dotnet/8.0)
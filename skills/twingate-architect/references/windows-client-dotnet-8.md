# Windows Client Migration to .NET 8

## Summary
Twingate Windows Client migrated to .NET 8 in November 2024 following Microsoft's end of .NET 6 support. EXE installer handles the .NET 8 dependency automatically; MSI deployments require manual .NET 8 Desktop Runtime installation.

## Key Information
- Migration occurred in **early November 2024** (Microsoft ended .NET 6 support November 12, 2024)
- **EXE installer**: Automatically installs .NET 8 Desktop Runtime — no admin action needed
- **MSI installer**: Admins must separately deploy .NET 8 Desktop Runtime x64 to each device
- Without .NET 8 Desktop Runtime, future client versions will not launch

## Prerequisites
- .NET 8 Desktop Runtime x64 (required for MSI deployments)
- Download from: [Microsoft website](https://dotnet.microsoft.com/download/dotnet/8.0)

## Silent Installation (MSI Path)

Push .NET 8 Desktop Runtime via MDM or manually using:

```cmd
c:\path\to\windowsdesktop-runtime-8.0.10-win-x64.exe /install /quiet /norestart
```

## Configuration Values

| Flag | Purpose |
|------|---------|
| `/install` | Install the runtime |
| `/quiet` | Silent install (no UI) |
| `/norestart` | Suppress automatic reboot |

## Verify Installation

**GUI**: Control Panel → Programs → Programs and Features → look for ".NET 8 Desktop Runtime"

**PowerShell**:
```powershell
Get-WmiObject -Query "SELECT * FROM Win32_Product WHERE Name LIKE '%.NET%Runtime%8.%.%'"
```

Expected output confirms installation:
```
Name    : Microsoft .NET Runtime - 8.0.10 (x64)
Vendor  : Microsoft Corporation
Version : 64.40.21578
```

## Gotchas
- MSI deployments will **silently fail to run** if .NET 8 is not pre-installed — no automatic fallback
- Must use x64 variant of the runtime
- EXE and MSI deployment paths have different admin responsibilities — don't assume EXE behavior applies to MSI

## Related Docs
- [Twingate Client Download Page](https://www.twingate.com/downloads)
- [Windows Client Deployment Documentation](https://www.twingate.com/docs/windows-client-deployment)
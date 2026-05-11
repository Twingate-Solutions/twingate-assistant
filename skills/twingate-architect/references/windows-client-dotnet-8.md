# Windows Client Migration to .NET 8

## Summary
Twingate Windows Client moved to .NET 8 in November 2024 following Microsoft's end of .NET 6 support. EXE installer handles the dependency automatically; MSI deployments require manual .NET 8 Desktop Runtime installation.

## Key Information
- Migration occurred in **early November 2024** (release date: November 12, 2024)
- Requires **.NET 8 Desktop Runtime (x64)**
- EXE installer: automatically installs .NET 8 as prerequisite — no admin action needed
- MSI installer: admins must manually ensure .NET 8 Desktop Runtime is present on each device
- Without .NET 8 runtime, future client versions will not launch

## Prerequisites
- .NET 8 Desktop Runtime x64 (for MSI deployments)
- Download from: [Microsoft website](https://dotnet.microsoft.com)

## Step-by-Step (MSI Deployment)

1. Download .NET 8 Desktop Runtime x64 from Microsoft
2. Push via MDM or install manually using silent install flags
3. Verify installation on target devices
4. Deploy updated Twingate Windows Client MSI as usual

## Configuration Values

**Silent install flags (required for remote/quiet deployment):**
```
c:\path\to\windowsdesktop-runtime-8.0.10-win-x64.exe /install /quiet /norestart
```

**PowerShell command to verify .NET 8 installation:**
```powershell
Get-WmiObject -Query "SELECT * FROM Win32_Product WHERE Name LIKE '%.NET%Runtime%8.%.%'"
```

**Manual verification path:**
```
Control Panel > Programs > Programs and Features
```
Look for "Microsoft .NET Desktop Runtime - 8.x.x (x64)"

## Gotchas
- MSI deployments will **break** on future client versions if .NET 8 runtime is not pre-installed
- Must use x64 runtime variant specifically
- Silent install flags are required for non-interactive/MDM deployment — omitting them may cause interactive prompts on remote devices
- Check for `.NET 8 Desktop Runtime` (not just `.NET Runtime`) — desktop apps require the Desktop variant

## Related Docs
- [Twingate Client Download Page](https://www.twingate.com/downloads)
- [Windows Client Deployment Documentation](https://www.twingate.com/docs/windows-client-deployment)
- [Microsoft .NET 6 End of Support](https://dotnet.microsoft.com/en-us/platform/support/policy)
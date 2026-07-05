# Windows Client Migration to .NET 8

## Summary
The Twingate Windows Client migrated to .NET 8 in November 2024 following Microsoft's end of support for .NET 6. EXE installer handles the dependency automatically; MSI deployments require manual .NET 8 Desktop Runtime installation.

## Key Information
- Migration occurred in **early November 2024** (release date: November 12, 2024)
- **EXE installer**: Automatically installs .NET 8 Desktop Runtime — no admin action required
- **MSI installer**: Admins must manually provision .NET 8 Desktop Runtime before or alongside deployment
- Without .NET 8 Desktop Runtime, future client versions will not launch

## Prerequisites
- .NET 8 Desktop Runtime x64 installed on each Windows device (MSI deployments only)
- Download from: [Microsoft website](https://dotnet.microsoft.com/download/dotnet/8.0)

## Step-by-Step (MSI Deployment)

1. Download `.NET 8 Desktop Runtime x64` from Microsoft
2. Push runtime to devices via MDM or install manually using silent flags (see below)
3. Verify installation on each device
4. Deploy updated Twingate Windows Client MSI as usual

## Configuration Values

**Silent install flags for .NET 8 Desktop Runtime:**
```cmd
c:\path\to\windowsdesktop-runtime-8.0.10-win-x64.exe /install /quiet /norestart
```

**PowerShell check for installed runtime:**
```powershell
Get-WmiObject -Query "SELECT * FROM Win32_Product WHERE Name LIKE '%.NET%Runtime%8.%.%'"
```

**Expected output if installed:**
```
IdentifyingNumber : {15B7D0C2-F209-4C28-AF1C-FD8326F4D58A}
Name              : Microsoft .NET Runtime - 8.0.10 (x64)
Vendor            : Microsoft Corporation
Version           : 64.40.21578
```

**Manual verification path:**
```
Control Panel > Programs > Programs and Features
```
Look for `.NET 8 Desktop Runtime` in the list.

## Gotchas
- MSI deployments have **no automatic dependency handling** — client silently fails to run if runtime is missing
- Flags `/install /quiet /norestart` are all required for silent MDM push; omitting `/norestart` may cause unexpected reboots
- Runtime is **x64 only** — verify device architecture before deploying

## Related Docs
- [Windows Client Deployment Documentation](https://www.twingate.com/docs/windows-client-deployment)
- [Client Download Page](https://www.twingate.com/download)
- [Microsoft .NET 6 End of Support](https://dotnet.microsoft.com/platform/support/policy)
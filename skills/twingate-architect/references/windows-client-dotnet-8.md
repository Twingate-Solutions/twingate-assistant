# Windows Client Migration to .NET 8

## Summary
Twingate Windows Client migrated to .NET 8 in November 2024 following Microsoft's end of support for .NET 6. MSI deployers must manually ensure .NET 8 Desktop Runtime is installed on managed devices; EXE installer handles this automatically.

## Key Information
- Migration occurred in **early November 2024**
- **EXE installer**: Automatically installs .NET 8 as prerequisite — no admin action required
- **MSI package**: Admins must separately deploy .NET 8 Desktop Runtime x64 to each device
- Without .NET 8 Desktop Runtime, future client versions will not run

## Prerequisites
- .NET 8 Desktop Runtime x64 installed on each Windows device (MSI deployments only)
- Download from [Microsoft website](https://dotnet.microsoft.com/download/dotnet/8.0)

## Configuration Values / CLI Flags

**Silent install flags for .NET 8 Desktop Runtime:**
```
c:\path\to\windowsdesktop-runtime-8.0.10-win-x64.exe /install /quiet /norestart
```

**PowerShell command to verify installation:**
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

## Step-by-Step (MSI Deployment)

1. Download .NET 8 Desktop Runtime x64 from Microsoft
2. Push runtime to devices via MDM or install manually using silent flags above
3. Verify installation via Control Panel → Programs → Programs and Features, or run PowerShell command
4. Deploy updated Twingate Windows Client MSI as normal

## Gotchas
- **MSI deployers only** need to take action — EXE installer handles .NET 8 automatically
- Manual verification path: Control Panel → Programs → Programs and Features → look for ".NET 8 Desktop Runtime"
- If .NET 8 is absent, the client will silently fail to run — no graceful fallback

## Related Docs
- [Windows Client Deployment Documentation](https://www.twingate.com/docs/windows-client-deployment)
- [Twingate Client Download Page](https://www.twingate.com/download)
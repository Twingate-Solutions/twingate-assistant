# Windows Client Migration to .NET 8

## Summary
Twingate Windows Client migrated to .NET 8 in November 2024 following Microsoft's end of .NET 6 support. EXE installer handles the dependency automatically; MSI deployments require manual .NET 8 Desktop Runtime installation.

## Key Information
- Migration occurred in **early November 2024**
- EXE installer: automatically installs .NET 8 runtime as prerequisite — no admin action needed
- MSI installer: admins must separately deploy .NET 8 Desktop Runtime x64 to each device
- Without .NET 8 runtime, future client versions will **not run**

## Prerequisites
- .NET 8 Desktop Runtime x64 (MSI deployments only)
- Download from [Microsoft website](https://dotnet.microsoft.com)

## Step-by-Step (MSI Deployment)

1. Download .NET 8 Desktop Runtime x64 from Microsoft
2. Push via MDM solution or install manually
3. Use silent install flags (see below)
4. Verify installation on each device
5. Deploy updated Twingate Windows Client MSI as normal

## Configuration Values

**Silent install flags:**
```
c:\path\to\windowsdesktop-runtime-8.0.10-win-x64.exe /install /quiet /norestart
```

**PowerShell verification command:**
```powershell
Get-WmiObject -Query "SELECT * FROM Win32_Product WHERE Name LIKE '%.NET%Runtime%8.%.%'"
```

**Manual verification:** Control Panel → Programs → Programs and Features → look for `.NET 8 Desktop Runtime`

**Expected PowerShell output (if installed):**
```
IdentifyingNumber : {15B7D0C2-F209-4C28-AF1C-FD8326F4D58A}
Name              : Microsoft .NET Runtime - 8.0.10 (x64)
Vendor            : Microsoft Corporation
```

## Gotchas
- MSI deployments have **no automatic dependency handling** — runtime must be pre-installed before deploying new client versions
- Runtime must be **x64** specifically
- If runtime is missing, the client silently fails to run — no graceful degradation
- Filename in silent install example (`8.0.10`) may differ; use actual downloaded filename

## Related Docs
- [Windows Client deployment documentation](https://www.twingate.com/docs/windows-deployment)
- [Twingate Client download page](https://www.twingate.com/docs/client-downloads)
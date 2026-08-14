---
source: https://www.twingate.com/docs/windows-client-dotnet-8
type: docs
fetched: 2026-08-14
source_version: 3c6c7c89ce82f8d1430932dbf778b777bb50bd1e2c9bb813977f61d0e3555a9c
---

# Windows Client Migration to .NET 8

## Summary
Twingate Windows Client migrated to .NET 8 in November 2024 following Microsoft's end of support for .NET 6. EXE installer handles the dependency automatically; MSI deployments require manual .NET 8 Desktop Runtime installation.

## Key Information
- Migration occurred in **early November 2024** (November 12, 2024 was Microsoft's .NET 6 EOL date)
- **EXE installer**: Automatically installs .NET 8 Desktop Runtime — no admin action required
- **MSI installer**: Admins must manually deploy .NET 8 Desktop Runtime to each device
- Without .NET 8 Desktop Runtime, future Twingate Windows Client versions will **not run**

## Prerequisites
- .NET 8 Desktop Runtime x64 (for MSI deployments)
- Download from: [Microsoft website](https://dotnet.microsoft.com)
- Local or domain admin permissions for deployment

## Configuration Values

### Silent Install Flags (for remote/MDM deployment)
```
c:\path\to\windowsdesktop-runtime-8.0.10-win-x64.exe /install /quiet /norestart
```

## Step-by-Step (MSI Deployment)
1. Download .NET 8 Desktop Runtime x64 from Microsoft
2. Push runtime installer via MDM using silent install flags above
3. Verify installation on target devices (see verification methods below)
4. Deploy updated Twingate Windows Client MSI as usual

## Verification

**GUI:** Control Panel → Programs → Programs and Features → look for ".NET 8 Desktop Runtime"

**PowerShell:**
```powershell
Get-WmiObject -Query "SELECT * FROM Win32_Product WHERE Name LIKE '%.NET%Runtime%8.%.%'"
```
Expected output includes:
```
Name: Microsoft .NET Runtime - 8.0.10 (x64)
Vendor: Microsoft Corporation
```

## Gotchas
- MSI deployments have **no automatic dependency handling** — runtime must be pre-installed
- Skipping the runtime update will break **all future client versions**, not just new installs
- Use x64 variant specifically; ensure architecture matches device

## Related Docs
- [Twingate Windows Client download page](https://www.twingate.com/downloads)
- [Windows Client deployment documentation](https://www.twingate.com/docs/windows-client-deployment)
---
source: https://www.twingate.com/docs/windows-client-dotnet-10
type: docs
fetched: 2026-10-25
source_version: f54c5f3b6b8cb75129b0e49ae20b8fb6a5c4182f8c462227471933d4d87619c4
trust: official
---

# Windows Client Migration to .NET 10

## Summary
The Twingate Windows Client is migrating to .NET 10 in late October 2026, ahead of Microsoft ending .NET 8 support on November 10, 2026. EXE installer deployments handle the runtime automatically; MSI deployments require manual .NET 10 Desktop Runtime installation.

## Key Information
- **Migration date**: Late October 2026 (before .NET 8 EOL: November 10, 2026)
- **EXE installer**: Automatically installs .NET 10 Desktop Runtime — no admin action needed
- **MSI package**: Requires manual installation of .NET 10 Desktop Runtime on each device
- .NET 10 installs **side-by-side** with .NET 8; no uninstall required
- Clients older than 12 months are unsupported — plan migration promptly

## Prerequisites
- Windows devices currently running Twingate Windows Client
- For MSI deployments: access to MDM solution (e.g., Intune) or manual device access
- .NET 10 Desktop Runtime x64 — download from [Microsoft website](https://dotnet.microsoft.com)

## Step-by-Step (MSI Deployments Only)

1. Download `.NET 10 Desktop Runtime x64` from the Microsoft website
2. Deploy via MDM or install manually using silent install flags (see below)
3. Verify installation on each device
4. Continue deploying updated Twingate Windows Client MSI versions as released

## Configuration Values

**Silent install flags** (for remote/MDM deployment):
```
c:\path\to\windowsdesktop-runtime-10.0.x-win-x64.exe /install /quiet /norestart
```
Replace `10.0.x` with the actual version in the downloaded filename.

**Verify installation via PowerShell**:
```powershell
dotnet --list-runtimes | Select-String "Microsoft.WindowsDesktop.App 10\."
```
Expected output if installed:
```
Microsoft.WindowsDesktop.App 10.0.0 [C:\Program Files\dotnet\shared\Microsoft.WindowsDesktop.App]
```

**Verify via UI**: Settings → Apps → Installed Apps → look for `Microsoft Windows Desktop Runtime - 10.0.x (x64)`

## Gotchas
- **MSI deployments are not handled automatically** — runtime must be pushed separately before or alongside the updated client
- If .NET 10 runtime is absent, the new client version **will not launch** — .NET 8 alone is insufficient
- Existing .NET 8 client builds continue running while .NET 8 runtime is present, but receive **no further updates**
- If `dotnet` is not recognized in PowerShell, the runtime is definitively not installed

## Related Docs
- [Windows Managed Devices](https://www.twingate.com/docs)
- [Deploy the Windows Client with Microsoft Intune](https://www.twingate.com/docs)
- [Twingate Client Download Page](https://www.twingate.com/download)
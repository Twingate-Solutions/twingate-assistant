---
source: https://www.twingate.com/docs/windows-managed-devices
type: docs
fetched: 2026-08-14
source_version: b31ffe6a2ba7ca8e025320c9d2e5700e5163307b85141071488a9ab80c5bcbeb
---

# Windows Managed Devices

## Summary
Twingate Windows Client supports EXE and MSI deployment formats for MDM distribution. EXE includes .NET Runtime automatically (recommended); MSI requires manual .NET 8 Desktop Runtime installation. Both support identical command-line parameters for automated deployment.

## Key Information
- EXE package: includes .NET Runtime, recommended for MDM
- MSI package: requires separate .NET Desktop Runtime 8.0 (x64) installation
- Clients older than 12 months are unsupported and cannot connect
- Chocolatey package available but not on automated release pipeline (may lag)

## Prerequisites
- MSI only: [.NET 8.0 Desktop Runtime x64](https://dotnet.microsoft.com/download) must be pre-installed
- MDM solution (Intune, Endpoint Manager, or third-party)
- Twingate Network name (e.g., `company.twingate.com`)

## Configuration Values (Command Line Parameters)

| Parameter | Values | Description |
|-----------|--------|-------------|
| `/qn` | flag | Silent install, auto-accepts ToS |
| `network=` | `<name>.twingate.com` | Pre-configure network name |
| `auto_update=` | `true`/`false` | Reconnect after update without re-login |
| `no_optional_updates=` | `true`/`false` | Disable user-triggered updates |
| `ncsi_global_dns=` | `true`/`false` | Fix false "No internet" NCSI warnings |
| `TUN_DRIVER=` | `TunTap` (default) / `Wintun` | Select tunnel driver |

## Step-by-Step: Silent Deployment Example
```powershell
TwingateWindowsInstaller.exe /qn network=beamreach.twingate.com no_optional_updates=true auto_update=true
```
Running on existing installation performs in-place upgrade; `auto_update=true` restores existing session.

## Chocolatey Install
```powershell
choco install twingate
```

## Gotchas
- **`no_optional_updates` decision depends on local admin rights:**
  - Users WITH local admin → leave enabled (default); users get update prompts they can act on
  - Users WITHOUT local admin → set `no_optional_updates=true`; otherwise users see prompts they cannot fulfill
- MSI installations require manual .NET 8 Desktop Runtime — easy to miss in MDM packaging
- Chocolatey packages have delayed releases; not suitable for strict version management
- Clients >12 months old stop working — critical if disabling user-triggered updates; requires MDM push process

## Related Docs
- [Microsoft Intune & Endpoint Manager guide](https://www.twingate.com/docs/microsoft-intune)
- [Microsoft Intune custom PowerShell script guide](https://www.twingate.com/docs/microsoft-intune-custom-script)
- [User Terms of Service](https://www.twingate.com/docs/terms)
- [Public changelog](https://www.twingate.com/docs/changelog)
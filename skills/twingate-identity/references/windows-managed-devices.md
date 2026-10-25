---
source: https://www.twingate.com/docs/windows-managed-devices
type: docs
fetched: 2026-10-25
source_version: 1850e80182ad757d75b6903541366e42f1fc2bfd0b7846bef6742550f5a7372f
trust: official
---

# Windows Managed Devices

## Summary
Twingate Windows Client is available as EXE (recommended) or MSI packages for managed device deployment. EXE includes the .NET runtime automatically; MSI requires manual .NET runtime installation. Both support command-line parameters for silent/automated deployments via MDM solutions.

## Key Information
- **EXE**: Recommended — bundles required .NET Desktop Runtime, installs automatically
- **MSI**: Requires separate .NET runtime deployment before client installation
- Both formats support identical command-line parameters
- Clients older than 12 months are unsupported and cannot connect

## .NET Runtime Requirements
| Client Version | Required Runtime |
|---|---|
| November 2024 – October 22, 2026 | .NET 8.0 Desktop Runtime (x64) |
| October 22, 2026 onward | .NET 10 Desktop Runtime (x64) |

## Command-Line Parameters

| Parameter | Description |
|---|---|
| `/quiet` | Silent install; auto-accepts ToS |
| `network=<name>` | Pre-configures Twingate network (e.g., `beamreach.twingate.com`) |
| `auto_update=true` | Reconnects existing session after update |
| `no_optional_updates=true` | Disables user-triggered update prompts |
| `ncsi_global_dns=true` | Fixes false "No internet" NCSI warnings |
| `TUN_DRIVER=Wintun` | Use Wintun driver (default: TunTap) |

## Example Command
```
TwingateWindowsInstaller.exe /quiet network=beamreach.twingate.com no_optional_updates=true auto_update=true
```
Run on existing installation: performs in-place upgrade and restores session via `auto_update=true`.

## Prerequisites
- Windows device enrolled in MDM (Intune, Endpoint Manager, or third-party)
- MSI only: install appropriate .NET Desktop Runtime (x64) **before** deploying client

## Deployment Paths
1. **Microsoft Intune**: Follow [Intune & Endpoint Manager guide](https://www.twingate.com/docs) for dedicated instructions
2. **Third-party MDM**: Deploy EXE/MSI with above CLI flags per your MDM's software deployment docs
3. **Chocolatey** (Early Access — delayed releases): `choco install twingate`

## Gotchas
- **MSI + .NET 10**: Must pre-install .NET 10 runtime before rolling out October 2026+ client versions; EXE handles this automatically
- **`no_optional_updates=true` required** when users lack local admin rights — otherwise users see update prompts they cannot act on
- If disabling user-triggered updates, **establish an MDM push process**; clients >12 months old stop working
- Chocolatey packages may lag behind official releases (not in automated release pipeline)

## Downloads
- EXE (latest): https://www.twingate.com/downloads/windows (latest)
- MSI (latest): linked from Twingate downloads page
- .NET 10 Desktop Runtime (x64): Microsoft download center
- .NET 8.0 Desktop Runtime (x64): Microsoft download center
- [Public changelog](https://www.twingate.com/docs/windows-changelog)

## Related Docs
- Microsoft Intune & Endpoint Manager guide
- Intune custom PowerShell script guide
- Windows Client Migration to .NET 10
- User Terms of Service
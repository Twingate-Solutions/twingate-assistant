---
source: https://help.twingate.com/articles/9261433921-installation-of-the-windows-twingate-client-fails-with-setup-wizard-ended-prematurely
type: help
fetched: 2026-08-06
source_version: 86aca057ff5fcca15c65ce498393b22908e2fedcce79828332c86c84c00baaf4
---

# Windows Twingate Client: "Setup Wizard Ended Prematurely" Error

## Page Title
Installation of the Windows Twingate Client fails with: "Setup wizard ended prematurely."

## Summary
The Twingate Windows Client installation may fail and rollback with a "Setup wizard ended prematurely" error. Multiple root causes exist, addressable through a structured troubleshooting sequence. Log generation and CLI installation help narrow the cause.

## Key Information
- Affects all supported Windows OS versions
- EXE installer auto-installs required .NET runtime; MSI does not
- Silent installs require specific argument ordering with EXE installer

## Prerequisites
- Administrator access (CMD as Administrator required for repairs)
- Correct .NET Desktop Runtime if using MSI installer:
  - Version ≥ 2024.311 → **.NET 8.X Desktop Runtime**
  - Version ≤ 2024.297 → **.NET 6.X Desktop Runtime**

## Step-by-Step Troubleshooting

**Step 1: Generate verbose install log**
```
'[path]\TwingateWindowsInstaller.exe' /L*V "TGinstall.log"
```
Review `TGinstall.log` to identify root cause before proceeding.

**Step 2: Verify .NET Desktop Runtime (MSI installs only)**
- Confirm correct version is installed per the version table above

**Step 3: Repair WMI**
```cmd
mofcomp %windir%\system32\wbem\cimwin32.mof
```
Run as Administrator, then retry installation.

**Step 4: Disable MSI Rollback**
- Follow [Microsoft MSI DisableRollback instructions](https://learn.microsoft.com/en-us/windows/win32/msi/disablerollback)
- Restart, then reinstall

**Step 5: Remove errant Twingate registry entries**
1. Uninstall Twingate
2. Open `regedit`
3. Navigate to: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles`
4. Check each GUID key for `ProfileName` = `Twingate`
5. Delete all matching GUID keys
6. Restart, then reinstall

**Step 6: Check for OS corruption**
```cmd
sfc /scannow
```
Run as Administrator, restart, retry. Use CCleaner for severe corruption cases.

## Configuration Values

**Silent install with prerequisites (EXE only — order matters):**
```
TwingateWindowsInstaller.exe preq_share=true /quiet
```

**Verbose log generation:**
```
TwingateWindowsInstaller.exe /L*V "TGinstall.log"
```

## Gotchas
- MSI installer does **not** auto-install .NET runtime — must be pre-installed manually
- Silent install args must be in exact order: `preq_share=true` before `/quiet`
- Must use EXE (not MSI) for silent installs with prerequisite handling
- Registry cleanup requires full uninstall first, then GUID key removal before reinstall

## Related Docs
- [Microsoft: DisableRollback MSI property](https://learn.microsoft.com/en-us/windows/win32/msi/disablerollback)
- [Microsoft: System File Checker (sfc /scannow)](https://support.microsoft.com/en-us/topic/use-the-system-file-checker-tool-to-repair-missing-or-corrupted-system-files)
- CCleaner (for OS corruption remediation)
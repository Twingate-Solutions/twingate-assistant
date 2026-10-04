---
source: https://help.twingate.com/articles/9261433921-installation-of-the-windows-twingate-client-fails-with-setup-wizard-ended-prematurely
type: help
fetched: 2026-10-04
source_version: e72eec01a8126b5b9cbe28ef91867e60e0557befa0ba8283427d8b4ca3848a1e
trust: official
---

# Installation of Windows Twingate Client Fails: "Setup Wizard Ended Prematurely"

## Summary
The Twingate Windows Client installation may fail and roll back with a "Setup wizard ended prematurely" error. Multiple root causes exist, addressed through a progressive troubleshooting sequence. Log generation and CLI-based installation help narrow the cause.

## Key Information
- Affects: All supported Windows OS versions
- Component: Twingate Windows Client
- EXE installer auto-installs required .NET runtime; MSI does not
- Silent install requires specific argument order (see Configuration Values)

## Prerequisites
- Administrator access (CMD as Administrator required for most fixes)
- Correct .NET Desktop Runtime version for MSI installs:
  - **v2024.311+** → .NET 8.x Desktop Runtime
  - **v2024.297 and older** → .NET 6.x Desktop Runtime

## Step-by-Step Troubleshooting

**Step 1: Generate verbose install log**
```
'[path]\TwingateWindowsInstaller.exe' /L*V "TGinstall.log"
```
Review `TGinstall.log` to identify specific failure point.

**Step 2: Verify .NET Desktop Runtime (MSI only)**
Confirm correct version is installed per the version table above. EXE handles this automatically.

**Step 3: Repair WMI**
Open CMD as Administrator:
```
mofcomp %windir%\system32\wbem\cimwin32.mof
```
Retry installation.

**Step 4: Disable MSI Rollback**
Follow Microsoft guidance at: https://learn.microsoft.com/en-us/windows/win32/msi/disablerollback  
Restart, then reinstall.

**Step 5: Remove errant Twingate registry entries**
1. Open `regedit`
2. Navigate to: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles`
3. Inspect each GUID key for `ProfileName` = `Twingate`
4. Delete all matching GUID keys
5. Restart and reinstall

**Step 6: Check for OS corruption**
Open CMD as Administrator:
```
sfc /scannow
```
Restart and retry. CCleaner recommended for suspected severe OS corruption.

## Configuration Values

**Silent install with prerequisites (EXE only — argument order is mandatory):**
```
TwingateWindowsInstaller.exe preq_share=true /quiet
```

**Verbose log generation flag:** `/L*V`

## Gotchas
- MSI installer does **not** auto-install .NET; EXE does — wrong installer type is a common failure cause
- Silent install args must be in the exact order shown (`preq_share=true` before `/quiet`); wrong order causes failure
- Registry cleanup must be done **after** uninstalling Twingate, not before

## Related Docs
- [Microsoft: DisableRollback](https://learn.microsoft.com/en-us/windows/win32/msi/disablerollback)
- [Microsoft: System File Checker](https://support.microsoft.com/en-us/topic/use-the-system-file-checker-tool-to-repair-missing-or-corrupted-system-files-79aa86cb-ca52-166a-92a3-966e85d4094e)
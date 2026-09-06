---
source: https://help.twingate.com/articles/9261433921-installation-of-the-windows-twingate-client-fails-with-setup-wizard-ended-prematurely
type: help
fetched: 2026-09-06
source_version: be88c581b01564f2904221a60727a75e090f1ec280bb81daeef7161e2ea6f19f
---

# Windows Twingate Client: "Setup Wizard Ended Prematurely" Error

## Page Title
Installation of the Windows Twingate Client fails with: "Setup wizard ended prematurely."

## Summary
The Twingate Windows Client installation may fail and roll back with a "Setup wizard ended prematurely" error due to several possible causes including missing .NET runtime, WMI corruption, MSI rollback issues, or registry conflicts. Diagnostic logging and a structured troubleshooting sequence can isolate the root cause.

## Key Information
- Affects all supported Windows OS versions
- EXE installer auto-installs required .NET runtime; MSI does not
- Silent installs require specific argument order (see Configuration Values)

## Prerequisites
- Administrator access (CMD as Administrator required for most steps)
- Correct .NET Desktop Runtime for MSI installs:
  - Version ≥ 2024.311 → **.NET 8.X Desktop Runtime**
  - Version ≤ 2024.297 → **.NET 6.X Desktop Runtime**

## Step-by-Step Troubleshooting

**Step 1: Generate verbose install log**
```
'[path]\TwingateWindowsInstaller.exe' /L*V "TGinstall.log"
```
Review log to narrow down cause.

**Step 2: Validate .NET Desktop Runtime (MSI installs only)**
Install the correct version per the version table above.

**Step 3: Repair WMI**
```
mofcomp %windir%\system32\wbem\cimwin32.mof
```
Run as Administrator, then retry installation.

**Step 4: Disable MSI Rollback**
Follow [Microsoft's DisableRollback instructions](https://learn.microsoft.com/en-us/windows/win32/msi/disablerollback), restart, then reinstall.

**Step 5: Remove errant Twingate registry entries**
1. Uninstall Twingate
2. Open `regedit`
3. Navigate to: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles`
4. Click each GUID key, find entries with `ProfileName` = `Twingate`
5. Delete all matching GUID keys
6. Restart and reinstall

**Step 6: Check for OS corruption**
```
sfc /scannow
```
Run as Administrator, restart, then retry. Use CCleaner for suspected severe OS corruption.

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
- MSI installer does **not** auto-install .NET; EXE does
- Silent install args must be in exact order: `preq_share=true` before `/quiet`
- WMI repair and registry cleanup both require a **restart** before retrying installation
- Disabling MSI rollback requires a restart before reinstalling

## Related Docs
- [Microsoft DisableRollback](https://learn.microsoft.com/en-us/windows/win32/msi/disablerollback)
- [Microsoft SFC Tool](https://support.microsoft.com/help/929833)
- CCleaner (for OS corruption cases)
---
source: https://help.twingate.com/articles/9261433921-installation-of-the-windows-twingate-client-fails-with-setup-wizard-ended-prematurely
type: help
fetched: 2026-11-01
source_version: 7d4134631ed480d14f4071fe54ba39fc55d596a5e7a977cb39284927d3ce9c74
trust: official
---

# Windows Twingate Client: "Setup Wizard Ended Prematurely" Error

## Page Title
Installation of the Windows Twingate Client fails with: "Setup wizard ended prematurely."

## Summary
The Windows Twingate Client installer may fail and roll back with a "Setup wizard ended prematurely" error, caused by several possible issues including missing .NET runtime, WMI corruption, MSI rollback interference, or OS corruption. Reviewing install logs narrows down the root cause. Solutions escalate from runtime checks to registry cleanup.

## Key Information
- Affects: All supported Windows OS versions, Twingate Windows Client component
- EXE installer auto-installs the required .NET Desktop Runtime; MSI does not
- Silent installs require a specific argument order (see Configuration Values)

## Prerequisites
- Administrative (elevated CMD) access for most repair steps
- Correct .NET Desktop Runtime for MSI installs:
  - Version **2024.311+** → **.NET 8.x Desktop Runtime**
  - Version **2024.297 and older** → **.NET 6.x Desktop Runtime**

## Step-by-Step Troubleshooting (in order)

1. **Generate verbose install log** to identify root cause:
   ```
   '[path]\TwingateWindowsInstaller.exe' /L*V "TGinstall.log"
   ```

2. **Verify .NET Desktop Runtime** version matches client version (MSI installs only).

3. **Repair WMI** — open CMD as Administrator:
   ```
   mofcomp %windir%\system32\wbem\cimwin32.mof
   ```
   Retry installation after.

4. **Disable MSI rollback** — follow Microsoft docs at `https://learn.microsoft.com/en-us/windows/win32/msi/disablerollback`, then restart and reinstall.

5. **Remove errant registry NetworkProfile entries:**
   - Open `regedit`
   - Navigate to: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles`
   - Click each GUID key; delete any where `ProfileName` = `Twingate`
   - Restart and reinstall

6. **Check for OS corruption** — open CMD as Administrator:
   ```
   sfc /scannow
   ```
   Restart and retry. Use CCleaner for severe corruption cases.

## Configuration Values

| Scenario | Command/Value |
|---|---|
| Verbose install log | `TwingateWindowsInstaller.exe /L*V "TGinstall.log"` |
| Silent install with prerequisites | `TwingateWindowsInstaller.exe preq_share=true /quiet` |

> **Note:** For silent installs, `preq_share=true` **must precede** `/quiet` — argument order matters.

## Gotchas
- MSI installer does **not** auto-install .NET; EXE installer does
- Argument order for silent EXE install is mandatory; reversing order will cause issues
- Registry cleanup requires prior Twingate uninstall before reinstalling

## Related Docs
- [Microsoft: DisableRollback](https://learn.microsoft.com/en-us/windows/win32/msi/disablerollback)
- [Microsoft: System File Checker (sfc /scannow)](https://support.microsoft.com/en-us/topic/use-the-system-file-checker-tool-to-repair-missing-or-corrupted-system-files)
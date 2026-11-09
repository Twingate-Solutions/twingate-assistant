---
source: https://help.twingate.com/articles/3973356701-windows-client-freezes-after-clicking-join-network
type: help
fetched: 2026-11-08
source_version: 6b3871992cc704e1740e38796ce703bceea8ec6721b69842bbc59a76da17076c
trust: official
---

# [Windows Client] Freezes After Clicking Join Network

## Summary
The Twingate Windows client freezes at the "Join Network" step when the WMI (Windows Management Instrumentation) win32 repository is corrupt. The service cannot complete device posture checks required before authentication. Recompiling the WMI MOF file resolves the issue.

## Key Information
- **Affected component**: Twingate Windows Client — device posture check during network join
- **Root cause**: Corrupt WMI win32 repository (caused by improper shutdowns, BSODs, or application crashes)
- **Log file location**: `%LOCALAPPDATA%\Twingate\logs\Twingate.Service.log`
- **Error indicator in logs**: `CommunicationObjectFaultedException` during `RunPreconnectionChecks`
- **WMI failure stage**: `DevicePostureDataProvider.GenerateClientData`

## Symptoms
- Client UI freezes after clicking "Join Network"
- Errors appear in **Windows Event Viewer → Application**
- PowerShell WMI queries hang or return no data:
  ```powershell
  gwmi Win32_DISKDRIVE | select *
  ```

## Diagnostic Log Signature
Look for this sequence in `Twingate.Service.log`:
```
[DEBUG] DevicePostureDataProvider.GenerateClientData Start client posture data collection.
[ERROR] ServiceCommunication.RunPreconnectionChecks Communication faulted. System.ServiceModel.CommunicationObjectFaultedException
```

## Resolution

**Prerequisite**: Administrative command prompt (run as Administrator)

**Step 1** — Recompile the WMI win32 MOF file:
```cmd
mofcomp %windir%\system32\wbem\cimwin32.mof
```

**Step 2** — Verify WMI is working by running in PowerShell:
```powershell
gwmi Win32_DISKDRIVE | select *
```
If data returns, WMI is healthy.

**Step 3** — Retry joining the Twingate network.

## Gotchas
- Must run `mofcomp` from an **elevated** (Administrator) command prompt — it will silently fail or have no effect otherwise.
- WMI corruption can recur if underlying system stability issues (frequent BSODs, forced shutdowns) are not addressed.
- Errors in Windows Event Viewer → Application may point to WMI issues even if the Twingate log alone is ambiguous.

## Related Docs
- [Twingate Windows Client documentation](https://help.twingate.com)
- Microsoft: [WMI Troubleshooting](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmi-troubleshooting)
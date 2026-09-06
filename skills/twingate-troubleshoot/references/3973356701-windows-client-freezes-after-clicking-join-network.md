---
source: https://help.twingate.com/articles/3973356701-windows-client-freezes-after-clicking-join-network
type: help
fetched: 2026-09-06
source_version: 9797f9b5ae92cb2053b559156960c447392ce90bc2c7d8a67454616c587163f4
---

# [Windows Client] Freezes After Clicking Join Network

## Summary
The Twingate Windows client freezes during network join when the WMI (Windows Management Instrumentation) win32 repository is corrupt, preventing device posture checks from completing. The Twingate service requires WMI to collect system/hardware information before establishing a connection.

## Key Information
- **Affected component**: Windows Twingate client during initial network join
- **Root cause**: Corrupt WMI win32 repository (caused by improper shutdowns, BSODs, application crashes)
- **Log file location**: `%LOCALAPPDATA%\Twingate\logs\Twingate.Service.log`
- **Failure point**: `DevicePostureDataProvider.GenerateClientData` → `ServiceCommunication.RunPreconnectionChecks` faults

## Symptoms
- Client UI freezes after clicking "Join Network"
- Error in logs: `CommunicationObjectFaultedException` — service channel in Faulted state
- Twingate errors appear in **Windows Event Viewer → Application**
- PowerShell WMI queries fail to return data (e.g., `gwmi Win32_DISKDRIVE | select *`)

## Diagnostic Verification
Run in PowerShell to confirm WMI corruption:
```powershell
gwmi Win32_DISKDRIVE | select *
```
If this returns no data or errors, WMI is likely corrupt.

## Resolution

Run from an **administrative command prompt**:
```cmd
mofcomp %windir%\system32\wbem\cimwin32.mof
```
This recompiles the win32 MOF (Managed Object Format) within WMI.

## Gotchas
- Must run command prompt as **Administrator** — standard user privileges will not work
- WMI corruption can recur if underlying system stability issues (hardware faults, frequent crashes) are not addressed
- Check Windows Event Viewer Application logs for additional Twingate service errors if recompilation does not resolve the issue

## Related Docs
- [WMI documentation (Microsoft)](https://docs.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page)
- Twingate device posture configuration
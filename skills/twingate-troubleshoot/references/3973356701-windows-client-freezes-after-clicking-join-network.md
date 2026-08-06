---
source: https://help.twingate.com/articles/3973356701-windows-client-freezes-after-clicking-join-network
type: help
fetched: 2026-08-06
source_version: e8454691f44cd72802e1211653aa9c045e40de90918af55d7e92486e1cb24fdf
---

# [Windows Client] Freezes After Clicking Join Network

## Summary
The Twingate Windows client freezes at the "Join Network" stage due to a corrupted WMI (Windows Management Instrumentation) win32 repository. The service fails to complete device posture checks required before establishing a connection.

## Key Information
- **Affected component**: Twingate Windows Client
- **Log file location**: `%LOCALAPPDATA%\Twingate\logs\Twingate.Service.log`
- **Root cause**: Corrupt WMI win32 repository prevents hardware/OS identity verification
- **Common corruption triggers**: Improper shutdowns, BSODs, application crashes

## Symptoms
- Client UI freezes after clicking "Join Network"
- Log shows error: `CommunicationObjectFaultedException` during `RunPreconnectionChecks`
- Twingate errors appear in **Windows Event Viewer → Application**
- PowerShell WMI queries fail to return data (e.g., `gwmi Win32_DISKDRIVE | select *`)

## Diagnosis
Verify WMI is broken by running in PowerShell:
```powershell
gwmi Win32_DISKDRIVE | select *
```
If this returns no data or errors, WMI repository is corrupt.

## Resolution

**Recompile the WMI win32 MOF file from an administrative command prompt:**

```cmd
mofcomp %windir%\system32\wbem\cimwin32.mof
```

> **Requires**: Administrative command prompt (not PowerShell)

## Gotchas
- Must run from an **elevated/administrative** command prompt
- This recompiles the MOF (Managed Object Format) file specifically for the win32 namespace — it does not rebuild the entire WMI repository
- If the issue persists after recompiling, full WMI repository rebuild may be needed (not covered in this article)

## Related Docs
- [WMI Documentation (Microsoft)](https://docs.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page)
- Twingate Device Posture configuration
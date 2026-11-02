---
source: https://help.twingate.com/articles/3973356701-windows-client-freezes-after-clicking-join-network
type: help
fetched: 2026-11-01
source_version: 0c9829f7b73668e74982f8c82089f3b9f1c015810d62ebffd81131c0ba9e2d91
trust: official
---

# [Windows Client] Freezes After Clicking Join Network

## Summary
The Twingate Windows client freezes at "Join Network" when the WMI (Windows Management Instrumentation) win32 repository is corrupt, preventing device posture checks from completing. The fix is to recompile the corrupted MOF file from an administrative command prompt.

## Key Information
- **Affected component**: Twingate Windows Client
- **Log file location**: `%LOCALAPPDATA%\Twingate\logs\Twingate.Service.log`
- **Root cause**: Corrupt WMI win32 repository blocks device posture data collection
- **Error indicator in logs**: `CommunicationObjectFaultedException` during `RunPreconnectionChecks`
- **WMI corruption causes**: Improper shutdowns, BSODs, application crashes

## Symptoms
- Client UI freezes after clicking "Join Network"
- Log shows state reaching `Authenticating` then faulting at `RunPreconnectionChecks`
- Twingate errors appear in **Windows Event Viewer → Application**
- PowerShell WMI queries return no data:
  ```powershell
  gwmi Win32_DISKDRIVE | select *
  ```

## Prerequisites
- Administrative command prompt on the affected Windows machine

## Resolution

Run the following from an **elevated (Administrator) command prompt** to recompile the WMI win32 MOF file:

```cmd
mofcomp %windir%\system32\wbem\cimwin32.mof
```

## Diagnostic Steps
1. Check log file at `%LOCALAPPDATA%\Twingate\logs\Twingate.Service.log` for `CommunicationObjectFaultedException`
2. Verify WMI is broken by running `gwmi Win32_DISKDRIVE | select *` in PowerShell — no output confirms corruption
3. Check Windows Event Viewer → Application for Twingate errors
4. Run `mofcomp` fix above if WMI is confirmed broken

## Gotchas
- This issue is **OS-level**, not Twingate-specific — the WMI repository must be repaired before the client can function
- Reinstalling Twingate will **not** fix this; WMI must be repaired directly
- If `mofcomp` does not resolve the issue, a full WMI repository rebuild may be required (outside scope of this article)

## Related Docs
- [WMI (Windows Management Instrumentation) — Microsoft Docs](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page)
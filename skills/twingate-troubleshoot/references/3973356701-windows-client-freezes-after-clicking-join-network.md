---
source: https://help.twingate.com/articles/3973356701-windows-client-freezes-after-clicking-join-network
type: help
fetched: 2026-10-04
source_version: 362895118673ce6c4d15bed15b25f7d5c7940a7e8ecc793a5684eab33f19693c
trust: official
---

# [Windows Client] Freezes After Clicking Join Network

## Summary
The Twingate Windows client freezes at the "Join Network" step due to a corrupted WMI win32 repository preventing device posture checks from completing. The fix is to recompile the WMI MOF file from an administrative command prompt.

## Key Information
- Affected component: Windows Twingate Client during initial network join
- Root cause: Corrupt WMI (Windows Management Instrumentation) win32 repository
- WMI corruption sources: improper shutdowns, BSODs, application crashes
- The Twingate service uses the WMI win32 repository to collect device posture data required before authentication

## Symptoms
- Client UI freezes after clicking "Join Network"
- Log file at `%LOCALAPPDATA%\Twingate\logs\Twingate.Service.log` shows:
  - `DevicePostureDataProvider.GenerateClientData Start client posture data collection.`
  - `ServiceCommunication.RunPreconnectionChecks Communication faulted. System.ServiceModel.CommunicationObjectFaultedException`
  - State stuck at `Authenticating`
- Errors visible in Windows Event Viewer → Application log
- PowerShell WMI queries fail to return data (e.g., `gwmi Win32_DISKDRIVE | select *` returns nothing)

## Prerequisites
- Administrative command prompt (run as Administrator)

## Resolution Steps

1. Open Command Prompt as Administrator
2. Run the following command to recompile the WMI win32 MOF:
   ```cmd
   mofcomp %windir%\system32\wbem\cimwin32.mof
   ```
3. After completion, retry joining the Twingate network

## Verification
Before attempting the fix, confirm WMI is the issue by running this in PowerShell:
```powershell
gwmi Win32_DISKDRIVE | select *
```
If this returns no data or errors, WMI corruption is confirmed.

## Gotchas
- Must run from an **administrative** command prompt — standard user prompt will not work
- WMI corruption can recur if the underlying instability (e.g., hardware issues causing BSODs) is not addressed
- This affects only the Windows client; no Twingate network-side changes are needed

## Related Docs
- [WMI Overview (Microsoft)](https://docs.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page)
- Twingate Windows client logs: `%LOCALAPPDATA%\Twingate\logs\Twingate.Service.log`
---
source: https://help.twingate.com/articles/9526675912-windows-client-applications-report-no-internet-connection-while-twingate-is-connected
type: help
fetched: 2026-10-25
source_version: 15f29de639bc81d06e756411cc0299ede840025083b2f2434273ca8631cf90c1
trust: official
---

# [Windows Client] Applications Report No Internet Connection While Twingate Is Connected

## Summary
Certain Windows applications (Microsoft Store, Spotify) report no internet access while Twingate is connected because Windows NCSI marks the connection as local-only. NCSI's per-adapter DNS probe fails because Twingate blocks UDP DNS queries to non-Twingate resolvers. Enabling `UseGlobalDns` allows NCSI to use Twingate's resolver and succeed.

## Key Information
- Affected apps query Windows connectivity status before running; browsers and general traffic are unaffected
- Root cause: NCSI sends DNS probe per adapter; Twingate blocks UDP DNS to external servers (by design)
- Fix: `UseGlobalDns` registry policy lets NCSI resolve on any adapter, picking up Twingate's resolver
- This is a device-wide Windows policy change, not Twingate-specific; fully reversible

## Prerequisites
- Windows device with Twingate Client installed
- Elevated Command Prompt or PowerShell (Run as administrator)

## Diagnosis
Check Event Viewer: `Applications and Services Logs > Microsoft > Windows > NCSI > Operational`
- Look for **Event 4042**: `Capability: Local  ChangeReason: SuspectDnsProbeFailed`

## Step-by-Step (Single Device)

**1. Check if already set:**
```cmd
reg query "HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator" /v UseGlobalDns
```
Expected on most devices: `ERROR: The system was unable to find the specified registry key or value`

**2. Enable the setting:**
```cmd
reg add "HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator" /v UseGlobalDns /t REG_DWORD /d 1 /f
```

**3.** Relaunch affected application. If still failing, restart the device.

**4. To revert:**
```cmd
reg delete "HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator" /v UseGlobalDns /f
```

## Configuration Values

| Method | Key/Flag | Value |
|---|---|---|
| Registry | `HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator\UseGlobalDns` | `REG_DWORD = 1` |
| Installer flag (fleet) | `ncsi_global_dns=true` | Writes same registry value at install time |

## Fleet Deployment
Pass `ncsi_global_dns=true` to the Windows Client installer — applies the registry fix during installation. **Does not apply retroactively** to already-installed clients; those require the manual registry change above.

See: [Windows Managed Devices](https://help.twingate.com/articles/windows-managed-devices)

## Gotchas
- DNS queries targeting a **specific external DNS server** will still time out while Twingate is connected — this is expected behavior, not fixed by this setting
- Installer flag only applies **at install time**; existing deployments need the registry edit manually
- Change affects all connectivity detection on the device, not just Twingate sessions

## Related Docs
- [Using nslookup with Manually Defined Nameserver Fails on Windows with Twingate Client Running](https://help.twingate.com)
- [Microsoft ADMX_NCSI policy reference](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-admx-ncsi)
- [Windows Managed Devices](https://help.twingate.com/articles/windows-managed-devices)
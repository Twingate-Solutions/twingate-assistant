---
source: https://help.twingate.com/articles/9526675912-windows-client-applications-report-no-internet-connection-while-twingate-is-connected
type: help
fetched: 2026-09-27
source_version: 4e531cd106391f41fda99ee978a47fbebc186a46b256872033a4adcc48e2ed50
---

# [Windows Client] Applications Report No Internet Connection While Twingate Is Connected

## Summary
Certain Windows applications (Microsoft Store, Spotify) refuse to connect while Twingate is active because Windows NCSI marks the connection as local-only. Twingate blocks UDP DNS queries to non-Twingate resolvers per-adapter, causing NCSI's connectivity probe to fail. Enabling `UseGlobalDns` allows NCSI to use Twingate's resolver and resolve the false-offline state.

## Key Information
- Affected: Apps that query Windows connectivity status before running (Store, Spotify)
- Unaffected: Browsers, general DNS, Twingate Resources
- Root cause: NCSI sends DNS probe per-adapter; Twingate blocks UDP DNS to external resolvers
- Event Viewer indicator: `Applications and Services Logs > Microsoft > Windows > NCSI > Operational` → Event 4042, `Capability: Local ChangeReason: SuspectDnsProbeFailed`
- Fix is a standard Microsoft policy (`NCSI_GlobalDns`) — fully reversible

## Prerequisites
- Windows device with Twingate Client installed
- Elevated Command Prompt or PowerShell (Run as Administrator)

## Step-by-Step Resolution

**1. Check current state:**
```
reg query "HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator" /v UseGlobalDns
```
Expected on most devices: `ERROR: The system was unable to find the specified registry key or value`

**2. Enable global DNS for NCSI:**
```
reg add "HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator" /v UseGlobalDns /t REG_DWORD /d 1 /f
```

**3. Test the affected application.** If still failing, restart the device and retry.

**4. To revert:**
```
reg delete "HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator" /v UseGlobalDns /f
```

## Configuration Values

| Method | Value |
|--------|-------|
| Registry key | `HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator` |
| Registry value | `UseGlobalDns` (REG_DWORD = 1) |
| Installer flag (fleet) | `ncsi_global_dns=true` |

## Fleet Deployment
Use the Windows Client installer flag `ncsi_global_dns=true` to apply the registry value at install time — preferred for managed device deployments. **Only applies during installation**; existing installs require manual registry change above.

## Gotchas
- This change affects NCSI behavior device-wide, not just for Twingate
- DNS queries specifying an explicit external nameserver still time out while Twingate is connected — this remains expected behavior
- Devices with Twingate already installed must apply the registry fix manually; the installer flag does not retroactively apply

## Related Docs
- [Using nslookup with Manually Defined Nameserver Fails on Windows with Twingate Client Running](https://help.twingate.com)
- [Microsoft ADMX_NCSI policy reference](https://learn.microsoft.com)
- Windows Managed Devices deployment guide
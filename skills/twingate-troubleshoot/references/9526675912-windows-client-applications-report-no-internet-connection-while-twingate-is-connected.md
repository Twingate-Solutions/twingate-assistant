---
source: https://help.twingate.com/articles/9526675912-windows-client-applications-report-no-internet-connection-while-twingate-is-connected
type: help
fetched: 2026-10-04
source_version: 6f60959fe9b48f630f9ced1f336bd39df67d6b6a1e7d2d2be03fdb67c4dfabbb
trust: official
---

# [Windows Client] Applications Report No Internet Connection While Twingate Is Connected

## Summary
Certain Windows applications (Microsoft Store, Spotify) report no internet connection while Twingate is connected because Windows NCSI marks the connection as local-only. NCSI's DNS probe fails because Twingate blocks UDP DNS queries sent to servers other than its own resolver. Enabling `UseGlobalDns` allows NCSI to use Twingate's resolver and succeed.

## Key Information
- Affects apps that query Windows connectivity status before running (not browsers or general web traffic)
- Root cause: NCSI sends DNS probes per-adapter using that adapter's configured DNS server; Twingate drops non-Twingate DNS UDP traffic
- Diagnostic: Event 4042 in Event Viewer → `Applications and Services Logs > Microsoft > Windows > NCSI > Operational` with `Capability: Local  ChangeReason: SuspectDnsProbeFailed`
- Fix applies device-wide (not Twingate-specific); it's a standard Microsoft policy

## Prerequisites
- Windows device with Twingate Client installed
- Elevated Command Prompt or PowerShell (Run as Administrator)

## Step-by-Step (Single Device)

**1. Check if setting already exists:**
```
reg query "HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator" /v UseGlobalDns
```
`ERROR: The system was unable to find...` = not set (expected on most devices)

**2. Enable UseGlobalDns:**
```
reg add "HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator" /v UseGlobalDns /t REG_DWORD /d 1 /f
```

**3. Test the affected application.** If still failing, restart the device and retry.

**4. To revert:**
```
reg delete "HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator" /v UseGlobalDns /f
```

## Configuration Values

| Context | Key/Flag | Value |
|---|---|---|
| Registry path | `HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator` | — |
| Registry value | `UseGlobalDns` | `REG_DWORD = 1` |
| Installer flag (fleet) | `ncsi_global_dns=true` | Applied at install time only |

## Fleet Deployment
- Pass `ncsi_global_dns=true` to the Windows Client installer to write the registry value automatically during installation
- Devices already installed require the manual registry change above
- Reference: [Windows Managed Devices](https://help.twingate.com/articles/windows-managed-devices)

## Gotchas
- Installer flag only applies at install time; existing deployments need the registry fix applied separately
- DNS queries explicitly targeting an external nameserver (e.g., `nslookup example.com 8.8.8.8`) will still time out while Twingate is connected — this is expected behavior and is not fixed by this setting
- Change affects all connectivity detection on the device, not just Twingate connections

## Related Docs
- [Using nslookup with Manually Defined Nameserver Fails on Windows with Twingate Client Running](https://help.twingate.com/articles/using-nslookup-with-manually-defined-nameserver)
- [Microsoft ADMX_NCSI policy reference](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-admx-ncsi)
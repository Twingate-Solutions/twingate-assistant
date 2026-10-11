---
source: https://help.twingate.com/articles/9526675912-windows-client-applications-report-no-internet-connection-while-twingate-is-connected
type: help
fetched: 2026-10-11
source_version: ad2ccfdd265dccd0781cadef71a8ae29f6ebfef4bffe5d52876905662a1427f3
trust: official
---

# [Windows Client] Applications Report No Internet Connection While Twingate Is Connected

## Summary
Certain Windows applications (Microsoft Store, Spotify) report no internet while Twingate is connected because Windows NCSI marks the connection as local-only. NCSI's per-adapter DNS probe fails because Twingate blocks UDP DNS to non-Twingate resolvers. Enabling `UseGlobalDns` allows NCSI to use Twingate's resolver and succeed.

## Key Information
- Browsers, email, and general web traffic are **unaffected**; only apps that query Windows connectivity status before running break
- Root cause: NCSI sends DNS probes per-adapter; Twingate blocks UDP DNS to external servers (by design)
- Fix scope: Changes Windows-wide internet detection, not Twingate-specific; standard Microsoft policy, fully reversible
- After fix: External DNS queries targeting a specific nameserver still time out (expected Twingate behavior)

## Symptoms
- Microsoft Store: "you'll need the internet for this"
- Spotify: won't connect / stays offline
- Network icon shows limited/no internet
- Event Viewer → `Applications and Services Logs > Microsoft > Windows > NCSI > Operational` logs **Event 4042**: `Capability: Local ChangeReason: SuspectDnsProbeFailed`

## Prerequisites
- Elevated Command Prompt or PowerShell (Run as Administrator)

## Step-by-Step (Single Device)

**1. Check current state:**
```
reg query "HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator" /v UseGlobalDns
```
Expected on most devices: `ERROR: The system was unable to find the specified registry key or value`

**2. Enable the fix:**
```
reg add "HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator" /v UseGlobalDns /t REG_DWORD /d 1 /f
```

**3. Test** — reopen the affected application. If still broken, restart the device and retry.

**4. Revert (if needed):**
```
reg delete "HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator" /v UseGlobalDns /f
```

## Configuration Values

| Context | Value |
|---|---|
| Registry key | `HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator` |
| Registry value name | `UseGlobalDns` |
| Type | `REG_DWORD` |
| Enabled | `1` |
| Installer flag (fleet) | `ncsi_global_dns=true` |

## Fleet Deployment
Pass `ncsi_global_dns=true` to the Windows Client installer — writes the same registry value at install time. Applies **only during installation**; already-installed devices require the manual registry change above.

## Gotchas
- `ncsi_global_dns=true` installer flag does **not** retroactively fix existing installations
- External DNS queries specifying a non-Twingate nameserver will still time out while connected — this is expected and unchanged by this fix
- Microsoft policy reference: ADMX_NCSI `NCSI_GlobalDns`

## Related Docs
- [Using nslookup with Manually Defined Nameserver Fails on Windows with Twingate Client Running](https://help.twingate.com)
- [Windows Managed Devices](https://help.twingate.com)
- [Microsoft ADMX_NCSI policy reference](https://learn.microsoft.com)
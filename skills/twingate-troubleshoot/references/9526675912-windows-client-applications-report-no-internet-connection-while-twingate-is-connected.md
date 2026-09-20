---
source: https://help.twingate.com/articles/9526675912-windows-client-applications-report-no-internet-connection-while-twingate-is-connected
type: help
fetched: 2026-09-20
source_version: 2f015dc92f8725198b158462312a510e334acbe1c2385a8e04e835b4a113c82e
---

# [Windows Client] Applications Report No Internet Connection While Twingate Is Connected

## Summary
Certain Windows applications (Microsoft Store, Spotify) report no internet while Twingate is connected because Windows NCSI marks the connection as local-only. This occurs because Twingate blocks UDP DNS queries to non-Twingate resolvers, causing NCSI's per-adapter DNS probe to fail. Enabling `UseGlobalDns` allows NCSI to use Twingate's resolver and succeed.

## Key Information
- Affected apps check Windows network status before launching; browsers/email are unaffected
- Root cause: NCSI sends DNS probes per-adapter; Twingate blocks UDP DNS to external resolvers
- Diagnostic event: `Applications and Services Logs > Microsoft > Windows > NCSI > Operational` → Event 4042, `ChangeReason: SuspectDnsProbeFailed`
- Fix uses Microsoft's `NCSI_GlobalDns` policy (`UseGlobalDns` registry value)
- External DNS queries to specific servers still time out while Twingate is connected (expected behavior)

## Prerequisites
- Windows device with Twingate Client installed
- Elevated Command Prompt or PowerShell (Run as Administrator)

## Step-by-Step

**1. Check current state:**
```
reg query "HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator" /v UseGlobalDns
```
`ERROR: The system was unable to find...` = not set (normal).

**2. Enable fix:**
```
reg add "HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator" /v UseGlobalDns /t REG_DWORD /d 1 /f
```

**3. Test:** Reopen affected app. If still failing, restart device and retry.

**4. Revert (if needed):**
```
reg delete "HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator" /v UseGlobalDns /f
```

## Configuration Values

| Parameter | Type | Value | Context |
|---|---|---|---|
| `UseGlobalDns` | `REG_DWORD` | `1` | Registry key under `HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator` |
| `ncsi_global_dns=true` | Installer flag | `true` | Windows Client installer CLI flag for fleet deployment |

## Fleet Deployment
- Pass `ncsi_global_dns=true` to the Windows Client installer to apply the registry value at install time
- Applies **only during installation**; already-installed devices require manual registry fix above
- See: Windows Managed Devices documentation

## Gotchas
- This setting affects NCSI behavior device-wide, not only for Twingate
- Does **not** fix explicit external DNS queries (e.g., `nslookup` with manually specified nameserver) — those still fail while Twingate is connected
- `ncsi_global_dns=true` installer flag does not retroactively apply to existing installs

## Related Docs
- [Using nslookup with Manually Defined Nameserver Fails on Windows with Twingate Client Running](https://help.twingate.com)
- [Microsoft ADMX_NCSI policy reference](https://docs.microsoft.com)
- Windows Managed Devices (Twingate)
---
source: https://help.twingate.com/articles/9526675912-windows-client-applications-report-no-internet-connection-while-twingate-is-connected
type: help
fetched: 2026-10-18
source_version: 85b797ad1599be26c2fdbc89ef9e310aac270f15696e10422fda7d40ac406366
trust: official
---

# [Windows Client] Applications Report No Internet Connection While Twingate Is Connected

## Summary
Certain Windows applications (e.g., Microsoft Store, Spotify) report no internet access while Twingate is connected because Windows NCSI (Network Connectivity Status Indicator) marks the connection as local-only. Twingate blocks UDP DNS queries to non-Twingate resolvers per-adapter, causing NCSI's per-adapter DNS probe to fail. Enabling `UseGlobalDns` allows NCSI to resolve via Twingate's resolver instead.

## Key Information
- Browsers, general DNS, and Twingate Resources continue working normally
- Only apps that query Windows connectivity status before running are affected
- Disconnecting Twingate restores affected apps immediately
- Root cause: NCSI probes each adapter's DNS separately; Twingate blocks those UDP queries
- Fix is a standard Microsoft policy (`NCSI_GlobalDns`) — reversible at any time
- Affects the whole device's connectivity detection, not just Twingate

## Symptoms
- Microsoft Store: "you'll need the internet for this"
- Spotify: stays offline/won't connect
- Network icon may show limited/no internet
- Event Viewer → `Applications and Services Logs > Microsoft > Windows > NCSI > Operational` → **Event 4042**: `Capability: Local ChangeReason: SuspectDnsProbeFailed`

## Prerequisites
- Windows device with Twingate Client installed
- Elevated (Administrator) Command Prompt or PowerShell

## Step-by-Step (Single Device Fix)

1. **Check current state** (elevated prompt):
   ```
   reg query "HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator" /v UseGlobalDns
   ```
   - `ERROR: The system was unable to find...` = not set (expected on most devices)

2. **Enable the fix**:
   ```
   reg add "HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator" /v UseGlobalDns /t REG_DWORD /d 1 /f
   ```

3. **Test** the affected application. If still failing, restart the device and retry.

4. **Revert if needed**:
   ```
   reg delete "HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator" /v UseGlobalDns /f
   ```

## Configuration Values

| Method | Key/Flag | Value |
|--------|----------|-------|
| Registry | `HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator\UseGlobalDns` | `REG_DWORD = 1` |
| Installer flag (fleet) | `ncsi_global_dns=true` | Writes same registry value at install time |

## Fleet Deployment
- Use `ncsi_global_dns=true` with the Windows Client installer — preferred for fleet rollouts
- Applies **at install time only**; already-installed devices require the manual registry change above
- See: [Windows Managed Devices](https://help.twingate.com/articles/windows-managed-devices)

## Gotchas
- DNS queries targeting a specific external nameserver (e.g., `nslookup example.com 8.8.8.8`) still time out while Twingate is connected — this is expected behavior, not fixed by this change
- The registry fix affects NCSI behavior device-wide, not scoped to Twingate

## Related Docs
- [Using nslookup with Manually Defined Nameserver Fails on Windows](https://help.twingate.com/articles/using-nslookup-with-manually-defined-nameserver-fails-on-windows)
- [Microsoft ADMX_NCSI policy reference](https://learn.microsoft.com/en-us/windows/client-management/admx-ncsi)
- [Windows Managed Devices](https://help.twingate.com/articles/windows-managed-devices)
---
source: https://help.twingate.com/articles/9526675912-windows-client-applications-report-no-internet-connection-while-twingate-is-connected
type: help
fetched: 2026-11-19
source_version: 3273a7e4ef591ead31f16450749833f64cff2de699af4dba03b88ca260b7419f
trust: official
---

# Page Title
[Windows Client] Applications Report No Internet Connection While Twingate Is Connected

## Summary
Some Windows apps (Microsoft Store, Spotify) report being offline while the Twingate Client is connected, even though browsing and DNS work. Windows' NCSI connectivity check sends a DNS query per adapter to that adapter's DNS server, Twingate drops UDP DNS to non-Twingate resolvers, so Windows marks the connection "local only." Enabling the `UseGlobalDns` policy (NCSI_GlobalDns) fixes it.

## Key Information
- Applies to: Twingate Client, Windows.
- Symptoms: Microsoft Store says "you'll need the internet for this"; Spotify stays offline; network icon may show limited/no internet; browsers, DNS and Twingate Resources work; everything recovers when the Client is disconnected.
- Diagnostic: Event Viewer > Applications and Services Logs > Microsoft > Windows > NCSI > Operational, Event 4042: `Capability: Local  ChangeReason: SuspectDnsProbeFailed`.
- Cause: NCSI restricts DNS lookups to the interface being probed. Twingate intentionally does not deliver UDP DNS to servers other than its own resolver, so NCSI gets no reply.
- The fix lets NCSI resolve on any adapter, so it can use Twingate's resolver.
- The change is device-wide (it alters how Windows detects connectivity, not only for Twingate), is a standard Microsoft policy, and is reversible.

## Prerequisites
- Elevated Command Prompt or PowerShell (Run as administrator).

## Step-by-Step
1. Check whether the setting exists:
   `reg query "HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator" /v UseGlobalDns`
   (Typically returns "unable to find the specified registry key or value", meaning not set.)
2. Enable it:
   `reg add "HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator" /v UseGlobalDns /t REG_DWORD /d 1 /f`
3. Reopen the affected app. If it still reports no internet, restart the device and retry.

Revert:
`reg delete "HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator" /v UseGlobalDns /f`

## Configuration Values
- Registry key: `HKLM\Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator`
- Value: `UseGlobalDns` (REG_DWORD) = `1`
- Installer option: `ncsi_global_dns=true` (writes the same registry value)
- Microsoft policy name: NCSI_GlobalDns (ADMX_NCSI)

## Gotchas
- `ncsi_global_dns=true` applies only at install time. Devices with the Client already installed need the registry change (or a reinstall).
- The fix only corrects the Windows connectivity check. DNS queries (e.g., nslookup) that name a specific external DNS server will still time out while the Client is connected; this is expected behavior.
- A restart may be required for the change to take effect.

## Related Docs
- Using nslookup with Manually Defined Nameserver Fails on Windows with Twingate Client Running
- Windows Managed Devices (for fleet deployment with the installer option)
- Microsoft ADMX_NCSI policy reference
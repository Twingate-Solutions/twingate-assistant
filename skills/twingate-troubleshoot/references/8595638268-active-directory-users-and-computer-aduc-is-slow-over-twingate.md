---
source: https://help.twingate.com/articles/8595638268-active-directory-users-and-computer-aduc-is-slow-over-twingate
type: help
fetched: 2026-11-08
source_version: 68fdcc463f49eb87b68af5e7162831d7e92215fb1d73d5c9e4cc6cc5c6fbd358
trust: official
---

# Active Directory Users and Computers (ADUC) Slow Over Twingate

## Summary
ADUC opens slowly (tens of seconds to minutes) when the Twingate Client is running on Windows due to DNS timeout behavior. Windows queries DNS servers on all adapters in parallel; queries routed through Twingate's resolver never return to the physical adapter, causing Windows to wait out the full ~12-second timeout for each failed lookup. ADUC performs multiple non-existent-name lookups during domain controller discovery, stacking these timeouts.

## Key Information
- Affects: domain-joined Windows machines running Twingate Client, on or off corporate network
- Only failed/non-existent name lookups are slow; successful lookups return at normal speed
- Packet captures on the affected machine will show nothing (queries dropped below capture layer) — this is expected, not evidence against this cause
- Timeout is approximately 12 seconds per failed lookup; ADUC triggers multiple such lookups
- Other AD operations may also be affected: domain logon, Group Policy processing

## Prerequisites
- Windows machine running Twingate Client
- PowerShell access (elevated for Option 3)
- Active Directory domain name known

## Confirming the Cause
Run in PowerShell while Twingate Client is running (substitute your AD domain):
```powershell
ipconfig /flushdns
Measure-Command { Resolve-DnsName -Type SRV "_ldap._tcp.doesnotexist.example.local" -ErrorAction SilentlyContinue }
```
- `TotalSeconds` ≈ 12 → confirms this issue
- `TotalSeconds` well under 1 → different root cause

## Workarounds (Ordered by Ease)

### Option 1: Connect to Domain Controller Directly (Fastest, No Config Change)
```
dsa.msc /server="<domain controller IP>"
```
- Use IP address, not hostname, to avoid additional resolution
- May still show some delay in heavily nested or multi-domain environments

### Option 2: Use an Administrative/Jump Host (Recommended for Regular AD Admins)
- Run ADUC from a jumpbox on the same network as the AD domain
- Avoids the issue entirely; no per-machine configuration; aligns with Microsoft secure admin host guidance

### Option 3: NRPT Rule Pointing AD Namespace to Twingate DNS Proxy
Run in elevated PowerShell (replace namespace with your AD domain):
```powershell
Add-DnsClientNrptRule `
    -Namespace ".ad.example.com" `
    -NameServers "100.95.0.251","100.95.0.252","100.95.0.253","100.95.0.254" `
    -DisplayName "Twingate AD DNS"
```
Verify and test:
```powershell
Get-DnsClientNrptPolicy -Effective
ipconfig /flushdns
```
Remove rule when done:
```powershell
Get-DnsClientNrptRule | Where-Object { $_.DisplayName -eq "Twingate AD DNS" } | Remove-DnsClientNrptRule -Force
ipconfig /flushdns
```

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Twingate DNS proxy IPs | `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254` |
| NRPT namespace format | `.ad.example.com` (leading dot required) |

## Gotchas
- **NRPT rule has no fallback**: if Twingate Client is stopped/uninstalled, names under that namespace will not resolve at all, including on corporate network
- **Never scope NRPT rule to `"."`** — this applies to every lookup on the machine
- Remove NRPT rule when removing the Twingate Client
- Option 3 leaves persistent configuration that must be actively managed

## Related Docs
- [Using nslookup with Manually Defined Nameserver Fails on Windows with Twingate Client Running](https://help.twingate.com)
- [Microsoft guidance on secure administrative hosts](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/implementing-
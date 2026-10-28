---
source: https://help.twingate.com/articles/8595638268-active-directory-users-and-computer-aduc-is-slow-over-twingate
type: help
fetched: 2026-10-28
source_version: bcc81b8cfa61daa37ddb5a82612b9751758355a1ec541e3c6de9640963f2dca1
trust: official
---

# Active Directory Users and Computers (ADUC) Slow Over Twingate

## Summary
ADUC opens slowly (tens of seconds to minutes) when the Twingate Client is running on Windows. The root cause is Windows waiting for DNS timeouts (~12s each) on adapters managed by Twingate when ADUC queries non-existent hostnames during domain controller location. This is expected behavior, not a bug.

## Key Information
- Only affects DNS lookups that **fail to resolve** — successful lookups are unaffected
- ADUC's DC-location phase deliberately queries names expected not to exist, compounding the delay
- Failed queries don't appear in packet captures (dropped below capture layer) — a blank capture is consistent with this cause
- Other AD operations may also be slow: domain logon, Group Policy processing

## Prerequisites
- Windows domain-joined machine
- Twingate Client running
- PowerShell access (elevated for Option 3)

## Confirming the Cause
Run in PowerShell while Twingate Client is active:
```powershell
ipconfig /flushdns
Measure-Command { Resolve-DnsName -Type SRV "_ldap._tcp.doesnotexist.example.local" -ErrorAction SilentlyContinue }
```
- `TotalSeconds` ≈ 12 → confirms this issue
- `TotalSeconds` < 1 → different root cause

## Workarounds (Ordered by Speed of Implementation)

### Option 1: Connect to DC Directly (No Config Changes)
```
dsa.msc /server="<domain controller IP>"
```
- Use IP address, not hostname, to avoid additional resolution
- May still show some delay in multi-domain or heavily nested environments

### Option 2: Use an Administrative Host (Recommended for Regular AD Admins)
- Run ADUC from a jumpbox on the same network as the domain
- Eliminates the issue entirely; no per-machine config; aligns with Microsoft secure admin host guidance

### Option 3: NRPT Rule Pointing AD Namespace to Twingate DNS Proxy
Run in **elevated** PowerShell (replace namespace with your AD domain):
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
Remove when Client is uninstalled:
```powershell
Get-DnsClientNrptRule | Where-Object { $_.DisplayName -eq "Twingate AD DNS" } | Remove-DnsClientNrptRule -Force
ipconfig /flushdns
```

## Configuration Values
| Parameter | Value |
|---|---|
| Twingate DNS proxy IPs | `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254` |
| NRPT rule namespace format | `.ad.example.com` (leading dot required) |

## Gotchas
- **Option 3 has no fallback**: If Twingate Client is stopped/uninstalled, all names under the NRPT namespace will fail to resolve entirely, even on the corporate network
- **Never scope NRPT rule to `"."`** — this breaks all DNS on the machine when Client is offline
- Must remove the NRPT rule whenever the Twingate Client is removed
- Option 3 requires active management; Option 2 requires no per-machine config

## Related Docs
- [Using nslookup with Manually Defined Nameserver Fails on Windows with Twingate Client Running](https://help.twingate.com)
- [Microsoft guidance on secure administrative hosts](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/implementing-secure-administrative-hosts)
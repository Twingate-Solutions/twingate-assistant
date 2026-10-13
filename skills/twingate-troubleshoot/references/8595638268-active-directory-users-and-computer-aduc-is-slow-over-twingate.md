---
source: https://help.twingate.com/articles/8595638268-active-directory-users-and-computer-aduc-is-slow-over-twingate
type: help
fetched: 2026-10-11
source_version: fca4027b24af9d7abc74f914dc1f5e3266ad3793ef320b81308cd6d84e38897c
trust: official
---

# Active Directory Users and Computers (ADUC) Slow Over Twingate

## Summary
ADUC opens slowly (tens of seconds to minutes) when the Twingate Client is running on Windows because Windows waits for DNS timeouts (~12s each) on queries that the Client silently drops. This is expected behavior caused by how Windows handles parallel DNS resolution across multiple network adapters. The issue affects only failed DNS lookups; successful lookups return at normal speed.

## Key Information
- Root cause: Twingate Client handles DNS via its own resolver; queries to physical adapter DNS servers are dropped, causing Windows to wait out full ~12s timeout per failed lookup
- ADUC location phase deliberately queries non-existent names, multiplying the delay
- Affects domain logon and Group Policy processing too
- Dropped queries don't appear in packet captures on the affected machine (capture showing nothing is consistent with this cause)
- Applies to domain-joined Windows machines, on or off corporate network

## Prerequisites
- Twingate Client running on Windows
- Access to PowerShell (elevated for Option 3)
- Your Active Directory domain name

## Confirming the Cause
Run in PowerShell while Client is running (replace domain name):
```powershell
ipconfig /flushdns
Measure-Command { Resolve-DnsName -Type SRV "_ldap._tcp.doesnotexist.example.local" -ErrorAction SilentlyContinue }
```
- `TotalSeconds ≈ 12` → confirmed cause
- `TotalSeconds << 1` → different root cause

## Resolution Options

### Option 1: Connect to DC Directly (fastest, no config changes)
```
dsa.msc /server="<domain controller IP>"
```
Use IP address, not hostname. May not fully resolve heavily nested or multi-domain environments.

### Option 2: Use an Administrative Jumpbox (recommended for regular AD admins)
Run ADUC from a host on the same network as the domain. No per-machine config; aligns with Microsoft secure administrative host guidance.

### Option 3: NRPT Rule (most effective, leaves persistent config)
Run in elevated PowerShell — replace namespace with your AD domain:
```powershell
Add-DnsClientNrptRule `
  -Namespace ".ad.example.com" `
  -NameServers "100.95.0.251","100.95.0.252","100.95.0.253","100.95.0.254" `
  -DisplayName "Twingate AD DNS"

Get-DnsClientNrptPolicy -Effective
ipconfig /flushdns
```

**Remove rule when done:**
```powershell
Get-DnsClientNrptRule | Where-Object { $_.DisplayName -eq "Twingate AD DNS" } | Remove-DnsClientNrptRule -Force
ipconfig /flushdns
```

## Configuration Values
| Parameter | Value |
|---|---|
| Twingate DNS proxy IPs | `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254` |
| NRPT namespace format | `.ad.example.com` (leading dot required) |

## Gotchas
- **NRPT rule has no fallback**: if Client is stopped/uninstalled, all names under the scoped namespace fail to resolve, even on corporate network
- Never scope NRPT rule to `"."` — this breaks all DNS resolution when Client is not running
- Remove NRPT rule before uninstalling the Client
- Option 1 may still show some delay in multi-domain environments

## Related Docs
- [Using nslookup with Manually Defined Nameserver Fails on Windows with Twingate Client Running](https://help.twingate.com) (linked in source)
- Microsoft documentation on secure administrative hosts
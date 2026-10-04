---
source: https://help.twingate.com/articles/8595638268-active-directory-users-and-computer-aduc-is-slow-over-twingate
type: help
fetched: 2026-10-04
source_version: cc0180e5a67e7a20abf353ccfaa59c13ed6bc4805d8b64df7e69852b5b7fbb2d
trust: official
---

# Active Directory Users and Computers (ADUC) Slow Over Twingate

## Summary
ADUC opens slowly (tens of seconds to minutes) when the Twingate Client is running on Windows because ADUC's domain controller discovery phase sends DNS queries that time out on physical adapters the Client intercepts. Each failed lookup costs ~12 seconds, and multiple lookups compound the delay. This is expected behavior, not a bug.

## Key Information
- Affects: Domain-joined Windows machines running Twingate Client (on or off corporate network)
- Root cause: Windows queries all adapter DNS servers in parallel; Twingate intercepts physical adapter queries, causing timeouts (~12s each)
- Only **failed** lookups are slow; successful resolutions return immediately
- Packet captures on the affected machine will show nothing (queries are dropped below capture layer) — this is consistent with the cause
- ADUC's DC location phase issues multiple non-existent name queries, each timing out individually

## Prerequisites
- Windows with Twingate Client running
- Domain-joined machine or RSAT tools installed
- Elevated PowerShell for Option 3

## Confirming the Issue
Run in PowerShell while Twingate Client is active (replace domain name):
```powershell
ipconfig /flushdns
Measure-Command { Resolve-DnsName -Type SRV "_ldap._tcp.doesnotexist.example.local" -ErrorAction SilentlyContinue }
```
- **~12 seconds** → confirmed Twingate timeout behavior
- **< 1 second** → different root cause

## Workarounds (Ordered by Ease)

### Option 1: Direct DC Connection (No Config Changes)
```cmd
dsa.msc /server="<domain-controller-IP>"
```
Use an IP address, not hostname, to skip resolution. Fast to apply; may not fully resolve delays in multi-domain environments.

### Option 2: Administrative Jumpbox (Recommended for Regular Admins)
Run ADUC from a host on the same network as the AD domain. Aligns with Microsoft secure admin host guidance. No per-machine config required.

### Option 3: NRPT Rule (Most Effective, Persistent Config)
Add rule in elevated PowerShell (replace namespace with your AD domain):
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
Remove when done:
```powershell
Get-DnsClientNrptRule | Where-Object { $_.DisplayName -eq "Twingate AD DNS" } | Remove-DnsClientNrptRule -Force
ipconfig /flushdns
```

## Configuration Values (Option 3)
| Parameter | Value |
|-----------|-------|
| `-NameServers` | `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254` (Twingate DNS proxy) |
| `-Namespace` | Your AD domain with leading dot (e.g., `.ad.example.com`) |

## Gotchas
- **NRPT rules have no fallback**: If Twingate Client is stopped/uninstalled, names under the scoped namespace will fail to resolve entirely, including on corporate network
- **Never scope NRPT to `"."`** — this applies the rule to all lookups system-wide
- **Must remove the NRPT rule** when uninstalling the Twingate Client
- No Twingate Client setting can change the underlying timeout behavior

## Related Docs
- [Using nslookup with Manually Defined Nameserver Fails on Windows with Twingate Client Running](https://help.twingate.com) (same DNS interception behavior)
- [Microsoft secure administrative hosts guidance](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/implementing-secure-administrative-hosts)
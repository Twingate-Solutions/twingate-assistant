---
source: https://help.twingate.com/articles/8595638268-active-directory-users-and-computer-aduc-is-slow-over-twingate
type: help
fetched: 2026-10-18
source_version: 01e8932b9d96f8d361d1119e216175c2b819806ce2c5c722df21d83814324fd6
trust: official
---

# Active Directory Users and Computers (ADUC) Slow Over Twingate

## Summary
ADUC opens slowly when the Twingate Client is running because Windows queries DNS servers on all network adapters in parallel, and queries routed through Twingate's resolver time out (~12s each) for non-existent names. ADUC's domain controller discovery phase deliberately queries names expected not to exist, and each failed lookup incurs the full timeout. This is expected behavior, not a bug.

## Key Information
- Affects: domain-joined Windows machines with Twingate Client running
- Slowness occurs only on lookups with **no DNS record**; successful lookups return at normal speed
- Failed queries are dropped below packet-capture layer — empty packet captures are consistent with this cause, not evidence against it
- Symptoms may extend to domain logon and Group Policy processing, not just ADUC

## Prerequisites
- Twingate Client installed on Windows
- Domain-joined machine
- PowerShell (elevated for Option 3)

## Confirming the Cause
Run while Twingate Client is active (replace domain name):
```powershell
ipconfig /flushdns
Measure-Command { Resolve-DnsName -Type SRV "_ldap._tcp.doesnotexist.example.local" -ErrorAction SilentlyContinue }
```
- **~12 seconds** → confirmed Twingate DNS timeout cause
- **< 1 second** → different root cause

## Workarounds (Ordered by Speed to Implement)

### Option 1: Launch ADUC with Explicit Domain Controller IP
```cmd
dsa.msc /server="<domain controller IP>"
```
- Use IP address, not hostname, to avoid additional resolution
- No machine configuration changes; may not fully resolve multi-domain environments

### Option 2: Use an Administrative Jumpbox (Recommended for Regular AD Admins)
- Run ADUC from a host on the same network as the managed domain
- Eliminates the behavior entirely; no per-machine config; aligns with Microsoft secure admin host guidance

### Option 3: Add NRPT Rule Pointing AD Namespace to Twingate DNS Proxy
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
Measure-Command { Resolve-DnsName -Type SRV "_ldap._tcp.doesnotexist.ad.example.com" -ErrorAction SilentlyContinue }
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
| Timeout per failed lookup | ~12 seconds |

## Gotchas
- **NRPT rules have no fallback**: if the Twingate Client is stopped or disconnected, names under the scoped namespace will **not resolve at all**, even on the corporate network
- Never scope NRPT rule to `"."` — this applies the rule to every lookup on the machine
- Must remove the NRPT rule if the Twingate Client is uninstalled
- No Twingate Client setting exists to change this DNS timeout behavior

## Related Docs
- [Using nslookup with Manually Defined Nameserver Fails on Windows with Twingate Client Running](https://help.twingate.com) (referenced in article)
- [Microsoft guidance on secure administrative hosts](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/privileged-
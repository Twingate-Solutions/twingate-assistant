---
source: https://help.twingate.com/articles/8595638268-active-directory-users-and-computer-aduc-is-slow-over-twingate
type: help
fetched: 2026-10-25
source_version: c0408bd9c38f88f98e994d905b6cca879ad862821e2b53c4a42a88d8a23f2c8f
trust: official
---

# Active Directory Users and Computers (ADUC) Slow Over Twingate

## Summary
ADUC opens slowly (tens of seconds to minutes) when the Twingate Client is running on Windows due to DNS timeout behavior. Windows queries all network adapters' DNS servers in parallel; queries routed through the Twingate resolver don't return, causing ~12s timeouts per failed lookup. ADUC's domain controller discovery phase triggers multiple such lookups, compounding the delay.

## Key Information
- Only affects lookups that return **no record** — successful lookups are unaffected
- Each failed lookup incurs ~12 second timeout
- Packet captures on the affected machine will show nothing (queries dropped below capture layer) — this is expected, not evidence against this cause
- Twingate Client DNS resolver intercepts queries; physical adapter queries time out silently

## Prerequisites
- Windows domain-joined machine running Twingate Client
- PowerShell (elevated for Option 3)
- RSAT/ADUC (`dsa.msc`) installed

## Confirming the Cause

```powershell
ipconfig /flushdns
Measure-Command { Resolve-DnsName -Type SRV "_ldap._tcp.doesnotexist.example.local" -ErrorAction SilentlyContinue }
```
- **~12 seconds** → confirmed Twingate DNS timeout issue
- **< 1 second** → different root cause

## Workarounds (ordered by speed of implementation)

### Option 1: Connect directly to a domain controller (no config change)
```
dsa.msc /server="<domain controller IP>"
```
- Use IP address, not hostname, to avoid additional resolution
- May still have minor delays in multi-domain environments

### Option 2: Use an administrative/jump host (recommended for regular AD admins)
- Run ADUC from a host on the same network as the AD domain
- Eliminates the issue entirely with no per-machine config
- Aligns with Microsoft secure administrative host guidance

### Option 3: NRPT Rule (most effective, leaves persistent config)

**Add rule** (elevated PowerShell, replace namespace):
```powershell
Add-DnsClientNrptRule `
  -Namespace ".ad.example.com" `
  -NameServers "100.95.0.251","100.95.0.252","100.95.0.253","100.95.0.254" `
  -DisplayName "Twingate AD DNS"
```

**Verify:**
```powershell
Get-DnsClientNrptPolicy -Effective
ipconfig /flushdns
```

**Remove rule:**
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
- **NRPT rule has no fallback**: If the Twingate Client is stopped/uninstalled, names under the scoped namespace won't resolve at all — even on the corporate network
- **Never scope NRPT to `"."`** — this applies the rule to every DNS lookup on the machine
- **Must remove the NRPT rule** when uninstalling the Twingate Client
- Packet capture showing nothing is consistent with this issue, not a contradiction

## Related Docs
- [Using nslookup with Manually Defined Nameserver Fails on Windows with Twingate Client Running](https://help.twingate.com) (referenced in article)
- [Microsoft secure administrative hosts guidance](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/implementing-secure-administrative-hosts)
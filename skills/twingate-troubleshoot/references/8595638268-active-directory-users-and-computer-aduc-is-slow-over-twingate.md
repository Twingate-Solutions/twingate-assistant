---
source: https://help.twingate.com/articles/8595638268-active-directory-users-and-computer-aduc-is-slow-over-twingate
type: help
fetched: 2026-11-01
source_version: 9518c24ddbaf91794f5405dac9abca1fff454f61ae17b3bb838c83842de4678f
trust: official
---

# Active Directory Users and Computers (ADUC) Slow Over Twingate

## Summary
ADUC opens slowly (tens of seconds to minutes) when the Twingate Client is running on Windows because Windows queries DNS servers on all network adapters in parallel, and queries routed through Twingate's resolver time out (~12s each) for non-existent names. ADUC's domain controller discovery phase deliberately queries several non-existent names, causing cumulative delays. This is expected behavior, not a bug.

## Key Information
- Affects: domain-joined Windows machines with Twingate Client running (on or off corporate network)
- Only **failed** lookups are slow; successful resolutions return immediately
- Affects ADUC, domain logon, and Group Policy processing
- Packet captures on the affected machine will show nothing (queries are dropped below capture layer) — this is consistent with the issue, not evidence against it
- Timeout per failed query: ~12 seconds

## Prerequisites
- Windows machine running Twingate Client
- Active Directory domain name known
- PowerShell access (elevated for Option 3)

## Confirming the Cause

Run in PowerShell while Twingate Client is active:

```powershell
ipconfig /flushdns
Measure-Command { Resolve-DnsName -Type SRV "_ldap._tcp.doesnotexist.example.local" -ErrorAction SilentlyContinue }
```

- **~12 seconds** → confirms this issue
- **Under 1 second** → different root cause

## Workarounds (Ordered by Speed of Implementation)

### Option 1: Launch ADUC with Explicit Domain Controller (fastest, no config changes)
```
dsa.msc /server="<domain controller IP>"
```
Use IP address, not hostname, to avoid additional resolution. May not fully resolve delay in complex multi-domain environments.

### Option 2: Use an Administrative/Jump Host (recommended for regular AD admins)
Run ADUC from a host on the same network as the AD domain. No per-machine config; aligns with Microsoft secure administrative host guidance.

### Option 3: Add NRPT Rule to Route AD Namespace to Twingate DNS (most effective, leaves config)

**Add rule** (elevated PowerShell, replace namespace with your AD domain):
```powershell
Add-DnsClientNrptRule `
  -Namespace ".ad.example.com" `
  -NameServers "100.95.0.251","100.95.0.252","100.95.0.253","100.95.0.254" `
  -DisplayName "Twingate AD DNS"
```

**Verify and test:**
```powershell
Get-DnsClientNrptPolicy -Effective
ipconfig /flushdns
Measure-Command { Resolve-DnsName -Type SRV "_ldap._tcp.doesnotexist.ad.example.com" -ErrorAction SilentlyContinue }
```

**Remove rule** (required when uninstalling Twingate):
```powershell
Get-DnsClientNrptRule | Where-Object { $_.DisplayName -eq "Twingate AD DNS" } | Remove-DnsClientNrptRule -Force
ipconfig /flushdns
```

## Configuration Values (Option 3)
| Parameter | Value |
|---|---|
| `-NameServers` | `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254` |
| `-Namespace` | `.ad.example.com` (leading dot required; use your actual domain) |

## Gotchas
- **NRPT rule has no fallback**: if Twingate Client is stopped/uninstalled, names under the scoped namespace will not resolve at all, even on the corporate network
- **Never scope NRPT to `"."`** — this applies the rule to every DNS lookup on the machine
- Must **remove the NRPT rule** when removing the Twingate Client
- No Twingate Client setting can change the underlying timeout behavior

## Related Docs
- [Using nslookup with Manually Defined Nameserver Fails on Windows with Twingate Client Running](https://help.twingate.com) (referenced in article)
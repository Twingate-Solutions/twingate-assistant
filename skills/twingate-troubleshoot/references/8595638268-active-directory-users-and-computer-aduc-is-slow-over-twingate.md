---
source: https://help.twingate.com/articles/8595638268-active-directory-users-and-computer-aduc-is-slow-over-twingate
type: help
fetched: 2026-11-22
source_version: 68fdcc463f49eb87b68af5e7162831d7e92215fb1d73d5c9e4cc6cc5c6fbd358
trust: official
---

# Page Title
Active Directory Users and Computers (ADUC) is slow over Twingate

## Summary
ADUC (`dsa.msc`) can take tens of seconds to several minutes to open while the Twingate Client runs on domain-joined Windows machines. This is expected Windows DNS behavior, not a Client fault. Workarounds: connect to a DC directly, use an administrative host, or add an NRPT rule.

## Key Information
- Applies to: Twingate Client, Windows, domain-joined machines (on or off the corporate network).
- Symptoms: slow `dsa.msc` launch, slow container expansion or domain switching, possibly slow domain logon and Group Policy processing.
- Cause: the Client uses its own DNS resolver. Queries sent directly to the physical adapter's DNS servers do not complete while the Client runs. Windows queries all adapters in parallel and waits for every server to answer or time out (~12 seconds) before reporting a name doesn't exist.
- Only lookups with no record are affected. Successful lookups are normal speed.
- ADUC's DC-locator phase queries many names that don't exist, so the timeouts add up.
- Packet captures on the affected machine will show nothing, because the queries are dropped below the capture layer. This is consistent with the cause.
- No Client setting changes this behavior.

## Prerequisites
- Windows machine running the Twingate Client.
- Elevated PowerShell for Option 3.

## Step-by-Step

**Confirm the cause** (PowerShell, Client running):
```
ipconfig /flushdns
Measure-Command { Resolve-DnsName -Type SRV "_ldap._tcp.doesnotexist.example.local" -ErrorAction SilentlyContinue }
```
`TotalSeconds` ≈ 12 confirms it. Well under 1 second means another cause.

**Option 1: connect directly to a DC** (fastest, no machine changes):
```
dsa.msc /server="domain controller IP"
```
Prefer an IP over a hostname. Nested or multi-domain environments may still see some delay.

**Option 2: administrative host.** Run ADUC from a jumpbox on the same network as the domain. Recommended for regular AD admins. Requires no per-machine configuration.

**Option 3: NRPT rule** (most effective, leaves lasting config):
```
Add-DnsClientNrptRule `
    -Namespace ".ad.example.com" `
    -NameServers "100.95.0.251","100.95.0.252","100.95.0.253","100.95.0.254" `
    -DisplayName "Twingate AD DNS"
```
Verify:
```
Get-DnsClientNrptPolicy -Effective
ipconfig /flushdns
```
Then re-run the `Measure-Command` test against your own namespace. In testing, the lookup dropped from ~12 s to under 1 s.

Remove the rule:
```
Get-DnsClientNrptRule | Where-Object { $_.DisplayName -eq "Twingate AD DNS" } | Remove-DnsClientNrptRule -Force
ipconfig /flushdns
```

## Configuration Values
- `dsa.msc /server=<DC IP>`
- NRPT `-Namespace`: your AD domain with a leading dot (e.g. `.ad.example.com`)
- NRPT `-NameServers`: `100.95.0.251`–`100.95.0.254` (Client DNS proxy)
- NRPT `-DisplayName`: "Twingate AD DNS"

## Gotchas
- An NRPT rule is authoritative with no fallback. If the Client is stopped, uninstalled, or disconnected, names in that namespace will not resolve at all, even on the corporate network.
- Scope the rule to your AD domain only. Never use `"."`, which applies to every lookup.
- Remove the rule when the Client is removed.
- Empty packet captures do not rule out this cause.

## Related Docs
- Using nslookup with Manually Defined Nameserver Fails on Windows with Twingate Client Running (https://help.twingate.com/articles/4982245028-using-nslookup-with-manually-defined-nameserver-fails-on-windows-with-twingate-client-running)
- Microsoft's guidance on secure administrative hosts (https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/implementing-secure-administrative-hosts)
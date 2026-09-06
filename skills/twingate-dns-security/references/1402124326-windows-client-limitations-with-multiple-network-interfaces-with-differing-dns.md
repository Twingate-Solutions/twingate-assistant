---
source: https://help.twingate.com/articles/1402124326-windows-client-limitations-with-multiple-network-interfaces-with-differing-dns
type: help
fetched: 2026-09-06
source_version: 2936846a4d1347c4d0907a45a1268d11398e4df11ad146f774c6e000832f3732
---

# [Windows Client] Limitations with Multiple Network Interfaces with Differing DNS

## Summary
The Windows Twingate Client only uses DNS servers assigned to the system's default gateway interface for non-Twingate traffic resolution. Systems with multiple network interfaces, each with unique DNS servers, will experience failures when attempting to resolve hostnames that require a secondary interface's DNS servers.

## Key Information
- Twingate acts as a transparent DNS proxy but only for a single interface
- All non-Twingate DNS queries are forwarded exclusively to DNS servers on the **default gateway interface**
- Secondary interface DNS servers are completely ignored for non-Twingate traffic
- Backend hostnames/FQDNs resolvable only via a secondary interface's DNS will fail

## Prerequisites / Affected Environments
- Windows Twingate Client
- Systems with multiple network interfaces (e.g., separate frontend and backend interfaces)
- Each interface has distinct DNS servers accessible only through that specific interface

## Behavior Details
| Traffic Type | DNS Behavior |
|---|---|
| Twingate Resources | Resolved by Twingate directly |
| Non-Twingate (all) | Forwarded to default gateway interface DNS only |
| Secondary interface DNS | Never queried for any traffic |

## Workarounds

### Option 1: DNS Forwarding (Preferred)
Configure internal DNS servers to forward queries between frontend and backend DNS zones, so a single DNS server reachable from the default gateway interface can resolve both frontend and backend records.

### Option 2: Static hosts file entries
For backend resources with static IPs, manually add entries to:
```
C:\Windows\System32\drivers\etc\hosts
```
This bypasses DNS resolution entirely for those hostnames.

## Gotchas
- This is a **known limitation**, not a bug — multiple DNS configurations across interfaces are explicitly unsupported
- Even if backend DNS servers are technically reachable, Twingate will not route DNS queries to them if they are not on the default gateway interface
- The hosts file workaround only works for resources with **static IPs**; dynamic IPs require the DNS forwarding approach

## Related Docs
- Twingate Windows Client documentation
- Windows DNS configuration and interface management
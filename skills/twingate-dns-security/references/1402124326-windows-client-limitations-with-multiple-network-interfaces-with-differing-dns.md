---
source: https://help.twingate.com/articles/1402124326-windows-client-limitations-with-multiple-network-interfaces-with-differing-dns
type: help
fetched: 2026-11-01
source_version: 1c40938def8fa78422a9bee46f98f4d823c63cfd9022149a159129a4883bbf8d
trust: official
---

# [Windows Client] Limitations with Multiple Network Interfaces with Differing DNS

## Summary
The Windows Twingate Client only uses DNS servers assigned to the system's default gateway interface for non-Twingate traffic resolution. Systems with multiple network interfaces, each with separate DNS servers, will experience DNS resolution failures for resources on secondary interfaces.

## Key Information
- Twingate acts as a transparent DNS proxy but only for a single interface
- All non-Twingate DNS queries are forwarded exclusively to DNS servers on the **default gateway interface**
- Secondary interface DNS servers are ignored for non-Twingate traffic
- Backend hostnames/FQDNs resolvable only via a secondary interface's DNS will fail

## Prerequisites / Affected Environments
- Windows Twingate Client
- Systems with multiple network interfaces (e.g., separate frontend and backend NICs)
- Each interface has unique DNS servers not accessible from the other interface

## Workarounds

### Option 1: Consolidate DNS via Forwarding
Configure internal DNS servers to forward queries between frontend and backend DNS zones, so a **single DNS server** (reachable via the default gateway interface) handles all name resolution.

### Option 2: Static Hosts File Entries
For backend resources with static IPs, manually add entries to the Windows hosts file:
- **Path:** `C:\Windows\System32\drivers\etc\hosts`
- Bypasses DNS entirely for those hostnames

## Configuration Values
| Item | Value |
|------|-------|
| Hosts file path | `C:\Windows\System32\drivers\etc\hosts` |

## Gotchas
- This is a **known limitation**, not a bug — no client-side setting overrides this behavior
- DNS forwarding failures are silent from Twingate's perspective; troubleshoot by checking which interface holds the default gateway
- Hosts file workaround requires manual updates if backend IPs change

## Related Docs
- Twingate Windows Client documentation
- Windows DNS configuration and interface binding
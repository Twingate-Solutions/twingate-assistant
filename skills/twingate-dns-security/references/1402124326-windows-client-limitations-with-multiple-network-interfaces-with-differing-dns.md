---
source: https://help.twingate.com/articles/1402124326-windows-client-limitations-with-multiple-network-interfaces-with-differing-dns
type: help
fetched: 2026-08-06
source_version: a6193d3abf2c8691f10d961fddf232f0dd9de0ff2dd0e38c642ea90971b36c1f
---

# [Windows Client] Limitations with Multiple Network Interfaces with Differing DNS

## Summary
The Windows Twingate Client only uses DNS servers assigned to the system's default gateway interface for non-Twingate traffic resolution. Systems with multiple network interfaces using separate DNS servers per interface will experience DNS resolution failures for resources tied to non-default interfaces.

## Key Information
- Twingate acts as a transparent DNS proxy for a **single interface only**
- All non-Twingate DNS queries route to DNS servers on the **default gateway interface**
- Secondary interface DNS servers are never queried, regardless of configuration
- Backend hostnames/FQDNs resolvable only via secondary interface DNS will fail

## Prerequisites
- Affected environments: Windows systems with multiple NICs (e.g., frontend + backend interfaces)
- Each interface must have unique DNS servers assigned
- Issue occurs when backend DNS records are only accessible through a non-default interface

## Configuration Values
- Hosts file path: `C:\Windows\System32\drivers\etc\hosts`

## Workarounds

1. **DNS Forwarding (Preferred)**
   - Configure internal DNS servers to forward queries between frontend and backend DNS zones
   - Single DNS server on the default gateway interface handles all resolution
   - No client-side changes required

2. **Static Hosts File Entries**
   - Manually add backend resource IP/hostname mappings to `C:\Windows\System32\drivers\etc\hosts`
   - Bypasses DNS resolution entirely for those entries
   - Only viable if backend resources have static IPs

## Gotchas
- This is a **known limitation**, not a bug — no fix is implied
- Twingate-destined traffic is unaffected; only non-Twingate DNS resolution is impacted
- Hosts file workaround breaks if backend IPs change
- DNS forwarding workaround requires control over internal DNS infrastructure

## Related Docs
- Twingate Windows Client documentation
- Windows DNS configuration (multiple interface environments)
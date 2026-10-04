---
source: https://help.twingate.com/articles/1402124326-windows-client-limitations-with-multiple-network-interfaces-with-differing-dns
type: help
fetched: 2026-10-04
source_version: 2374150a16d1c575994fc1c2618a0780402cffbf6aaf4edade91719201e7fae8
trust: official
---

# [Windows Client] Limitations with Multiple Network Interfaces with Differing DNS

## Summary
The Windows Twingate Client only uses DNS servers assigned to the system's default gateway interface for non-Twingate traffic resolution. Systems with multiple network interfaces, each with unique DNS servers, are not supported. Backend DNS resolution may fail if those records are only resolvable via a secondary interface.

## Key Information
- Twingate acts as a transparent DNS proxy for a **single interface only**
- All non-Twingate DNS queries are forwarded exclusively to the DNS servers on the **default gateway interface**
- Secondary interface DNS servers are ignored for non-Twingate traffic
- Backend hostnames/FQDNs resolvable only via secondary interface DNS will fail to resolve

## Affected Configuration
- **Component:** Windows Client
- **Environment:** Multi-interface systems (e.g., separate frontend/backend NICs) where each interface has distinct, non-overlapping DNS servers

## Limitations
- Multiple DNS configurations (frontend DNS on one interface, backend DNS on another) are **not supported**
- No per-interface DNS routing for non-Twingate resources

## Workarounds

### Option 1: DNS Forwarding (Preferred)
Configure internal DNS servers to forward queries between frontend and backend DNS zones so a **single DNS server** (reachable via the default gateway interface) can resolve both frontend and backend records.

### Option 2: Hosts File (Static IPs Only)
If backend resources have static IPs, add entries manually to the Windows hosts file:
- **Path:** `C:\Windows\System32\drivers\etc\hosts`
- Ensures backend resources remain reachable even when their DNS servers are inaccessible through the default gateway interface

## Gotchas
- There is no client-side configuration to specify per-interface DNS routing; this is a fundamental architectural limitation
- Hosts file workaround only works for resources with **static IP addresses**; dynamic or load-balanced backends remain problematic
- The limitation applies specifically to **non-Twingate** traffic; Twingate-proxied resources use Twingate's own DNS resolution path

## Related Docs
- Twingate DNS resolution architecture
- Windows Client configuration
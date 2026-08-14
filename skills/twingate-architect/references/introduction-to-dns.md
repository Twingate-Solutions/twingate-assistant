---
source: https://www.twingate.com/docs/introduction-to-dns
type: docs
fetched: 2026-08-14
source_version: 6922fa3f489cb22cba73a72929b09e337904d852658c6fb3266aebd5623fc357
---

# Introduction to DNS

## Page Title
Introduction to DNS

## Summary
Conceptual overview of DNS mechanics for Twingate users. Covers how DNS translates human-readable names to IP addresses through a hierarchical resolution system. Provides foundational knowledge needed to understand how Twingate intercepts and handles DNS queries.

## Key Information

- **DNS resolution hierarchy**: Root Servers → TLD Servers → Domain Level Nameservers
- **Zonefile**: Text file containing all DNS records for a domain; lives on a DNS server
- **DNS Record Types**:
  - `A` — hostname to IPv4
  - `AAAA` — hostname to IPv6
  - `CNAME` — alias to another record
  - `MX` — mail server with priority
  - `PTR` — IP to hostname (Reverse DNS)
  - `SOA` — zone authority metadata (includes TTL/expiry)
  - `SRV` — service location
  - `TXT` — arbitrary data (SPF, verification codes)
- **TTL**: Per-record expiry override; controls cache invalidation speed
- **Twingate DNS Resolvers**: `100.95.0.251–100.95.0.254` (injected as resolver #1 when client is active)

## Prerequisites
- None (conceptual reference doc)

## Configuration Values

| Item | Value/Location |
|------|---------------|
| Hosts file (Unix) | `/etc/hosts` |
| Hosts file (Windows) | `C:\Windows\System32\drivers\etc\hosts` |
| Resolver config (Unix) | `/etc/resolv.conf` |
| View resolvers (macOS) | `scutil --dns` |
| View DNS cache (Windows) | `ipconfig /displaydns` |
| Twingate resolver IPs | `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254` |

## Gotchas

- `/etc/hosts` always takes precedence over DNS; only supports `A`-equivalent records (no MX, CNAME, etc.)
- DNS cache propagation delay is bounded by SOA expiry value — up to 24hrs if set that high
- On Unix/Linux, DNS caching is per-application (e.g., browser has its own cache); on Windows it's OS-level
- First four lines of `/etc/hosts` are auto-generated at boot — don't modify without knowing the impact
- Reverse DNS requires PTR records in the zonefile; not automatic from A records

## Reverse DNS Quick Reference
To reverse-lookup `22.33.44.55`:
1. Reverse octets: `55.44.33.22`
2. Append `.in-addr.arpa` → `55.44.33.22.in-addr.arpa`
3. Resolution follows same hierarchy via `arpa` → `in-addr.arpa` nameservers

## Related Docs
- [How DNS Works with Twingate](https://www.twingate.com/docs/dns-with-twingate) — explains why Twingate inserts its own resolver and how private DNS queries are handled
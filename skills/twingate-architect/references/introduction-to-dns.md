# Introduction to DNS

## Page Title
Introduction to DNS

## Summary
Conceptual overview of DNS mechanics for Twingate users. Covers how DNS translates human-readable names to IP addresses through a hierarchical resolution system. Provides foundation for understanding how Twingate intercepts and handles DNS queries.

## Key Information
- **DNS hierarchy**: Root Servers → TLD Servers → Domain Level Nameservers
- **Zonefiles**: Text files containing DNS records for a domain, stored on DNS servers
- **DNS record types**:
  - `A` — hostname to IPv4
  - `AAAA` — hostname to IPv6
  - `CNAME` — alias to another record
  - `MX` — mail server with priority
  - `PTR` — IP to hostname (reverse DNS)
  - `SOA` — zone authority/metadata
  - `SRV` — service location
  - `TXT` — arbitrary data (SPF, verification codes)
- **Twingate DNS resolvers**: `100.95.0.251–254` inserted as first resolver when client is active
- **Resolution order**: `/etc/hosts` → first resolver → subsequent resolvers (fallback chain)

## Prerequisites
- None (conceptual doc)

## Configuration Values
| Item | Value/Path |
|------|-----------|
| Unix hosts file | `/etc/hosts` |
| Windows hosts file | `C:\Windows\System32\drivers\etc\hosts` |
| Unix resolver config | `/etc/resolv.conf` |
| Twingate DNS resolvers | `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254` |
| View Mac resolvers | `scutil --dns` |
| View Windows DNS cache | `ipconfig /displaydns` |
| Default TTL field | `$TTL` in zonefile (seconds) |

## Gotchas
- `/etc/hosts` **always takes precedence** over DNS — use for per-machine overrides only
- `/etc/hosts` only supports `A`-record equivalents (IP-to-name), not full DNS record types
- DNS propagation delay is bounded by SOA expiry value (e.g., 24hr SOA = up to 24hr for changes to propagate)
- On Unix/Linux, DNS caching is **per-application** (e.g., browser cache); on Windows it's OS-level
- Twingate client inserts its resolvers **at the top** of the resolver list — relevant for split DNS behavior
- Reverse DNS requires `PTR` records and reverses octets + appends `in-addr.arpa` (e.g., `22.33.44.55` → `55.44.33.22.in-addr.arpa`)
- Don't modify the first 4 auto-generated lines of `/etc/hosts` (loopback/broadcast entries)

## Related Docs
- [How DNS Works with Twingate](https://www.twingate.com/docs/how-dns-works-with-twingate)
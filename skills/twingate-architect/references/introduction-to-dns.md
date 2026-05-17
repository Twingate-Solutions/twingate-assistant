# Introduction to DNS

## Page Title
Introduction to DNS

## Summary
Conceptual overview of DNS mechanics for Twingate users. Covers how DNS translates human-readable names to IP addresses through a hierarchical resolution system. Provides foundational knowledge needed to understand how Twingate intercepts and handles DNS queries.

## Key Information
- **DNS resolution hierarchy**: Root Servers → TLD Servers → Domain-Level Nameservers
- **Zonefiles**: Text files containing DNS records for a domain, stored on DNS servers
- **DNS record types**:
  - `A` — hostname to IPv4
  - `AAAA` — hostname to IPv6
  - `CNAME` — alias to another record
  - `MX` — mail server with priority
  - `PTR` — IP to hostname (Reverse DNS)
  - `SOA` — zone authority/metadata
  - `SRV` — service location
  - `TXT` — arbitrary data (SPF, verification)
- **Resolvers**: OS maintains ordered list; queries fall through sequentially until resolved
- **Twingate inserts its resolver first** (`100.95.0.25[1-4]`) when client is active
- **DNS caching**: Controlled by SOA expiry value and per-record TTL values
- **`/etc/hosts`** always takes precedence over DNS; supports only A-record equivalents

## Prerequisites
- None — purely conceptual/reference content

## Configuration Values
| Item | Value/Path |
|------|-----------|
| Twingate DNS resolver IPs | `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254` |
| Unix hosts file | `/etc/hosts` |
| Windows hosts file | `C:\Windows\System32\drivers\etc\hosts` |
| Unix resolver config | `/etc/resolv.conf` |
| Check resolvers (macOS) | `scutil --dns` |
| View DNS cache (Windows) | `ipconfig /displaydns` |
| Reverse DNS suffix | `<reversed-octets>.in-addr.arpa` |
| Default TTL field in zonefile | `$TTL <seconds>` |

## Gotchas
- `/etc/hosts` only supports A-record equivalents — cannot substitute full DNS
- First four lines of `/etc/hosts` are auto-generated at boot; don't modify them
- DNS cache propagation delay = up to the SOA expiry value (can be 24hrs+)
- Lower TTLs before DNS migrations to reduce propagation lag
- Unix DNS caching is per-application (e.g., browser cache); Windows caches centrally
- Private DNS records are not publicly resolvable — requires VPN/Twingate to reach

## Related Docs
- [How DNS Works with Twingate](https://www.twingate.com/docs/how-dns-works-with-twingate)
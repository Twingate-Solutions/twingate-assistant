# Introduction to DNS

## Page Title
Introduction to DNS

## Summary
Foundational reference explaining DNS concepts including resolution hierarchy, record types, zonefiles, and caching. Covers host-level DNS configuration (`/etc/hosts`, resolvers) and how Twingate inserts its own DNS resolver. Serves as prerequisite reading for understanding Twingate's DNS integration.

## Key Information

- **DNS purpose**: Translates human-readable names (e.g., `google.com`) to IP addresses and vice versa
- **Resolution hierarchy**: Root Servers → TLD Servers → Domain Level Nameservers (always top-down)
- **Twingate DNS resolvers**: `100.95.0.251–254` (injected as resolver #1 when Twingate Client is active)
- **`/etc/hosts` takes precedence** over DNS; supports only A record equivalents
- **DNS caching**: Unix = app-level (browser); Windows = OS-level (`ipconfig /displaydns`)
- **TTL** controls per-record cache expiry; SOA record sets zone-wide default expiry

## DNS Record Types

| Record | Purpose |
|--------|---------|
| `A` | Hostname → IPv4 |
| `AAAA` | Hostname → IPv6 |
| `CNAME` | Alias one record to another |
| `MX` | Mail server(s) with priority |
| `PTR` | IP → hostname (Reverse DNS) |
| `SOA` | Zone authority/metadata |
| `SRV` | Service location |
| `TXT` | Arbitrary data (SPF, verification) |

## Configuration Values

- **macOS resolver check**: `scutil --dns`
- **Windows DNS cache**: `ipconfig /displaydns`
- **Hosts file (Unix)**: `/etc/hosts`
- **Hosts file (Windows)**: `C:\Windows\System32\drivers\etc\hosts`
- **Default TTL field** in zonefile: `$TTL 3600` (seconds)

## Reverse DNS

- Reverse octets of IP → append `in-addr.arpa`
- Example: `22.33.44.55` → query `55.44.33.22.in-addr.arpa`
- Requires `PTR` records in zonefile

## Gotchas

- First 4 lines of `/etc/hosts` are auto-generated; do not modify without expertise
- DNS record updates can take up to the SOA expiry time (e.g., 24h) to propagate network-wide
- `/etc/hosts` cannot replace DNS — limited to A record equivalents only
- Multiple space-separated names on one `/etc/hosts` line all resolve to that IP
- Twingate Client adds its resolvers **at the top** of the OS resolver list, taking priority

## Related Docs

- [How DNS Works with Twingate](https://www.twingate.com/docs/how-dns-works-with-twingate)
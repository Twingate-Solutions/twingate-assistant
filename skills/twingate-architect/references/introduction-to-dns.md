# Introduction to DNS

## Page Title
Introduction to DNS

## Summary
Conceptual overview of DNS fundamentals for Twingate users. Covers how domain names resolve to IP addresses through hierarchical nameservers, DNS record types, zonefiles, caching/TTL mechanics, and private DNS. Serves as prerequisite reading for understanding Twingate's DNS integration.

## Key Information

- **DNS hierarchy**: Root Servers → TLD Servers → Domain Level Nameservers → IP address
- **Resolution order**: Always hierarchical, top-level down
- **Twingate DNS resolvers**: `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254` (inserted as highest-priority resolver when client is active)
- **Hosts file takes precedence** over DNS on all systems

## DNS Record Types

| Record | Purpose |
|--------|---------|
| `A` | Hostname → IPv4 |
| `AAAA` | Hostname → IPv6 |
| `CNAME` | Alias one name to another |
| `MX` | Mail server with priority |
| `PTR` | IP → hostname (Reverse DNS) |
| `SOA` | Zone authority/metadata |
| `SRV` | Service location |
| `TXT` | Arbitrary data (SPF, verification) |

## Configuration Files

- **Unix DNS resolver config**: `/etc/resolv.conf`
- **Unix hosts file**: `/etc/hosts`
- **Windows hosts file**: `C:\Windows\System32\drivers\etc\hosts`
- **Windows DNS cache view**: `ipconfig /displaydns`
- **macOS resolver inspection**: `scutil --dns`

## DNS Caching & TTL

- `$TTL` in zonefile = default cache duration (seconds) for all records
- SOA record `expiry` = max time clients cache the full zonefile
- Per-record TTL overrides SOA expiry
- **Unix**: caching typically at application level (per-browser)
- **Windows**: OS-level centralized DNS cache

## Reverse DNS

- Reverse octets of IP: `22.33.44.55` → `55.44.33.22`
- Append `in-addr.arpa`: `55.44.33.22.in-addr.arpa`
- Requires `PTR` records in zonefile

## Gotchas

- `/etc/hosts` only supports `A`-record equivalents; cannot replace full DNS
- First four lines of `/etc/hosts` are auto-generated; do not modify without understanding implications
- DNS record updates propagate slowly if SOA expiry/TTL is long (up to 24hrs)
- When Twingate client is active, its resolvers (`100.95.0.25x`) are prepended at highest priority — this is intentional for private resource resolution
- Multiple hostnames can map to one IP in `/etc/hosts` via space-separated names on one line

## Related Docs

- [How DNS Works with Twingate](https://www.twingate.com/docs/how-dns-works-with-twingate)
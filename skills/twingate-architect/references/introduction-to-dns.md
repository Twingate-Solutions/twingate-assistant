# Introduction to DNS

## Page Summary
Conceptual reference covering DNS fundamentals including resolution hierarchy, record types, zonefiles, resolvers, caching, TTLs, reverse DNS, and private DNS. Provides context for understanding how Twingate integrates with DNS. No configuration steps — pure reference material.

## Key Information

### DNS Resolution Hierarchy
1. **Root Servers** → handle TLD queries (`.com`, `.net`, `.org`)
2. **TLD Servers** → resolve second-level domain (`google` in `google.com`)
3. **Domain-Level Nameservers** → return actual IP for full address (`www.google.com`)

### DNS Record Types
| Record | Purpose |
|--------|---------|
| `A` | Hostname → IPv4 |
| `AAAA` | Hostname → IPv6 |
| `CNAME` | Alias one record to another |
| `MX` | Mail server with priority |
| `PTR` | IP → hostname (reverse DNS) |
| `SOA` | Zone authority + expiry metadata |
| `SRV` | Generic service location |
| `TXT` | Arbitrary data (SPF, verification) |

### Key Files (Unix)
- `/etc/hosts` — local DNS override, always takes precedence over DNS; supports only A-record equivalents
- `/etc/resolv.conf` — defines resolver list
- Windows hosts file: `C:\Windows\System32\drivers\etc\hosts`
- Windows DNS cache: `ipconfig /displaydns`

### Twingate Resolver Behavior
- With Twingate Client **off**: resolver points to router (e.g., `192.168.1.1`)
- With Twingate Client **on**: Twingate DNS resolvers (`100.95.0.251–254`) inserted as **first** in resolver list
- Mac diagnostic command: `scutil --dns`

## Caching & TTL
- **SOA record** sets default zone expiry (e.g., `$TTL 3600` = 1 hour)
- Individual records can override with per-record TTL values
- Unix: caching typically at **application level** (per-browser)
- Windows: OS-level centralized DNS cache
- DNS propagation delay = maximum TTL value on cached records

## Reverse DNS
- Resolves IP → hostname using `PTR` records
- Syntax: reverse IP octets + append `in-addr.arpa`
  - `22.33.44.55` → query `55.44.33.22.in-addr.arpa`

## Private DNS
- Internal DNS servers only accessible within private network
- Allows name resolution of private resources (e.g., `nas.home.int`) without public exposure
- Standard practice for corporate environments

## Gotchas
- `/etc/hosts` takes precedence over DNS — unintended entries cause resolution failures
- Don't modify the first 4 auto-generated lines in `/etc/hosts`
- High SOA TTLs cause slow propagation when records change — reduce TTL **before** making changes
- DNS caching layer varies by OS; flushing browser cache ≠ flushing OS DNS cache

## Related Docs
- [How DNS Works with Twingate](https://www.twingate.com/docs/how-dns-works-with-twingate)
# Introduction to DNS

## Page Title
Introduction to DNS

## Summary
Conceptual reference covering DNS fundamentals including resolution hierarchy, record types, zonefiles, and host-side configuration. Establishes foundational knowledge needed to understand how Twingate intercepts and handles DNS queries. Covers both forward and reverse DNS, caching/TTL mechanics, and private DNS concepts.

## Key Information

- **DNS hierarchy**: Root Servers → TLD Servers → Domain Level Nameservers → returns IP
- **Zonefile**: Text file containing all DNS records for a domain; lives on a DNS server
- **Resolver order**: OS maintains ordered list; queries fall through to next resolver on failure
- **Twingate inserts its own resolver** (`100.95.0.25[1-4]`) as resolver #1 when client is active
- **`/etc/hosts` always takes precedence** over DNS; supports only A-record equivalents
- **DNS caching** reduces network load; propagation delay determined by SOA expiry value
- **Private DNS**: Internal DNS servers expose hostnames only within private networks

## DNS Record Types

| Type | Purpose |
|------|---------|
| A | Hostname → IPv4 |
| AAAA | Hostname → IPv6 |
| CNAME | Alias one record to another |
| MX | Mail server with priority |
| PTR | IP → hostname (reverse DNS) |
| SOA | Zone authority metadata, expiry, serial |
| SRV | Service location (generic) |
| TXT | Arbitrary data (SPF, verification) |

## Configuration Files

- **`/etc/resolv.conf`** — Linux/macOS resolver configuration
- **`/etc/hosts`** — Local DNS override (Unix); `C:\Windows\System32\drivers\etc\hosts` (Windows)
- **`scutil --dns`** — macOS command to inspect active resolvers
- **`ipconfig /displaydns`** — Windows command to view DNS cache

## Gotchas

- `/etc/hosts` cannot replicate MX, CNAME, SRV, TXT records — A records only
- First four lines of `/etc/hosts` are auto-generated at boot; do not modify
- DNS cache propagation delay = SOA expiry value (up to 24hrs if set that way)
- Per-record TTLs override the SOA expiry on individual records
- Reverse DNS requires PTR records in zonefile; format: reverse octets + `.in-addr.arpa`
- Unix caches DNS at **application level** (per-browser); Windows caches centrally at OS level

## Related Docs

- [How DNS Works with Twingate](https://www.twingate.com/docs/how-dns-works-with-twingate) — explains why Twingate prepends its resolver
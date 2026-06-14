# Introduction to DNS

## Page Title
Introduction to DNS

## Summary
Conceptual overview of DNS mechanics for Twingate users. Covers how domain names resolve to IPs through hierarchical nameservers, DNS record types, zonefiles, caching/TTLs, and private DNS. Establishes foundational knowledge needed to understand how Twingate intercepts and routes DNS queries.

## Key Information

### DNS Resolution Hierarchy
1. Browser queries Root Server (handles TLD like `.com`)
2. Root Server returns TLD Server location
3. TLD Server returns Domain Level Nameserver location
4. Domain Level Nameserver returns actual IP(s)

### DNS Record Types
| Record | Purpose |
|--------|---------|
| A | Hostname → IPv4 |
| AAAA | Hostname → IPv6 |
| CNAME | Alias one record to another |
| MX | Mail server with priority |
| PTR | IP → hostname (reverse DNS) |
| SOA | Zone authority, serial, expiry |
| SRV | Service location (generic) |
| TXT | Arbitrary data (SPF, verification) |

### Twingate DNS Resolver
- With Twingate Client active, resolver `100.95.0.25[1-4]` is inserted as **first** resolver
- Default router resolver becomes second in chain
- See [How DNS Works with Twingate](https://www.twingate.com/docs/how-dns-works-with-twingate)

## Configuration Values

### Host Files
- **Linux/Mac**: `/etc/hosts`
- **Windows**: `C:\Windows\System32\drivers\etc\hosts`
- Takes **precedence over DNS**; supports only A-record equivalents

### resolv.conf / Resolvers
- Mac command to inspect resolvers: `scutil --dns`
- Windows DNS cache: `ipconfig /displaydns`
- OS maintains **ordered list**; queries fail over sequentially

### Zonefile Directives
- `$TTL` — default record expiry in seconds
- SOA record sets zone-wide expiry
- Per-record TTL overrides SOA expiry

## Gotchas

- `/etc/hosts` **cannot** replace DNS — only holds A-record equivalents
- First four lines of `/etc/hosts` are auto-generated on Unix; do not modify
- DNS cache propagation delay = up to the TTL/SOA expiry value (can be 24hrs+)
- On Unix, DNS caching is **per-application** (e.g., browser cache); on Windows it's OS-level
- Reverse DNS requires PTR records; format: reverse IP octets + `.in-addr.arpa`
- `www.example.com` resolving same as `example.com` is due to CNAME aliasing

## Private DNS
- Companies use DNS servers accessible only within private networks
- Private resources remain unresolvable from public internet
- Twingate leverages this pattern for resource access

## Related Docs
- [How DNS Works with Twingate](https://www.twingate.com/docs/how-dns-works-with-twingate)
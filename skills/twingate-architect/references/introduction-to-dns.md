# Introduction to DNS

## Page Title
Introduction to DNS

## Summary
Conceptual overview of DNS mechanics for Twingate users. Covers how DNS translates human-readable names to IP addresses through a hierarchical resolution system. Provides foundational knowledge needed to understand how Twingate intercepts and handles DNS queries.

## Key Information

**DNS Resolution Hierarchy:**
- Root Servers → TLD Servers → Domain Level Nameservers
- Resolution always flows top-level down
- Each level returns a pointer to the next, not the final IP

**DNS Record Types:**
| Type | Purpose |
|------|---------|
| A | Hostname → IPv4 |
| AAAA | Hostname → IPv6 |
| CNAME | Alias one record to another |
| MX | Mail server mapping |
| PTR | IP → hostname (Reverse DNS) |
| SOA | Zone authority/metadata |
| SRV | Service location (generic) |
| TXT | Arbitrary key/value data |

**Twingate DNS Behavior:**
- With Twingate Client active, inserts its own resolver first: `100.95.0.25[1-4]` (on `utun7`)
- Original resolver (e.g., router at `192.168.1.1`) becomes fallback
- See full behavior: [How DNS Works with Twingate](https://www.twingate.com/docs/dns)

## Configuration Values

- **Twingate DNS resolver IPs:** `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254`
- **Default TTL field in zonefile:** `$TTL <seconds>` (e.g., `3600`)
- **Reverse DNS suffix:** `<reversed-octets>.in-addr.arpa`

## Host-Side DNS Configuration

**Linux/Mac:**
- `/etc/hosts` — local overrides, takes precedence over DNS, A-record equivalent only
- `/etc/resolv.conf` — defines resolver order
- Check resolvers (Mac): `scutil --dns`

**Windows:**
- Hosts file: `C:\Windows\System32\drivers\etc\hosts`
- View DNS cache: `ipconfig /displaydns`

## Gotchas

- `/etc/hosts` always overrides DNS — useful for testing but easy to forget
- DNS caching means record updates can take up to the SOA expiry time to propagate network-wide
- Unix systems cache DNS at the application level (per-browser); Windows caches centrally
- Reduce TTL *before* a planned DNS change to speed propagation
- Private DNS records (e.g., `nas.home.int`) must be served by internal-only DNS servers — not publicly resolvable by design
- `www.example.com` resolving the same as `example.com` is due to a CNAME record, not automatic behavior

## Related Docs
- [How DNS Works with Twingate](https://www.twingate.com/docs/dns)
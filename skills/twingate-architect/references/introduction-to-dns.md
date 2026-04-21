## Page Title
Introduction to DNS

## Summary
Primer on DNS concepts for readers unfamiliar with the technology. Covers how domain names map to IP addresses, DNS record types (A, AAAA, CNAME, MX, PTR, SOA, TXT), zone files, resolvers, TTL/caching, and private DNS. Referenced by Twingate's DNS docs as prerequisite reading.

## Key Information
- **DNS purpose**: translates human-readable names (google.com) to machine-readable IPs (IPv4/IPv6)
- **Resolution hierarchy**: Root servers -> TLD servers -> Domain-level nameservers -> authoritative answer
- **Zone file**: text file of DNS records for a domain; hosted on a DNS server
- **Record types**:
  - `A` — hostname to IPv4
  - `AAAA` — hostname to IPv6
  - `CNAME` — alias to another name
  - `MX` — mail server for domain
  - `PTR` — reverse DNS (IP to name)
  - `SOA` — zone authority and expiry metadata
  - `TXT` — arbitrary text (SPF, verification tokens)
- **Resolvers**: OS maintains ordered list; first resolver queried, then fallback; Twingate prepends `100.95.0.251-254` when Client is active
- **TTL**: controls how long records are cached; reducing TTL before DNS changes speeds propagation
- **`/etc/hosts`** (`C:\Windows\System32\drivers\etc\hosts` on Windows): local override file, takes precedence over DNS; supports only A-equivalent records
- **Private DNS**: DNS servers accessible only within a private network; used to resolve internal FQDNs not publicly visible

## Prerequisites
None — introductory reference page.

## Step-by-Step
Not applicable.

## Configuration Values
- Twingate DNS resolvers (added when Client is active): `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254`

## Gotchas
- `/etc/hosts` always takes precedence over DNS — can mask DNS issues during troubleshooting
- DNS caching means record updates can take up to the SOA expiry to propagate; lower TTL in advance of planned changes

## Related Docs
- `/docs/how-dns-works-with-twingate` — how Twingate intercepts and proxies DNS
- `/docs/how-twingate-forwards-dns` — non-A record forwarding behavior
- `/docs/private-dns-best-practices` — private DNS configuration recommendations
- `/docs/supporting-unqualified-domain-names` — search domain / unqualified name resolution

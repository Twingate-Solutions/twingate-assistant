# Introduction to DNS

## Page Title
Introduction to DNS

## Summary
Conceptual overview of DNS fundamentals for Twingate users. Covers how DNS translates human-readable names to IP addresses through a hierarchical resolution system. Provides foundation for understanding how Twingate intercepts and handles DNS queries.

## Key Information

- **DNS resolution hierarchy**: Root Servers → TLD Servers → Domain Level Nameservers → IP address
- **Twingate DNS resolvers**: `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254` (inserted as first resolver when client is active)
- **DNS record types**:
  - `A` – hostname to IPv4
  - `AAAA` – hostname to IPv6
  - `CNAME` – alias to another record
  - `MX` – mail server
  - `PTR` – IP to hostname (Reverse DNS)
  - `SOA` – zone authority metadata
  - `SRV` – service location
  - `TXT` – arbitrary data (SPF, verification)
- **TTL** controls cache expiry per-record; SOA defines zone-wide default
- **Private DNS**: Internal DNS servers not publicly accessible; used by companies for private resource resolution

## Prerequisites
- None (conceptual/reference article)

## Configuration Values

| Item | Value/Path |
|------|-----------|
| Twingate DNS IPs | `100.95.0.25[1-4]` via `utun7` interface |
| Hosts file (Unix) | `/etc/hosts` |
| Hosts file (Windows) | `C:\Windows\System32\drivers\etc\hosts` |
| Resolver config (Unix) | `/etc/resolv.conf` |
| View DNS config (macOS) | `scutil --dns` |
| View DNS cache (Windows) | `ipconfig /displaydns` |

## Gotchas

- `/etc/hosts` always takes precedence over DNS; only supports A-record equivalents
- First 4 lines of `/etc/hosts` are auto-generated on Unix — do not modify
- DNS cache propagation delay = up to SOA expiry time (e.g., 24hr TTL = 24hr max propagation)
- On Unix/Linux, DNS caching is per-application (e.g., browser cache); on Windows it is OS-level
- Reverse DNS requires PTR records in zonefile; IP octets are reversed + `.in-addr.arpa` appended
- When Twingate client is active, its resolvers are prepended to the OS resolver list

## Related Docs
- [How DNS Works with Twingate](https://www.twingate.com/docs/how-dns-works-with-twingate)
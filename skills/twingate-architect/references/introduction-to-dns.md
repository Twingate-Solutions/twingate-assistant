# Introduction to DNS

## Page Title
Introduction to DNS

## Summary
Conceptual overview of DNS fundamentals including resolution hierarchy, record types, zonefiles, and caching. Explains how DNS translates human-readable names to IP addresses and introduces how Twingate integrates its own DNS resolver. Foundational reading before implementing Twingate DNS configuration.

## Key Information
- DNS resolution hierarchy: Root Servers → TLD Servers → Domain Level Nameservers
- **DNS Record Types:**
  - `A` – hostname to IPv4
  - `AAAA` – hostname to IPv6
  - `CNAME` – alias to another record
  - `MX` – mail server with priority
  - `PTR` – IP to hostname (Reverse DNS)
  - `SOA` – zone authority/metadata
  - `SRV` – service location
  - `TXT` – arbitrary data (SPF, verification)
- Twingate inserts its own resolver (`100.95.0.25[1-4]`) at the top of the OS resolver list when client is active
- `/etc/hosts` (Unix) / `C:\Windows\System32\drivers\etc\hosts` (Windows) takes precedence over DNS; supports only A-record equivalents
- DNS caching controlled by SOA expiry and per-record TTL values

## Configuration Values
- **Twingate DNS resolver IPs:** `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254` (interface: `utun7`)
- **Zonefile TTL field:** `$TTL 3600` (seconds; default expiry for all records)
- **SOA record format:** `( serial refresh retry expire minimum-ttl )`

## Gotchas
- `/etc/hosts` only supports A-record equivalents — cannot replace full DNS functionality
- DNS propagation delay equals the SOA expiry time (up to 24hrs if set that way); reduce TTL before planned IP changes
- On Unix/Linux, DNS caching is per-application (e.g., browser cache); on Windows it's OS-level (`ipconfig /displaydns`)
- First four lines of `/etc/hosts` are auto-generated at boot — do not modify unless intentional
- Reverse DNS requires PTR records in zonefile; uses reversed octets + `.in-addr.arpa` suffix

## Related Docs
- [How DNS Works with Twingate](https://www.twingate.com/docs/how-dns-works-with-twingate) — required follow-up for implementation details
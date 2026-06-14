# How DNS Works with Twingate

## Summary
Twingate uses a transparent proxy system where the Client intercepts DNS requests for defined Resources and resolves them to CGNAT IP addresses (100.64.0.0/10 range) instead of actual private IPs. DNS resolution for private resources is delegated to the Connector, which queries the private DNS server on behalf of the client. This architecture allows remote users to access private resources without VPN or direct private DNS resolver access.

## Key Information
- Twingate Client runs a local DNS resolver that intercepts queries for defined Resources
- Resources resolve to CGNAT range IPs (`100.96/12`), not actual private IPs
- Twingate DNS servers: `100.95.0.251–254`
- Client creates a virtual network interface (e.g., `utun7` on macOS) and modifies routing table to route CGNAT traffic through it
- Connector performs actual DNS resolution against private DNS server
- Destination host IP is never revealed to the client device
- Applies to both private DNS entries AND public DNS entries (connector still proxies resolution)
- Three proxy types handled: TCP, UDP, ICMP (ping only)
- Network traffic is encrypted client-side; Twingate cannot decrypt it

## Prerequisites
- Twingate Client installed on user device
- Connector deployed inside private network with access to private DNS server
- Resource defined in Twingate admin console as FQDN, IP, or CIDR

## DNS Resolution Flow (Step-by-Step)
1. App sends DNS request → OS → intercepted by Twingate Client's local DNS resolver
2. Client resolves FQDN to a CGNAT IP (e.g., `100.108.194.142`), not the actual private IP
3. App connects to CGNAT IP → Client's transparent proxy forwards to Connector
4. Connector queries private DNS server for the original FQDN
5. Private DNS returns actual private IP (e.g., `192.168.1.50`) to Connector
6. Connector initiates connection to private IP, proxying payload from Client

## Configuration Values
| Item | Value |
|------|-------|
| Twingate DNS servers | `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254` |
| CGNAT range used for Resource IPs | `100.96/12` |
| CGNAT broader allocation range | `100.64.0.0/10` |
| macOS network interface | `utun7` (example) |

## Gotchas
- **Public DNS resources still route through Connector** — even if a resource has a public DNS entry, resolution is overridden and proxied through the Connector
- **Client only intercepts defined Resources** — traffic to undefined FQDNs/IPs is ignored by Twingate
- **Routing table is modified on install** — all traffic to `100.96/12` is directed to Twingate's virtual interface
- **Source IP at destination is the Connector's IP**, not the client's IP — affects logging, firewall rules, and application access controls
- CGNAT IPs assigned to Resources are not persistent across sessions and are not related to actual resource IPs

## Related Docs
- [Twingate transparent proxy system](#)
- [DNS primer (external)](#)
- [CGNAT explanation](#)
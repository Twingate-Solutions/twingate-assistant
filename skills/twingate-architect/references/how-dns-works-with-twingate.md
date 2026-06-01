# How DNS Works with Twingate

## Summary
Twingate uses a transparent proxy system where the client intercepts DNS queries for defined Resources and resolves them to CGNAT IP addresses (100.64.0.0/10 range) locally, then proxies traffic through a Connector on the private network. The Connector performs actual DNS resolution against the private DNS server, keeping private IP addresses hidden from the client device.

## Key Information
- Twingate Client runs a local DNS resolver that responds to Resource FQDN queries with CGNAT-range IPs (not actual private IPs)
- DNS servers used by Twingate Client: `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254`
- CGNAT range used: `100.96/12` (subset of `100.64.0.0/10`)
- Client creates a virtual network interface (`utun7` on macOS) and modifies the local routing table to route CGNAT traffic through it
- The Connector performs actual DNS resolution against the private network's DNS server
- Actual private IP addresses are never revealed to the client device
- Traffic is encrypted client-side; Twingate cannot decrypt it
- Same flow applies to Resources with public DNS entries — resolution still goes through the Connector

## DNS Resolution Flow (Step-by-Step)
1. App sends DNS request → intercepted by Twingate Client's local DNS resolver
2. Client resolves FQDN to a CGNAT IP (e.g., `100.108.194.142`) — not the real private IP
3. App sends traffic to CGNAT IP → Twingate network interface intercepts via routing table
4. Client proxy strips source/destination, forwards payload to Connector
5. Connector queries private DNS server → gets actual private IP (e.g., `192.168.1.50`)
6. Connector reassembles packet with its own IP as source, private IP as destination
7. Return traffic flows back through Connector proxy → Client proxy → user application

## Configuration Values
| Item | Value |
|------|-------|
| Twingate DNS servers | `100.95.0.251–254` |
| CGNAT routing range | `100.96/12` |
| Network interface (macOS) | `utun7` |

## Client-Side Changes Made on Install
- Adds Twingate DNS resolvers as **primary** (top of resolver list)
- Creates virtual network interface
- Modifies routing table: all `100.96/12` traffic → Twingate interface
- Three proxies for TCP, UDP, and ICMP (ping only)

## Gotchas
- Resources must be resolvable **by the Connector**, not the client — the Connector must have network access to the private DNS server
- Client only intercepts FQDNs/IPs explicitly defined as Twingate Resources; other traffic passes through normally
- The assigned CGNAT IP is not the resource's real IP and changes — do not hardcode it
- Public DNS Resources are also routed through the Connector (overrides direct public DNS lookup from client)

## Related Docs
- [How DNS Works (primer)](https://www.twingate.com/docs/how-dns-works)
- [Transparent proxy system](https://www.twingate.com/docs/)
- [Resources documentation](https://www.twingate.com/docs/resources)
- CGNAT RFC (100.64.0.0/10 range)
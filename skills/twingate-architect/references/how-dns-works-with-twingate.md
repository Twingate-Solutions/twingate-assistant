# How DNS Works with Twingate

## Summary
Twingate uses a transparent proxy architecture where the Client intercepts DNS queries for defined Resources and resolves them to CGNAT IP addresses instead of actual private IPs. The Connector handles real DNS resolution on the private network, so clients never need direct access to private DNS resolvers.

## Key Information

- Twingate Client runs a local DNS resolver that intercepts queries for defined Resources
- Resources resolve to IPs in the `100.64.0.0/10` CGNAT range (specifically `100.96/12` for routing), not actual private IPs
- Twingate DNS servers: `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254`
- The Connector performs actual DNS resolution against the private DNS server
- Works for both private DNS entries and public DNS entries (resolution still routes through Connector)
- Client traffic is encrypted; Twingate cannot decrypt it
- Three proxies handle TCP, UDP, and ICMP (ping only)

## DNS Resolution Flow

1. App sends DNS query → intercepted by Twingate Client's local resolver
2. Client returns a CGNAT IP (e.g., `100.108.194.142`) mapped to the Resource
3. App sends traffic to CGNAT IP → Client routes via Twingate network interface (`utun7` on macOS)
4. Client proxy strips source/destination, forwards payload to Connector
5. Connector resolves the original FQDN against private DNS → gets actual private IP
6. Connector reassembles packet: source = Connector IP, destination = resolved private IP
7. Response travels back through Connector proxy → Client → application

## Client-Side System Changes

| Change | Detail |
|--------|--------|
| Network interface created | `utun7` (macOS) / visible in Windows Control Panel |
| Primary DNS resolver added | `100.95.0.251-254` prepended to resolver list |
| Routing table modified | All `100.96/12` traffic directed to Twingate interface |
| CGNAT IP mapping | Each Resource gets unique CGNAT IP assignment |

## Configuration Values

- **CGNAT range used**: `100.96/12` (routed to Twingate interface)
- **DNS resolver IPs**: `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254`
- **Twingate network interface IP** (macOS example): `172.16.30.1`

## Gotchas

- The CGNAT IP returned by Twingate DNS is **not** the Resource's actual IP — it's a proxy mapping
- Client only intercepts DNS for Resources it has explicit access to; other hostnames pass through normally
- Even Resources with **public DNS entries** route through the Connector (overrides direct public lookup)
- The Connector must be able to resolve the FQDN and route to the destination — if Connector can't resolve it, the connection fails
- Actual destination IP is never exposed to the client device (hidden behind proxy)

## Prerequisites

- Twingate Client installed on user device
- Twingate Connector deployed on private network with access to private DNS resolver
- Resource defined in Twingate admin console as FQDN, IP, or CIDR

## Related Docs

- [Twingate transparent proxy system](https://www.twingate.com/docs)
- [DNS basics primer](https://www.twingate.com/docs/how-dns-works)
- CGNAT RFC (shared `100.64.0.0/10` range)
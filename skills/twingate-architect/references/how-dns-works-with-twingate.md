# How DNS Works with Twingate

## Summary
Twingate uses a transparent proxy system where the Client intercepts DNS requests for defined Resources and returns CGNAT-range IP addresses instead of actual private IPs. The Connector handles real DNS resolution on the private network, keeping internal IP addresses hidden from client devices. This allows access to private FQDNs without users needing direct access to private DNS resolvers.

## Key Information
- Twingate Client runs a local DNS resolver that intercepts queries for defined Resources
- Resources resolve to IPs in the `100.64.0.0/10` CGNAT range (specifically `100.96/12` for routing), not actual private IPs
- Twingate DNS servers: `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254`
- Client adds itself as the **primary** DNS resolver on the device (above existing resolvers)
- Client creates a virtual network interface (e.g., `utun7` on macOS)
- Client modifies local routing table so all `100.96/12` traffic routes through Twingate interface
- Connector performs actual DNS resolution against the private DNS server
- Actual destination IP is never exposed to the client device
- Flow applies equally to Resources with **public** DNS entries — resolution still goes through the Connector

## DNS Resolution Flow
1. App sends DNS request → OS → intercepted by Twingate Client DNS resolver
2. Client returns a CGNAT IP (e.g., `100.108.194.142`) mapped to the Resource
3. App connects to CGNAT IP → Client transparent proxy forwards to Connector
4. Connector queries private DNS server → receives actual private IP (e.g., `192.168.1.50`)
5. Connector assembles new packets with its own IP as source, private IP as destination
6. Return traffic reverses: Connector → Client proxy → app

## Configuration Values
| Item | Value |
|------|-------|
| CGNAT DNS resolver IPs | `100.95.0.251–254` |
| CGNAT routing range | `100.96/12` |
| IP assignment pool | `100.64.0.0/10` |
| macOS DNS check command | `scutil --dns` |
| Routing table check | `netstat -rn \| grep utun7` |
| DNS resolution test | `dig <resource-fqdn>` |

## Protocols Proxied
- TCP
- UDP  
- ICMP (ping only)

## Gotchas
- The CGNAT IP assigned to a Resource is **not** the Resource's actual private IP — don't use it for direct routing
- With Client ON, `dig` will show CGNAT IP and `100.95.0.251` as DNS server — this is expected behavior
- Client must have permission to modify routing tables and DNS resolver order on the device
- Connector must be able to resolve the FQDN and reach the destination — if Connector can't resolve it, the connection fails
- Traffic is encrypted client-side; Twingate cannot decrypt it in transit

## Related Docs
- [Twingate transparent proxy system](#)
- [Resources documentation](#)
- [DNS primer (external)](#)
- [CGNAT overview (external)](#)
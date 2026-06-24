# How DNS Works with Twingate

## Summary
Twingate uses a transparent proxy system where the Client intercepts DNS queries for defined Resources and resolves them to CGNAT IP addresses (100.64.0.0/10), routing traffic through a Connector that performs actual private DNS resolution. User devices never join the private network and never need direct access to private DNS resolvers.

## Key Information

- Twingate Client runs a local DNS resolver that intercepts queries for defined Resources
- Resources resolve to CGNAT range IPs (`100.96/12`), not actual private IPs
- Twingate DNS servers: `100.95.0.251–254` (added as primary resolvers on the device)
- Client creates a virtual network interface (`utun7` on macOS) and modifies the routing table to route all CGNAT traffic through it
- The Connector performs actual DNS resolution against the private DNS server and proxies traffic to the real destination IP
- Actual destination IPs are never revealed to the client device
- Supports three protocols via separate proxies: TCP, UDP, ICMP (ping only)
- Network traffic is encrypted client-side; Twingate cannot decrypt it

## DNS Resolution Flow

1. App sends DNS request → intercepted by Twingate Client's local DNS resolver
2. Client returns a CGNAT IP (e.g., `100.108.194.142`) mapped to the Resource
3. App sends traffic to CGNAT IP → routed via Twingate virtual interface
4. Client proxy strips source/destination, forwards payload to Connector
5. Connector resolves original FQDN against private DNS server → gets real private IP
6. Connector reassembles packet (source: Connector IP, destination: real private IP) and sends to Resource
7. Return traffic reverses: Connector strips and forwards payload back to Client

## Configuration Values

| Value | Purpose |
|-------|---------|
| `100.95.0.251–254` | Twingate DNS resolver IPs (added as primary) |
| `100.96/12` (100.64.0.0/10 CGNAT) | IP range used for Resource address mapping |
| `utun7` | Twingate virtual network interface (macOS) |

## Verification Commands

```bash
# Check DNS resolution with Client on vs off
dig nas.home.int

# Verify DNS resolver configuration (macOS)
scutil --dns

# Check routing table entries for Twingate interface
netstat -rn | grep utun7
```

## Gotchas

- Resources defined as FQDNs resolve differently depending on Client state — CGNAT IP when Client is ON, real private IP when OFF on local network
- Same DNS interception flow applies to Resources with **public** DNS entries — resolution still passes through the Connector, overriding direct public DNS lookup
- Client only intercepts DNS for explicitly defined Resources; undefined FQDNs pass through normally
- Connector must be able to both resolve the FQDN via private DNS **and** route traffic to the destination for the connection to succeed

## Related Docs

- [DNS Primer](https://www.twingate.com/docs/how-dns-works) (linked in page)
- [Transparent Proxy System](https://www.twingate.com/docs/)
- [CGNAT Overview](https://en.wikipedia.org/wiki/Carrier-grade_NAT)
- Twingate Resources configuration docs
# How DNS Works with Twingate

## Summary
Twingate uses a transparent proxy system where the client intercepts DNS queries for defined Resources and resolves them to CGNAT IP addresses (100.64.0.0/10 range) rather than actual private IPs. The Connector performs the actual private DNS resolution on the internal network, keeping destination IPs hidden from client devices. This eliminates the need for users to have direct access to private DNS resolvers or private network routing.

## Key Information
- Twingate Client runs its own DNS resolver that intercepts queries for defined Resources
- Resources resolve to CGNAT range IPs (100.96.0.0/12) on the client, not actual private IPs
- Twingate DNS servers: `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254`
- Client creates a virtual network interface (e.g., `utun7` on macOS) and modifies the routing table
- Connector performs actual DNS resolution against the private DNS server
- Works for both private DNS entries and public DNS entries (Connector still resolves, overriding client-side public lookup)
- Three proxies handle TCP, UDP, and ICMP traffic
- Packets are encrypted client-side; Twingate cannot decrypt traffic

## DNS Resolution Flow
1. App sends DNS query → intercepted by Twingate Client's DNS resolver
2. Client returns a CGNAT IP (e.g., `100.108.194.142`) mapped to the Resource
3. App connects to CGNAT IP → Client transparent proxy forwards to Connector
4. Connector queries private DNS server → gets actual private IP (e.g., `192.168.1.50`)
5. Connector initiates connection to private IP, proxying traffic bidirectionally

## Configuration Values
| Item | Value |
|------|-------|
| CGNAT range (routing) | `100.96.0.0/12` |
| Twingate DNS servers | `100.95.0.251–254` |
| DNS TTL for Resources | 15 seconds (when Client active) |

## Verification Commands
```bash
# Check DNS resolution with Client ON vs OFF
dig nas.home.int

# Verify Twingate DNS is primary resolver (macOS)
scutil --dns

# Confirm routing table entries via Twingate interface
netstat -rn | grep utun7
```

## Gotchas
- The CGNAT IP assigned to a Resource is **not** the Resource's actual private IP — do not rely on it for direct routing
- Client only intercepts traffic for explicitly defined Resources; undefined FQDNs pass through normally
- Routing table modification routes all `100.96.0.0/12` traffic through the Twingate interface — conflicts with networks using this range are possible
- Public DNS resources still route through the Connector (not resolved locally on the client device)
- Destination host IP is never revealed to the client application

## Related Docs
- [Twingate Resources](https://www.twingate.com/docs/resources)
- [Transparent Proxy System](https://www.twingate.com/docs/how-twingate-works)
- [DNS Primer](https://www.twingate.com/docs/how-dns-works)
- [CGNAT RFC](https://tools.ietf.org/html/rfc6598)
# How DNS Works with Twingate

## Summary
Twingate uses a transparent proxy system where the client intercepts DNS queries for defined Resources and resolves them to CGNAT IP addresses (100.64.0.0/10 range) rather than actual private IPs. The Connector performs the actual private DNS resolution on the internal network, keeping private IP addresses hidden from client devices. This allows remote users to access private FQDNs without direct access to private DNS resolvers.

## Key Information
- Twingate Client runs a local DNS resolver that intercepts queries for defined Resources
- Resources resolve to CGNAT range IPs (`100.96/12`), not actual private IPs
- Twingate DNS servers: `100.95.0.251–100.95.0.254`
- Client adds itself as **primary DNS resolver** above existing resolvers
- Client creates a virtual network interface (e.g., `utun7` on macOS)
- Client modifies routing table so all `100.96/12` traffic routes through Twingate interface
- Connector performs actual DNS resolution against private DNS server
- Destination host's real IP is never exposed to the client device
- Works for both private DNS entries **and** public DNS entries (Connector still proxies resolution)
- Three proxies handle TCP, UDP, and ICMP (ping only)
- Traffic is encrypted client-side; Twingate cannot decrypt it

## DNS Resolution Flow (Step-by-Step)
1. App sends DNS request → OS → intercepted by Twingate Client's local DNS resolver
2. Client resolver returns a CGNAT IP (e.g., `100.108.194.142`) mapped to the Resource
3. App sends traffic to CGNAT IP → Twingate network interface (via routing table)
4. Client proxy strips source/destination, forwards payload to Connector
5. Connector resolves original FQDN via private DNS server → gets real private IP
6. Connector reassembles packet: source=Connector IP, destination=real private IP
7. Return traffic reverses: Connector strips/forwards payload → Client reassembles with Twingate interface IP as source

## Configuration Values
| Value | Description |
|-------|-------------|
| `100.95.0.251–254` | Twingate DNS resolver IPs added to client |
| `100.96/12` | CGNAT routing range used by Twingate interface |
| `100.64.0.0/10` | Full CGNAT range for Resource IP assignment |

## Diagnostic Commands
```bash
# Check DNS resolution (macOS/Linux)
dig nas.home.int

# Verify DNS resolver config (macOS)
scutil --dns

# Check routing table entries for Twingate interface
netstat -rn | grep utun7
```

## Gotchas
- Client only intercepts DNS for **defined Twingate Resources**—other FQDNs pass through normally
- Resolved CGNAT IPs are not stable/meaningful outside Twingate; don't use them for configuration
- Connector must be able to resolve the Resource FQDN and route to the destination—if Connector DNS fails, connection fails
- Public DNS Resources still route through the Connector (bypasses direct public resolution from client)
- Client must be running for Resource FQDNs to resolve; without Client, private FQDNs fail unless on local network

## Related Docs
- [Twingate Resources documentation](https://www.twingate.com/docs)
- [Transparent proxy system overview](https://www.twingate.com/docs)
- [CGNAT explanation (RFC 6598)](https://www.rfc-editor.org/rfc/rfc6598)
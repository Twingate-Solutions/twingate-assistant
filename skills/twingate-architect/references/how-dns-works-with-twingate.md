# How DNS Works with Twingate

## Summary
Twingate uses a transparent proxy system where the client intercepts DNS queries for defined Resources and resolves them to CGNAT IP addresses (100.64.0.0/10 range) rather than actual private IPs. The Connector handles real DNS resolution on the private network, so clients never need direct access to private DNS resolvers. Traffic flows Client → Connector → Resource with payload-only forwarding (source/destination addresses stripped).

## Key Information
- Twingate Client runs a local DNS resolver that intercepts queries for known Resources
- Resources resolve to CGNAT range IPs (`100.96.0.0/12`) on the client, not actual private IPs
- Twingate DNS servers: `100.95.0.251–254` (added as primary resolver on client device)
- Client creates a virtual network interface (`utun7` on macOS) and modifies routing table to route all `100.96/12` traffic through it
- The Connector performs actual DNS resolution against the private DNS server
- Real destination IP is never exposed to the client — stays behind the proxy
- Same flow applies to Resources with public DNS entries (Connector still resolves, overriding local DNS path)
- Three proxies in the client handle TCP, UDP, and ICMP (ping only)
- Traffic is encrypted client-side; Twingate cannot decrypt it

## DNS Resolution Flow
1. App on device sends DNS query → intercepted by Twingate Client's local DNS resolver
2. Client returns a CGNAT IP (e.g., `100.108.194.142`) mapped to the Resource
3. App connects to CGNAT IP → Client acts as transparent proxy, forwards payload to Connector
4. Connector resolves the FQDN against the private DNS server (e.g., `nas.home.int` → `192.168.1.50`)
5. Connector sends packets to actual Resource IP using its own IP as source
6. Response returns to Connector → stripped → forwarded back to Client → reassembled for user device

## Configuration Values
| Item | Value |
|------|-------|
| Twingate DNS servers | `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254` |
| CGNAT routing range | `100.96/12` |
| CGNAT assigned IP range | `100.64.0.0/10` |
| Network interface (macOS) | `utun7` (varies) |

## Gotchas
- Client only intercepts DNS for explicitly defined Resources — unlisted FQDNs pass through normally
- With Twingate ON, `dig` will show CGNAT IP and Twingate DNS server, not local resolver/IP
- Connector must be able to both resolve the Resource's DNS and route to the destination
- Resource IP is never revealed to the client application

## Diagnostics
```bash
# Check DNS resolution with client on/off
dig nas.home.int

# Verify DNS resolvers (macOS)
scutil --dns

# Verify routing table entries for Twingate interface
netstat -rn | grep utun7
```

## Related Docs
- [Twingate Transparent Proxy System](#)
- [DNS Primer (external)](#)
- [CGNAT RFC](#)
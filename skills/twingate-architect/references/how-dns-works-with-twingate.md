# How DNS Works with Twingate

## Summary
Twingate uses a transparent proxy system where the client intercepts DNS requests and maps private resource FQDNs to CGNAT IP addresses (100.64.0.0/10 range). DNS resolution for private resources is performed by the Connector on the private network, not the client device. This allows remote users to access private resources without joining the private network or having access to the private DNS resolver.

## Key Information
- Twingate Client runs its own DNS resolver that intercepts DNS queries for configured Resources
- Resources resolve to CGNAT range IPs (`100.96/12`) on the client, not actual private IPs
- Twingate DNS servers: `100.95.0.251-254` (added as primary resolver on client device)
- The Connector performs actual DNS resolution against the private DNS server
- Works for FQDNs, IP addresses, and CIDR ranges as Resource types
- Same flow applies to Resources with public DNS entries — resolution still routes through the Connector
- Traffic payload is encrypted client-side; Twingate cannot decrypt it

## DNS Resolution Flow
1. App sends DNS request → intercepted by Twingate Client's local DNS resolver
2. Client resolver returns a CGNAT IP (e.g., `100.108.194.142`) mapped to the Resource
3. App sends traffic to CGNAT IP → Twingate network interface (`utun7` on macOS) handles it
4. Twingate Client proxy strips source/destination, forwards payload to Connector
5. Connector resolves FQDN via private DNS server → gets actual private IP
6. Connector sends packet to private IP; response returns via reverse proxy path

## Client-Side System Changes
- Creates a new **network interface** (e.g., `utun7` on macOS)
- Inserts **primary DNS resolver** pointing to `100.95.0.251-254` at top of resolver list
- Maps Resource FQDNs → CGNAT IPs in its local DNS
- Modifies **routing table** so all `100.96/12` traffic routes through Twingate interface

## Configuration Values
| Item | Value |
|------|-------|
| CGNAT range used | `100.64.0.0/10` (routing: `100.96/12`) |
| Twingate DNS servers | `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254` |
| Twingate network interface (macOS) | `utun7` |

## Gotchas
- The IP returned by DNS when Twingate is active is **not** the resource's real IP — it's a temporary CGNAT mapping
- Connector must be able to both **resolve the FQDN** and **route to the destination** for the connection to succeed
- Client only intercepts DNS for explicitly configured Resources — other FQDNs pass through normally
- Protocols supported by the proxy: TCP, UDP, ICMP (ping only)

## Verification Commands
```bash
# Check DNS resolution with/without Twingate
dig nas.home.int

# Check active DNS resolvers (macOS)
scutil --dns

# Verify routing table entries for Twingate interface
netstat -rn | grep utun7
```

## Related Docs
- Twingate Resources configuration
- Twingate Connector setup
- [DNS primer](https://www.twingate.com/docs/how-dns-works)
- Transparent proxy architecture
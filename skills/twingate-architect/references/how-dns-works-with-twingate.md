# How DNS Works with Twingate

## Summary
Twingate uses a transparent proxy system where the client intercepts DNS queries for private Resources and resolves them to CGNAT IP addresses locally, then proxies traffic through Connectors that perform actual DNS resolution on the private network. Users never join the private network directly, and private IPs are never exposed to client devices.

## Key Information

- Twingate Client runs a local DNS resolver that intercepts queries for configured Resources
- Private Resources resolve to IPs in the `100.64.0.0/10` (CGNAT) range on the client device, not their actual private IPs
- The Connector performs real DNS resolution against the private network's DNS server
- Works for both private DNS entries and public DNS entries — resolution always routes through the Connector
- Three proxies handle TCP, UDP, and ICMP (ping only)
- Network payloads are encrypted client-side; Twingate cannot decrypt traffic

## How the Client Intercepts Traffic (4 Steps)

1. **Network interface**: Creates a virtual interface (e.g., `utun7` on macOS)
2. **Primary DNS resolver**: Inserts Twingate DNS servers (`100.95.0.251–254`) at top of resolver list
3. **DNS remapping**: Maps Resource FQDNs to CGNAT range IPs
4. **Routing table**: Routes all `100.96/12` traffic through the Twingate network interface

## DNS Resolution Flow

1. App sends DNS query → intercepted by Twingate Client's local resolver
2. Client returns a CGNAT IP (e.g., `100.108.194.142`) mapped to the Resource
3. App connects to CGNAT IP → Client transparent proxy forwards to Connector
4. Connector resolves the original FQDN against private DNS server
5. Private DNS returns actual private IP (e.g., `192.168.1.50`)
6. Connector proxies traffic to/from the Resource; private IP never revealed to client

## Configuration Values

| Value | Detail |
|-------|---------|
| CGNAT range (Resources) | `100.64.0.0/10` |
| CGNAT routing range | `100.96/12` |
| Twingate DNS servers | `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254` |
| DNS server port | `53` |

## Gotchas

- The client only intercepts traffic for explicitly defined Resources — non-Resource FQDNs pass through normally
- When Twingate Client is ON, DNS server changes from your local resolver to `100.95.0.25x` — this is expected behavior
- The Connector must be able to resolve the Resource FQDN and route to the destination; if Connector-side DNS fails, connection fails
- Private IPs are never exposed to the client application — the proxy relationship is opaque to the end application

## Diagnostic Commands

```bash
# Check DNS resolution (macOS/Linux)
dig nas.home.int

# Check DNS resolver config (macOS)
scutil --dns

# Check routing table for Twingate interface
netstat -rn | grep utun7
```

## Related Docs
- [Twingate transparent proxy system](https://www.twingate.com/docs)
- DNS primer (linked from page)
- Resources configuration (FQDNs vs IPs vs CIDR ranges)
---
source: https://www.twingate.com/docs/how-dns-works-with-twingate
type: docs
fetched: 2026-08-14
source_version: c9ec7484f5ef1630e919093fc8aa7e1473c54210a5c0925d98018e4dc43b4e89
---

# How DNS Works with Twingate

## Summary
Twingate uses a transparent proxy system rather than VPN, meaning client devices never join the private network and don't need direct access to private DNS resolvers. The Twingate Client intercepts DNS queries, maps FQDNs to CGNAT IP addresses locally, then routes traffic through a Connector which performs actual DNS resolution against the private network's DNS server.

## Key Information

- **Client devices never access private DNS resolvers directly** — the Connector handles private DNS resolution on behalf of the client
- **FQDN Resources resolve to CGNAT IPs** (`100.64.0.0/10` range) on the client device, not their actual private IPs
- **Same flow applies to public DNS resources** — resolution still passes through the Connector, overriding public DNS lookup from the client
- **Twingate Client DNS servers**: `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254`
- **CGNAT routing range handled by Twingate interface**: `100.96/12`
- **Three proxies** in the Twingate Client handle TCP, UDP, and ICMP (ping only)
- **Traffic is encrypted client-side** — Twingate cannot decrypt network traffic in transit

## DNS Resolution Flow (Step-by-Step)

1. App sends DNS request → intercepted by Twingate Client's local DNS resolver
2. Client DNS resolver returns a CGNAT IP (e.g., `100.108.194.142`) mapped to the Resource — not the actual private IP
3. App traffic goes to CGNAT IP → Twingate Client acts as transparent proxy, forwards to appropriate Connector
4. Connector performs DNS resolution against the **private network's DNS server**
5. Private DNS returns actual private IP (e.g., `192.168.1.50`)
6. Connector proxies traffic to the Resource's private IP; actual IP is never revealed to the client

## What the Twingate Client Modifies on the Device

| Modification | Purpose |
|---|---|
| Creates virtual network interface (`utun7` on macOS) | Handles Twingate traffic |
| Adds primary DNS resolver (`100.95.0.251–254`) | Intercepts DNS queries for Resources |
| Remaps Resource FQDNs to CGNAT IPs | Enables traffic interception |
| Modifies routing table for `100.96/12` | Routes CGNAT traffic to Twingate interface |

## Configuration Values

- **Client DNS resolver IPs**: `100.95.0.251–254`
- **CGNAT range used for Resource IPs**: `100.64.0.0/10` (routing via `100.96/12`)
- **macOS interface name**: `utun7` (example)
- **Twingate interface gateway IP**: `172.16.30.1` (example)

## Gotchas

- The CGNAT IP assigned to a Resource **changes** when the Twingate Client is active — do not hardcode these IPs
- Connector must be able to **both resolve the FQDN and route traffic** to the destination for the connection to succeed
- Client only intercepts traffic for **explicitly defined Twingate Resources** — other FQDNs pass through normally
- Actual private IP of the destination is **never exposed** to the client application

## Related Docs

- [Twingate transparent proxy system](#)
- [DNS primer (external)](#)
- [CGNAT explanation](#)
- Resources configuration (FQDNs vs IPs vs CIDR ranges)
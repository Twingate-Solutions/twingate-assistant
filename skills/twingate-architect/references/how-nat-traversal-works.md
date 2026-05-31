# How NAT Traversal Works

## Page Title
How NAT Traversal Works

## Summary
Twingate establishes secure Client-to-Connector connections without open inbound ports using two methods: Relays (intermediary servers) and NAT traversal (peer-to-peer tunnels). NAT traversal works by having both parties simultaneously send outbound packets to each other, exploiting firewall behavior that permits inbound packets from addresses previously contacted. Relays act as fallback when P2P cannot be established.

## Key Information
- **Two connectivity methods**: Relay-based (intermediary) and NAT traversal (peer-to-peer)
- **No open inbound ports required** for either method
- NAT translates private IPs (e.g., `192.168.1.4`) to unique public IPs for internet routing
- Ports (0–65,535) differentiate sessions sharing the same public IP
- Firewall rule: inbound packets allowed **only if** an outbound packet was previously sent to that same IP+port
- Relays serve dual role: traffic relay **and** STUN server (IP/port discovery broker)
- Client-Connector traffic is end-to-end encrypted; Relays cannot decrypt it

## NAT Traversal Step-by-Step
1. Client and Connector each connect to the Relay and report their public IP + port
2. Relay shares each party's public IP + port with the other (STUN broker function)
3. Relay coordinates simultaneous outbound packet sending from both Client and Connector
4. Each firewall permits inbound packets because an outbound packet was already sent to that address
5. P2P tunnel established; Relay no longer needed for data transfer

## Configuration Values
- HTTPS default port: `443`
- Standard NAT port range: `1–65,535`
- Relay fallback: automatic when P2P fails due to network conditions

## Gotchas
- **Symmetric NAT** and certain strict firewall configurations can prevent P2P establishment; Relay is used as fallback
- Opening inbound ports (port forwarding) is explicitly discouraged — open ports attract automated scanning and exploit attempts
- Timing is critical: both sides must send packets **simultaneously** for traversal to succeed
- Relays add latency vs. P2P; Twingate deploys Relays globally to mitigate this
- VPN gateways require open inbound ports — a key architectural difference from Twingate

## Prerequisites
- Outbound internet connectivity from both Client and Connector networks
- Access to Twingate Relay infrastructure (handled automatically)

## Related Docs
- Twingate Relays worldwide deployment
- NAT traversal troubleshooting guide (linked from page)
- Port forwarding configuration (consumer routers)
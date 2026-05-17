# How NAT Traversal Works

## Summary
Twingate establishes secure Client-to-Connector tunnels without requiring open inbound ports using two methods: Relay servers (intermediaries) and NAT traversal (peer-to-peer). NAT traversal works by coordinating simultaneous outbound connections from both Client and Connector, exploiting firewall rules that allow return traffic from previously contacted addresses.

## Key Information

- **No open inbound ports required** — core security principle for both Clients and Connectors
- **Two connectivity methods**: Relay (intermediary) and NAT traversal (P2P direct tunnel)
- **NAT**: Translates private IPs (e.g., `192.168.1.4`) to unique public IPs; uses ports to track multiple sessions from the same network
- **Ports**: 65,535 per IP address; NAT devices use IP+port combinations to route return traffic to correct private device
- **Firewall rule exploited**: Inbound packets allowed only if outbound packets were sent first to that same IP+port
- **Relays serve dual role**: End-to-end encrypted tunnel for initial messaging channel AND fallback transport when P2P fails
- **Relay encryption**: Relays cannot decrypt Client-Connector traffic (end-to-end encrypted between Client and Connector)

## NAT Traversal Connection Flow (Step-by-Step)

1. Client and Connector both connect to a Relay (acting as STUN server) to discover their own public IP + port
2. Relay shares each party's public IP + port with the other via the encrypted messaging channel
3. Relay coordinates **simultaneous** outbound connections — Client sends packets to Connector's public IP+port; Connector sends packets to Client's public IP+port at the same time
4. Because each side already sent packets to the other, each firewall allows the return traffic through
5. P2P tunnel established — no intermediary required for ongoing traffic

## Configuration Values

- No user-configurable parameters for NAT traversal — handled automatically by Twingate infrastructure
- Port `443` referenced as HTTPS convention example

## Gotchas

- **Symmetric NAT** and certain restrictive network configurations can **prevent P2P establishment** — fallback to Relay occurs automatically
- Opening inbound ports is explicitly discouraged — bots continuously scan public IPs for open ports
- Port forwarding on consumer routers defeats the security model
- NAT traversal requires **simultaneous** outbound connections — timing is coordinated by the Relay
- VPN gateways require open inbound ports (vulnerability surface); Twingate Connectors do not

## Prerequisites

- Outbound connectivity from both Client and Connector to Twingate Relays
- No special firewall configuration needed on private network side

## Related Docs

- [Twingate Relay locations](https://www.twingate.com/docs) — global Relay deployment
- [NAT traversal troubleshooting guide](https://www.twingate.com/docs) — for when P2P connections fail to establish
---
source: https://www.twingate.com/docs/how-nat-traversal-works
type: docs
fetched: 2026-08-14
source_version: 20b0a3e206cb42efdcf520b27f7428a7e57590219b433b351f5fee0fcce5603a
---

# How NAT Traversal Works

## Page Title
How NAT Traversal Works

## Summary
Twingate never requires open inbound ports. Instead, it uses two methods to establish Client-Connector connectivity: Relay servers (intermediaries) and NAT traversal (direct peer-to-peer tunnels). NAT traversal works by having both parties simultaneously send outbound packets to each other's public IP/port, exploiting the firewall rule that allows return traffic from addresses you've already contacted.

## Key Information
- **Two connectivity methods**: Relays (fallback, adds latency) and NAT traversal (preferred, peer-to-peer)
- **NAT traversal core mechanic**: Firewalls allow inbound packets from a public IP/port *only if* outbound packets were previously sent to that same address/port
- **Relay dual role**: Acts as both traffic relay (fallback) and STUN/broker server (coordinates NAT traversal)
- **End-to-end encryption**: Traffic is encrypted between Client and Connector; Relays cannot decrypt it even when proxying
- **NAT**: Translates private IPs (e.g., `192.168.1.4`) to unique public IPs using port assignments to track sessions
- **Ports**: 65,535 per IP address; NAT devices use source port + IP combos to track which private device initiated which session

## Prerequisites
- Understanding that open inbound ports are avoided by design
- Twingate Relay infrastructure is always available as fallback
- Both Client and Connector must be able to make outbound connections

## Step-by-Step: NAT Traversal Connection Establishment
1. Client and Connector each connect to a Relay, reporting their public IP/port
2. Relay brokers exchange: shares Client's public IP/port with Connector, and vice versa
3. Relay establishes an encrypted messaging channel between Client and Connector
4. Client and Connector **simultaneously** send packets to each other's public IP/port
5. Because each side sent packets first, each side's firewall allows the return packets through
6. Peer-to-peer tunnel is established — no open inbound ports required

## Configuration Values
- None specific to this conceptual page; see troubleshooting guide for network-specific tuning

## Gotchas
- **Certain network conditions can block NAT traversal** (e.g., symmetric NAT); in those cases, traffic falls back to Relays automatically
- **Never open inbound ports**: open ports are continuously scanned and probed by bots; VPN gateways with open ports are a known attack surface
- **Simultaneous packet send is critical**: timing must be coordinated by the Relay; if one side sends before the other has sent, the return packet will be dropped
- Port forwarding on consumer routers bypasses these protections — avoid for Connector deployments

## Related Docs
- [Twingate Relay documentation] (referenced but not linked inline)
- [NAT traversal troubleshooting guide](https://www.twingate.com/docs/) — for cases where P2P cannot be established
- [Global Relay deployment](https://www.twingate.com/docs/) — Relay locations worldwide
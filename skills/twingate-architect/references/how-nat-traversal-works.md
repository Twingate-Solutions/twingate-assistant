# How NAT Traversal Works

## Page Title
How NAT Traversal Works

## Summary
Twingate never requires open inbound ports. Instead, it establishes connectivity between Clients and Connectors via two methods: Relay servers (intermediaries) and NAT traversal (direct peer-to-peer tunnels). NAT traversal exploits the firewall rule that allows inbound packets from a public IP/port if the private network previously sent packets to that same address/port.

## Key Information
- **Two connectivity methods**: Relay (intermediary) and NAT traversal (P2P direct tunnel)
- **NAT**: Translates private IPs (e.g., `192.168.1.4`) to unique public IPs using port mapping to track sessions
- **Ports**: 65,535 per IP address; NAT uses public IP + port combos to disambiguate multiple devices behind the same public IP
- **Firewall rule exploited by NAT traversal**: Inbound packets allowed only if outbound packets were first sent to that same public IP + port
- **Relay dual role**: Acts as both STUN server (exchanges IP/port info between peers) and fallback data relay
- **P2P tunnel requires simultaneous outbound connections**: Both Client and Connector must send packets to each other at the same time, coordinated by the Relay

## Prerequisites
- Understanding that Twingate Connectors require no open inbound firewall ports
- Relays are deployed globally to minimize latency for both relay-based and NAT traversal coordination

## Step-by-Step: NAT Traversal Connection Establishment
1. Client and Connector each connect outbound to a Twingate Relay (acting as STUN server) and report their public IP + port
2. Relay shares each peer's public IP + port with the other peer via an encrypted messaging channel
3. Relay coordinates **simultaneous** outbound packet transmission from both Client → Connector and Connector → Client
4. Each firewall allows inbound packets because outbound packets were already sent to that peer's address/port
5. P2P tunnel is established; Relay is no longer needed for data transfer

## Configuration Values
- No user-configurable parameters for NAT traversal — handled automatically by Twingate platform
- HTTPS default port example: `:443`

## Gotchas
- **Symmetric NAT or restrictive firewalls** can prevent P2P tunnel establishment — fallback to Relay occurs automatically
- **Simultaneous packet exchange is required**: if timing is off or one side is blocked, P2P fails
- **Opening inbound ports is explicitly discouraged**: open ports attract continuous bot scanning and exploit attempts
- **Port forwarding is not needed** and should not be configured for Twingate Connectors
- Relay sees encrypted traffic only — end-to-end encryption between Client and Connector means Relay cannot decrypt payload

## Related Docs
- [Troubleshooting NAT traversal / P2P connections](https://www.twingate.com/docs/) (referenced as "troubleshooting guide")
- Twingate Relays worldwide deployment documentation
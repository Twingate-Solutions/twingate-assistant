# How NAT Traversal Works

## Summary
Twingate establishes secure Client-to-Connector connections without open inbound ports using two methods: Relay-based intermediary routing and NAT traversal peer-to-peer tunnels. NAT traversal works by having both parties simultaneously send outbound packets to each other's public IP/port, exploiting firewall rules that permit inbound traffic from addresses already contacted outbound.

## Key Information

- **Two connectivity methods**: Relays (intermediary) and NAT traversal (peer-to-peer/P2P)
- **Core firewall rule exploited**: Inbound packets are allowed from a public IP/port *only if* outbound packets were previously sent to that same address/port
- **NAT function**: Translates private IP addresses (e.g., `192.168.1.4`) to unique public IPs; uses ports to track multiple simultaneous sessions from different devices
- **Ports**: 65,535 available per IP address; NAT devices use IP+port combinations to route return traffic to correct private devices
- **Relay role (STUN broker)**: Facilitates exchange of public IP/port info between Client and Connector, coordinates simultaneous outbound connection timing
- **End-to-end encryption**: Traffic is encrypted between Client and Connector; Relays cannot decrypt it
- **Relays deployed globally** to minimize latency when P2P fails or is used as fallback

## NAT Traversal Step-by-Step

1. Client and Connector both connect to a Relay (acting as STUN server) and report their public IP/port
2. Relay shares each party's public IP/port with the other via encrypted messaging channel
3. Client sends packets to Connector's public IP/port **simultaneously** as Connector sends to Client's
4. Simultaneous outbound sends satisfy each firewall's requirement (packets came from a known address)
5. Inbound packets from each peer are now permitted — P2P tunnel established

## Why Not Just Open Ports (VPN Gateway Model)

- Open ports are continuously scanned by bots
- Any vulnerability on a listening service is exploitable by anyone on the internet
- VPN gateways require an open inbound port by design — Twingate does not

## Gotchas

- **Certain network conditions can block P2P**: Symmetric NAT or strict firewall policies may prevent NAT traversal from succeeding; Twingate falls back to Relay routing
- **Relay adds latency**: Extra hop vs. direct P2P; mitigated by global Relay deployment
- **Relay cannot decrypt traffic**: Encryption is handled between Client and Connector only — Relay is a packet forwarder, not a termination point
- Port forwarding (consumer routers) can enable inbound connections but is strongly discouraged for security reasons

## Configuration Values

- HTTPS default port: `443`
- Private IP range example: `192.168.x.x` (non-routable, reused across networks)

## Related Docs

- [Twingate Relay troubleshooting guide](https://www.twingate.com/docs/) — for P2P/NAT traversal failure scenarios
- Twingate global Relay infrastructure documentation
- Connector deployment documentation
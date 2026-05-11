# How NAT Traversal Works

## Summary
Twingate never requires open inbound ports. Instead, it uses two methods to connect Clients to Connectors: Relay-based intermediary tunnels and direct peer-to-peer (P2P) tunnels via NAT traversal. This document explains the underlying networking concepts and the mechanics of both approaches.

## Key Information

- **Two connectivity methods:**
  - **Relays**: Public intermediaries; both Client and Connector make outbound connections to the Relay, which forwards encrypted traffic between them
  - **NAT Traversal**: Direct P2P tunnel; no intermediary after setup, lower latency

- **NAT**: Translates private IP addresses (e.g., `192.168.1.4`) to public IPs using port mapping to track sessions across devices

- **Ports**: 65,535 ports per IP address; NAT uses unique public IP + port combinations to route return traffic to correct private devices

- **Firewall rule critical to NAT traversal**: Inbound packets from a public IP:port are allowed **only if** an outbound packet was previously sent to that same IP:port

- **Open ports are a security risk**: Immediately attract bot scanning and exploit attempts; Twingate explicitly avoids this

## NAT Traversal Mechanism (Step-by-Step)

1. Client and Connector both connect outbound to a Relay (acting as STUN server + broker)
2. Relay returns each party's public IP:port to the other
3. Relay coordinates simultaneous outbound packet sends: Client → Connector's public IP:port, Connector → Client's public IP:port
4. Each firewall accepts the inbound packets because an outbound packet was already sent to that source
5. P2P tunnel established — Relay no longer needed for data transfer

## Configuration Values

- No user-configurable NAT traversal settings exposed directly
- Relays are globally distributed; selection is automatic
- Port `443` used as default HTTPS convention example (not NAT-traversal-specific)

## Gotchas

- **Simultaneity required**: Both Client and Connector must send packets to each other at the same time; Relay coordinates this timing
- **Some network conditions block P2P**: Certain NAT types (e.g., symmetric NAT) or strict firewalls may prevent traversal — fallback to Relay occurs automatically
- **Relay traffic is end-to-end encrypted**: Relay cannot decrypt Client↔Connector traffic; encryption is handled independently of the Relay
- **Port forwarding is explicitly discouraged**: Opening any inbound port immediately attracts malicious scanning

## Related Docs

- [Troubleshooting NAT Traversal / Peer-to-Peer Connections](https://www.twingate.com/docs/) (referenced as "troubleshooting guide")
- Twingate Relay infrastructure / global Relay deployment docs
# How NAT Traversal Works

## Summary
Twingate establishes secure Client-to-Connector connections without open inbound ports using two methods: Relay servers (intermediaries) and NAT traversal (peer-to-peer tunnels). NAT traversal uses the Relay as a coordination broker to enable simultaneous outbound connections that punch through firewalls on both sides.

## Key Information
- Twingate **never requires open inbound ports** on any network device
- Two connectivity methods: **Relay-based** (intermediary) and **NAT traversal** (P2P)
- NAT traversal is preferred; Relays are fallback when P2P cannot be established
- Relay serves dual role: P2P traffic intermediary AND STUN-like coordination broker
- All Client↔Connector traffic is **end-to-end encrypted**; Relays cannot decrypt it
- Relays are deployed globally to minimize latency on fallback connections

## Core Concepts
- **NAT**: Translates private IPs (e.g., `192.168.1.4`) to unique public IPs for internet routing
- **Ports**: 65,535 per IP address; NAT uses IP+port combos to track sessions per device
- **Firewall rule**: Inbound packets allowed **only if** outbound packets were first sent to that same IP+port
- **Port forwarding / open ports**: Explicitly not used; considered a security risk

## NAT Traversal Mechanism (Step-by-Step)

1. Client and Connector both connect outbound to the Relay
2. Relay establishes an encrypted messaging channel between them (acts as STUN server + broker)
3. Client and Connector exchange their public IP address + port via the messaging channel
4. Relay **coordinates simultaneous** outbound packet sends from both sides
5. Client sends packets to Connector's public IP+port; Connector sends to Client's public IP+port at the same time
6. Each firewall allows return traffic because it recognizes the prior outbound connection
7. P2P tunnel established — Relay no longer needed for data transfer

## Why Relays Are Still Needed
- Some network configurations (symmetric NAT, strict firewalls) block P2P establishment
- Relay provides fallback when NAT traversal fails
- Trade-off: Relay adds latency (extra hop) vs. P2P direct path

## Gotchas
- **Simultaneous sends are critical**: Both sides must send packets at the same time for firewall rules to open on both ends
- Certain network conditions (e.g., symmetric NAT, carrier-grade NAT) can prevent P2P — system falls back to Relay automatically
- VPN gateways require open inbound ports; Twingate Connectors do not — this is a fundamental architectural difference
- Opening inbound ports exposes them to constant bot scanning and vulnerability probing

## Configuration Values
No direct configuration required for NAT traversal — handled automatically by Twingate infrastructure.

## Related Docs
- [Troubleshooting NAT traversal / P2P issues](https://www.twingate.com/docs/) — referenced for cases where P2P cannot be established
- Twingate global Relay network documentation
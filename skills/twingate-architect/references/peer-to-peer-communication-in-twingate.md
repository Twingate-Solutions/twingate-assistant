# Peer-to-Peer Communication in Twingate

## Summary
Twingate enables peer-to-peer connections between Clients and Connectors using NAT traversal without requiring open inbound ports. When direct P2P is not possible, Twingate automatically falls back to relay infrastructure. The system is transparent to end users and administrators with no additional configuration required.

## Key Information
- Available to all Twingate customers; no additional deployment needed
- Uses QUIC (RFC 9000) as the transport layer protocol
- Automatically selects lowest-latency transport option
- No open inbound ports required on either end
- Relay infrastructure serves as global backup transport

## Connection Establishment Flow
1. **Signaling channel**: Client and Connector both connect to Twingate's Relay Infrastructure (publicly accessible)
2. **Peer discovery**: STUN server (hosted in Twingate relay infra) discovers public IP:port assigned by NAT
3. **Address exchange**: Each peer receives candidate addresses for the other peer via signaling channel
4. **Negotiation**: Peers attempt direct P2P connection using candidate addresses (NAT traversal)
5. **Fallback**: If P2P fails, traffic routes through relay infrastructure automatically

## Configuration Values
- No configuration required — behavior is automatic for both Client and Connector

## QUIC Protocol Details
- Built on UDP with its own reliable delivery mechanisms
- Multiplexes concurrent data streams over a single connection
- **TLS 1.3 minimum** — no older cryptographic protocols supported
- Supports client-side IP/port changes (roaming, NAT rebinding, network switching)
- Single round-trip initial connection; zero round-trip resumption possible

## QUIC Advantages Over TCP+TLS
| Feature | Benefit |
|---|---|
| Connection establishment | 1 RTT initial; 0 RTT resumption |
| Head-of-line blocking | Eliminated (per-stream, not per-connection) |
| Client roaming | Connections survive IP/port changes |
| Cryptography | TLS 1.3 only |
| Packet loss | More efficient recovery than TCP |

## Gotchas
- P2P is **not guaranteed** — incompatible NAT layers or blocked ports will trigger relay fallback
- Relay fallback is automatic but may introduce higher latency than direct P2P
- QUIC runs over UDP — ensure UDP is not blocked on network paths between Client and Connector for optimal performance

## Prerequisites
- No special prerequisites — feature is enabled by default for all customers
- Existing deployments require no changes

## Related Docs
- Twingate Client documentation
- Twingate Connector documentation
- Twingate Relay Infrastructure
- [RFC 9000 (QUIC)](https://datatracker.ietf.org/doc/html/rfc9000)
# Peer-to-Peer Communication in Twingate

## Summary
Twingate enables peer-to-peer connections between Clients and Connectors using NAT traversal (STUN/ICE) without requiring open inbound ports. When direct P2P is not possible, Twingate automatically falls back to relay infrastructure. Built on QUIC protocol for improved latency, connection resilience, and multi-stream performance.

## Key Information
- Available to all customers; no additional deployment or configuration required
- Transparent to end users and administrators
- Automatically selects lowest-latency transport (P2P preferred, relay as fallback)
- Uses QUIC (UDP-based) as the transport protocol
- Relay infrastructure is globally distributed and always accessible as backup

## Connection Establishment Flow
1. **Signaling channel**: Client and Connector connect to Twingate's globally available Relay Infrastructure on startup
2. **Peer discovery**: STUN server (hosted in Twingate relay infra) discovers public IP:port behind NAT
3. **Address exchange**: Signaling channel distributes candidate addresses to each peer
4. **NAT traversal**: Peers attempt direct P2P connection using exchanged candidate addresses; falls back to relay if unsuccessful

## Configuration Values
- No configuration required — fully automatic
- No inbound ports need to be opened on Client or Connector side

## Technical Details (QUIC Protocol)
| Feature | Detail |
|---|---|
| Protocol | QUIC over UDP (RFC 9000) |
| TLS | 1.3 only |
| Connection init | Single round-trip; zero-RTT resumption supported |
| Stream multiplexing | Multiple app flows mapped to individual QUIC streams |
| IP roaming | Survives NAT rebinding and network switches |
| Packet loss | Per-stream recovery (no head-of-line blocking) |

## Gotchas
- P2P is **not always possible**: symmetric NAT or blocked UDP ports force relay fallback
- Relay fallback is automatic — no admin intervention needed, but expect slightly higher latency
- QUIC runs over UDP; ensure UDP is not blocked between Client and Twingate relay infrastructure
- NAT traversal failure scenarios: incompatible NAT types, firewall rules blocking UDP hole-punching

## Prerequisites
- No special prerequisites; works with existing Twingate Client and Connector deployments

## Related Docs
- Twingate Client documentation
- Twingate Connector documentation
- Twingate Relay Infrastructure
- [RFC 9000 (QUIC)](https://www.rfc-editor.org/rfc/rfc9000)
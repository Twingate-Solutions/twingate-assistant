# Peer-to-Peer Communication in Twingate

## Summary
Twingate enables peer-to-peer connections between Clients and Connectors using NAT traversal (STUN/ICE), with relay infrastructure as automatic fallback. No configuration is required from administrators or end users. The feature uses QUIC (UDP-based) as the transport protocol.

## Key Information
- Available to all customers; no additional deployment needed
- Completely transparent to end users and administrators
- No open inbound ports required
- Automatically selects lowest-latency transport (P2P preferred, relay as fallback)
- Uses QUIC protocol (RFC 9000) over UDP

## Connection Establishment Flow

1. **Signaling channel**: Client and Connector both connect to Twingate's globally distributed Relay Infrastructure on startup
2. **Peer discovery**: STUN server (hosted in Twingate relay infra) discovers public IP:port behind NAT for each peer
3. **Address exchange**: Signaling channel delivers candidate addresses to each peer
4. **NAT traversal**: Peers attempt direct P2P connection using candidate addresses

## Fallback Behavior
- When NAT traversal fails (blocked ports, incompatible NAT types), traffic routes through Twingate's relay infrastructure
- Relays have public addresses, globally distributed — always reachable
- Selection is automatic, no manual configuration

## Configuration Values
- None required — zero-config feature

## QUIC Protocol Details
| Feature | Benefit |
|---|---|
| Built on UDP | Avoids TCP head-of-line blocking |
| TLS 1.3 only | Stronger cryptographic security |
| Single round-trip setup | Faster initial connection |
| Connection resumption | Zero additional RTT |
| Connection ID-based routing | Survives IP/port changes (NAT rebinding, network switching) |
| Multi-stream multiplexing | Concurrent flows to multiple resources over one connection |

## Gotchas
- P2P is not always achievable — incompatible NAT configurations or port blocking will force relay fallback silently
- QUIC runs over UDP; firewalls that block UDP may prevent P2P (relay would still function if relay traffic is permitted)
- No admin visibility into whether a given session is P2P vs relayed

## Related Docs
- Twingate Relay Infrastructure
- Twingate Client documentation
- Twingate Connector documentation
- [RFC 9000 (QUIC)](https://www.rfc-editor.org/rfc/rfc9000)
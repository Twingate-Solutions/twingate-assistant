# Peer-to-Peer Communication in Twingate

## Summary
Twingate enables peer-to-peer connections between Clients and Connectors using NAT traversal, with relay infrastructure as a fallback. No configuration, open inbound ports, or additional deployment is required. The feature uses QUIC (UDP-based) as the transport protocol.

## Key Information
- Available to all customers; no additional deployment needed
- Transparent to end users and administrators
- No open inbound ports required
- Automatically selects lowest-latency transport option
- Uses QUIC protocol (RFC 9000, IETF standardized)

## Connection Flow
1. **Signaling channel**: Client and Connector both connect to Twingate's globally distributed Relay Infrastructure on startup
2. **Peer discovery**: STUN server (hosted in Twingate relay infra) discovers public IP:port assigned by NAT
3. **Address exchange**: Each peer receives candidate addresses for the other via signaling channel
4. **Negotiation**: Peers attempt direct P2P connection using candidate addresses (NAT traversal)
5. **Fallback**: If P2P fails (blocked ports, incompatible NAT), traffic routes through relay infrastructure

## Configuration Values
- None required — fully automatic

## Technical Details (QUIC)
| Feature | Detail |
|---|---|
| Protocol | QUIC over UDP (RFC 9000) |
| TLS | 1.3+ only |
| Connection establishment | 1 round-trip (0-RTT resumption available) |
| Multiplexing | Multiple app data flows mapped to single QUIC streams |
| Roaming | Survives client IP/port changes (NAT rebinding, network switches) |

## QUIC Advantages Over TCP+TLS
- No head-of-line blocking (packet loss affects only impacted streams)
- Faster initial handshake and resumption
- Better mobile/roaming support
- Stronger cryptography (TLS 1.3 mandatory)
- More efficient packet loss recovery

## Gotchas
- P2P is not guaranteed — symmetric NAT or firewall rules blocking UDP may force relay fallback
- Relay is always the backup; no configuration needed to enable it
- QUIC runs over UDP — ensure UDP is not broadly blocked in your network environment

## Related Docs
- Twingate Relay Infrastructure
- Twingate Client documentation
- Twingate Connector documentation
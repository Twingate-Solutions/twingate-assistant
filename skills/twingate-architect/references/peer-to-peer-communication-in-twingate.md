# Peer-to-Peer Communication in Twingate

## Summary
Twingate automatically establishes peer-to-peer connections between Clients and Connectors using NAT traversal (ICE/STUN), with relay infrastructure as fallback. No configuration, open inbound ports, or additional deployment is required. Uses QUIC (UDP-based) as the transport protocol.

## Key Information
- Available to all customers; no additional deployment needed
- No open inbound ports required on either Client or Connector
- Twingate auto-selects lowest-latency transport (P2P preferred, relay as fallback)
- Transport protocol: QUIC (RFC 9000), built on UDP
- QUIC enforces TLS 1.3+ only
- Relay infrastructure is globally distributed and always accessible as backup

## Connection Establishment Flow
1. **Signaling channel**: Client and Connector both connect outbound to Twingate's Relay Infrastructure (public, globally available)
2. **STUN discovery**: Each peer discovers its public IP:port via STUN server (hosted in Twingate relay infra)
3. **Candidate exchange**: Peers exchange candidate addresses via signaling channel
4. **NAT traversal**: Peers attempt direct P2P connection using candidate addresses
5. **Fallback**: If P2P fails (blocked ports, incompatible NAT), traffic routes through relay infrastructure

## Configuration Values
- No configuration required — fully automatic
- No CLI flags, env vars, or API parameters to set

## QUIC Protocol Benefits
| Feature | Detail |
|---|---|
| Connection establishment | Single round trip; zero-RTT resumption |
| Cryptography | TLS 1.3 only |
| Client roaming | Survives IP/port changes (NAT rebinding, network switching) |
| Head-of-line blocking | Eliminated (vs. TCP/HTTP2) |
| Multi-stream | Multiplexes multiple app flows over single connection |

## Gotchas
- P2P is **not guaranteed** — incompatible NAT types or firewall rules blocking UDP will fall back to relay automatically
- Relay fallback is transparent; no admin action needed but may have higher latency than direct P2P
- QUIC runs over UDP — ensure UDP is not blocked on networks where Clients operate
- Outbound connectivity to Twingate relay infrastructure must be available from both Client and Connector sides

## Related Docs
- Twingate Connector documentation
- Twingate Client documentation
- Twingate Relay Infrastructure / networking requirements
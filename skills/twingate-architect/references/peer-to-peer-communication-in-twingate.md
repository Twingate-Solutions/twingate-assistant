# Peer-to-Peer Communication in Twingate

## Summary
Twingate enables peer-to-peer connections between Clients and Connectors using NAT traversal (ICE/STUN), with relay infrastructure as automatic fallback. No configuration is required and no inbound ports need to be opened. The transport layer uses QUIC (UDP-based) for improved latency, multi-stream handling, and network roaming support.

## Key Information
- Available to all customers; no additional deployment required
- No open inbound ports required on either Client or Connector side
- Twingate automatically selects lowest-latency transport (P2P preferred, relay as fallback)
- Transparent to end users and administrators

## Connection Establishment Flow
1. **Signaling channel**: Client and Connector both connect outbound to Twingate's Relay Infrastructure
2. **STUN discovery**: Each peer discovers its public IP:port via Twingate-hosted STUN server
3. **Candidate exchange**: Peers exchange discovered addresses via signaling channel
4. **NAT traversal**: Peers attempt direct connection using candidate addresses

## Fallback Behavior
- When P2P fails (blocked ports, incompatible NAT types), traffic routes through Twingate's global relay infrastructure
- Relay operates at transport layer; globally distributed for availability
- Automatic failover, no user/admin action required

## Technical Implementation (QUIC)
- Transport protocol: **QUIC** (RFC 9000), built on UDP
- Replaces TCP+TLS for Twingate's transport layer

**QUIC advantages used by Twingate:**
| Feature | Benefit |
|---|---|
| 1-RTT initial connection, 0-RTT resumption | Faster connection setup |
| TLS 1.3 only | Stronger encryption |
| Connection ID-based routing | Survives IP/port changes (roaming, NAT rebinding) |
| Per-stream reliability over UDP | No head-of-line blocking across flows |
| Multi-stream multiplexing | Maps flows from multiple apps to single QUIC connection |

## Configuration Values
None required. Feature is automatic for all deployments.

## Gotchas
- P2P is **not guaranteed** — NAT incompatibility or port blocking forces relay fallback automatically
- QUIC uses **UDP**; ensure UDP is not blocked between Client/Connector and Twingate relay infrastructure
- Client IP/port changes (network switching, NAT rebinding) are handled gracefully via QUIC connection migration — no session drops

## Prerequisites
- Standard Twingate Client and Connector deployment
- Outbound UDP access from Client and Connector to Twingate relay infrastructure

## Related Docs
- Twingate Connector deployment
- Twingate Relay Infrastructure
- Resource access configuration
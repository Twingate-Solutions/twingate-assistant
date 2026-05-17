# Peer-to-Peer Communication in Twingate

## Summary
Twingate supports peer-to-peer (P2P) connections between Clients and Connectors using NAT traversal, requiring no open inbound ports or additional configuration. When P2P is unavailable, Twingate automatically falls back to relay infrastructure. The system is transparent to both end users and administrators.

## Key Information
- Available to all Twingate customers; no additional deployment required
- No open inbound ports needed on either Client or Connector
- Automatically selects lowest-latency transport (P2P preferred, relay as fallback)
- Uses **QUIC** (RFC 9000) as the transport protocol, built on UDP
- QUIC enforces TLS 1.3 minimum

## Connection Establishment Flow
1. **Signaling channel**: Client and Connector connect to Twingate's global Relay Infrastructure on startup
2. **STUN discovery**: Both peers discover their public IP:port via Twingate-hosted STUN servers
3. **Candidate exchange**: Peers exchange discovered addresses via the signaling channel
4. **NAT traversal**: Peers attempt direct P2P connection using candidate addresses
5. **Fallback**: If P2P fails (blocked ports, incompatible NAT), traffic routes through Twingate's relay infrastructure

## Prerequisites
- No special configuration required
- Works with existing Client and Connector deployments

## Configuration Values
- None required — fully automatic

## Technical Details (QUIC)
| Feature | Benefit |
|---|---|
| UDP-based with reliable delivery | Lower latency than TCP+TLS |
| Single round-trip initial connection | Faster establishment |
| TLS 1.3 only | Stronger encryption |
| Connection ID-based routing | Survives IP/port changes (roaming, NAT rebinding) |
| Stream multiplexing | No head-of-line blocking (unlike HTTP/2 over TCP) |

## Gotchas
- P2P is **not always achievable** — incompatible NAT types or firewalls blocking UDP will force relay fallback
- Relay fallback is automatic; no administrator action needed
- QUIC runs in user space, meaning it can be updated independently of kernel TCP stack
- Twingate maps multiple application flows to individual QUIC streams across a single connection

## Related Docs
- Twingate Connector documentation
- Twingate Client documentation
- Relay Infrastructure overview
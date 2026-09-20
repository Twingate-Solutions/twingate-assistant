---
source: https://www.twingate.com/docs/peer-to-peer-communication-in-twingate
type: docs
fetched: 2026-09-20
source_version: d6a1e7ae0283eead53a4686ef4651d00cba336655fcf35129f4a5e5409a5c7a0
---

# Peer-to-Peer Communication in Twingate

## Summary
Twingate enables peer-to-peer connections between Clients and Connectors using NAT traversal (STUN/ICE), with relay infrastructure as automatic fallback. No configuration, open inbound ports, or additional deployment is required. Uses QUIC (UDP-based) as the transport layer protocol.

## Key Information
- Available to all customers; zero additional deployment required
- No open inbound ports needed on either Client or Connector
- Automatically selects lowest-latency transport (P2P preferred, relay as fallback)
- Same-LAN connections use direct local path (no NAT hairpinning required)
- Transport protocol: QUIC (RFC 9000), built on UDP

## Connection Establishment Flow
1. **Signaling channel** — Client and Connector both connect outbound to Twingate's globally distributed relay infrastructure
2. **Peer discovery** — STUN server (hosted in Twingate relay infra) discovers public IP:port for each peer; local network address also collected as candidate
3. **Candidate exchange** — Signaling channel distributes candidate addresses to each peer
4. **NAT traversal** — Peers attempt direct connection using exchanged candidates

## Fallback Behavior
- When NAT traversal fails (blocked ports, incompatible NAT types), traffic routes through Twingate's relay infrastructure
- Relays are globally distributed with public addresses — always reachable
- Switching between P2P and relay is automatic and transparent

## Configuration Values
- **None required** — fully automatic, no CLI flags, env vars, or API params to set

## QUIC Protocol Details
| Feature | Detail |
|---|---|
| Base protocol | UDP |
| TLS support | TLS 1.3 only |
| Initial connection | 1 RTT |
| Connection resumption | 0 RTT |
| Multiplexing | Multiple streams over single connection |
| Head-of-line blocking | Eliminated (per-stream loss recovery) |
| IP/port changes | Survived (client roaming support) |

## Gotchas
- P2P is not guaranteed — incompatible NAT configurations will fall back to relay automatically
- QUIC requires UDP to be unblocked on the network; heavily restrictive firewalls blocking UDP may prevent P2P (relay still works)
- Local network detection avoids NAT hairpinning dependency — relevant if your NAT doesn't support hairpinning
- QUIC's performance advantages over TCP+TLS are primarily latency-focused, not raw throughput

## Prerequisites
- No special prerequisites; works with existing Client and Connector deployments

## Related Docs
- Twingate Relay Infrastructure
- Twingate Client documentation
- Twingate Connector documentation
- RFC 9000 (QUIC specification)
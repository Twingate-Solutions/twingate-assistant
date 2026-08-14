---
source: https://www.twingate.com/docs/peer-to-peer-communication-in-twingate
type: docs
fetched: 2026-08-14
source_version: 3c33fe034ad77a6f4a90aade6091d7121057e111fc92084f384c3ea748057a56
---

# Peer-to-Peer Communication in Twingate

## Summary
Twingate enables peer-to-peer connections between Clients and Connectors using NAT traversal via STUN, with relay infrastructure as automatic fallback. No configuration, open inbound ports, or additional deployment is required. The feature uses QUIC (UDP-based) as the transport protocol.

## Key Information
- Available to all customers; zero additional deployment for existing setups
- Transparent to end users and administrators
- Automatically selects lowest-latency transport (P2P preferred, relay as fallback)
- Uses QUIC protocol (RFC 9000) over UDP for transport layer
- No open inbound ports required on either Client or Connector side

## Connection Establishment Flow
1. **Signaling channel**: Client and Connector both connect to Twingate's globally distributed Relay Infrastructure on startup
2. **Discover peer candidates**: STUN server (hosted in Twingate relay infra) discovers public IP:port assigned by NAT
3. **Exchange candidates**: Peers exchange candidate addresses via signaling channel
4. **Negotiate connection**: Peers attempt direct P2P connection using candidate addresses (NAT traversal)
5. **Fallback**: If P2P fails (blocked ports, incompatible NAT), traffic routes through relay infrastructure

## Configuration Values
- None required — fully automatic

## QUIC Protocol Details
| Feature | Detail |
|---|---|
| Base protocol | UDP |
| TLS version | 1.3+ only |
| Initial connection | 1 round-trip |
| Connection resumption | 0 round-trips |
| Multiplexing | Multiple app flows → individual QUIC streams over single connection |

## Benefits Over TCP+TLS
- **Faster handshake**: 1-RTT initial, 0-RTT resumption
- **Client roaming**: Survives IP/port changes (NAT rebinding, network switches)
- **No head-of-line blocking**: Per-stream reliability; packet loss on one stream doesn't block others
- **Modern crypto**: TLS 1.3 mandatory

## Gotchas
- P2P is not guaranteed — incompatible NAT types or blocked UDP ports will trigger relay fallback automatically
- Relay fallback is always available globally but may have higher latency than direct P2P
- QUIC runs on UDP; firewalls blocking UDP outbound will prevent P2P (relay via TCP may still work — verify firewall rules)

## Related Docs
- Twingate Client documentation
- Twingate Connector documentation
- Relay Infrastructure documentation
- [RFC 9000 (QUIC)](https://datatracker.ietf.org/doc/html/rfc9000)
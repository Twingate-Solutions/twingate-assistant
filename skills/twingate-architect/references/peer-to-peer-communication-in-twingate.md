# Peer-to-Peer Communication in Twingate

## Summary
Twingate enables peer-to-peer connections between Clients and Connectors using NAT traversal, with automatic fallback to relay infrastructure when direct connections aren't possible. Uses QUIC (UDP-based) as the transport protocol. No configuration required; works transparently for all customers.

## Key Information
- Available to all Twingate customers; no additional deployment needed
- No open inbound ports required on either Client or Connector
- Automatically selects lowest-latency transport (P2P preferred, relay as fallback)
- Uses QUIC protocol (RFC 9000) over UDP
- Relay infrastructure is globally distributed and always accessible as backup

## Connection Establishment Flow
1. **Signaling channel**: Client and Connector both connect to Twingate's Relay Infrastructure (publicly accessible)
2. **Peer discovery**: STUN server (hosted in Twingate relay infra) discovers public IP:port behind NAT
3. **Address exchange**: Each peer receives candidate addresses for its partner via signaling channel
4. **NAT traversal**: Peers attempt direct connection using candidate addresses

## When P2P Fails
- Fallback: Twingate relay infrastructure (transport layer)
- Triggers: blocked ports, incompatible NAT configurations
- Automatic — no manual intervention needed

## QUIC Protocol Details
| Feature | Detail |
|---|---|
| Base protocol | UDP |
| TLS support | TLS 1.3+ only |
| Standardization | IETF RFC 9000 |
| Initial connection | 1 round-trip |
| Connection resumption | 0 round-trips |

**QUIC advantages over TCP+TLS:**
- No head-of-line blocking (packet loss affects only impacted streams, not all)
- Faster connection establishment
- Client-side roaming: survives IP/port changes (NAT rebinding, network switches)
- Multiplexes concurrent data flows from multiple applications over single connection
- Better packet loss recovery

## Configuration Values
None required. Feature is automatic and zero-configuration.

## Gotchas
- Direct P2P is **not always achievable** — incompatible NAT types or firewall rules blocking UDP will force relay fallback
- QUIC runs over UDP — ensure UDP is not broadly blocked in network environments where Connectors are deployed
- Relay fallback adds latency; P2P is always preferred when possible

## Prerequisites
- No special prerequisites; works with existing Client and Connector deployments
- UDP traffic should not be blocked if P2P performance is desired

## Related Docs
- Twingate Client documentation
- Twingate Connector documentation
- Relay Infrastructure documentation
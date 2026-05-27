# Peer-to-Peer Communication in Twingate

## Summary
Twingate enables peer-to-peer connections between Clients and Connectors using NAT traversal, eliminating the need for open inbound ports. When direct P2P isn't possible, Twingate automatically falls back to relay infrastructure. No additional configuration or deployment is required.

## Key Information
- Available to all Twingate customers; no extra deployment needed
- Transparent to end users and administrators
- Automatically selects lowest-latency transport option
- Uses QUIC (UDP-based) as the transport layer protocol
- Relay infrastructure serves as global backup when P2P fails

## Connection Establishment Flow
1. **Signaling channel**: Client and Connector both connect to Twingate's Relay Infrastructure (publicly accessible, globally distributed)
2. **Peer discovery**: STUN server (hosted in Twingate relay infra) discovers public IP:port assigned by NAT
3. **Address exchange**: Each peer receives candidate addresses for its partner via signaling channel
4. **NAT traversal**: Peers use candidate addresses to attempt direct P2P connection

## Fallback Behavior
- When NAT traversal fails (blocked ports, incompatible NAT layers), traffic routes through relay infrastructure
- Relays have public addresses and are globally available
- Automatic failover — no configuration required

## Technical Implementation (QUIC)
- Built on **QUIC** protocol (RFC 9000, IETF standardized)
- QUIC runs over UDP with its own reliable delivery mechanisms
- Multiple application data flows map to individual QUIC streams over a single connection

**QUIC advantages over TCP+TLS:**
| Feature | Detail |
|---|---|
| Connection setup | Single round trip (resumption = zero RTT) |
| Crypto | TLS 1.3 minimum |
| Roaming | Survives client IP/port changes (NAT rebinding, network switches) |
| Head-of-line blocking | Eliminated — packet loss affects only impacted streams |
| Packet loss recovery | More efficient than TCP |

## Configuration Values
- No configuration required on Client or Connector side
- No inbound ports need to be opened

## Gotchas
- P2P is **not guaranteed** — incompatible NAT types or firewall rules blocking UDP can prevent direct connections; relay is always the fallback
- QUIC uses UDP; firewalls that block UDP outbound may impact P2P performance (relay still works)
- Outbound connectivity to Twingate relay infrastructure must be available from both Client and Connector

## Related Docs
- Twingate Connector deployment
- Twingate Relay Infrastructure
- Resource access configuration
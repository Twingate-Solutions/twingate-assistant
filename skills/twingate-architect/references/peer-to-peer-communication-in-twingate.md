# Peer-to-Peer Communication in Twingate

## Summary
Twingate enables peer-to-peer connections between Clients and Connectors using NAT traversal, eliminating the need for open inbound ports. When direct P2P fails, traffic automatically falls back to Twingate's global relay infrastructure. No additional configuration or deployment is required.

## Key Information
- Available to all customers; no additional deployment needed
- Transparent to end users and administrators
- Uses QUIC (UDP-based) as the transport protocol
- Automatically selects lowest-latency transport method
- Relay infrastructure serves as automatic fallback when NAT traversal fails

## Connection Establishment Flow
1. **Signaling channel**: Client and Connector connect to Twingate's Relay Infrastructure (publicly accessible)
2. **Peer discovery**: STUN server (hosted in Twingate relay infra) discovers public IP:port assigned by NAT layer
3. **Address exchange**: Each peer receives candidate addresses for its partner via the signaling channel
4. **Connection negotiation**: Peers use candidate addresses to attempt direct P2P connection via NAT traversal

## Fallback Behavior
- Direct P2P fails when: ports are blocked, NAT layers are incompatible
- Fallback: Twingate's globally distributed relay infrastructure (always reachable)
- Failover is automatic; no configuration required

## Technical Implementation (QUIC)
- Protocol: QUIC (RFC 9000), built on UDP
- Replaces TCP+TLS for transport layer

**QUIC advantages used by Twingate:**
- **Faster handshake**: 1 round-trip initial connection; 0-RTT resumption
- **No head-of-line blocking**: Independent stream delivery; packet loss affects only impacted streams
- **Client roaming**: Connections survive IP/port changes (NAT rebinding, network switches)
- **Cryptography**: TLS 1.3 minimum
- **Multi-app multiplexing**: Individual app data flows map to single QUIC streams per Connector

## Configuration Values
- None required — fully automatic

## Gotchas
- P2P traversal is **not guaranteed**; symmetric NAT or firewall rules blocking UDP may prevent it, triggering relay fallback
- Relay fallback adds latency compared to direct P2P — if performance matters, ensure UDP is not blocked between Client and Connector
- QUIC runs over UDP; environments that block or rate-limit UDP will impact P2P capability

## Prerequisites
- No special prerequisites; works with existing Twingate Client and Connector deployments

## Related Docs
- Twingate Relay Infrastructure
- Twingate Client documentation
- Twingate Connector documentation
- [RFC 9000 (QUIC)](https://datatracker.ietf.org/doc/html/rfc9000)
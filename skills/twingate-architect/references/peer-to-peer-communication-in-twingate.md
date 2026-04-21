## Page Title
Peer-to-Peer Communication in Twingate

## Summary
Describes how Twingate establishes direct peer-to-peer connections between Clients and Connectors using QUIC and NAT traversal, with Relay infrastructure as an automatic fallback. No configuration required; available on all plans; transparent to users and admins.

## Key Information
- P2P uses QUIC (UDP-based, RFC 9000) for transport — faster connection establishment, better packet loss handling than TCP
- Connection flow: (1) Client and Connector register with Relay via outbound connection; (2) STUN resolves public IP:port for each peer; (3) candidate addresses exchanged via signaling channel; (4) NAT traversal attempted for direct connection
- Relay used as fallback when P2P is not possible (symmetric NAT, blocked UDP ports) — always accessible, globally distributed
- Twingate automatically selects lowest-latency transport (P2P preferred, Relay fallback) — no config or admin action needed
- QUIC advantages over TCP+TLS: single round-trip initial connection; TLS 1.3 only; connection survives IP/port changes (client-side roaming, network switches); better multi-stream performance
- Available to all Twingate plans with no additional deployment

## Prerequisites
None — available automatically on all deployments.

## Step-by-Step
Not applicable — fully automatic.

## Configuration Values
None — P2P is enabled by default with no configuration.

## Gotchas
- P2P requires UDP to be unblocked between Client and Relay (STUN); strict firewalls that block all UDP will fall back to Relay transport
- Relay fallback does NOT mean plaintext — data remains end-to-end encrypted; Relay only forwards encrypted packets
- P2P may not establish in environments with symmetric NAT — Relay fallback handles this automatically
- Client-side roaming (IP/port changes) is handled by QUIC without dropping connections

## Related Docs
- `/docs/how-twingate-works` — full architecture context
- `/docs/understanding-relays` — Relay infrastructure detail
- `/docs/how-nat-traversal-works` — NAT traversal mechanics
- `/docs/troubleshooting-p2p` — diagnosing P2P connection failures
- `/docs/local-peer-to-peer-best-practices` — P2P optimization for local networks

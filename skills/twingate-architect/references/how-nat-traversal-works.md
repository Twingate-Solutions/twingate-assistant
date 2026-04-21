## Page Title
How NAT Traversal Works

## Summary
Explains how Twingate establishes peer-to-peer tunnels between Clients and Connectors without opening any inbound ports, using NAT traversal as the primary method and Relay infrastructure as fallback. Covers NAT fundamentals, port mechanics, and the step-by-step ICE/STUN-style candidate exchange process Twingate uses.

## Key Information
- **No open inbound ports required** — Twingate never requires inbound port forwarding
- **Two transport methods**: (1) Relay intermediary — both Client and Connector connect outbound to public Relay, which forwards encrypted packets; (2) NAT traversal — direct P2P tunnel
- **NAT basics**: private IPs (e.g. 192.168.x.x) are translated to public IP:port by router; firewalls allow inbound only from previously established outbound connections
- **NAT traversal flow**:
  1. Client and Connector both register with Relay (acting as STUN server) — share public IP:port
  2. Relay distributes each peer's address to the other
  3. Client and Connector simultaneously send packets to each other's public IP:port
  4. Simultaneous outbound packets "punch holes" in each NAT — inbound packets from the other peer are now allowed
  5. P2P tunnel established
- **Relay fallback**: used when symmetric NAT or blocked UDP prevents P2P; Relays are globally distributed; traffic is end-to-end encrypted through Relay (Relay cannot decrypt)
- Opening inbound ports is explicitly called out as dangerous and not required by Twingate

## Prerequisites
- Understanding of Twingate architecture (Client, Connector, Relay roles)

## Step-by-Step
Not applicable — this is a reference/explainer page.

## Configuration Values
None — P2P and Relay transport are automatic with no configuration.

## Gotchas
- Symmetric NAT environments will fall back to Relay — P2P is not guaranteed
- Relay fallback does not mean unencrypted — end-to-end encryption is maintained
- Port forwarding (opening inbound ports) is explicitly discouraged; Twingate's design avoids it entirely

## Related Docs
- `/docs/peer-to-peer-communication-in-twingate` — QUIC transport layer detail
- `/docs/understanding-relays` — Relay infrastructure
- `/docs/how-twingate-works` — full architecture overview
- `/docs/troubleshooting-p2p` — diagnosing P2P failures

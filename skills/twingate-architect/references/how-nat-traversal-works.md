---
source: https://www.twingate.com/docs/how-nat-traversal-works
type: docs
fetched: 2026-09-20
source_version: 6cd71cb52de90f67265a99902177262670dd4810da4e014cf6e439ab5f6d2fb5
---

# How NAT Traversal Works

## Page Title
How NAT Traversal Works

## Summary
Twingate establishes secure Client-to-Connector connections without opening inbound ports using two methods: Relay-based intermediary connections and NAT traversal for direct peer-to-peer (P2P) tunnels. NAT traversal works by coordinating simultaneous outbound connections from both Client and Connector through a Relay acting as a signaling broker, leveraging firewall behavior that permits inbound packets from addresses the local device has already sent packets to.

## Key Information
- **No open inbound ports required** — core security principle of Twingate's architecture
- **Two connectivity methods:**
  1. **Relays** — global intermediaries; both Client and Connector make outbound connections; traffic is end-to-end encrypted (Relay cannot decrypt)
  2. **NAT Traversal** — direct P2P tunnel; removes relay hop, reduces latency
- **NAT traversal mechanism:** Relay acts as STUN server + signaling broker; exchanges public IP/port between Client and Connector; coordinates simultaneous outbound connections so each side's firewall permits inbound packets from the other
- **Local network optimization:** Client and Connector also exchange local (private) IP addresses; if on same LAN, attempt direct local connection in parallel with NAT traversal; avoids dependency on NAT hairpinning support
- **Relays are worldwide** to minimize latency when P2P fails or isn't possible
- Firewalls permit inbound packets from a public IP:port **only if** the local device previously sent packets to that same IP:port

## Prerequisites
- Understanding of private vs. public IP addresses
- No open inbound ports needed on Connector or Client networks

## Step-by-Step: NAT Traversal P2P Establishment
1. Client and Connector each connect outbound to Relay; Relay records their public IP:port combinations
2. Relay creates an encrypted signaling channel between Client and Connector
3. Client and Connector exchange public IP:port (and local IP:port) via signaling channel
4. Relay coordinates **simultaneous** outbound packet sends from both sides to each other's public IP:port
5. Each firewall sees prior outbound traffic to the other's address → permits inbound packets
6. P2P tunnel established; Relay no longer in data path

## Configuration Values
- No user-configurable parameters documented on this page
- Port **443** referenced as example (HTTPS convention)
- IP ports range: 1–65,535

## Gotchas
- **NAT hairpinning** not supported by all routers — two devices on the same LAN may fail to reach each other via public IP; Twingate handles this with parallel local connection attempts
- **Opening inbound ports is strongly discouraged** — open ports are continuously scanned by bots and probed for vulnerabilities
- Relay fallback occurs when P2P cannot be established due to restrictive network conditions
- Relay cannot decrypt Client↔Connector traffic (end-to-end encryption excludes Relay)

## Related Docs
- [Troubleshooting peer-to-peer and NAT traversal](https://www.twingate.com/docs/) — referenced for P2P connection issues
- Twingate Relay documentation (referenced inline, separate page)
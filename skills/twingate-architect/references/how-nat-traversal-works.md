# How NAT Traversal Works

## Summary
Twingate establishes secure Client-to-Connector connections without requiring open inbound ports using two methods: Relay servers (intermediaries) and NAT traversal (peer-to-peer tunnels). NAT traversal uses the Relay as a coordination/STUN server to exchange public IP/port information, then both parties simultaneously initiate outbound connections to each other.

## Key Information
- Twingate **never requires open inbound ports** on any network device
- Two connectivity methods: **Relay-based** (intermediary) and **NAT traversal** (P2P)
- NAT traversal preferred: removes extra hop, reduces latency vs. Relay routing
- All traffic is **end-to-end encrypted**; Relays cannot decrypt traffic in transit
- Relays serve dual role: P2P traffic fallback AND STUN/coordination server for NAT traversal setup
- Firewalls allow inbound packets only from IP:port combinations that received prior outbound packets

## How NAT Traversal Works (Step-by-Step)
1. Client and Connector both connect to a Relay, reporting their public IP address and port
2. Relay acts as STUN server — returns each party's public IP:port to the other
3. Relay establishes an encrypted messaging channel between Client and Connector
4. Client and Connector exchange public IP:port info via this channel
5. Both **simultaneously** send packets to each other's public IP:port
6. Each party's firewall now accepts inbound packets from the other (prior outbound connection satisfies firewall rules)
7. P2P tunnel established — no open inbound ports required

## Firewall Rule That Makes This Possible
> Inbound packets from a public IP:port are allowed **if and only if** outbound packets were previously sent to that same IP:port from within the private network.

## Configuration Values
- No special port forwarding or firewall rules required on user networks
- Port **443** used by convention for HTTPS (referenced as example); Twingate uses its own port configuration
- Relays deployed globally to minimize latency

## Gotchas
- **Certain network conditions can prevent P2P establishment** — system falls back to Relay routing automatically
- Opening inbound ports is explicitly discouraged; bots continuously scan public IPs for open ports
- P2P requires **simultaneous** outbound connection initiation — timing is coordinated by the Relay
- Symmetric NAT environments may block NAT traversal (see troubleshooting guide)
- Relay-only routing adds latency; P2P is preferred when network conditions allow

## Related Docs
- [Troubleshooting NAT traversal / P2P connections](https://www.twingate.com/docs/) — for cases where P2P cannot be established
- Twingate Relay infrastructure documentation
- Twingate Connector deployment documentation
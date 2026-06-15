# How NAT Traversal Works

## Summary
Twingate establishes secure Client-to-Connector connections without open inbound ports using two methods: Relay servers (intermediaries) and NAT traversal (peer-to-peer). NAT traversal uses the Relay as a coordination broker to simultaneously exchange public IP/port information, enabling direct P2P tunnels. When NAT traversal fails due to network conditions, traffic falls back to Relay routing.

## Key Information
- **No open inbound ports required** — core architectural principle
- Two connectivity methods: Relay (intermediary) and NAT traversal (P2P)
- NAT translates private IPs (e.g., `192.168.1.4`) to public IPs using port mapping to track sessions
- Firewalls allow inbound packets **only** from IP+port combinations that received prior outbound packets
- Each IP address has 65,535 ports; NAT devices track sessions via source IP+port → public IP+port mappings
- Relays are deployed globally to minimize latency when used as fallback
- Traffic between Client and Connector is **end-to-end encrypted** — Relays cannot decrypt it

## NAT Traversal Flow (Step-by-Step)

1. Client and Connector both connect outbound to the Relay (acting as STUN server + broker)
2. Relay shares each party's public IP address and port with the other
3. Relay coordinates **simultaneous** outbound packet transmission from both Client and Connector
4. Each side's firewall allows inbound packets because it already sent packets to that IP+port
5. P2P tunnel established — Relay no longer needed for data path

## Relay Flow (Fallback)
1. Both Client and Connector initiate outbound connections to Relay
2. Relay forwards packets between both parties
3. All traffic remains E2E encrypted; Relay cannot inspect content

## Configuration Values
- HTTPS port **443** — standard convention referenced for illustration
- Private IP ranges — not routable publicly (e.g., `192.168.x.x`)
- No specific env vars or CLI flags documented on this page

## Gotchas
- **Certain network conditions can prevent P2P establishment** — falls back to Relay automatically
- Opening inbound ports defeats the security model; never required by Twingate
- NAT port replacement: source private IP+port → public IP + newly assigned port (mapping tracked by NAT device)
- Simultaneous packet sending is required — timing is coordinated by the Relay
- Symmetric NAT configurations may block NAT traversal (see troubleshooting guide)

## Related Docs
- [Troubleshooting NAT traversal / peer-to-peer issues](https://www.twingate.com/docs/) — linked from page as "troubleshooting guide"
- Twingate Relays worldwide deployment documentation
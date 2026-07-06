# Firewall Failures - Twingate Troubleshooting

## Page Title
Firewall, NAT, and Routing Issues

## Summary
Twingate requires no inbound firewall rules but has specific outbound connectivity requirements. Performance issues typically stem from falling back to Relay connections instead of direct Peer-to-Peer (P2P) connections, usually caused by blocked UDP or incompatible NAT configurations.

## Key Information
- **P2P connections**: Direct encrypted tunnel between Client and Connector — preferred, lower latency
- **Relay connections**: Traffic routed through Twingate's public infrastructure — secure but higher latency
- Relayed connections indicate P2P negotiation failed
- STUN Discovery must show "Available" in Admin Console for P2P to work

## Common Symptoms
- Users report slow/laggy resource access
- Admin Console Connector details show most/all connections as "Relayed"
- Client or Connector fails to connect entirely

## Configuration Values / Required Outbound Rules

| Destination | Protocol/Port | Purpose |
|-------------|--------------|---------|
| `*.twingate.com` | TCP 443 | Controller & Relay communication |
| Twingate Relay infrastructure | TCP 30000–31000 | Relayed connection fallback |
| All destinations | UDP (all ports) | P2P / NAT traversal — **critical** |
| STUN servers | UDP 3478 | STUN Discovery for P2P |

## Troubleshooting Steps

1. **Verify outbound firewall rules** — confirm all ports in table above are permitted on both client-side and connector-side networks
2. **Check for blocked UDP/QUIC** — use `nmap` from Connector host to test outbound UDP reachability
3. **Check NAT type** — P2P requires **endpoint-independent NAT**; symmetric NAT breaks traversal
4. **Check for double NAT** — two NAT layers will break P2P connections
5. **Confirm STUN Discovery status** — in Admin Console → Connector details page; must show "Available"

## Gotchas
- **Blocked outbound UDP is the #1 cause** of relayed connections and performance issues
- **AWS NAT Gateway** is known to be incompatible with robust NAT traversal — use a self-hosted EC2 NAT instance or AWS Marketplace NAT product instead
- Enterprise firewalls often use symmetric NAT, which is incompatible with P2P traversal
- Double NAT scenarios (common in home/office setups with multiple routers) break P2P

## Prerequisites
- Access to Admin Console to check Connector connection details
- Ability to modify firewall/NAT rules on both client and connector networks
- `nmap` or equivalent tool for UDP connectivity testing

## Related Docs
- How to troubleshoot peer-to-peer connections
- Outbound connectivity requirements
- Split tunneling (for local device conflicts when network path is clear)
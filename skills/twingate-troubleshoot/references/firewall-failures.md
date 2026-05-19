# Firewall Failures - Twingate Troubleshooting

## Summary
Twingate requires no inbound firewall rules but has specific outbound connectivity requirements. Performance issues typically stem from connections falling back to Relay mode instead of Peer-to-Peer (P2P), usually caused by blocked UDP or incompatible NAT configurations.

## Key Information
- **P2P connections**: Direct encrypted tunnel between Client and Connector — lower latency
- **Relay connections**: Traffic routed through Twingate's public infrastructure — higher latency fallback
- Relayed connections are secure but slower; most performance issues trace back to P2P failure
- STUN Discovery must show "Available" in Admin Console as a prerequisite for P2P

## Common Symptoms
- Users report slow/laggy access to Resources
- Admin Console Connector details show most/all connections as "Relayed"
- Client or Connector fails to connect entirely

## Required Outbound Connectivity

| Destination | Protocol/Port | Purpose |
|---|---|---|
| `*.twingate.com` | TCP 443 | Controller and Relay communication |
| Twingate Relay infrastructure | TCP 30000–31000 | Relayed connection fallback |
| All destinations | UDP (any port) | P2P / NAT traversal — **critical** |
| STUN servers | UDP 3478 | STUN Discovery for P2P |

## Troubleshooting Steps

1. **Verify outbound firewall rules** — confirm all ports in table above are allowed on both Client and Connector networks
2. **Check for blocked UDP/QUIC** — use `nmap` from Connector host to test outbound UDP; blocked UDP is #1 cause of relayed connections
3. **Check NAT type** — P2P requires endpoint-independent NAT; symmetric NAT and double-NAT scenarios break P2P
4. **Check Admin Console** — navigate to Connector details page; verify STUN Discovery shows "Available"
5. **If STUN unavailable** — check outbound UDP 3478 is not blocked

## Gotchas
- **AWS NAT Gateway** is known to be incompatible with robust NAT traversal; use a self-hosted EC2 NAT instance or third-party NAT from AWS Marketplace instead
- Enterprise firewalls are more likely to use symmetric NAT (incompatible) than consumer routers
- Double-NAT (device behind two router layers) breaks P2P even if individual NAT types would otherwise be compatible
- Overzealous firewalls blocking all outbound UDP are the most common cause of relayed connections

## Related Docs
- [Outbound connectivity requirements](#) — full port/destination list
- [How to troubleshoot peer-to-peer connections](#) — detailed P2P diagnostics
- [Split tunneling](#) — for local device conflicts after resolving network path issues
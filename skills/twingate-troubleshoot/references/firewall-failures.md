# Firewall Failures - Twingate Troubleshooting

## Page Title
Firewall, NAT, and Routing Issues

## Summary
Twingate requires no inbound firewall rules but has specific outbound connectivity requirements. Performance issues typically stem from connections being forced through Twingate's Relay infrastructure instead of direct Peer-to-Peer (P2P) tunnels. Diagnosing slowness means diagnosing why P2P establishment is failing.

## Key Information
- **P2P connection**: Direct encrypted tunnel between Client and Connector — preferred, lower latency
- **Relay connection**: Traffic routed through Twingate's public relay infrastructure — secure but potentially higher latency
- **#1 cause of relayed connections**: Firewalls blocking outbound UDP
- STUN Discovery must show "Available" in Admin Console for P2P to work

## Common Symptoms
- Users report slow/laggy Resource access
- Admin Console shows most/all connections as "Relayed"
- Client or Connector fails to connect entirely

## Prerequisites
- Access to firewall/NAT configuration on both client-side and connector-side networks
- Admin Console access to check Connector connection details

## Required Outbound Connectivity

| Destination | Protocol/Port | Purpose |
|-------------|--------------|---------|
| `*.twingate.com` | TCP 443 | Controller & Relay communication |
| Twingate Relay infrastructure | TCP 30000-31000 | Relay fallback |
| All destinations | UDP (any port) | P2P / NAT traversal |
| STUN servers | UDP 3478 | STUN Discovery for P2P |

## Step-by-Step Troubleshooting

1. **Verify outbound firewall rules** — confirm TCP 443, TCP 30000-31000, and all outbound UDP are permitted on both client and connector networks
2. **Check Admin Console** — navigate to Connector details page; verify "STUN Discovery" shows "Available"
3. **Test UDP availability** — use `nmap` from the Connector host to test outbound UDP to a public endpoint
4. **Check NAT type** — confirm NAT is endpoint-independent (not symmetric); symmetric NAT breaks P2P
5. **Identify double-NAT** — devices behind two router layers can prevent P2P establishment
6. **AWS-specific**: Replace AWS NAT Gateway with a self-hosted EC2 NAT instance or AWS Marketplace NAT product if P2P is required

## Configuration Gotchas
- **AWS NAT Gateway** is known incompatible with robust NAT traversal — do not use for P2P-critical deployments
- **Symmetric NAT** (common in enterprise firewalls) blocks P2P traversal even if UDP is permitted
- **Double NAT** scenarios break P2P regardless of firewall rules
- Blocking UDP port 3478 prevents STUN Discovery, disabling P2P entirely
- Enterprise firewalls that block QUIC/UDP by default require explicit UDP allowlisting

## Related Docs
- [Outbound Connectivity Requirements](https://www.twingate.com/docs/outbound-connectivity)
- [How to Troubleshoot Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- Split Tunneling (for local device conflicts after network path is confirmed clear)
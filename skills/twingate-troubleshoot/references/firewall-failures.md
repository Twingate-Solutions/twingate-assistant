# Firewall Failures - Twingate Troubleshooting

## Page Title
Firewall Failures: How to Troubleshoot Firewall and NAT Issues

## Summary
Twingate requires no inbound firewall rules but has specific outbound connectivity requirements. Performance issues typically stem from connections falling back to Relay mode instead of establishing direct Peer-to-Peer (P2P) tunnels. The primary causes are blocked outbound UDP and incompatible NAT configurations.

## Key Information
- **P2P connection**: Direct encrypted tunnel between Client and Connector — lowest latency
- **Relay connection**: Traffic routed through Twingate's public infrastructure — secure but higher latency
- **#1 cause of relay fallback**: Firewalls blocking outbound UDP traffic
- STUN Discovery must show "Available" in Admin Console for P2P to function

## Common Symptoms
- Users report slow/laggy Resource access
- Admin Console shows most/all connections as "Relayed"
- Client or Connector fails to connect entirely

## Prerequisites
- Access to firewall rules on both client network and Connector network
- Admin Console access to check Connector details

## Configuration Values

| Destination | Protocol | Port | Purpose |
|-------------|----------|------|---------|
| `*.twingate.com` | TCP | 443 | Controller and Relay communication |
| Twingate Relay infrastructure | TCP | 30000–31000 | Relay fallback |
| All destinations | UDP | Any | P2P/NAT traversal (critical) |
| STUN servers | UDP | 3478 | STUN discovery for P2P |

## Step-by-Step Troubleshooting

1. **Verify outbound firewall rules** — Confirm TCP 443, TCP 30000-31000, and all outbound UDP are allowed on both client and Connector networks
2. **Check for blocked UDP/QUIC** — Test from Connector host using `nmap` against a public test port
3. **Check STUN Discovery status** — In Admin Console → Connector details page; must show "Available"
4. **Diagnose NAT type** — Confirm NAT is endpoint-independent (not symmetric NAT)
5. **Check for double NAT** — Two layers of routers will break P2P

## Gotchas
- **AWS NAT Gateway**: Known incompatible with robust NAT traversal. Use a self-hosted EC2 NAT instance or AWS Marketplace NAT alternative for P2P-critical deployments
- **Symmetric NAT**: Enterprise firewalls often use symmetric NAT, which breaks P2P — consumer routers typically use compatible endpoint-independent NAT
- **Double NAT**: Device behind two router layers breaks P2P connections
- Overly restrictive enterprise firewalls blocking UDP is the single most common cause of performance issues
- If connectivity is fine but local device conflicts exist, the issue is likely split tunneling (separate concern)

## Related Docs
- How to troubleshoot peer-to-peer connections
- Outbound connectivity requirements
- Split tunneling documentation
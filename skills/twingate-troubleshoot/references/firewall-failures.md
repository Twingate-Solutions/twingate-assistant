# Firewall Failures - Twingate Troubleshooting

## Page Title
Firewall, NAT, and Routing Issues

## Summary
Twingate requires no inbound firewall rules but has specific outbound connectivity requirements. Performance issues typically stem from connections falling back to Relay mode instead of establishing direct Peer-to-Peer (P2P) tunnels. Root cause is almost always blocked outbound UDP or incompatible NAT configuration.

## Key Information
- **P2P connection**: Direct encrypted tunnel between Client and Connector — lower latency
- **Relay connection**: Traffic routed through Twingate's public infrastructure — secure but higher latency
- Relayed connections appear in Admin Console on the Connector details page
- STUN Discovery status on Connector details page indicates P2P readiness

## Common Symptoms
- Users report slow/laggy access to Resources
- Admin Console shows most/all connections as "Relayed"
- Client or Connector fails to connect entirely

## Prerequisites
- Access to Admin Console (Connector details page)
- Ability to modify firewall/NAT rules on both client-side and connector-side networks
- Network diagnostic tools (e.g., `nmap`)

## Configuration Values

| Destination | Protocol/Port | Purpose |
|-------------|---------------|---------|
| `*.twingate.com` | TCP 443 | Controller and Relay communication |
| Twingate Relay infrastructure | TCP 30000–31000 | Relayed connection fallback |
| All destinations | UDP (all ports) | P2P/NAT traversal — **critical** |
| STUN servers | UDP 3478 | STUN Discovery for P2P |

## Step-by-Step Troubleshooting

1. **Check Admin Console** → Connector details → verify connection types (Relayed vs. P2P) and STUN Discovery status
2. **Verify outbound TCP 443** from both Client and Connector networks to `*.twingate.com`
3. **Verify outbound UDP is unrestricted** — blocked UDP is the #1 cause of relay fallback
4. **Verify UDP 3478 is not blocked** — required for STUN Discovery
5. **Test UDP connectivity** from Connector host using `nmap` against a public test port
6. **Audit NAT type** — must be endpoint-independent NAT; symmetric NAT breaks P2P
7. **Check for double NAT** — two router layers can break P2P traversal
8. **AWS deployments**: Replace AWS NAT Gateway with EC2-based NAT instance or marketplace NAT product

## Gotchas
- **AWS NAT Gateway is incompatible** with robust NAT traversal — use self-hosted EC2 NAT or marketplace alternative
- Enterprise firewalls often use symmetric NAT, which blocks P2P regardless of port rules
- Blocking outbound UDP entirely is the single most common misconfiguration
- Double NAT scenarios (home router + corporate VPN, nested cloud networks) silently break P2P

## Related Docs
- [Outbound connectivity requirements](#) — specific port/protocol requirements
- [How to troubleshoot peer-to-peer connections](#) — detailed P2P diagnostics
- Split tunneling guide — for local device conflicts when network path is clear
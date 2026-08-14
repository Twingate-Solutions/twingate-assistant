---
source: https://www.twingate.com/docs/firewall-failures
type: docs
fetched: 2026-08-14
source_version: 234a480da022830fd4018272a51ee28d598bef23e81e2b8e3d9067662932e3ae
---

# Firewall Failures - Twingate Troubleshooting

## Summary
Twingate requires no inbound firewall rules but has specific outbound connectivity requirements. Performance issues typically stem from connections falling back to Relay mode instead of direct Peer-to-Peer (P2P), usually caused by blocked UDP or incompatible NAT configurations.

## Key Information
- **P2P connections**: Direct encrypted tunnel between Client and Connector (preferred, lower latency)
- **Relay connections**: Traffic routed through Twingate's public infrastructure (secure but higher latency)
- Relayed connections = P2P failed; diagnosing performance = diagnosing why P2P fails
- AWS NAT Gateway is known incompatible with robust NAT traversal

## Common Symptoms
- Users report slow/laggy Resource access
- Admin Console shows most/all connections as "Relayed"
- Client or Connector fails to connect entirely

## Outbound Connectivity Requirements

| Destination | Protocol/Port | Purpose |
|-------------|---------------|---------|
| `*.twingate.com` | TCP 443 | Controller + Relay communication |
| Twingate Relay infrastructure | TCP 30000-31000 | Relay fallback |
| All destinations | UDP (all ports) | P2P/NAT traversal (**#1 critical requirement**) |
| STUN servers | UDP 3478 | STUN discovery for P2P |

## Troubleshooting Steps

1. **Verify outbound firewall rules** — confirm all ports in table above are allowed from both Client network and Connector network
2. **Check for blocked UDP/QUIC** — use `nmap` from Connector host against a public test port to verify UDP is not blocked
3. **Check NAT type** — P2P requires "endpoint-independent NAT"; symmetric NAT and double-NAT configurations will break P2P
4. **Check Admin Console** — Connector details page shows STUN Discovery status; "Available" is prerequisite for P2P
5. **AWS deployments** — replace AWS NAT Gateway with EC2-based NAT instance or third-party AWS Marketplace NAT product

## Gotchas
- Blocking outbound UDP is the **#1 cause** of relayed connections and performance issues
- Enterprise firewalls often use symmetric NAT — incompatible with Twingate P2P
- Double-NAT (two router layers) breaks P2P connections
- AWS NAT Gateway is explicitly incompatible in some P2P scenarios
- STUN uses UDP 3478 — must not be blocked for P2P to function
- If STUN Discovery shows unavailable in Admin Console, check outbound UDP rules first

## Prerequisites
- Access to Admin Console (Connector details page)
- Ability to modify firewall/NAT rules on both Client-side and Connector-side networks
- `nmap` or equivalent tool for connectivity testing

## Related Docs
- [Outbound connectivity requirements](https://www.twingate.com/docs) (referenced inline)
- [How to troubleshoot peer-to-peer connections](https://www.twingate.com/docs) (referenced inline)
- Split tunneling documentation (for local device conflicts after network path is clear)
# Firewall Failures - Twingate Troubleshooting

## Page Title
Firewall, NAT, and Routing Issues

## Summary
Twingate requires no inbound firewall rules but has specific outbound connectivity requirements. Performance issues typically stem from connections falling back to Relay mode instead of Peer-to-Peer (P2P), usually caused by blocked UDP or incompatible NAT configurations.

## Key Information
- **P2P connections**: Direct encrypted tunnel between Client and Connector — faster, lower latency
- **Relay connections**: Traffic routed through Twingate's public infrastructure — secure but potentially higher latency
- **#1 cause of relay fallback**: Firewalls blocking outbound UDP

## Prerequisites
- Access to firewall/network configuration on both Client and Connector networks
- Admin Console access to verify connection status

## Common Symptoms
- Users report slow/laggy Resource access
- Admin Console shows most/all connections as "Relayed"
- Client or Connector fails to connect entirely

## Required Outbound Rules (Both Clients and Connectors)

| Destination | Protocol/Port | Purpose |
|------------|---------------|---------|
| `*.twingate.com` | TCP 443 | Controller + Relay communication |
| Twingate Relay infrastructure | TCP 30000–31000 | Relay fallback |
| All destinations | UDP (all ports) | P2P / NAT traversal |
| STUN servers | UDP 3478 | STUN discovery for P2P |

## Troubleshooting Steps

1. **Verify outbound firewall rules** — confirm all entries in table above are permitted on both client-side and connector-side networks
2. **Check for blocked UDP/QUIC** — use `nmap` against a public test port from the Connector host to verify UDP is not blocked
3. **Check NAT type** — P2P requires **endpoint-independent NAT**; symmetric NAT or double-NAT will break P2P
4. **Check STUN Discovery in Admin Console** — Connector details page shows if STUN Discovery is "Available"; if not, UDP port 3478 is likely blocked
5. **AWS-specific**: Replace AWS NAT Gateway with a self-hosted EC2 NAT instance or third-party AWS Marketplace NAT product

## Configuration Values
- `*.twingate.com` — wildcard domain for outbound TCP 443
- TCP ports `30000–31000` — relay infrastructure range
- UDP port `3478` — STUN discovery

## Gotchas
- **AWS NAT Gateway** is known incompatible with robust NAT traversal; avoid for P2P-critical deployments
- **Double-NAT** (device behind two router layers) breaks P2P
- **Symmetric NAT** (common in enterprise firewalls) is incompatible with NAT traversal
- Blocking outbound UDP entirely is the single most common misconfiguration

## Related Docs
- Outbound connectivity requirements
- How to troubleshoot peer-to-peer connections
- Split tunneling (for local device conflicts when network path is clear)
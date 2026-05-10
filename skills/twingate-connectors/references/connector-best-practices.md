# Connector Best Practices

## Page Title
Connector Best Practices

## Summary
Guidelines for deploying Twingate Connectors optimally across network environments. Covers redundancy requirements, token management, network requirements, hardware sizing, and load balancing behavior.

## Key Information
- **Minimum 2 Connectors per Remote Network** for redundancy; automatic load balancing and failover are built-in
- Each Connector requires **unique token pairs** — reusing tokens causes connection failures
- Connectors on the same Remote Network must have **identical network scope and permissions** (they're interchangeable)
- Deploy Connectors **co-located with target Resources** to minimize last-mile latency
- Performance bottleneck: add more Connectors, not more CPU/RAM to a single Connector
- Geographic routing: single Remote Network + Connectors in each location → users auto-routed to nearest Connector

## Prerequisites
- Each Connector provisioned separately in the Admin Console to generate unique tokens
- Outbound internet access from Connector host

## Network Requirements
| Traffic Type | Ports | Purpose |
|---|---|---|
| Outbound TCP | 443 | Controller/Relay communication |
| Outbound TCP | 30000–31000 | Relay fallback (no P2P) |
| Outbound UDP/QUIC | 1–65535 | Peer-to-peer (optimal performance) |

- No inbound internet access required or recommended
- Connector host needs routing/permission to access private Resources
- ICMP: explicitly allow if required
- Public exit nodes: require static public IP (direct or via NAT gateway)

## Hardware Recommendations
| Platform | Recommendation |
|---|---|
| AWS | t3a.micro Linux EC2 |
| GCP | e2-small |
| Azure | Container Instance service |
| On-prem/VPS | 1 CPU, 2GB RAM Linux VM |

Hardware priority order: **Network bandwidth > Memory > CPU**

## Gotchas
- Azure Container Instances don't auto-recognize custom VNet DNS — use "Custom DNS" option and specify manually
- Adding CPU/RAM to a single Connector **does not improve performance** — deploy additional Connectors instead
- Tokens cannot be shared; each Admin Console Connector entry = one deployed Connector
- Connectors with mismatched permissions on same Remote Network will cause inconsistent Resource availability

## Load Balancing Behavior
- Automatic when 2+ Connectors exist in same Remote Network
- Client tries next Connector if current one is unreachable
- Connector additions/removals automatically reflected — no manual adjustment needed

## Related Docs
- Understanding Connectors
- Help Me Choose (deployment method selector)
- QUIC/HTTP3 guide (UDP port usage)
- Public exit nodes documentation
- Additional Connectors deployment guide
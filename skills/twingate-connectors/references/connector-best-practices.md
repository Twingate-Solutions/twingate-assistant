# Connector Best Practices

## Page Title
Connector Best Practices

## Summary
Guidelines for deploying Twingate Connectors optimally across network architectures. Covers redundancy, token management, network requirements, hardware sizing, and load balancing behavior.

## Key Information
- Deploy multiple Remote Networks matching your network segments—no benefit to funneling traffic through fewer Connectors
- Minimum **2 Connectors per Remote Network** for load balancing and failover
- Each Connector requires **unique token pair**—reusing tokens causes connection failure
- All Connectors in the same Remote Network should have identical network scope/permissions
- Deploy Connectors co-located with target Resources for best performance
- Load balancing and failover are **automatic** when multiple Connectors exist in a Remote Network
- Geographic routing: create one Remote Network with replicated Resources, deploy Connectors per location—users auto-routed to nearest

## Prerequisites
- Twingate Admin Console access to provision Connectors and generate tokens
- Each Connector provisioned separately in Admin Console before deployment

## Network Requirements
| Direction | Protocol | Ports | Purpose |
|-----------|----------|-------|---------|
| Outbound only | TCP | 443 | Controller/Relay communication |
| Outbound only | TCP | 30000–31000 | Relay fallback (no P2P) |
| Outbound only | UDP/QUIC (HTTP/3) | 1–65535 | P2P connectivity (optimal) |

- **No inbound Internet access** required or recommended
- Connector host needs routing/permissions to reach private Resources
- ICMP must be explicitly permitted if required
- Public exit nodes require static public IP (direct or via NAT gateway)

## Hardware Recommendations
| Platform | Recommendation |
|----------|---------------|
| AWS | t3a.micro Linux EC2 |
| GCP | e2-small |
| Azure | Container Instance service |
| On-prem/VPS | 1 CPU, 2GB RAM Linux VM |

**Optimization priority:** Network bandwidth > Memory > CPU

**Note:** Adding CPU/memory to a single Connector does not improve performance—deploy additional Connectors instead.

## Configuration Values
- Azure Container Instance + custom VNet DNS: use **Custom DNS** option and specify DNS server manually during deployment

## Gotchas
- Reusing tokens across multiple Connectors causes connection failure—provision one Connector in Admin Console per physical Connector
- Adding resources to a single Connector host won't help under load—scale horizontally
- Azure Container Instances don't auto-detect custom VNet DNS servers
- ICMP traffic requires explicit permission on Connector host if needed

## Related Docs
- Understanding Connectors
- Help Me Choose (deployment method selector)
- Public Exit Nodes guide
- UDP/QUIC/HTTP3 configuration guide
- Deploying additional Connectors
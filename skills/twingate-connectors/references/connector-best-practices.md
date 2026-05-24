# Connector Best Practices

## Page Title
Connector Best Practices

## Summary
Best practices for deploying Twingate Connectors covering redundancy, token management, network requirements, and hardware sizing. Connectors only require outbound internet access and automatically load balance/failover when multiple are deployed in the same Remote Network.

## Key Information
- Deploy multiple Remote Networks matching your network architecture segments
- Minimum **2 Connectors per Remote Network** for redundancy (auto load balancing + failover)
- Each Connector requires **unique token pair** — never reuse tokens across Connectors
- All Connectors in same Remote Network must have identical network scope/permissions
- Deploy Connectors co-located with target Resources (minimize "last mile" distance)
- Geographic routing: single Remote Network + Connectors in each region → users route to nearest

## Prerequisites
- Twingate Admin Console access to provision Connectors (generates unique tokens)
- Outbound internet access from Connector host

## Network Requirements
| Traffic Type | Ports | Purpose |
|---|---|---|
| Outbound TCP | 443 | Controller + Relay communication |
| Outbound TCP | 30000–31000 | Relay fallback (non-P2P) |
| Outbound UDP/QUIC (HTTP/3) | 1–65535 | Peer-to-peer (optimal performance) |

- **No inbound internet access required or recommended**
- Connector host needs routing + permission to reach private Resources
- ICMP: explicitly grant if required by environment
- Public exit nodes: require static public IP (direct or via NAT gateway)

## Hardware Recommendations
**Priority order:** Network bandwidth > Memory > CPU

| Platform | Recommended Spec |
|---|---|
| AWS | t3a.micro Linux EC2 |
| GCP | e2-small |
| Azure | Container Instance service |
| On-prem/VPS | 1 CPU, 2GB RAM Linux VM |

- Supports x86, AMD64, ARM; any Linux distro with systemd, Docker, or Helm
- Azure Container Instances with custom VNet DNS: use "Custom DNS" option and specify DNS server manually

## Gotchas
- Reusing tokens across multiple Connectors causes **connection failure**
- Adding CPU/RAM to a single Connector does **not** improve performance — deploy additional Connectors instead
- Connectors with mismatched permissions in same Remote Network cause inconsistent Resource access
- Azure Container Instances do **not** auto-recognize custom VNet DNS servers

## Load Balancing & Failover
- Automatic when >1 Connector exists in a Remote Network
- Clients retry other Connectors if one goes offline
- Adding/removing Connectors automatically adjusts routing

## Related Docs
- Understanding Connectors
- Help Me Choose (deployment method selector)
- UDP/QUIC/HTTP3 guide
- Public exit nodes
- Additional Connectors deployment
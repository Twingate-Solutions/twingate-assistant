# Connector Best Practices

## Page Title
Connector Best Practices

## Summary
Covers deployment recommendations, network requirements, hardware sizing, and load balancing behavior for Twingate Connectors. Key themes: redundancy through multiple Connectors per Remote Network, unique tokens per Connector, and co-location with resources.

## Key Information
- Deploy ≥2 Connectors per Remote Network for automatic load balancing and failover
- Multiple Connectors in the same Remote Network are auto-clustered — no manual configuration needed
- Each Connector requires **unique token pairs** — reusing tokens causes connection failure
- Connectors in the same Remote Network must have identical network scope/permissions
- Deploy Connectors as close to target Resources as possible ("last mile" optimization)
- Geographic routing: place all replicated resources in one Remote Network, deploy Connectors per location — Twingate auto-routes to nearest Connector

## Prerequisites
- Twingate Admin Console access to provision Connectors and generate tokens
- Outbound internet access from Connector host

## Network Requirements
| Traffic Type | Port(s) | Purpose |
|---|---|---|
| Outbound TCP | 443 | Controller/Relay communication |
| Outbound TCP | 30000–31000 | Relay fallback (no P2P) |
| Outbound UDP/QUIC (HTTP/3) | 1–65535 | Peer-to-peer (optimal) |

- No inbound internet access required or recommended
- Connector host must have routing/permission to reach private Resources
- ICMP: ensure Connector host can send ICMP to targets if needed
- Public exit nodes: require static public IP (direct or via NAT gateway)

## Hardware Recommendations
**Priority order:** Network bandwidth > Memory > CPU

| Platform | Recommended |
|---|---|
| AWS | t3a.micro Linux EC2 |
| GCP | e2-small |
| Azure | Container Instance (no hardware selection) |
| On-prem/VPS | 1 CPU, 2GB RAM Linux VM |

- Architectures: x86, AMD64, ARM
- Adding CPU/RAM to one Connector does **not** improve performance — deploy additional Connectors instead

## Gotchas
- **Token reuse across Connectors = connection failure** — provision one Connector in Admin Console per physical Connector deployed
- Azure Container Instances do **not** auto-recognize custom VNet DNS servers — must specify DNS manually via "Custom DNS" option during deployment
- Mismatched network permissions between Connectors in same Remote Network causes inconsistent Resource access depending on which Connector handles traffic
- Adding resources (CPU/memory) to a single Connector host won't scale performance — horizontal scaling only

## Configuration Values
- No specific env vars documented on this page
- See deployment-specific guides for token configuration

## Related Docs
- [Understanding Connectors](https://www.twingate.com/docs/understanding-connectors)
- [Help Me Choose (deployment method guide)](https://www.twingate.com/docs/connector-deployment)
- [Additional Connectors deployment](https://www.twingate.com/docs/connector)
- [HTTP/3 / QUIC guide](https://www.twingate.com/docs/connector-best-practices#network-requirements)
- [Public exit nodes](https://www.twingate.com/docs/exit-nodes)
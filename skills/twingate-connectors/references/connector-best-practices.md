# Connector Best Practices

## Page Title
Connector Best Practices

## Summary
Guidelines for deploying Twingate Connectors optimally across network architectures. Covers redundancy, token management, network requirements, hardware sizing, and load balancing behavior. Focuses on performance and reliability for production deployments.

## Key Information
- **Minimum 2 Connectors per Remote Network** for load balancing and failover
- Multiple Connectors in same Remote Network auto-cluster — no manual configuration needed
- Each Connector requires **unique token pair** — reusing tokens causes connection failure
- All Connectors in same Remote Network must have **identical network scope/permissions**
- Connectors only require **outbound** internet access; no inbound required
- Geographic routing: deploy Connectors in multiple locations under **one Remote Network** to route users to nearest Connector

## Prerequisites
- Connectors provisioned individually in Admin Console (one provisioning per deployed Connector)
- Network routing rules allowing Connector host to reach private Resources
- Static public IP required only for public exit node use case

## Network Requirements

| Traffic Type | Port(s) | Purpose |
|---|---|---|
| Outbound TCP | 443 | Controller/Relay communication |
| Outbound TCP | 30000–31000 | Relay fallback (non-P2P) |
| Outbound UDP/QUIC (HTTP/3) | 1–65535 | Peer-to-peer (optimal performance) |

## Hardware Recommendations

| Platform | Recommended Spec |
|---|---|
| AWS | t3a.micro Linux EC2 |
| GCP | e2-small |
| Azure | Container Instance service |
| On-prem/VPS | 1 CPU, 2GB RAM Linux VM |

**Priority order for optimization:** Network bandwidth > Memory > CPU

## Configuration Values
- Azure Container Instance + custom VNet DNS: use **Custom DNS option** and specify DNS server manually
- Supported architectures: x86, AMD64, ARM
- Supported Linux deployment methods: systemd, Docker, Helm

## Gotchas
- Adding CPU/memory to a single Connector **does not improve performance** — deploy additional Connectors instead
- Reusing tokens across multiple Connectors causes connection failure
- Azure Container Instance does **not** auto-detect custom DNS servers from VNet config
- ICMP traffic requires explicit permission on Connector host to reach target Resources
- Exit nodes require static public IP (direct or via NAT gateway)

## Related Docs
- Understanding Connectors
- Help Me Choose (deployment method selector)
- Public Exit Nodes
- UDP/QUIC/HTTP3 configuration guide
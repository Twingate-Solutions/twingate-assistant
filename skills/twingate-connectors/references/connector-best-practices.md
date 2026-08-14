---
source: https://www.twingate.com/docs/connector-best-practices
type: docs
fetched: 2026-08-14
source_version: 00abbc7ba9f6eb3e3aa604b34cc5c11fd6359916248168d5170575ca50ddb7b6
---

# Connector Best Practices

## Page Title
Connector Best Practices

## Summary
Covers deployment best practices, network requirements, hardware sizing, and load balancing/failover behavior for Twingate Connectors. Key principles: deploy multiple Connectors per Remote Network for redundancy, each Connector requires unique tokens, and Connectors should be co-located with target Resources.

## Key Information
- **Minimum 2 Connectors per Remote Network** for automatic load balancing and failover
- Multiple Connectors in same Remote Network are auto-clustered — no manual configuration needed
- Traffic automatically routes to the Connector associated with a Resource
- Users can be simultaneously connected to multiple Connectors across different Remote Networks
- Geographic routing: single Remote Network + Connectors in each location → users auto-routed to nearest active Connector

## Prerequisites
- Unique token pair per Connector (generated in Admin Console at provision time)
- All Connectors in same Remote Network must have identical network scope/permissions
- Connector host needs outbound Internet access only (no inbound required)

## Network Requirements
| Traffic Type | Ports | Purpose |
|---|---|---|
| TCP outbound | 443 | Controller/Relay communication |
| TCP outbound | 30000–31000 | Relay fallback (no P2P) |
| UDP/QUIC outbound | 1–65535 | Peer-to-peer (optimal performance) |

- Connector host must have routing + permission to reach private Resources
- ICMP: explicitly grant if required by environment
- Public exit nodes: requires static public IP (direct or via NAT gateway)

## Hardware Recommendations
| Platform | Recommendation |
|---|---|
| AWS | t3a.micro Linux EC2 |
| GCP | e2-small |
| Azure | Container Instance service |
| On-prem/VPS | 1 CPU, 2GB RAM Linux VM |

**Priority order for host optimization:** Network bandwidth > Memory > CPU

- Adding CPU/memory to a single Connector does **not** improve performance — deploy additional Connectors instead
- Supported architectures: x86, AMD64, ARM

## Gotchas
- **Reusing tokens across multiple Connectors causes connection failure** — provision one Connector in Admin Console per physical Connector deployed
- Azure Container Instances don't auto-detect custom VNet DNS — must specify DNS server manually via "Custom DNS" option
- Connectors in same Remote Network must be interchangeable (same permissions/scope); mismatched configs cause inconsistent Resource access
- "Last mile" latency matters — deploy Connectors on same network segment as Resources

## Configuration Values
- No environment variables or CLI flags documented on this page
- Token pairs generated via Twingate Admin Console UI

## Related Docs
- [Understanding Connectors](https://www.twingate.com/docs/understanding-connectors)
- [Help Me Choose (deployment method guide)](https://www.twingate.com/docs/help-me-choose)
- [UDP/QUIC HTTP3 guide](https://www.twingate.com/docs/quic)
- [Public exit nodes](https://www.twingate.com/docs/exit-nodes)
- [Additional Connectors deployment](https://www.twingate.com/docs/connector-deployment)
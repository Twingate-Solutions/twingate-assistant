# Connector Best Practices

## Page Title
Connector Best Practices

## Summary
Covers deployment recommendations for Twingate Connectors including redundancy, token management, network requirements, hardware sizing, and load balancing behavior. Multiple Connectors per Remote Network provide automatic load balancing and failover. Connectors require only outbound internet access.

## Key Information
- **Minimum 2 Connectors per Remote Network** for redundancy; auto load-balanced and failover-capable
- Each Connector requires **unique token pair** — reusing tokens causes connection failure
- Connectors in the same Remote Network should have **identical network scope and permissions**
- Deploy Connectors **co-located with target Resources** to minimize last-mile latency
- Traffic routes directly from user device → Connector → Resource (not through Twingate cloud)
- Geographic routing: single Remote Network + Connectors in each region → users routed to nearest active Connector

## Network Requirements
| Direction | Protocol | Ports | Purpose |
|-----------|----------|-------|---------|
| Outbound only | TCP | 443 | Controller/Relay communication |
| Outbound only | TCP | 30000–31000 | Relay fallback if P2P unavailable |
| Outbound only | UDP/QUIC (HTTP/3) | 1–65535 | P2P connectivity (optimal performance) |

- No inbound internet access required or recommended
- Connector host needs routing/permissions to reach private Resources
- ICMP must be explicitly permitted if required
- Public exit node use: requires static public IP (direct or via NAT gateway)

## Hardware Recommendations (Priority: Bandwidth > Memory > CPU)

| Platform | Recommended Spec |
|----------|-----------------|
| AWS | t3a.micro Linux EC2 |
| GCP | e2-small |
| Azure | Container Instance service (no hardware selection needed) |
| On-prem/VPS | 1 CPU, 2GB RAM Linux VM |

- Adding CPU/memory to a single Connector **does not improve performance** — deploy additional Connectors instead
- Azure Container Instances with custom VNet DNS: use "Custom DNS" option and specify DNS server manually

## Gotchas
- **Never reuse tokens** across Connectors — each provisioned Connector in Admin Console generates its own token pair
- Scaling vertically (more CPU/RAM) on a single Connector is ineffective; scale horizontally instead
- All Connectors in a Remote Network must have the same network permissions — mismatched permissions cause inconsistent Resource availability depending on which Connector handles the connection
- Azure Container Instances do not auto-detect custom VNet DNS servers

## Load Balancing & Failover Behavior
- Automatic when >1 Connector exists in a Remote Network
- Client tries alternate Connectors if one goes offline
- Adding/removing Connectors is detected and adjusted automatically
- Users can be simultaneously connected to multiple Connectors across different Remote Networks

## Prerequisites
- Twingate Admin Console access to provision Connector tokens
- Outbound internet connectivity from Connector host
- Routing from Connector host to target private Resources

## Related Docs
- Understanding Connectors
- Help Me Choose (deployment method selector)
- HTTP/3/QUIC guide (UDP port usage)
- Public exit nodes configuration
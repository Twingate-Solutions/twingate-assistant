# Connector Best Practices

## Page Title
Connector Best Practices

## Summary
Guidelines for deploying Twingate Connectors optimally across network environments. Covers redundancy, token management, network requirements, hardware sizing, and load balancing behavior. Connectors in the same Remote Network auto-cluster for failover and load balancing.

## Key Information
- **Minimum 2 Connectors per Remote Network** for redundancy and automatic load balancing/failover
- Each Connector requires a **unique token pair** — reusing tokens causes connection failure
- Connectors in the same Remote Network should have **identical network scope and permissions** (they're interchangeable)
- Deploy Connectors **close to target Resources** to minimize last-mile latency
- **Geographic routing**: deploy multiple Connectors across locations in one Remote Network; users auto-route to nearest active Connector
- Hardware priority order: **Network bandwidth > Memory > CPU**
- Adding CPU/memory to one Connector does NOT improve performance — add more Connectors instead

## Prerequisites
- Admin console access to provision Connectors
- Outbound internet access from Connector host
- Routing/permission rules allowing Connector to reach private Resources

## Network Requirements
| Traffic Type | Port(s) | Purpose |
|---|---|---|
| Outbound TCP | 443 | Controller/Relay communication |
| Outbound TCP | 30000–31000 | Relay fallback (no P2P) |
| Outbound UDP/QUIC (HTTP/3) | 1–65535 | Peer-to-peer (optimal performance) |

- **No inbound internet access required or recommended**
- For public exit nodes: Connector host needs static public IP (direct or via NAT gateway)

## Configuration Values

**Hardware Recommendations by Platform:**
- **AWS**: `t3a.micro` Linux EC2
- **GCP**: `e2-small`
- **Azure**: Container Instance service (no hardware selection needed)
- **On-prem/VPS**: 1 CPU, 2GB RAM Linux VM (x86, AMD64, or ARM)

**Azure-specific**: If using custom DNS for VNet, specify DNS server manually using "Custom DNS" option during deployment.

## Step-by-Step: Multi-Location Geographic Routing
1. Create a **single Remote Network** for all replicated Resources
2. Deploy Connectors in each geographic location within that Remote Network
3. Twingate automatically routes users to nearest active Connector

## Gotchas
- Token reuse across multiple Connectors → connection failure; always provision a new Connector in admin console per physical deployment
- Connectors with different network permissions in the same Remote Network can cause inconsistent Resource access depending on which Connector handles traffic
- Azure Container Instances won't auto-detect custom VNet DNS servers — must configure manually
- ICMP traffic requires explicit permission on Connector host if needed by environment
- Do not consolidate Connectors to reduce count — no performance or cost benefit from fewer Connectors

## Related Docs
- Understanding Connectors
- Help Me Choose (deployment method selector)
- UDP/QUIC/HTTP3 guide
- Public exit nodes
- Connector deployment options (systemd, Docker, Helm)
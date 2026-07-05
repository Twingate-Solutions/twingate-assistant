# Connector Best Practices

## Page Title
Connector Best Practices

## Summary
Guidelines for deploying Twingate Connectors optimally across network architectures. Covers redundancy requirements, token management, network configuration, hardware sizing, and load balancing behavior. Intended for admins planning or scaling Connector deployments.

## Key Information
- Deploy multiple Remote Networks matching your network segments; no benefit to funneling traffic through fewer Connectors
- Minimum **2 Connectors per Remote Network** for load balancing and failover (automatic, no configuration needed)
- Connectors in the same Remote Network are auto-clustered and interchangeable
- Geographic routing: create one Remote Network for replicated resources, deploy Connectors per location—Twingate routes users to nearest active Connector
- Adding CPU/RAM to a single Connector does **not** improve performance; deploy additional Connectors instead
- Optimize Connector host hardware priority: **Network bandwidth > Memory > CPU**

## Prerequisites
- Twingate Admin Console access to provision Connectors
- Each Connector requires its own unique token pair (generated per Connector in Admin Console)
- Connectors need outbound internet access only; no inbound required

## Configuration Values

### Network Ports (Outbound Only)
| Port/Protocol | Purpose |
|---|---|
| TCP 443 | Controller and Relay communication |
| TCP 30000–31000 | Relay fallback if P2P unavailable |
| UDP/QUIC 1–65535 | Peer-to-peer optimal performance |

### Recommended Hardware by Platform
| Platform | Recommendation |
|---|---|
| AWS | t3a.micro Linux EC2 |
| GCP | e2-small |
| Azure | Container Instance service |
| On-prem/VPS | 1 CPU, 2GB RAM Linux VM |

All platforms: x86, AMD64, or ARM; Linux with systemd, Docker, or Helm support.

## Gotchas
- **Tokens cannot be reused** across Connectors—each must have its own unique pair or connections will fail
- All Connectors in the same Remote Network must have **identical network scope and permissions**; mismatched permissions cause inconsistent Resource access
- Azure Container Instances do **not** auto-recognize custom VNet DNS servers—must manually specify DNS using the "Custom DNS" option
- Public exit node Connectors require a **static public IP** (direct or via NAT gateway) for whitelisting
- Connector host must have routing and permission rules to reach private Resources (including ICMP if needed)

## Step-by-Step: Deploy Redundant Connectors
1. In Admin Console, provision **two separate Connector entries** per Remote Network
2. Generate unique token pairs for each
3. Deploy each Connector on the same network segment as target Resources
4. Verify identical network permissions on both hosts
5. Twingate automatically enables load balancing and failover

## Related Docs
- Understanding Connectors
- Help Me Choose (deployment method selector)
- HTTP/3 / QUIC guide
- Public exit nodes
- Additional Connectors (scaling)
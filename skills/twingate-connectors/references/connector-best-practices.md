# Connector Best Practices

## Page Title
Connector Best Practices

## Summary
Guidelines for deploying Twingate Connectors effectively across network architectures. Covers redundancy, token management, network requirements, hardware sizing, and load balancing behavior. Focuses on performance and reliability optimization.

## Key Information
- Multiple Remote Networks and Connectors are encouraged—no benefit to consolidating traffic through fewer Connectors
- Connectors in the same Remote Network are automatically clustered for load balancing and failover
- Each Connector requires **unique token pairs**—reusing tokens causes connection failure
- All Connectors in a Remote Network should have identical network scope and permissions
- Deploy Connectors co-located with target Resources to minimize last-mile latency
- Geographic routing: single Remote Network with Connectors in each location → automatic nearest-Connector routing

## Prerequisites
- Connector tokens provisioned individually via Admin Console (one provisioning per deployed Connector)
- Outbound internet access from Connector host
- Routing/permission rules allowing Connector to reach private Resources

## Network Requirements
| Traffic Type | Ports | Purpose |
|---|---|---|
| Outbound TCP | 443 | Controller/Relay communication |
| Outbound TCP | 30000–31000 | Relay fallback (no P2P) |
| Outbound UDP/QUIC | 1–65535 | Peer-to-peer (optimal performance) |

- No inbound internet access required or recommended
- For exit nodes: Connector host needs static public IP (direct or via NAT gateway)

## Hardware Recommendations
| Platform | Recommended |
|---|---|
| AWS | t3a.micro Linux EC2 |
| GCP | e2-small |
| Azure | Container Instance service |
| On-prem/VPS | 1 CPU, 2GB RAM Linux VM |

**Priority order for optimization:** Network bandwidth > Memory > CPU

Adding CPU/memory to a single Connector does **not** improve performance—deploy additional Connectors instead.

## Gotchas
- Reusing tokens across multiple Connectors causes connection failure—each must have unique tokens
- Azure Container Instances won't auto-detect custom VNet DNS servers; use "Custom DNS" option and specify manually
- ICMP traffic requires explicit permission on Connector host if needed for your environment
- Connectors handle DNS resolution and routing from the host—ensure routing rules are in place
- Scaling single Connector resources (CPU/RAM) is ineffective; horizontal scaling is required

## Step-by-Step: Redundant Deployment
1. Create Remote Network in Admin Console
2. Provision **two or more** separate Connector applications (generates unique tokens per Connector)
3. Deploy each Connector with its own token pair on separate hosts
4. Ensure all Connectors have identical network access scope
5. Twingate automatically handles load balancing and failover

## Related Docs
- Understanding Connectors
- Help Me Choose (deployment method selector)
- Connector deployment options (systemd, Docker, Helm)
- Public exit nodes guide
- UDP/QUIC/HTTP3 configuration guide
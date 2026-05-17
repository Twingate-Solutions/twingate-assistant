# Connector Best Practices

## Page Title
Connector Best Practices

## Summary
Guidelines for deploying Twingate Connectors effectively, covering deployment topology, redundancy, network requirements, and hardware sizing. Multiple Connectors per Remote Network provide automatic load balancing and failover. Each Connector requires unique tokens and consistent network permissions within a Remote Network.

## Key Information
- Deploy Connectors close to target Resources to minimize "last mile" latency
- Minimum 2 Connectors per Remote Network for redundancy and load balancing
- Connectors in the same Remote Network auto-cluster; any Connector can serve any Resource in that network
- Each Connector requires its own unique token pair — token reuse causes connection failure
- All Connectors in the same Remote Network must have identical network scope/permissions
- Geographic routing: use one Remote Network with Connectors deployed in each region; users auto-route to nearest active Connector
- Adding CPU/memory to a single Connector does not improve performance — deploy additional Connectors instead

## Network Requirements
- **Only outbound internet access required** — no inbound connections needed
- Port restrictions if limiting outbound:
  - TCP `443` — Controller/Relay communication
  - TCP `30000-31000` — Relay fallback connections
  - UDP/QUIC ports `1-65535` — peer-to-peer (optimal performance)
- Connector host must have routing and permission to reach private Resources
- ICMP must be explicitly permitted if required
- Public exit nodes require static public IP (direct or via NAT gateway)

## Hardware Recommendations (Priority: Bandwidth > Memory > CPU)

| Platform | Recommendation |
|----------|---------------|
| AWS | `t3a.micro` Linux EC2 |
| GCP | `e2-small` |
| Azure | Container Instance service |
| On-prem/VPS | 1 CPU, 2GB RAM Linux VM |

- Supports x86, AMD64, ARM via systemd, Docker, or Helm
- Azure Container Instance with custom VNet DNS: use "Custom DNS" option and specify DNS server manually

## Gotchas
- Reusing tokens across multiple Connectors causes connection failures
- Connectors with differing network permissions in the same Remote Network may make Resources intermittently inaccessible
- Azure Container Instances do not auto-detect custom VNet DNS servers
- Adding resources to a single Connector host won't improve performance — scale horizontally

## Prerequisites
- Twingate Admin Console access to provision Connector tokens
- Outbound internet access from Connector host
- Routing rules on Connector host to reach target private Resources

## Related Docs
- Understanding Connectors
- Help Me Choose (deployment method selector)
- HTTP/3 / QUIC guide
- Public exit nodes guide
- Additional Connectors deployment
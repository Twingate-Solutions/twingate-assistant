---
source: https://www.twingate.com/docs/connector-best-practices
type: docs
fetched: 2026-11-13
source_version: 24f255b70b0602561dd5fa81618f446f5c104878afe6d68c585aa55855021228
trust: official
---

# Connector Best Practices

## Summary
Guidance for deploying Twingate Connectors: how many to deploy, how to scope them, network requirements, hardware sizing, and how load balancing, failover, and geographic routing work. The core principle is to scale out with more Connectors rather than scaling up a single host.

## Key Information
- Deploy as many Remote Networks and Connectors as your network architecture needs. Traffic is automatically routed to the Connector associated with a Resource. Define one Remote Network per network segment.
- Deploy at least **two Connectors per Remote Network** for redundancy. Connectors in the same Remote Network are clustered automatically for load balancing and failover.
- Each Connector needs its **own unique token pair**. Provision one Connector per deployment in the Admin Console. Reusing tokens causes connection failure.
- Connectors in the same Remote Network should have identical network scope and permissions, since they are interchangeable.
- Place Connectors on the same network as the target Resources to keep the "last mile" short.
- Host optimization priority: network bandwidth, then memory, then CPU.
- **Scale out, not up.** Adding CPU or memory to one Connector will not improve performance. Deploy more Connectors instead.

## Prerequisites
- Familiarity with "Understanding Connectors" and the "Deploying Connectors" guide.
- A Remote Network provisioned in the Admin Console.
- Connector host with routing and permission rules to reach private Resources (and ICMP permission if ICMP is needed).

## Network Requirements
- Outbound Internet access only. Inbound access is neither required nor recommended.
- If restricting outbound traffic, allow:
  - TCP 443 (Controller and Relay communication)
  - TCP 30000-31000 (Relay connections when peer-to-peer is unavailable)
  - UDP and QUIC (HTTP/3) ports 1-65535 (peer-to-peer connectivity)
- Resources are resolved and routed from the Connector host.
- For public exit nodes, the Connector host needs a static public IP (direct or via NAT gateway). Use that IP for allowlisting in the target service.

## Hardware Recommendations
| Platform | Recommendation |
|---|---|
| AWS | `t3a.micro` Linux EC2 (hundreds of users) |
| Google Cloud | `e2-small` as a starting point |
| Azure | Container Instance service (no hardware selection) |
| On-prem/Colo/VPS | Linux VM, 1 CPU, 2 GB RAM; any distro supporting systemd, Docker, or Helm on x86, AMD64, or ARM |

## Load Balancing, Failover, and Geographic Routing
- Clients are distributed across Connectors in a Remote Network. If one is unreachable, the client tries others until it connects.
- Adding or removing Connectors is handled automatically.
- For geographic routing, create a **single Remote Network** for the replicated Resources and deploy Connectors in each location. Users are routed to the nearest active Connector.

## Gotchas
- Reusing tokens across Connectors causes connection failure.
- Azure Container Instance does not automatically recognize a custom VNet DNS server. Use the "Custom DNS" option and specify the DNS server manually when deploying.
- Inconsistent permissions across Connectors in the same Remote Network can make Resources intermittently inaccessible.
- ICMP requires explicit permission on the Connector host.

## Related Docs
- Deploying Connectors
- Understanding Connectors
- Public exit nodes
- HTTP/3 and QUIC guide
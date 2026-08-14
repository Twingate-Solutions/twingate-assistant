---
source: https://www.twingate.com/docs/connector-placement-best-practices
type: docs
fetched: 2026-08-14
source_version: 5e0e615c7ce46ef58d437a1869e97acabad3fb9289ee8dc2f85bcb91643ee269
---

# Best Practices for Connector Placement

## Summary
Guide for determining optimal Twingate Connector placement in cloud and on-premises environments. Connectors must have network path access to Resources and DNS resolution capability for Resource FQDNs. Multiple placement strategies can be combined and changed over time.

## Key Information
- Connectors deploy on VMs or containers
- Deploy in pairs/multiples for load balancing and high availability
- No cap on number of Connectors or Remote Networks
- Connectors serve bidirectional connections (Client→Resource and Resource→Client)
- Connector host machine must resolve FQDNs of Resources it serves
- Combination of placement approaches is supported

## Prerequisites
- Network path must exist between Connector and its Resources
- Connector host must resolve FQDNs of served Resources (e.g., `myprivatewebapp.corp.int`)
- Firewall rules allowing outbound Connector traffic

## Placement Options

### Cloud Environments
| Option | Description |
|--------|-------------|
| Within individual VPC/VNet | Deploy in same VPC/VNet as Resources; dedicated or shared subnet |
| Dedicated VPC/VNet (peered) | Connector in own VPC/VNet with peering to Resource VPCs/VNets |
| Transit/VNet Gateway | Deploy in AWS Transit Gateway or Azure VNet Gateway for access to underlying VPCs/VNets |

### On-Premises Environments
| Option | Description |
|--------|-------------|
| Within individual subnets | Deploy directly in subnets containing Resources |
| Dedicated subnets | Deploy in separate subnet with routable access to Resource subnets |

## Gotchas
- Connector placement must be **physically near** Resources for performance
- DNS resolution must work **from the Connector host**, not just from user clients — internal FQDNs must be resolvable on the Connector's network
- High availability requires **pairs or multiples** of Connectors; single Connector = single point of failure
- Peered VPC/VNet architectures require peering to be configured before Connector can reach Resources

## Related Docs
- Connector deployment (VM/container setup)
- Remote Networks configuration
- High availability and load balancing for Connectors
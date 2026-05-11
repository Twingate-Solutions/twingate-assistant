# Best Practices for Connector Placement

## Summary
Covers where to deploy Twingate Connectors in cloud and on-premises environments. Connectors must have network path access to Resources and DNS resolution capability for Resource FQDNs. Multiple placement strategies can be combined and changed over time.

## Key Information
- Connectors deploy on VMs or in containers
- Deploy in pairs/multiples for load balancing and high availability
- No cap on number of Connectors or Remote Networks
- Connectors must have network path to Resources they serve
- Connector host machines must be able to resolve FQDNs of Resources (e.g., `myprivatewebapp.corp.int`)
- Combinations of placement strategies are supported

## Prerequisites
- Understanding of your network topology (VPCs, VNets, subnets, peering, transit gateways)
- DNS resolution configured on Connector host machines for Resource FQDNs

## Placement Options

### Cloud Environments
| Option | Description |
|--------|-------------|
| Within individual VPC/VNet | Deploy in dedicated subnet or alongside Resources |
| Dedicated VPC/VNet (peered) | Connectors in own VPC/VNet, access Resources via VPC peering |
| Transit/VNet Gateway | Deploy in AWS Transit Gateway or Azure VNet Gateway for access to multiple underlying VPCs/VNets |

### On-Premises Environments
| Option | Description |
|--------|-------------|
| Within individual subnets | Deploy Connectors in same subnet as Resources |
| Dedicated subnets | Deploy in separate subnet with routable access to Resource subnets |

## Gotchas
- Connector host must resolve Resource FQDNs — place Connectors where internal DNS is accessible
- Network path between Connector and Resource is required, not just network adjacency
- Single Connector deployments have no HA — use pairs or multiples for production
- Placement strategy can evolve; no need to commit to one approach permanently

## Related Docs
- Connector deployment (VMs, containers)
- Remote Networks configuration
- High availability / load balancing for Connectors
# Best Practices for Connector Placement

## Summary
Guide for determining where to deploy Twingate Connectors in cloud or on-premises environments. Connectors must have network reachability to the Resources they serve and must be able to resolve Resource FQDNs. Multiple placement strategies can be combined.

## Key Information
- Connectors deploy on VMs or in containers
- Deploy in pairs/multiples for load balancing and high availability
- No cap on number of Connectors or Remote Networks
- Connectors must have a network path to their Resources
- Connector host must resolve FQDNs of Resources it serves
- Approaches can be mixed; design can evolve over time

## Prerequisites
- Resources defined in Twingate
- Network path exists between Connector host and target Resources
- DNS resolution available on Connector host for Resource FQDNs

## Cloud Placement Options

| Option | Description |
|---|---|
| Within individual VPC/VNet | Deploy in same VPC/VNet as Resources (dedicated or shared subnet) |
| Dedicated VPC/VNet (peered) | Deploy in isolated VPC/VNet with peering to Resource VPCs/VNets |
| Transit/VNet Gateway | Deploy in AWS Transit Gateway or Azure VNet Gateway for access to multiple underlying VPCs/VNets |

## On-Premises Placement Options

| Option | Description |
|---|---|
| Within resource subnets | Deploy directly in subnets containing Resources |
| Dedicated subnets | Deploy in separate subnets with routing to Resource subnets |

## Gotchas
- **DNS is critical**: Connector host must resolve Resource FQDNs — if DNS is unavailable or misconfigured, connections will fail even if network routing is correct
- **Physical proximity matters**: Connectors should be as close as practicable to their Resources to minimize latency
- **Single Connector = no HA**: A lone Connector is a single point of failure; always deploy at least two per Remote Network for production
- **Peering required for cross-VPC**: If using a dedicated Connector VPC, VPC/VNet peering must be explicitly configured to reach Resource networks

## Related Docs
- Connector deployment (VM/container)
- Remote Networks configuration
- Load balancing and high availability setup
- Resource configuration
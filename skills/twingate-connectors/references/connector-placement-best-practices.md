# Best Practices for Connector Placement

## Summary
Guide for determining optimal Twingate Connector placement in cloud and on-premises environments. Covers deployment topologies for VPCs/VNets, transit gateways, and on-premises subnets. Multiple approaches can be combined and changed over time.

## Key Information
- Connectors deploy on VMs or containers
- Pairs (or multiples) provide load balancing and high availability
- No cap on number of Connectors or Remote Networks
- Connectors serve bidirectional connections: Clients↔Resources
- Connectors must have network path to their Resources
- Connector host must be able to DNS-resolve Resource FQDNs

## Prerequisites
- Network path must exist between Connector host and Resources
- DNS resolution of Resource FQDNs must work from Connector host machine
- Resources must be reachable from Connector's subnet/VPC

## Cloud Placement Options

| Option | Description |
|--------|-------------|
| Within individual VPC/VNet | Deploy in same VPC as Resources; dedicated or shared subnet |
| Dedicated VPC/VNet (peered) | Connectors in isolated VPC, access Resources via VPC peering |
| Transit/VNet Gateway | Deploy in AWS Transit Gateway or Azure VNet Gateway; serves multiple underlying VPCs/VNets |

## On-Premises Placement Options

| Option | Description |
|--------|-------------|
| Within individual subnets | Deploy directly in subnets containing Resources |
| Dedicated subnets | Deploy in separate subnet with routing access to Resource subnets |

## Gotchas
- Connector host DNS must resolve private FQDNs (e.g., `myprivatewebapp.corp.int`) — if DNS isn't reachable from the Connector machine, users cannot access Resources by hostname
- Physical/network proximity matters: place Connectors as close as possible to Resources they serve
- A single Connector is a SPOF — always deploy in pairs for production HA

## Related Docs
- Connector deployment (VM/container installation)
- Remote Networks configuration
- Load balancing and high availability setup
# Best Practices for Connector Placement

## Summary
Guide for determining optimal Twingate Connector deployment locations in cloud and on-premises environments. Covers placement topologies for VPCs/VNets, transit gateways, and on-premises subnets. Multiple approaches can be combined and changed over time.

## Key Information
- Connectors deploy on VMs or containers
- Deploy in pairs/multiples for load balancing and high availability
- No cap on number of Connectors or Remote Networks
- Connectors must have network path to the Resources they serve
- Connectors must be able to DNS-resolve Resource FQDNs (e.g., the host machine must resolve `myprivatewebapp.corp.int`)
- Approaches can be mixed; design is not permanent

## Prerequisites
- Network path must exist between Connector host and target Resources
- Connector host must have DNS resolution for Resource FQDNs
- Resources must be reachable from Connector's subnet/VPC

## Cloud Placement Options

| Option | Description |
|--------|-------------|
| Within individual VPC/VNet | Connector in same VPC as Resources; dedicated or shared subnet |
| Dedicated VPC/VNet (peered) | Connector in its own VPC, peered to Resource VPCs |
| Transit/VNet Gateway | Connector in AWS Transit Gateway or Azure VNet Gateway, serving underlying VPCs |

## On-Premises Placement Options

| Option | Description |
|--------|-------------|
| Within resource subnet | Connector co-located in subnet containing Resources |
| Dedicated subnet | Connector in separate subnet with routable access to Resource subnets |

## Gotchas
- Connector must resolve FQDNs of Resources—not just have IP connectivity; DNS must work from the Connector host
- Peered VPC/VNet setups require peering to be properly configured before Connector can reach Resources
- Physical/network proximity matters: place Connectors as close as practical to Resources they serve
- Single Connector = no HA; always deploy pairs for production

## Related Docs
- Connector deployment (VM and container options)
- Remote Networks configuration
- Load balancing and high availability setup
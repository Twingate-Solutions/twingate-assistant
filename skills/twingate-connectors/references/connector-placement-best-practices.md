# Best Practices for Connector Placement

## Summary
Guide for determining optimal Twingate Connector placement in cloud and on-premises environments. Connectors must have network path access to Resources and DNS resolution capability for Resource FQDNs. Multiple deployment patterns are supported and can be combined.

## Key Information
- Connectors deploy on VMs or containers
- Deploy in pairs/multiples for load balancing and high availability
- No cap on number of Connectors or Remote Networks
- Connectors must have network path to Resources they serve
- Connectors must resolve FQDNs of Resources (e.g., host machine must resolve `myprivatewebapp.corp.int`)
- Approaches can be mixed; design is not permanent

## Prerequisites
- Network path must exist between Connector host and target Resources
- DNS resolution for Resource FQDNs must work from Connector host machine

## Placement Options

### Cloud Environments
| Pattern | Description |
|---|---|
| Within individual VPC/VNet | Deploy in same VPC/VNet as Resources; use dedicated or existing subnet |
| Dedicated VPC/VNet (peered) | Deploy in isolated VPC/VNet peered to Resource VPCs/VNets |
| Transit/VNet Gateway | Deploy in AWS Transit Gateway or Azure VNet Gateway for access to underlying VPCs/VNets |

### On-Premises Environments
| Pattern | Description |
|---|---|
| Within individual subnets | Deploy in same subnet as Resources |
| Dedicated subnet | Deploy in separate subnet with routable access to Resource subnets |

## Gotchas
- Connector host DNS resolution is required — not just Twingate routing. If the host can't resolve the FQDN, users can't access the Resource
- Physical/network proximity matters for performance; place Connectors close to Resources
- Single Connector = no HA; always deploy in pairs minimum for production

## Related Docs
- Connector deployment (VM/container options)
- Remote Networks configuration
- High availability setup
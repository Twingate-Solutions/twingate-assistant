# Best Practices for Connector Placement

## Summary
Guide for determining where to deploy Twingate Connectors in cloud and on-premises environments. Connectors must have network path access to Resources and DNS resolution capability for Resource FQDNs. Multiple placement strategies can be combined and changed over time.

## Key Information
- Connectors deploy on VMs or in containers
- Deploy in pairs/multiples for load balancing and high availability
- No cap on number of Connectors or Remote Networks
- Connectors serve bidirectional connections (Clients↔Resources)
- Connector host machine must resolve FQDNs of Resources it serves
- Mixed placement strategies are supported simultaneously

## Prerequisites
- Network path must exist between Connector and its Resources
- Connector host must resolve FQDNs of all Resources in that Remote Network (e.g., `myprivatewebapp.corp.int` must resolve from the Connector's host)

## Placement Options

### Cloud Environments
| Strategy | Description |
|---|---|
| Within individual VPC/VNet | Deploy inside VPC/VNet containing Resources; use dedicated or existing subnet |
| Dedicated peered VPC/VNet | Deploy in isolated VPC/VNet, access Resources via VPC peering |
| Transit/VNet Gateway | Deploy in AWS Transit Gateway or Azure VNet Gateway for access to multiple underlying VPCs/VNets |

### On-Premises Environments
| Strategy | Description |
|---|---|
| Within resource subnet | Deploy directly in subnet containing Resources |
| Dedicated subnet | Deploy in separate subnet with routable access to Resource subnets |

## Gotchas
- Connectors should be **physically near** the Resources they serve — latency matters
- DNS resolution must work **from the Connector host**, not just from clients
- A single placement strategy is not required — hybrid approaches are valid
- Design is not permanent; reconfigure as infrastructure grows

## Related Docs
- Connector deployment (VM/container options)
- Remote Networks configuration
- High availability setup for Connectors
# Connector Placement Best Practices

## Summary
Guide for determining optimal Twingate Connector deployment locations in cloud and on-premises environments. Connectors must have network reachability to Resources and DNS resolution capability for Resource FQDNs. Multiple placement strategies can be combined and changed over time.

## Key Information
- Connectors run on VMs or in containers
- Deploy in pairs/multiples for load balancing and high availability
- No cap on number of Connectors or Remote Networks
- Connectors must have network path to Resources they serve
- Connector host must resolve FQDNs of Resources (e.g., `myprivatewebapp.corp.int`)
- Connectors handle bidirectional connections (Client→Resource and Resource→Client)
- Approaches can be mixed; design is not permanent

## Cloud Placement Options

| Option | Description |
|--------|-------------|
| Within individual VPC/VNet | Deploy inside same VPC/VNet as Resources; use dedicated or shared subnet |
| Dedicated VPC/VNet (peered) | Connectors in isolated VPC/VNet with peering to Resource VPCs/VNets |
| Transit/VNet Gateway | Deploy in AWS Transit Gateway or Azure VNet Gateway for access to underlying VPCs/VNets |

## On-Premises Placement Options

| Option | Description |
|--------|-------------|
| Within individual subnets | Deploy directly in subnets containing Resources |
| Dedicated subnets | Deploy in separate subnet with routable access to Resource subnets |

## Prerequisites
- Network path must exist between Connector host and Resources
- Connector host must have DNS resolution for all Resource FQDNs
- Resources must be reachable from Connector's network location

## Gotchas
- **DNS resolution is required on the Connector host** — not just network reachability; if the Connector can't resolve a private FQDN, users can't access it
- Placing Connectors in transit/gateway networks is valid but adds routing complexity
- Single Connector deployments have no failover — always deploy in pairs for production
- Physically distant Connectors from Resources increase latency; place Connectors close to Resources

## Related Docs
- Connector deployment (VM, container)
- Remote Networks configuration
- High availability / load balancing setup
- VPC/VNet peering configuration
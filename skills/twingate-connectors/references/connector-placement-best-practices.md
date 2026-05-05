## Connector Placement Best Practices

Guidance on where to deploy Twingate Connectors relative to Resources, both in cloud and on-premises environments.

**Core Rules:**
- Deploy in pairs (or multiples) for HA and load balancing — Twingate automatically balances across Connectors in the same Remote Network
- Connectors must have a network path to the Resources they serve (and be able to resolve Resource FQDNs)
- Deploy as physically close to Resources as possible to minimize latency
- No cap on number of Connectors or Remote Networks

**Cloud Deployment Options:**
- **Within the same VPC/VNet as Resources** -- simplest; dedicated or shared subnet; no cross-network routing needed
- **In a dedicated VPC/VNet peered to resource VPCs** -- central Connector network peered to multiple resource networks; useful for hub-spoke topologies
- **In a transit gateway (AWS) or VNet gateway (Azure)** -- Connectors in the gateway tier serve multiple underlying VPCs/VNets

**On-Premises Deployment Options:**
- **Within the same subnet as Resources** -- simplest; no additional routing
- **In a dedicated subnet** -- Connectors in their own subnet, with routing to resource subnets

**Key Design Principles:**
- Use combinations of approaches — not all networks need the same pattern
- Design is not permanent — you can change placement as your architecture evolves
- One Remote Network per logical network boundary is a common pattern; multiple Connectors per Remote Network for HA

**Related Docs:**
- /docs/understanding-connectors -- Connector fundamentals
- /docs/connector-deployment -- General deployment guide
- /docs/connector-placement-best-practices -- (this page)

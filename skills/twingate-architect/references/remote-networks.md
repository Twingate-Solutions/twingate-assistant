## Page Title
Remote Networks

## Summary
A Remote Network is a logical container in Twingate that groups Resources together. All Resources in a Remote Network must be reachable from any Connector deployed in that network. Each Remote Network maps roughly to one physical network, VPC, or subnet you want to provide access to.

## Key Information
- **Logical grouping**: Remote Network ≈ one physical network or VPC; Resources inside must all be reachable by the Connectors
- **Connector requirement**: at least one Connector must be deployed and running — without it, all Resources in the network are inaccessible
- **Recommended: 2+ Connectors per Remote Network** for load balancing and failover
- **Load balancing**: automatic as Connector count changes; if one Connector fails, others handle traffic
- **Scalability**: a single Connector handles hundreds of users depending on usage; add more as needed
- **Consistency requirement**: all Connectors in the same Remote Network must have identical network routing and access rules

## Prerequisites
- Twingate account with Admin access
- Target network/VPC accessible from the host where Connector will be deployed

## Step-by-Step
1. Admin Console → Network → Remote Networks → Add
2. Select location type (AWS, Azure, GCP, On-Prem, etc.)
3. Name the Remote Network
4. Deploy at least one Connector into it (see Deploying Connectors doc)
5. Add Resources to the Remote Network

## Configuration Values
None specific to this page — see Connector deployment docs for Connector-level config.

## Gotchas
- Resources are inaccessible until a Connector is deployed and connected — no Connector = no access
- All Connectors in the same Remote Network are interchangeable and must have the same routing rules — misconfigured routing on one Connector causes inconsistent access
- A single Connector is a single point of failure; always deploy at least 2 in production

## Related Docs
- `/docs/quick-start` — step-by-step setup
- `/docs/resources` — defining resources within a Remote Network
- `/docs/architecture` — how Connectors fit into the overall design

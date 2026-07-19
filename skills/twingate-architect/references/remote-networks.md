# Remote Networks

## Page Title
Remote Networks

## Summary
Remote Networks are logical containers that group Twingate Resources together. Each Remote Network maps to a physical network or VPC and requires at least one deployed Connector to enable access. Connectors sit behind the firewall and handle traffic routing for authenticated users.

## Key Information
- Remote Network = logical grouping of Resources corresponding to a physical network/VPC
- All Resources in a Remote Network must be reachable by any Connector deployed within it
- No running Connector = Resources are inaccessible to end users
- Load balancing across Connectors is automatic and adjusts as Connectors are added/removed
- Single Connector can handle traffic for hundreds of users depending on usage patterns

## Prerequisites
- At least one Connector deployed and running per Remote Network
- Connectors must be deployed behind the firewall with network access to all Resources in that Remote Network

## Best Practices
- **Deploy minimum 2 Connectors per Remote Network** for:
  - Load balancing and automatic failover
  - Scalability as user count grows
- All Connectors within the same Remote Network must have **identical network routing and access rules**
- Add more Connectors as needed—no upper limit specified

## Architecture Notes
- Connectors within a Remote Network are **interchangeable** (stateless from a routing perspective)
- Failover is automatic—if one Connector fails, others handle traffic
- Scaling is horizontal: add more Connectors to handle increased traffic load

## Gotchas
- Resources become completely inaccessible if all Connectors in a Remote Network go offline
- Connectors must have uniform network access rules—inconsistent rules across Connectors in the same Remote Network will cause unpredictable behavior
- One Remote Network per discrete network boundary (don't mix networks with different routing rules into one Remote Network)

## Related Docs
- Connectors (deployment details)
- Deploying Connectors (scaling guidance)
- Resources (configuration)
- Best Practices documentation
# Remote Networks

## Summary
Remote Networks are logical containers in Twingate that group Resources together. Each Remote Network requires at least one deployed Connector to provide access, and all Connectors within a Remote Network must have identical network routing and access rules.

## Key Information
- Remote Network ≈ one physical network or VPC in your infrastructure
- Resources within a Remote Network must be reachable by all Connectors in that same Remote Network
- Connectors deploy behind the firewall to proxy access to Resources
- Load balancing across Connectors is automatic and adjusts as Connectors are added/removed
- A single Connector can handle traffic for hundreds of users depending on usage patterns

## Prerequisites
- At least one Connector deployed and running per Remote Network
- Connectors must have network-level access to all Resources in the Remote Network

## Recommendations
- **Deploy minimum 2 Connectors per Remote Network** for:
  - Automatic load balancing
  - Failover redundancy if one Connector fails
- All Connectors in the same Remote Network must have identical network routing and access rules (they are treated as interchangeable)

## Gotchas
- Resources are completely inaccessible to end users if no Connector is deployed and running
- Connectors within the same Remote Network must have the same network routing/access rules — mismatched configurations will cause inconsistent behavior
- Adding more Connectors triggers automatic load rebalancing

## Related Docs
- Connectors
- Deploying Connectors
- Resources
- Best Practices documentation
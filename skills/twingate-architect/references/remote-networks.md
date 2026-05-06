# Remote Networks

## Summary
Remote Networks are logical containers that group Twingate Resources together. Each Remote Network requires at least one deployed Connector to provide access, with two or more recommended for redundancy and load balancing.

## Key Information
- Remote Network ≈ one physical network or VPC in your infrastructure
- All Resources in a Remote Network must be reachable by any Connector deployed in that same network
- Without an active Connector, Resources are inaccessible to all end users
- Load balancing across Connectors is automatic and adjusts as Connectors are added/removed
- A single Connector can handle traffic for hundreds of users depending on usage patterns

## Prerequisites
- At least one Connector deployed and running per Remote Network
- Connectors must be deployed behind the firewall with access to the Remote Network's Resources

## Best Practices
- **Deploy minimum two Connectors per Remote Network** for:
  - Automatic load balancing
  - Failover redundancy
- All Connectors within the same Remote Network must have **identical network routing and access rules**
- Add additional Connectors as user count scales beyond single-Connector capacity

## Gotchas
- Connectors within a Remote Network are treated as interchangeable — misconfigured routing on one Connector will cause inconsistent behavior
- Resources remain completely inaccessible if no Connector is deployed or all Connectors go offline

## Related Docs
- Connectors (deployment guide)
- Resources
- Deploying Connectors (scaling details)
- Best Practices documentation
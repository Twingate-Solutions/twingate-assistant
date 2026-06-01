# Remote Networks

## Summary
Remote Networks are logical containers in Twingate that group Resources together. Each Remote Network requires at least one deployed Connector to enable access, and all Connectors within a Remote Network must have identical network routing and access rules.

## Key Information
- Remote Network ≈ one physical network or VPC
- All Resources in a Remote Network must be reachable by any Connector deployed in that same network
- Without an active Connector, Resources are inaccessible to end users
- Load balancing across Connectors is automatic and adjusts as Connectors are added/removed
- A single Connector can handle traffic for hundreds of users depending on usage patterns

## Prerequisites
- At least one Connector deployed and running per Remote Network
- Connectors must be deployed behind the firewall
- Users must be authenticated and authorized to access Resources

## Best Practices
- **Deploy minimum 2 Connectors per Remote Network** for:
  - Automatic load balancing
  - Failover/redundancy if one Connector fails
  - Scalability as user count grows
- All Connectors within the same Remote Network must have **identical network routing and access rules**
- Add additional Connectors as needed — no hard limit

## Gotchas
- Connectors within a Remote Network are interchangeable — misconfigured routing rules on one Connector will create inconsistent behavior
- Resources become completely inaccessible if all Connectors in a Remote Network go down (no Connector = no access)

## Related Docs
- Connectors (deployment details)
- Deploying Connectors (scalability guidance)
- Best Practices documentation
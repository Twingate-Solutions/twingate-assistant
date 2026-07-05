# Remote Networks

## Page Title
Remote Networks

## Summary
Remote Networks are logical containers in Twingate that group Resources together. Each Remote Network requires at least one deployed Connector to provide access to its Resources. Remote Networks typically map to existing physical networks or VPCs.

## Key Information
- Remote Network = logical grouping of Resources
- All Resources in a Remote Network must be accessible from any Connector deployed within that same Remote Network
- Without an active Connector, Resources are inaccessible to end users
- Load balancing across Connectors is automatic and adjusts as Connectors are added/removed
- A single Connector can handle traffic for hundreds of users depending on usage patterns

## Prerequisites
- At least one Connector deployed per Remote Network
- Connectors must be deployed behind the firewall
- Users must be authenticated and authorized to access Resources

## Recommendations
- **Deploy minimum two Connectors per Remote Network** for:
  - Automatic load balancing
  - Failover redundancy
  - Scalability as user count grows

## Configuration Notes
- Connectors within the same Remote Network must share identical **network routing and access rules**
- Connectors within the same Remote Network are interchangeable
- No upper limit on number of Connectors per Remote Network

## Gotchas
- All Connectors in a Remote Network must have the same network routing and access rules — mismatched configurations will cause inconsistent behavior
- Resources are completely inaccessible if no Connector is running, even if Resources are configured
- Remote Network ≠ physical network; it is a logical construct requiring explicit Connector deployment

## Related Docs
- Connectors
- Resources
- Deploying Connectors
- Best Practices documentation
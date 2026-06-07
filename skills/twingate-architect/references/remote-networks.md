# Remote Networks

## Summary
Remote Networks are logical containers that group Twingate Resources together. Each Remote Network requires at least one deployed Connector to provide access to its Resources. Remote Networks typically map to physical networks or VPCs.

## Key Information
- Remote Network = logical grouping of Resources that share network accessibility
- All Resources in a Remote Network must be reachable from any Connector in that same Remote Network
- Without a running Connector, Resources are inaccessible to end users
- Load balancing across Connectors is automatic and adjusts as Connectors are added/removed
- A single Connector can handle traffic for hundreds of users depending on usage patterns

## Prerequisites
- At least one Connector deployed and running per Remote Network
- Connectors must be deployed behind the firewall with access to the Remote Network's Resources

## Best Practices
- **Deploy minimum 2 Connectors per Remote Network** for:
  - Automatic load balancing
  - Failover redundancy if one Connector fails
- All Connectors within the same Remote Network must have **identical network routing and access rules**
- Add additional Connectors as needed for scalability

## Architecture Notes
- Remote Networks ≈ 1:1 mapping with physical networks or VPCs
- Connectors within the same Remote Network are interchangeable
- No upper limit on number of Connectors per Remote Network

## Gotchas
- Connectors in the same Remote Network must have consistent network routing/access rules — inconsistency can cause unpredictable behavior since load balancing is automatic
- Resources become completely inaccessible if all Connectors in a Remote Network go down

## Related Docs
- Connectors (deployment details)
- Resources (configuration)
- Deploying Connectors (scalability guidance)
- Best Practices documentation
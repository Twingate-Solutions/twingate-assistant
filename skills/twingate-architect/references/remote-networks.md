# Remote Networks

## Summary
Remote Networks are logical containers that group Resources together in Twingate. Each Remote Network corresponds to a physical network or VPC, and requires at least one deployed Connector to enable user access to Resources.

## Key Information
- Remote Network = logical grouping of Resources that share network accessibility
- All Resources in a Remote Network must be reachable from any Connector in that same network
- Without an active Connector, Resources are completely inaccessible to end users
- Load balancing across Connectors is automatic and adjusts dynamically
- A single Connector can typically handle traffic for hundreds of users

## Prerequisites
- At least one Connector deployed and running per Remote Network
- Connectors must be deployed behind the firewall
- Users must be authenticated and authorized to access Resources

## Best Practices
- **Deploy minimum 2 Connectors per Remote Network** for:
  - Automatic load balancing
  - Failover redundancy if one Connector fails
- All Connectors within the same Remote Network must have **identical network routing and access rules**
- Add Connectors as needed for scalability

## Architecture Notes
- Remote Networks map approximately 1:1 to physical networks or VPCs
- Connectors within the same Remote Network are interchangeable
- Multiple Connectors = automatic load distribution without manual configuration

## Gotchas
- Connectors in the same Remote Network must have consistent network routing/access rules — mismatched rules can cause inconsistent behavior since any Connector may handle a given request
- Resources become fully inaccessible if all Connectors in a Remote Network go offline

## Related Docs
- [Connectors](https://www.twingate.com/docs/connectors)
- [Deploying Connectors](https://www.twingate.com/docs/deploying-connectors)
- [Resources](https://www.twingate.com/docs/resources)
- [Best Practices](https://www.twingate.com/docs/best-practices)
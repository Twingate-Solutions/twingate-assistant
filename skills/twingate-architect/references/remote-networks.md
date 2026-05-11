# Remote Networks

## Summary
Remote Networks are logical containers in Twingate that group Resources together. Each Remote Network requires at least one deployed Connector to provide access, and all Connectors within a Remote Network must have identical network routing and access rules.

## Key Information
- Remote Network ≈ one physical network or VPC in your infrastructure
- Resources inside a Remote Network must be reachable by **all** Connectors in that same Remote Network
- No running Connector = Resources are inaccessible to end users
- Load balancing across Connectors is automatic and adjusts as Connectors are added/removed
- A single Connector can typically handle traffic for hundreds of users

## Prerequisites
- At least one Connector deployed and running per Remote Network
- Connectors must be deployed behind the firewall of the target network

## Best Practices
- Deploy **minimum two Connectors** per Remote Network for:
  - Automatic load balancing
  - Failover redundancy
- All Connectors within a Remote Network must share identical network routing and access rules (they are interchangeable)
- Add Connectors as needed for scalability

## Gotchas
- Connectors within the same Remote Network are treated as interchangeable — mismatched routing or firewall rules between Connectors will cause inconsistent behavior
- Resources become completely inaccessible if all Connectors in a Remote Network go offline

## Related Docs
- Connectors (deployment details)
- Resources
- Best Practices documentation
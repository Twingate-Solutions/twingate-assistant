# Remote Networks

## Summary
Remote Networks are logical containers that group Twingate Resources together. Each Remote Network maps approximately to a physical network or VPC, and requires at least one deployed Connector to provide access to its Resources.

## Key Information
- Remote Network = logical grouping of Resources that share network accessibility
- All Resources in a Remote Network must be reachable from any Connector deployed within it
- Minimum one Connector required; **two or more recommended**
- Without an active Connector, all Resources in the network are inaccessible to end users
- Load balancing across Connectors is automatic and adjusts as Connectors are added/removed
- A single Connector can typically handle traffic for hundreds of users (usage-dependent)

## Prerequisites
- Twingate account with admin access
- At least one Connector deployed and running per Remote Network
- Connectors must be deployed behind the firewall with network access to all Resources in the Remote Network

## Architecture Mapping
| Twingate Concept | Real-World Equivalent |
|---|---|
| Remote Network | Physical network, VPC, or subnet |
| Connector | Agent deployed inside that network |
| Resource | Specific service/host within the network |

## Best Practices
- **Deploy at least 2 Connectors per Remote Network** for:
  - Automatic load balancing
  - Failover redundancy
- All Connectors within the same Remote Network **must have identical network routing and access rules** (they are treated as interchangeable)
- Add Connectors as user count or traffic grows

## Gotchas
- Connectors are interchangeable within a Remote Network — inconsistent routing/firewall rules between Connectors will cause unpredictable access failures
- Zero active Connectors = zero Resource access, even if Resources are configured correctly
- Resources must be network-accessible from **every** Connector in the Remote Network, not just one

## Related Docs
- Connectors (deployment details)
- Deploying Connectors (scaling guidance)
- Resources
- Best Practices documentation
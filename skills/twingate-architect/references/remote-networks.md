# Remote Networks

## Summary
Remote Networks are logical containers that group Twingate Resources together. Each Remote Network requires at least one deployed Connector to provide access, and corresponds roughly to a physical network or VPC. Resources are inaccessible without an active Connector in the same Remote Network.

## Key Information
- Remote Network = logical grouping of Resources that share network accessibility
- All Resources in a Remote Network must be reachable by any Connector deployed in that same network
- Connectors deploy behind the firewall to proxy access for authenticated/authorized users
- Load balancing across Connectors is automatic and adjusts as Connectors are added/removed
- A single Connector can handle traffic for hundreds of users depending on usage patterns

## Prerequisites
- At least one Connector deployed and running per Remote Network
- Connectors must have network-level access to all Resources defined in the Remote Network

## Best Practices
- **Deploy minimum 2 Connectors per Remote Network** for:
  - Automatic load balancing
  - Failover redundancy if one Connector fails
- All Connectors within the same Remote Network must have **identical network routing and access rules**
- Add additional Connectors as user count/traffic grows

## Architecture Mapping
| Physical Concept | Twingate Concept |
|---|---|
| Physical network / VPC | Remote Network |
| Resources on that network | Resources (grouped in Remote Network) |
| Proxy agent on the network | Connector |

## Gotchas
- Resources are **completely inaccessible** if no Connector is deployed and running — there is no fallback
- Connectors within a Remote Network are treated as interchangeable, so misconfigured routing on one Connector will cause inconsistent behavior
- Load balancing is automatic but only applies within the same Remote Network — Connectors across different Remote Networks do not share load

## Related Docs
- Connectors (deployment guide)
- Deploying Connectors (scalability details)
- Resources
- Best Practices documentation
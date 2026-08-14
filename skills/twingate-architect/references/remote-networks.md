---
source: https://www.twingate.com/docs/remote-networks
type: docs
fetched: 2026-08-14
source_version: aba6495c460e8ed54919e229923e3d8d660abaf6cbc972639b2eda44a79d4b53
---

# Remote Networks

## Page Title
Remote Networks

## Summary
A Remote Network is a logical container in Twingate that groups Resources together. All Resources in a Remote Network must be reachable by any Connector deployed within it. Each Remote Network roughly maps to a physical network or VPC.

## Key Information
- Remote Networks group Resources logically
- All Resources must be accessible from **any** Connector in the same Remote Network
- At least one Connector required per Remote Network to enable access
- Resources are completely inaccessible without a running Connector
- Load balancing across Connectors is automatic and adjusts as Connectors are added/removed
- A single Connector can typically handle traffic for hundreds of users

## Prerequisites
- At least one Connector deployed per Remote Network
- Connector(s) deployed behind the firewall

## Best Practices
- **Deploy at least two Connectors** per Remote Network for:
  - **Failover**: If one Connector fails, others remain available
  - **Load balancing**: Automatically distributed across all active Connectors
  - **Scalability**: Add more Connectors as user count grows
- All Connectors within the same Remote Network must have **identical network routing and access rules**
- Connectors within the same Remote Network are interchangeable

## Gotchas
- If Connectors within the same Remote Network have different network routing/access rules, behavior will be inconsistent since any Connector may handle a given request
- No Connector = no access, regardless of Resource or policy configuration
- Resources must be reachable from **all** Connectors in the network, not just one — plan network topology accordingly

## Related Docs
- Resources
- Connectors / Deploying Connectors
- Remote Network Best Practices
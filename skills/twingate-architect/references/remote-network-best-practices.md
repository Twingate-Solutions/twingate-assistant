# Remote Network Best Practices

## Page Title
Remote Network Best Practices

## Summary
Guidelines for structuring Twingate Remote Networks around network segments, DNS configuration, routing, and firewall rules. Proper configuration avoids performance penalties and keeps internal networks hidden from the internet.

## Key Information

### Network Segmentation
- One Remote Network per accessible network segment (logical grouping, not necessarily physical)
- Peered VPCs sharing an address space can be a **single** Remote Network
- No performance penalty for multiple Remote Networks
- Separate Remote Networks with dedicated Connectors per VPC often **improves** performance by eliminating cross-VPC traversal

### Private DNS
- Not required, but strongly recommended
- Connectors resolve internal addresses locally — no public DNS entries needed
- Users connect via private DNS names (e.g., `resource.company.int`)
- DNS names become unresolvable if Twingate is disconnected or access is revoked
- Prevents IP address space collisions during deployment expansion

### Routing
- No changes to existing network routing rules required
- Deploy separate Connectors per isolated subnet instead of bridging subnets
- Example: Two isolated subnets (`10.1.0.0/16`, `10.2.0.0/16`) each get their own Connector — no cross-subnet routing needed

### Firewall Rules
- **No inbound traffic required** for Connectors or Resources
- Connectors initiate **outbound-only** connections to Twingate
- User-to-Resource traffic flows over the established outbound connection

## Prerequisites
- Connectors deployed within each target network segment
- Network accessibility confirmed between Connectors and target Resources

## Configuration Values
| Scenario | Recommendation |
|---|---|
| Peered VPCs, shared address space | Single Remote Network |
| Isolated VPCs/subnets | Separate Remote Network per segment |
| DNS format | `resource.company.int` (internal only) |

## Gotchas
- "Network segment" = any address space routable from deployed Connectors, regardless of physical topology
- Private DNS names only resolve while Twingate is active and access is authorized — plan user communication accordingly
- Routing traffic through a single Connector to reach multiple isolated subnets introduces unnecessary latency; deploy per-subnet instead

## Related Docs
- [How DNS works with Twingate](#) — DNS resolution details
- [Deploying Connectors](#) — Connector network requirements and outbound connection specs
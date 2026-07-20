# Remote Network Best Practices

## Page Title
Remote Network Best Practices

## Summary
Guidelines for structuring Twingate Remote networks around network segments, DNS configuration, routing, and firewall rules. Covers topology decisions that affect performance and security posture.

## Key Information

### Network Segmentation
- One Remote network per accessible network segment (logical grouping, not physical)
- Peered VPCs with shared address space → can use single Remote network
- No performance penalty for multiple Remote networks
- **Performance tip**: Separate Remote networks per VPC (without forced peering) routes traffic directly, avoiding unnecessary network traversal

### Private DNS
- Not required, but recommended
- Connectors resolve internal addresses locally — no public DNS entries needed
- Users connect via private DNS names (e.g., `resource.company.int`)
- Private DNS names become unresolvable when Twingate is disconnected or access is revoked
- Prevents address space collisions during deployment expansion

### Routing
- No changes to existing network routing rules required
- Deploy separate Connectors per subnet instead of routing traffic between subnets
- Example: `10.1.0.0/16` and `10.2.0.0/16` (no cross-subnet routing) → deploy Connectors at `10.1.0.35` and `10.2.0.35` respectively

### Firewall Rules
- **No inbound traffic required** for Connectors or Resources
- Connectors initiate outbound-only connections to Twingate
- User-to-Resource traffic travels over the established outbound connection

## Configuration Values
| Scenario | Configuration |
|----------|--------------|
| Isolated subnets | One Connector per subnet |
| Peered VPCs (shared address space) | Single Remote network |
| Independent VPCs | Separate Remote networks + separate Connector sets |

## Gotchas
- "Network segment" = any address space routable from deployed Connectors, regardless of physical topology
- Private DNS names only resolve while Twingate is connected and access is active — plan for user impact during outages/revocation
- Forcing VPC peering solely for remote access degrades performance vs. separate Remote networks

## Prerequisites
- Connectors deployed within each target network segment
- (Optional) Internal DNS infrastructure for private DNS resolution

## Related Docs
- [How DNS works with Twingate](#)
- [Deploying Connectors](#) (Connector network requirements)
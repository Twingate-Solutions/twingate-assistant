# Remote Network Best Practices

## Page Title
Remote Network Best Practices

## Summary
Guidelines for structuring Twingate Remote networks around network segments, DNS configuration, routing, and firewall rules. Proper configuration avoids performance penalties and keeps internal infrastructure hidden from the internet.

## Key Information

### Network Segmentation
- Configure **one Remote network per network segment** (any address space accessible from deployed Connectors)
- Peered VPCs with combined accessible address space can share a single Remote network
- No performance penalty for multiple Remote networks; separate networks may **improve performance** by avoiding unnecessary network traversal
- Deploy separate Connector sets per VPC when VPCs don't need to be peered

### Private DNS
- Not required, but **recommended** for better UX and to avoid address space collisions
- Twingate resolves internal addresses via Connectors—no public DNS entries needed
- Users connect via private DNS names (e.g., `resource.company.int`)
- Private DNS names become **unresolvable** when Twingate is disconnected or access is revoked
- Internal network remains fully hidden from the internet

### Routing
- **No routing rule changes required** when deploying Twingate
- Deploy one Connector per subnet when subnets are isolated from each other
- Each Connector resolves local addresses on its own subnet independently

### Firewall Rules
- **No inbound traffic required** from internet or any source for Connectors or Resources
- Connectors only initiate **outbound connections** to Twingate to authenticate and receive Resource lists
- User-to-Resource traffic flows over the established outbound connection

## Configuration Pattern

| Scenario | Recommendation |
|----------|---------------|
| Two peered VPCs, shared address space | Single Remote network, shared Connectors |
| Two isolated VPCs | Separate Remote networks, separate Connectors |
| Isolated subnets (e.g., `10.1.0.0/16`, `10.2.0.0/16`) | One Connector per subnet |

## Gotchas
- Peering VPCs solely for remote access introduces unnecessary network traversal—use separate Remote networks instead
- Private DNS names fail silently (unresolvable) when access is revoked, which is by design but may confuse users
- Connectors must have outbound internet access to reach Twingate services

## Related Docs
- [How DNS works with Twingate](#)
- [Deploying Connectors](#) (Connector network requirements)
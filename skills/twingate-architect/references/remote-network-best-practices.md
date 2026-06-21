# Remote Network Best Practices

## Page Title
Remote Network Best Practices

## Summary
Guidelines for structuring Twingate Remote networks across network segments, DNS configuration, routing, and firewall rules. One Remote network per accessible address space is the standard pattern, with private DNS recommended for better UX.

## Key Information

**Network Segmentation:**
- Configure one Remote network per network segment (any address space accessible from deployed Connectors)
- Peered VPCs sharing an address space can be a single Remote network
- Multiple Remote networks have no performance penalty; separate Connectors per segment often improves performance by avoiding cross-network traversal

**Private DNS:**
- Not required, but recommended
- Connectors resolve internal addresses locally — no public DNS entries needed
- Users connect via private hostnames (e.g., `resource.company.int`)
- If Twingate is disconnected or access revoked, private DNS names become unresolvable

**Routing:**
- No routing rule changes required for remote access
- Connectors resolve addresses local to their own subnet
- Example: Two isolated subnets (`10.1.0.0/16`, `10.2.0.0/16`) each get their own Connector — no cross-subnet traffic needed

**Firewall:**
- No inbound traffic required from Internet or any source to Connectors or Resources
- Connectors initiate outbound-only connections to Twingate relay
- User-to-Resource traffic flows over the established outbound connection

## Prerequisites
- Connectors deployed within the target network segment
- Network routing allows Connector hosts to reach Resources on their local subnet

## Configuration Values
| Scenario | Pattern |
|---|---|
| Peered VPCs, shared address space | Single Remote network, shared Connectors |
| Isolated subnets | Separate Remote network + Connector per subnet |
| Private DNS hostname | `resource.company.int` (any internal domain) |

## Gotchas
- "Network segment" = any address space routable from Connectors, regardless of physical location
- Private DNS names only resolve while Twingate is connected and user has access — plan user communications accordingly
- Do not deploy a single Connector expecting it to bridge two subnets that cannot route between each other

## Related Docs
- [How DNS works with Twingate](#) — DNS resolution behavior details
- [Deploying Connectors](#) — Connector network requirements and outbound connection specs
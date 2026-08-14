---
source: https://www.twingate.com/docs/remote-network-best-practices
type: docs
fetched: 2026-08-14
source_version: 7dc196d0fc2b48c6cfbb10f649d29a58339cb9f1a041a933cf8f56ad6179e7c9
---

# Remote Network Best Practices

## Page Title
Remote Network Best Practices

## Summary
Guidelines for configuring Twingate Remote networks optimally across network segments, DNS, routing, and firewall rules. One Remote network per routable network segment is the standard approach, with private DNS recommended for better UX and security.

## Key Information

### Remote Network Configuration
- **One Remote network per network segment** — group Resources accessible from the same Connector deployment
- Peered VPCs can share a single Remote network if their combined address space is accessible from deployed Connectors
- Multiple Remote networks have **no performance penalty** — multiple networks may actually improve performance by avoiding unnecessary network traversal
- Separate Connectors per network segment routes traffic directly to destination without cross-network hops

### Private DNS
- Twingate resolves addresses local to remote networks via Connectors — **no public DNS entries required**
- Private DNS is **recommended but not required**
- Benefits: better UX, avoids IP address space collisions as deployment scales
- Users access Resources via private names (e.g., `resource.company.int`)
- Private DNS names become **unresolvable** when Twingate is disconnected or access is revoked

### Routing
- **No routing rule changes required** for remote access deployment
- Each Connector resolves local addresses on its own subnet independently
- Example: Two isolated subnets (`10.1.0.0/16`, `10.2.0.0/16`) — deploy one Connector per subnet (`10.1.0.35`, `10.2.0.35`); no cross-subnet traffic required

### Firewall Rules
- **No inbound traffic required** from the Internet or any source for Connectors or Resources
- Connectors initiate **outbound-only** connections to Twingate to authenticate and receive authorized Resource list
- User-to-Resource traffic flows over the established outbound connection

## Prerequisites
- Twingate Connectors deployed within target network segments
- Network access from Connector host to destination Resources within same segment

## Gotchas
- "Network segment" = any address space routable from deployed Connectors, regardless of physical topology
- Peering VPCs solely for remote access is unnecessary with Twingate — separate Remote networks per VPC is more efficient
- Private DNS names only resolve while Twingate is active and user has access; plan UX accordingly

## Related Docs
- [How DNS works with Twingate](#) — DNS resolution details
- [Deploying Connectors](#) — Connector network requirements and outbound connection specifics
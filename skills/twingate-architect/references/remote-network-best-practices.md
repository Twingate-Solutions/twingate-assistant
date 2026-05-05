# Remote Network Best Practices

## Page Title
Remote Network Best Practices

## Summary
Guidelines for configuring Twingate Remote networks optimally across network segments, DNS, routing, and firewall rules. One Remote network per routable network segment is the standard model, with Connectors handling local address resolution without requiring infrastructure changes.

## Key Information

### Network Segmentation
- **One Remote network per network segment** (any address space accessible from deployed Connectors)
- Peered VPCs can share a single Remote network if their combined address space is accessible from the same Connectors
- Multiple Remote networks have **no performance penalty**; separate Connectors per VPC may improve performance by eliminating cross-VPC traversal
- "Network segment" is logical, not physical

### Private DNS
- Twingate does **not** require public DNS entries
- Connectors resolve internal addresses locally — internal network stays hidden from the internet
- Private DNS is **recommended but not required**
- Users connect via private names (e.g., `resource.company.int`); names become unresolvable if Twingate disconnects or access is revoked

### Routing
- **No routing rule changes required** for Twingate deployment
- Each Connector resolves addresses on its own local subnet
- Example: Two isolated subnets (`10.1.0.0/16`, `10.2.0.0/16`) each get one Connector; cross-subnet traffic flow is unnecessary

### Firewall Rules
- **No inbound traffic required** from internet or any source to Connectors or Resources
- Connectors initiate **outbound-only connections** to Twingate for auth and Resource list
- User-to-Resource traffic flows over this established outbound connection

## Prerequisites
- Connectors deployed within target network segments
- (Optional) Internal DNS infrastructure for private DNS names

## Configuration Values
- No specific env vars or CLI flags on this page
- Connector placement: one per isolated subnet for segmented networks

## Gotchas
- If two VPCs are peered **only** for remote access purposes, separate Remote networks with dedicated Connectors per VPC is more efficient
- Private DNS names fail to resolve entirely when Twingate is disconnected — users have no fallback resolution
- Address space collision becomes a risk without private DNS as deployments scale

## Related Docs
- [How DNS works with Twingate](#) — DNS resolution detail
- [Deploying Connectors](#) — Connector network requirements
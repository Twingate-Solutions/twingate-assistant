# Remote Network Best Practices

## Summary
Guidelines for structuring Twingate Remote networks to match network topology, optimize performance, and maintain security. Covers network segmentation, private DNS setup, routing, and firewall configuration for Connector deployments.

## Key Information

- **One Remote network per network segment** — group Resources by what's accessible from Connectors in that network
- Peered VPCs with shared address space can be a single Remote network; separate VPCs without peering should be separate Remote networks for better performance
- No performance penalty for multiple Remote networks
- Connectors resolve addresses local to their deployed network segment
- Private DNS recommended but not required
- No inbound firewall rules needed for Connectors or Resources
- Connectors only make outbound connections to Twingate

## Network Segmentation

- "Network segment" = any address space routable from deployed Connectors, regardless of physical location
- Separate Remote networks improve performance by routing traffic directly without additional network traversal
- Example: Two unpeered VPCs → two Remote networks with separate Connector sets

## Private DNS

- Twingate resolves internal addresses via Connectors without public DNS entries
- Private DNS names (e.g., `resource.company.int`) are resolvable only when Twingate is connected and user has access
- If Twingate disconnects or access is revoked, private DNS names become unresolvable
- Helps avoid IP address space collisions as deployment grows

## Routing

- No routing rule changes required to accommodate Twingate deployment
- Deploy separate Connectors per subnet to avoid requiring cross-subnet traffic flow
- **Example**: Two isolated subnets `10.1.0.0/16` and `10.2.0.0/16` → deploy one Connector on each (`10.1.0.35`, `10.2.0.35`); each resolves local addresses independently

## Firewall Configuration

- **No inbound traffic required** from Internet or any source to Connectors or Resources
- Connectors initiate outbound-only connections to Twingate for authentication and Resource list retrieval
- User-to-Resource traffic flows over the established outbound connection

## Gotchas

- Combining VPCs into one Remote network only works if the full combined address space is accessible from the Connectors — verify reachability before consolidating
- Private DNS names fail silently (unresolvable) when access is revoked; users may not immediately understand why
- Removing cross-subnet routing rules is safe with Twingate, but ensure Connectors are deployed on each isolated segment before making routing changes

## Related Docs

- [How DNS works with Twingate](#) — DNS resolution details
- [Deploying Connectors](#) — Connector network requirements and outbound connection specs
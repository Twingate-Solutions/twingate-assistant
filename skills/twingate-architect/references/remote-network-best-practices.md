# Remote Network Best Practices

## Page Title
Remote Network Best Practices

## Summary
Guidelines for configuring Twingate Remote networks efficiently across multiple network segments. Covers network topology decisions, DNS configuration, routing setup, and firewall requirements for Connector deployments.

## Key Information

### Network Segmentation
- Configure **one Remote network per network segment** (any address space accessible from deployed Connectors)
- Peered VPCs with combined accessible address space can be treated as a single Remote network
- Multiple Remote networks have **no performance penalty** if topology requires it
- For unpeered VPCs: deploy separate Connectors per VPC for better performance (avoids extra network traversal)

### Private DNS
- Not required, but **recommended** for better UX and to avoid address space collisions
- Connectors resolve internal addresses locally — no public DNS entries needed
- Users connect using private DNS names (e.g., `resource.company.int`)
- Private DNS names become **unresolvable** when Twingate is disconnected or access is revoked

### Routing
- **No routing rule changes required** when deploying Twingate
- Each Connector resolves addresses local to its own subnet
- Example: Two isolated subnets (`10.1.0.0/16`, `10.2.0.0/16`) each get their own Connector; no cross-subnet traffic needed

### Firewall Rules
- **No inbound traffic required** from Internet or any source for Connectors or Resources
- Connectors only initiate **outbound connections** to Twingate for authentication and resource list retrieval
- User-to-Resource traffic flows over the established outbound connection

## Prerequisites
- Twingate Connectors deployed within target network segments
- Network segments accessible from Connector hosts

## Configuration Values
| Scenario | Recommendation |
|----------|---------------|
| Peered VPCs (shared address space) | Single Remote network |
| Unpeered VPCs | Separate Remote networks + separate Connectors |
| Isolated subnets | One Connector per subnet |

## Gotchas
- Treating peered VPCs as one Remote network only works if the **combined address space has no conflicts**
- Private DNS names resolve only while Twingate is active and user has access — plan for client-side DNS fallback behavior
- Do not configure inbound firewall rules expecting Connector traffic; all connections are outbound-initiated

## Related Docs
- [How DNS works with Twingate](#) — DNS resolution behavior details
- [Deploying Connectors](#) — Connector network requirements and outbound connection specs
# Remote Network Best Practices

## Page Title
Remote Network Best Practices

## Summary
Guidance on structuring Twingate Remote networks for optimal performance and security. Covers network segmentation strategy, private DNS configuration, routing, and firewall rules for Connector deployments.

## Key Information

### Network Segmentation
- Configure **one Remote network per network segment** (any address space accessible from deployed Connectors)
- Peered VPCs sharing an address space can be a single Remote network
- Multiple Remote networks have **no performance penalty**
- If VPCs aren't otherwise peered, separate Remote networks with separate Connectors per VPC improves performance (avoids unnecessary network traversal)

### Private DNS
- Not required, but recommended for better UX and to avoid address space collisions
- Connectors resolve internal addresses locally — no public DNS entries needed
- Users connect via private DNS names (e.g., `resource.company.int`) while Twingate is active
- Private DNS names become unresolvable when Twingate is disconnected or access is revoked

### Routing
- **No routing rule changes required** when deploying Twingate
- Deploy Connectors per subnet to handle isolated subnets independently
- Example: Two isolated subnets (`10.1.0.0/16`, `10.2.0.0/16`) each get their own Connector; cross-subnet routing not needed

### Firewall Rules
- **No inbound traffic required** for Connectors or Resources from Internet or any source
- Connectors initiate **outbound-only** connections to Twingate to authenticate and receive Resource lists
- User-to-Resource traffic travels over the established outbound connection

## Prerequisites
- Twingate Connectors deployed within target network segments
- Network access from Connector hosts to Twingate control plane (outbound only)

## Configuration Values
| Scenario | Recommendation |
|----------|---------------|
| Peered VPCs, shared address space | Single Remote network |
| Independent VPCs | Separate Remote networks + separate Connectors |
| Isolated subnets | One Connector per subnet |

## Gotchas
- "Network segment" is logical (accessible from Connectors), not physical — geography doesn't determine segmentation
- Private DNS names fail silently to users when Twingate is off or access is revoked — communicate this to users
- Connector outbound connectivity to Twingate must be permitted; verify firewall egress rules aren't blocking this

## Related Docs
- [How DNS works with Twingate](#) — DNS resolution details
- [Deploying Connectors](#) — Connector network requirements
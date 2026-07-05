# Remote Network Best Practices

## Page Title
Remote Network Best Practices

## Summary
Guidelines for structuring Twingate Remote networks around network segments, DNS configuration, routing, and firewall rules. Proper network segmentation improves performance and security isolation. No inbound firewall rules or public DNS entries are required.

## Key Information

- **One Remote network per network segment** — group Resources that are routable/accessible from the same set of Connectors
- **Peered VPCs** can share a single Remote network if their combined address space is accessible from deployed Connectors
- **Multiple Remote networks** have no performance penalty; separate networks may *improve* performance by routing traffic directly without cross-network traversal
- **Connectors only make outbound connections** — no inbound traffic required from Internet or any source
- **Private DNS is recommended but not required** — enables friendly names (e.g., `resource.company.int`) and prevents address space collisions
- **DNS resolution** for internal addresses is handled by deployed Connectors; private DNS names become unresolvable when Twingate is disconnected or access is revoked
- **No routing rule changes required** — each Connector resolves addresses local to its own subnet

## Prerequisites
- Twingate Connectors deployed within each target network segment
- (Optional) Internal DNS infrastructure for private DNS setup

## Configuration Patterns

### Network Segmentation
| Scenario | Recommendation |
|---|---|
| Two peered VPCs, combined address space accessible from Connectors | Single Remote network |
| Two VPCs not otherwise peered | Separate Remote networks with Connectors in each |
| Two isolated subnets (e.g., `10.1.0.0/16`, `10.2.0.0/16`) | One Connector per subnet, separate Remote networks |

### Subnet Isolation Example
- Subnet A: `10.1.0.0/16` → Connector at `10.1.0.35`
- Subnet B: `10.2.0.0/16` → Connector at `10.2.0.35`
- Result: Remote access to both subnets without requiring inter-subnet routing

## Gotchas

- "Network segment" is logical, not physical — it means any address space accessible from deployed Connectors
- Private DNS names resolve **only while Twingate is connected and access is authorized**; revoked users cannot resolve names
- Do not configure routing rules to funnel all traffic through a single entry point — Twingate eliminates this need

## Related Docs
- [How DNS works with Twingate](#) — DNS resolution behavior details
- [Deploying Connectors](#) — Connector network requirements and outbound connection specs
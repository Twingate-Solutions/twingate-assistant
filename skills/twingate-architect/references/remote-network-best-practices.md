# Remote Network Best Practices

## Page Title
Remote Network Best Practices

## Summary
Guidelines for configuring Twingate Remote networks to match your network topology. Covers segmentation strategy, private DNS setup, routing, and firewall configuration. No changes to existing network routing or inbound firewall rules are required.

## Key Information

- **One Remote network per network segment** — group Resources by address spaces accessible from the same deployed Connectors
- Peered VPCs with a shared accessible address space can be a single Remote network
- Separate Remote networks per VPC (no peering) improves performance — traffic routes directly to destination without extra traversal
- Multiple Remote networks have **no performance penalty** when topology warrants it
- Connectors **only make outbound connections** to Twingate; no inbound traffic required from Internet or any source
- Private DNS is **recommended but not required**; enables user-friendly names (`resource.company.int`) and avoids IP collision
- Private DNS names become unresolvable when Twingate is disconnected or access is revoked — acts as natural access enforcement
- No changes to existing network routing rules needed

## Prerequisites
- Twingate Connectors deployed in target network segments
- (Optional) Internal DNS infrastructure for private DNS setup

## Configuration Patterns

### Multi-Subnet Routing Example
| Subnet | Connector Host | Remote Network |
|--------|---------------|----------------|
| `10.1.0.0/16` | `10.1.0.35` | Network A |
| `10.2.0.0/16` | `10.2.0.35` | Network B |

Each Connector resolves local addresses on its own subnet — no cross-subnet routing required.

## Gotchas

- Treating peered VPCs as **one** Remote network is valid only if the combined address space is fully routable from the same Connectors
- If VPCs are peered solely for remote access purposes, **separate** Remote networks with separate Connectors will perform better
- Private DNS names fail to resolve when Twingate is off — inform users so they don't mistake this for an outage
- Do not add inbound firewall rules for Connectors; doing so is unnecessary and expands attack surface

## Related Docs
- [How DNS works with Twingate](#) — DNS resolution behavior with Connectors
- [Deploying Connectors](#) — Connector network requirements and outbound connection details
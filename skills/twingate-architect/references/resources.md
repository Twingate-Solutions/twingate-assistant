# Twingate Resources

## Summary
Resources are network addresses (DNS names, IPs, CIDR ranges) secured via Twingate and accessible only to authorized users. Traffic routes through Connectors in an associated Remote Network, enabling access to private resources without exposing them publicly. Zero Trust principles apply—access is denied by default.

## Key Information
- Resource types: FQDN, wildcard FQDN, single IP, CIDR range
- Address resolution occurs **from the Connector**, not the client device
- Wildcards: `*` = 0+ chars, `?` = exactly 1 char; `*.autoco.internal` does NOT match `autoco.internal` itself
- CGNAT subnet `100.96.0.0/12` is reserved by Twingate client—resources in this range are blocked
- Default traffic: all TCP, UDP ports + ICMP ping forwarded
- Aliases are resolved by the Connector; no DNS entry required for alias addresses

## Prerequisites
- Connector(s) deployed in the target Remote Network
- Resource must be routable/resolvable from the Connector
- Port restrictions require **all Connectors on the Remote Network** at v1.20.0+
- Client visibility settings require minimum client versions (macOS 1.0.25, Windows 1.0.23, iOS 1.0.25, Android 1.0.22, Linux 1.0.74)

## Configuration Values

**Resource fields:**
- `label` — display name in Admin Console and Client
- `address` — FQDN, wildcard FQDN, IP, or CIDR
- `alias` — optional secondary address (Connector-resolved)
- `port restrictions` — TCP/UDP ports configurable independently; ICMP togglable
- `remote_network` — associated Remote Network
- `tags` — optional metadata
- `visibility` — `Standard Address` | `Browser Address` | `Background Address`

## Address Resolution Priority (overlapping resources)
1. Single IP > CIDR (smaller CIDR > larger CIDR)
2. Exact FQDN > wildcard FQDN (more non-wildcard chars = more specific)
3. Truly ambiguous addresses resolve arbitrarily

**DNS best practices for private IPs (ordered):**
1. Configure private DNS resolution
2. Use FQDN-based resource
3. Use private IP resource
4. Use CIDR block (least granular)

## Port Restrictions Use Cases
- Limit all users to specific ports (replaces per-host firewall rules)
- Split access by port: e.g., create two resources (`host:443` for all users, `host:22` for admin group)

## Gotchas
- Invalid CIDR notation (e.g., `10.1.0.1/16`) returns `Invalid IP or FQDN` error—use proper network addresses
- Overlapping resources should be avoided; use specificity rules to predict routing behavior
- DNS rebinding protection may interfere with public FQDNs resolving to private IPs—use FQDN or private DNS resource instead of IP resource
- Unqualified DNS names (e.g., `host`) require additional Connector configuration and latest client
- Visibility settings don't affect Admin Console display

## Related Docs
- How DNS Works with Twingate
- Resource Aliases
- Whitelisting Traffic to Public Resources
- IP Overlap Guide
- Upgrading Connectors
- Hiding Resources in the Client
# Twingate Resources

## Summary
Resources are network addresses (DNS names, IPs, CIDR ranges) secured via Twingate and accessible only to authorized users. Address resolution occurs from the Connector on the associated Remote Network, enabling private DNS and internal IPs to work transparently. Traffic is denied by default per Zero Trust principles.

## Key Information
- Resource types: FQDN, wildcard FQDN, single IP, CIDR range
- Wildcard `*` = 0+ characters; `?` = exactly 1 character
- `*.autoco.internal` matches `host.autoco.internal` but NOT `autoco.internal` itself
- Default: all TCP, UDP ports, and ICMP (ping) forwarded
- Address resolution performed **from the Connector**, not the user's device
- Zero Trust default: deny all unless explicitly granted via Group membership
- Reserved CGNAT subnet `100.96.0.0/12` is blocked by the client

## Prerequisites
- Connector(s) deployed in the target Remote Network
- Resource address must be resolvable/routable from the Connector
- Port restrictions require all Connectors on the Remote Network at **v1.20.0+**
- Client visibility settings require minimum client versions (macOS 1.0.25+, Windows 1.0.23+, Linux 1.0.74+, iOS 1.0.25+, Android 1.0.22+)

## Resource Definition Fields
| Field | Details |
|-------|---------|
| Label | Display name in Admin Console and Client |
| Address | FQDN, wildcard FQDN, IP, or CIDR |
| Alias | Extra address; resolved by Connector, no DNS setup needed |
| Port restrictions | TCP/UDP per-port; ICMP toggle |
| Remote Network | Must contain Connectors that can reach the resource |
| Tags | Optional metadata for organization |
| Client visibility | Standard, Browser (with shortcut), or Background (hidden) |

## Configuration Values
- Valid CIDR: `10.1.0.0/16` ✓ — Invalid: `10.1.0.1/16` → returns `Invalid IP or FQDN`
- Unqualified DNS names (e.g., `host`) require additional Connector configuration and latest client

## Address Resolution Best Practices
For DNS names resolving to private IPs (in priority order):
1. **Private DNS** — configure in private DNS, never exposed publicly
2. **FQDN Resource** — Connector handles resolution
3. **Private IP Resource** — direct routing, brittle if IP changes
4. **CIDR Resource** — broad coverage, less access control granularity

## Overlapping Addresses (Specificity Rules)
- Single IP > CIDR (smaller CIDR > larger CIDR)
- Exact FQDN > wildcard FQDN
- Wildcard with more non-wildcard characters wins
- Truly ambiguous addresses resolved arbitrarily — **avoid overlaps**

## Port Restrictions
- Apply TCP and UDP restrictions independently
- Use case 1: Limit all users to necessary ports
- Use case 2: Split same host into multiple Resources with different port/group combos (e.g., `host:443` for all users, `host:22` for admins)

## Gotchas
- DNS rebinding protection may break public FQDNs resolving to private IPs — use FQDN or private DNS Resource instead
- CGNAT range `100.96.0.0/12` is reserved by Twingate client and cannot be used
- Port restrictions unavailable if any Connector on the Remote Network is below v1.20.0
- Visibility settings don't affect Admin Console view
- Invalid CIDR notation (host bits set) causes error

## Related Docs
- [How DNS Works with Twingate](#)
- [Resource Aliases](#)
- [IP Overlap Guide](#)
- [Whitelisting Traffic to Public Resources](#)
- [Hiding Resources in the Client](#)
- [Upgrading Connectors](#)
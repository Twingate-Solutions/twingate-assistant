# Twingate Resources

## Summary
Resources are network addresses (DNS names, IPs, CIDR ranges) secured via Twingate and accessed through Connectors deployed in Remote Networks. Access is deny-by-default; users must be explicitly granted access via Groups. Resolution occurs from the Connector's perspective, enabling private DNS and IP routing for remote users.

## Key Information
- Resource address types: FQDN, wildcard FQDN, single IP, CIDR range
- Wildcard `*` = 0+ characters; `?` = exactly 1 character
- `*.autoco.internal` matches subdomains but NOT `autoco.internal` itself
- Reserved CGNAT subnet `100.96.0.0/12` is blocked by the Twingate client
- Default traffic forwarding: all TCP, UDP ports + ICMP ping
- Tags are optional metadata for organization
- Aliases provide additional addresses without DNS configuration

## Prerequisites
- Connector(s) deployed in the associated Remote Network
- Resource must be resolvable and routable **from the Connector**, not the end-user device
- Port restrictions require all Connectors on the Remote Network at **v1.20.0+**

## Configuration Values

| Field | Options/Notes |
|-------|--------------|
| Address | FQDN, wildcard FQDN, IP, CIDR |
| Invalid CIDR example | `10.1.0.1/16` returns `Invalid IP or FQDN` |
| Port protocols | TCP, UDP (configurable separately), ICMP (toggle) |
| Default ports | All TCP + UDP + ICMP |
| Client visibility | `Standard Address`, `Browser Address`, `Background Address` |

## Address Resolution Best Practices
For DNS resolving to private IPs (ordered by best practice):
1. **Private DNS** — configure in private DNS, never exposed publicly
2. **FQDN Resource** — Connector handles resolution
3. **Private IP Resource** — direct routing, no DNS flexibility
4. **CIDR Block** — broad coverage, less access control granularity

## Overlapping Address Resolution (Specificity Rules)
- Single IP > CIDR (smaller CIDR > larger CIDR)
- Exact domain > wildcard domain
- Wildcard with more non-wildcard characters wins
- Truly ambiguous resources are chosen arbitrarily

## Client Visibility Requirements (minimum versions)
- macOS 1.0.25, Windows 1.0.23, iOS 1.0.25, Android 1.0.22, Linux 1.0.74

## Gotchas
- **DNS rebinding protection**: public DNS names resolving to private IPs should be defined as FQDN Resources, not IP Resources
- **Invalid CIDR**: host bits set in CIDR notation (e.g., `10.1.0.1/16`) causes an error
- **CGNAT range** `100.96.0.0/12` is always blocked — cannot create resources in this range
- Port restrictions apply to **all Connectors** in the Remote Network; mixed versions disable the feature
- Overlapping resources are discouraged; ambiguous matches are non-deterministic
- Unqualified DNS names (e.g., `host`) require additional Connector configuration and latest client

## Related Docs
- How DNS Works with Twingate
- Resource Aliases
- Whitelisting Traffic to Public Resources
- IP Overlap Guide
- Hiding Resources in the Client
- Upgrading Connectors
- Port Restrictions
# Twingate Resources

## Summary
Resources are network addresses (IP, CIDR, FQDN, or wildcard DNS) secured via Twingate and accessed through Connectors deployed in Remote Networks. Access follows Zero Trust principles—denied by default unless explicitly granted via Group membership. DNS resolution and routing occur from the Connector's perspective, not the end user's device.

## Key Information
- Resource types: FQDN, wildcard FQDN, single IP, CIDR range, or unqualified DNS name
- Address resolution happens **from the Connector**, enabling private DNS and private IPs to work for remote users
- CGNAT subnet `100.96.0.0/12` is reserved by Twingate client—resources in this range are blocked
- Overlapping addresses resolved by specificity: single IP > small CIDR > large CIDR; exact domain > wildcard
- Ambiguous/identical addresses are resolved arbitrarily
- Tags are optional metadata for organization

## Prerequisites
- Connector(s) deployed in associated Remote Network
- Resource must be resolvable and routable from Connector
- Port restrictions require all Connectors on the Remote Network at **v1.20.0+**
- Client visibility settings require minimum client versions (macOS 1.0.25+, Windows 1.0.23+, Linux 1.0.74+, iOS 1.0.25+, Android 1.0.22+)

## Resource Definition Fields
| Field | Details |
|-------|---------|
| Label | Display name in Admin Console and Client |
| Address | FQDN, wildcard FQDN, IP, or CIDR (must be valid network address, e.g., `10.1.0.0/16` not `10.1.0.1/16`) |
| Alias | Optional extra address; resolved by Connector, no DNS entry needed |
| Port Restrictions | Default: all TCP/UDP + ICMP; configurable per protocol |
| Remote Network | Associated Remote Network with reachable Connector(s) |
| Tags | Optional metadata |
| Client Visibility | Standard, Browser (adds Open in Browser shortcut), or Background (hidden) |

## Configuration Values / Gotchas

**Address format errors:**
- Invalid CIDR (host bits set): `10.1.0.1/16` → returns `Invalid IP or FQDN`
- Wildcard `*.autoco.internal` matches `host.autoco.internal` but **not** `autoco.internal` itself

**DNS best practices (for resources resolving to private IPs):**
1. Configure private DNS (preferred)
2. Use FQDN-based Resource
3. Use private IP-based Resource
4. Use CIDR block (least granular)

**Port restriction split-access pattern:**
- Create two Resources with same address but different ports (e.g., `host:22`, `host:443`)
- Assign each to different Groups for granular access control

**ICMP:** Forwarded by default; can be explicitly toggled off via port restrictions

## Gotchas
- DNS rebinding protection on modern systems may break public FQDNs resolving to private IPs—use DNS Resources instead
- Overlapping CIDR Resources can cause unexpected routing; more specific always wins
- Unqualified DNS names (e.g., `host`) require additional Connector configuration
- Port restrictions unavailable if any Connector in the Remote Network is below v1.20.0
- Visibility settings don't affect Admin Console display

## Related Docs
- [How DNS Works with Twingate](#)
- [Resource Aliases](#)
- [IP Overlap Guide](#)
- [Whitelisting Traffic to Public Resources](#)
- [Upgrading Connectors](#)
- [Hiding Resources in the Client](#)
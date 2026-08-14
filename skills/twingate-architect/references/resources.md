---
source: https://www.twingate.com/docs/resources
type: docs
fetched: 2026-08-14
source_version: 9649710dd3af9e154bcfb163b6d8c60a985ba8b5a6fd77a6d8bd12de646b8b6d
---

# Twingate Resources

## Summary
Resources are network addresses (DNS names, IPs, CIDR ranges) secured via Twingate and accessed through Connectors deployed in Remote Networks. Access follows Zero Trust defaults—all traffic is denied unless explicitly granted to a user group. Resolution occurs from the Connector's perspective, enabling private DNS and IP access for remote users.

## Key Information
- Resource types: FQDN, wildcard FQDN, single IP, CIDR range
- Wildcards: `*` = 0+ chars, `?` = exactly 1 char; `*.autoco.internal` does NOT match `autoco.internal` itself
- Default traffic forwarding: all TCP, UDP ports + ICMP ping
- Address resolution happens **from the Connector**, not the client device
- Tags are optional metadata for organization
- Groups grant access; no group assignment = no access

## Prerequisites
- Connector(s) deployed in the target Remote Network
- Resource address must be resolvable and routable from the Connector
- Port restrictions require all Connectors on the Remote Network to be **v1.20.0+**

## Configuration Values

| Field | Options/Notes |
|-------|---------------|
| Address | FQDN, wildcard FQDN, single IP, CIDR (must be valid, e.g., `10.1.0.0/16` not `10.1.0.1/16`) |
| Ports | TCP and/or UDP; ICMP toggle; defaults to all |
| Visibility | `Standard Address`, `Browser Address`, `Background Address` |
| Alias | Extra address; no DNS entry needed; resolved by Connector |

## Gotchas
- **CGNAT block**: `100.96.0.0/12` is reserved by Twingate client—resources in this range are inaccessible by IP
- **Invalid CIDR**: Host bits set (e.g., `10.1.0.1/16`) returns `Invalid IP or FQDN` error
- **DNS rebinding protection**: Public FQDNs resolving to private IPs should be defined as DNS Resources, not IP Resources
- **Overlapping resources**: More specific wins (single IP > small CIDR > large CIDR; non-wildcard > wildcard; more non-wildcard chars > fewer). Truly ambiguous = arbitrary selection
- **Unqualified DNS names** (e.g., `host`): Require additional Connector config and latest client
- **Visibility settings** don't affect Admin Console display; client version minimums apply

## Address Resolution Best Practices (priority order)
1. Private DNS resolution (configure in private DNS)
2. FQDN-based Resource
3. Private IP-based Resource
4. CIDR block Resource

## Client Visibility Minimum Versions
- macOS 1.0.25+, Windows 1.0.23+, iOS 1.0.25+, Android 1.0.22+, Linux 1.0.74+

## Related Docs
- [How DNS Works with Twingate](#)
- [Resource Aliases](#)
- [Port Restrictions / Upgrading Connectors](#)
- [IP Overlap Guide](#)
- [Whitelisting Traffic to Public Resources](#)
- [Hiding Resources in the Client](#)
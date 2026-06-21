# Twingate Resources

## Summary
Resources are network addresses (DNS, IP, CIDR) secured via Twingate and accessed through Connectors deployed in Remote Networks. Access follows Zero Trust defaults—denied unless explicitly granted via Group membership. Address resolution occurs from the Connector's perspective, enabling private DNS and IP access without client-side configuration changes.

## Key Information
- Resource types: FQDN, wildcard FQDN, single IP, CIDR range
- Wildcards: `*` = 0+ chars, `?` = exactly 1 char; `*.autoco.internal` does NOT match `autoco.internal` itself
- Default traffic: all TCP, UDP ports + ICMP forwarded unless port restrictions applied
- CGNAT subnet `100.96.0.0/12` is reserved by Twingate client—resources in this range are blocked
- Port restrictions require all Connectors on Remote Network at **v1.20.0+**
- Aliases resolved by Connector; no DNS entry required for alias address

## Prerequisites
- Connector(s) deployed in target Remote Network
- Resource address must be resolvable/routable from Connector(s)
- Port restrictions: all Connectors ≥ v1.20.0

## Configuration Values

| Field | Options/Notes |
|-------|---------------|
| Address | FQDN, wildcard FQDN, IP, CIDR (must be valid, e.g. `10.1.0.0/16` not `10.1.0.1/16`) |
| Ports | TCP/UDP independently configurable; ICMP toggle; default = all |
| Visibility | `Standard Address`, `Browser Address`, `Background Address` |
| Access | Assigned via Groups |

## Specificity Rules (Overlapping Addresses)
- Single IP > CIDR; smaller CIDR > larger CIDR
- Exact domain > wildcard; more non-wildcard chars > fewer
- Truly ambiguous (same address) = arbitrary selection

## Gotchas
- Invalid CIDR notation (host bits set, e.g. `10.1.0.1/16`) returns `Invalid IP or FQDN` error
- DNS rebinding protection: define private-resolving public DNS names as DNS Resources, not IP Resources
- Unqualified hostnames (e.g. `host`) require additional Connector config + latest client
- Visibility settings require minimum client versions (macOS 1.0.25, Windows 1.0.23, Linux 1.0.74, iOS 1.0.25, Android 1.0.22)
- Avoid overlapping Resources; use most-specific addressing when overlap is unavoidable

## Address Resolution Best Practices (private IPs)
1. Private DNS resolution (preferred)
2. FQDN-based Resource
3. Private IP-based Resource
4. CIDR block (least granular)

## Related Docs
- How DNS Works with Twingate
- Resource Aliases
- Port Restrictions / Upgrading Connectors
- IP Overlap Guide
- Whitelisting Traffic to Public Resources
- Hiding Resources in the Client
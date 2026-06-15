# Twingate Resources

## Summary
Resources are network addresses (DNS names, IPs, CIDR ranges) secured via Twingate and accessed through Connectors in a Remote Network. Access is denied by default (Zero Trust); users must be explicitly granted access via Groups. Address resolution occurs from the Connector, enabling private DNS and IP access without client-side configuration changes.

## Key Information
- Resource types: FQDN, wildcard FQDN, single IP, CIDR range, unqualified DNS name
- Wildcard `*.autoco.internal` matches subdomains but **not** `autoco.internal` itself
- `*` = 0+ characters, `?` = exactly 1 character in wildcards
- CGNAT subnet `100.96.0.0/12` is reserved by Twingate client — resources in this range are blocked
- Default traffic: all TCP, UDP ports + ICMP (ping) forwarded
- Aliases are resolved by the Connector; no DNS entry required for alias addresses
- Tags are optional metadata for organizing resources

## Prerequisites
- Connector(s) deployed in target Remote Network, v1.20.0+ required for port restrictions
- Resource address must be resolvable and routable from the Connector(s)
- Unqualified DNS names require additional Connector configuration + latest client

## Configuration Values

| Field | Options/Notes |
|-------|---------------|
| Address | FQDN, wildcard FQDN, IP, CIDR (must use network address, e.g. `10.1.0.0/16` not `10.1.0.1/16`) |
| Ports | TCP and/or UDP, configurable per protocol; ICMP toggle |
| Visibility | `Standard Address`, `Browser Address`, `Background Address` |
| Default ports | All TCP + UDP + ICMP |

## Gotchas
- **Invalid CIDR**: `10.1.0.1/16` returns `Invalid IP or FQDN` — must use proper network address
- **DNS rebinding**: Public FQDNs resolving to private IPs should be defined as DNS Resources, not IP Resources
- **Port restrictions**: Require ALL Connectors in Remote Network to be v1.20.0+
- **Overlapping addresses**: Most specific match wins (single IP > small CIDR > large CIDR; exact domain > wildcard); truly ambiguous resources chosen arbitrarily
- **CGNAT block**: `100.96.0.0/12` range inaccessible via Twingate client
- **Client visibility**: Hiding resources requires minimum client versions (macOS 1.0.25, Windows 1.0.23, Linux 1.0.74, iOS 1.0.25, Android 1.0.22)

## Address Resolution Priority (Best Practice Order)
1. Private DNS resolution (configure in private DNS)
2. FQDN-based Resource
3. Private IP-based Resource
4. CIDR Block Resource

## Client Visibility Minimum Versions
macOS 1.0.25 | Windows 1.0.23 | iOS 1.0.25 | Android 1.0.22 | Linux 1.0.74

## Related Docs
- How DNS Works with Twingate
- Resource Aliases
- Port Restrictions
- Whitelisting Traffic to Public Resources
- IP Overlap Guide
- Hiding Resources in the Client
- Upgrading Connectors
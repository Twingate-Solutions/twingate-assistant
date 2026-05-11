# Twingate Resources

## Summary
Resources are network addresses (DNS names, IPs, CIDR ranges) secured via Twingate and accessed through Connectors on a Remote Network. Access is denied by default (Zero Trust); users must be explicitly granted access via Groups. Address resolution occurs from the Connector, enabling private DNS and IP access without client-side configuration changes.

## Key Information
- Resource address types: FQDN, wildcard FQDN, single IP, CIDR range
- Wildcard `*` = 0+ characters; `?` = exactly 1 character
- `*.autoco.internal` matches subdomains but **not** `autoco.internal` itself
- Reserved CGNAT subnet `100.96.0.0/12` is blocked by the Twingate client
- Default traffic forwarding: all TCP, UDP ports + ICMP ping
- DNS resolution performed **from the Connector**, not the client device
- Aliases are resolved by the Connector; no DNS entry required for alias address

## Prerequisites
- Connector(s) deployed in the associated Remote Network
- Resource address must be resolvable/routable from the Connector
- Port restrictions require all Connectors on Remote Network at **v1.20.0+**
- Client visibility settings require minimum client versions (macOS 1.0.25+, Windows 1.0.23+, Linux 1.0.74+, iOS 1.0.25+, Android 1.0.22+)

## Configuration Values

| Field | Options/Notes |
|-------|--------------|
| Address | FQDN, wildcard FQDN, IP, CIDR (must use network address, e.g. `10.1.0.0/16` not `10.1.0.1/16`) |
| Ports | TCP and/or UDP per port; ICMP toggle; default = all |
| Visibility | `Standard Address`, `Browser Address`, `Background Address` |
| Tags | Optional metadata key/value |
| Alias | Extra address; resolved by Connector only |

## Overlapping Address Specificity (most → least)
1. Single IP > CIDR (smaller range > larger range)
2. Exact FQDN > wildcard FQDN
3. Wildcard with more non-wildcard characters > broader wildcard
4. Truly ambiguous = arbitrary selection

## Gotchas
- Invalid CIDR notation (host bits set, e.g. `10.1.0.1/16`) returns `Invalid IP or FQDN` error
- DNS rebinding protection: define DNS addresses resolving to private IPs as DNS Resources, not IP Resources
- Unqualified DNS names (e.g. `host`) require additional Connector configuration
- Overlapping Resources should be avoided; specificity rules determine routing when overlap exists
- Port restrictions unavailable if any Connector in Remote Network is below v1.20.0
- CGNAT range `100.96.0.0/12` cannot be used as Resource addresses

## Address Definition Best Practices (ordered)
1. Private DNS resolution (configure in private DNS)
2. FQDN-based Resource
3. Private IP-based Resource
4. CIDR block Resource (least granular)

## Related Docs
- How DNS Works with Twingate
- Resource Aliases
- Port Restrictions
- Whitelisting Traffic to Public Resources
- IP Overlap Guide
- Hiding Resources in the Client
- Upgrading Connectors
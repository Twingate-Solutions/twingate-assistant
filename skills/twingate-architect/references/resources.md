# Twingate Resources

## Summary
Resources are network addresses (DNS, IP, CIDR) secured via Twingate and accessible only through authorized Connectors in a Remote Network. Access follows Zero Trust principles—denied by default unless explicitly granted. Resolution occurs from the Connector side, enabling private DNS and IPs to work for remote users without public exposure.

## Key Information
- Resource types: FQDN, wildcard FQDN, IP address, CIDR range
- Wildcard `*` = 0+ characters; `?` = exactly 1 character
- `*.autoco.internal` matches subdomains but NOT `autoco.internal` itself
- CGNAT subnet `100.96.0.0/12` is reserved by Twingate client—blocked for resource access
- Default: all TCP, UDP ports + ICMP forwarded; configure port restrictions as needed
- Tags are optional metadata for organization
- Aliases allow additional addresses without DNS configuration

## Prerequisites
- Connector(s) deployed in the Resource's Remote Network
- Resource must be resolvable and routable from the Connector
- Port restrictions require all Connectors on Remote Network at **v1.20.0+**
- Client visibility settings require minimum client versions (macOS 1.0.25, Windows 1.0.23, Linux 1.0.74, iOS 1.0.25, Android 1.0.22)

## Configuration Values

| Field | Options/Notes |
|---|---|
| Address | FQDN, wildcard FQDN, IP, CIDR |
| Ports | TCP and/or UDP, specific ports or all; ICMP toggle |
| Visibility | `Standard Address`, `Browser Address`, `Background Address` |
| Access | Assigned via Groups |

## Address Resolution Priority (Overlapping Resources)
Most specific wins:
1. Single IP > CIDR (smaller CIDR > larger CIDR)
2. Exact domain > wildcard domain
3. Wildcard with more non-wildcard chars > broader wildcard
4. Truly ambiguous → chosen arbitrarily (avoid this)

## DNS Best Practices (Private IPs)
Ordered by preference when a DNS name resolves to a private IP:
1. Configure in private DNS only
2. Use FQDN-based Resource (public resolution via Connector)
3. Use private IP-based Resource
4. Use CIDR block (least granular)

## Gotchas
- Invalid CIDR notation (e.g., `10.1.0.1/16`) returns `Invalid IP or FQDN` error
- Overlapping Resources should be avoided; ambiguous matches are resolved arbitrarily
- DNS rebinding protection in modern OSes can break public FQDNs resolving to private IPs—define as DNS Resource instead
- Port restrictions unavailable if any Connector in the Remote Network is below v1.20.0
- Unqualified DNS names (e.g., `host`) require additional Connector configuration
- Visibility settings don't affect Admin Console display

## Port Restriction Use Cases
- Limit all users to specific ports (replaces internal firewall rules)
- Split access: create two Resources with same address but different ports, assign to different Groups (e.g., `host.autoco.internal:443` vs `host.autoco.internal:22`)

## Related Docs
- How DNS Works with Twingate
- Resource Aliases
- Whitelisting Traffic to Public Resources
- IP Overlap Guide
- Upgrading Connectors
- Hiding Resources in the Client
- Port Restrictions
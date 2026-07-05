# Twingate Resources

## Summary
Resources are network addresses (DNS names, IPs, CIDR ranges) secured via Twingate and accessible only to authorized users. Traffic is routed through Connectors in the associated Remote Network, enabling access to private resources without exposing them publicly. Twingate denies all traffic by default (Zero Trust).

## Key Information
- Resource types: FQDN, wildcard FQDN, IP address, CIDR range
- Wildcard `*` = 0+ characters; `?` = exactly 1 character
- `*.autoco.internal` matches subdomains but NOT `autoco.internal` itself
- Address resolution occurs **from the Connector**, not the client device
- CGNAT subnet `100.96.0.0/12` is reserved by Twingate client — resources in this range are blocked
- Default: all TCP, UDP ports and ICMP (ping) forwarded
- Zero Trust default: users denied unless explicitly granted group access

## Prerequisites
- Connector(s) deployed in the Resource's Remote Network
- Resource address must be resolvable/routable from the Connector
- Port restrictions require all Connectors on Remote Network at **v1.20.0+**
- Client visibility settings require minimum client versions (macOS 1.0.25+, Windows 1.0.23+, Linux 1.0.74+, iOS 1.0.25+, Android 1.0.22+)

## Resource Definition Fields
| Field | Description |
|-------|-------------|
| Label | Display name in Admin Console and Client |
| Address | FQDN, wildcard FQDN, IP, or CIDR |
| Alias | Additional address (resolved by Connector, no DNS entry needed) |
| Port restrictions | Limit TCP/UDP ports; toggle ICMP |
| Remote Network | Associated network with deployed Connectors |
| Tags | Optional metadata for organization |
| Client visibility | Standard, Browser, or Background |
| Groups | Grant access; deny by default |

## Address Resolution Priority (Overlapping Resources)
More specific wins:
1. Single IP > CIDR range; smaller CIDR > larger CIDR
2. Exact domain > wildcard domain
3. Wildcard with more non-wildcard characters wins
4. Truly ambiguous addresses resolved arbitrarily

## Port Restrictions
- Apply TCP and UDP restrictions independently
- Toggle ICMP separately
- Use case: split a single resource into two (e.g., `host:443` for all users, `host:22` for admins) assigned to different groups

## Client Visibility Options
- **Standard Address**: visible in main Client list
- **Browser Address**: visible + "Open in Browser" shortcut
- **Background Address**: only visible in "Hidden Resources" section

## Gotchas
- Invalid CIDR notation (e.g., `10.1.0.1/16`) returns `Invalid IP or FQDN` error
- DNS rebinding protection: define public FQDNs resolving to private IPs as DNS Resources, not IP Resources
- Unqualified DNS names (e.g., `host`) require additional Connector configuration
- Overlapping resources should be avoided; consult IP overlap guide
- Aliases don't require actual DNS entries or Connector-side resolution
- Port restriction UI unavailable if any Connector on the Remote Network is below v1.20.0

## Related Docs
- [How DNS Works with Twingate](#)
- [Whitelisting Traffic to Public Resources](#)
- [Resource Aliases](#)
- [IP Overlap Guide](#)
- [Hiding Resources in the Client](#)
- [Upgrading Connectors](#)
- [Tags](#)
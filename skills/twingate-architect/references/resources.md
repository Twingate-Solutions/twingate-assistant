# Twingate Resources

## Summary
Resources are network addresses (DNS names, IPs, or CIDR ranges) secured via Twingate and accessible only to authorized users. Traffic is routed through Connectors deployed in the associated Remote Network. Access is denied by default following Zero Trust principles.

## Key Information
- Resource types: FQDN, wildcard FQDN, IP address, CIDR range
- Wildcard `*` = 0+ characters; `?` = exactly 1 character
- `*.autoco.internal` matches subdomains but NOT `autoco.internal` itself
- CGNAT subnet `100.96.0.0/12` is reserved by Twingate client — IPs in this range are blocked
- DNS resolution occurs **from the Connector**, not the client device
- Aliases are resolved by the Connector; no DNS setup required for aliases
- Tags are optional metadata for organization

## Prerequisites
- Connector(s) deployed in the target Remote Network
- Resource address must be resolvable and routable from those Connectors
- Port restrictions require **all Connectors on Remote Network at v1.20.0+**
- Client visibility settings require minimum client versions (macOS 1.0.25, Windows 1.0.23, iOS 1.0.25, Android 1.0.22, Linux 1.0.74)

## Resource Definition Fields
| Field | Details |
|-------|---------|
| Label | Display name in Admin Console and Client |
| Address | FQDN, wildcard FQDN, IP, or CIDR |
| Alias | Extra address; Connector-resolved, no DNS entry needed |
| Port restrictions | Default: all TCP/UDP + ICMP; configurable per resource |
| Remote Network | Must contain Connectors that can reach the resource |
| Tags | Optional metadata |
| Client visibility | Standard, Browser, or Background |

## Address Resolution Best Practices
For DNS names resolving to private IPs, prefer (in order):
1. **Private DNS** — configure in private DNS, never exposed publicly
2. **FQDN Resource** — Connector handles resolution
3. **Private IP Resource** — direct routing, no DNS flexibility
4. **CIDR Block** — broad coverage, less granular access control

## Overlapping Addresses — Specificity Rules
More specific address wins:
- Single IP > CIDR range; smaller CIDR > larger CIDR
- Exact domain > wildcard domain; wildcard with more non-wildcard chars > broader wildcard
- Truly ambiguous resources (same specificity) are chosen arbitrarily — **avoid this**

## Port Restrictions
- Default: all TCP, UDP, ICMP (ping)
- Can restrict TCP and UDP independently
- ICMP can be toggled on/off
- Use case: split access by port (e.g., separate resources for `:443` vs `:22` assigned to different groups)
- **Requires all Connectors in Remote Network at v1.20.0+**

## Client Visibility Options
- **Standard Address**: visible in main resource list
- **Browser Address**: visible + "Open in Browser" shortcut
- **Background Address**: visible only under "Hidden Resources" section

## Gotchas
- Invalid CIDR notation (e.g., `10.1.0.1/16`) returns `Invalid IP or FQDN` error
- CGNAT range `100.96.0.0/12` always blocked
- DNS rebinding protection in modern systems may break public DNS resolving to private IPs — use FQDN or private DNS resources instead
- Unqualified DNS names (e.g., `host`) require additional Connector configuration
- Overlapping resources should be avoided; ambiguous matches are arbitrary

## Related Docs
- How DNS Works with Twingate
- Resource Aliases
- Whitelisting Traffic to Public Resources
- IP Overlap Guide
- Upgrading Connectors
- Hiding Resources in the Client
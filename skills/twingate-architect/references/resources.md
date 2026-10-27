---
source: https://www.twingate.com/docs/resources
type: docs
fetched: 2026-10-25
source_version: 2ad0295d7cbd5dcfd113e6671160f0ddfe20cc290b0d92d412ea91f81b17613d
trust: official
---

# Twingate Resources

## Page Title
Resources — Configuring Network Resources in Twingate

## Summary
A Twingate Resource is any network address (FQDN, IP, CIDR, wildcard domain) accessible through Twingate once a Connector can resolve and route to it. Resources are associated with Remote Networks, governed by Zero Trust deny-by-default access, and assigned to user Groups via policies.

## Key Information
- **Resource types**: Private DNS names, private IPs, CIDR ranges, public IPs (for IP whitelisting)
- **Address formats**: FQDN, wildcard FQDN (`*.host-0?.autoco.internal`), single IP, CIDR range
- **Wildcards**: `*` = 0+ chars, `?` = exactly 1 char; `*.autoco.internal` does NOT match `autoco.internal` itself
- **Reserved subnet**: CGNAT `100.96.0.0/12` is reserved by Twingate client — resources in this range are blocked
- **Aliases**: Extra address for a resource; resolved by Connector, no DNS entry required
- **Default traffic**: All TCP, UDP ports + ICMP (ping) forwarded unless restricted
- **Zero Trust default**: All access denied unless explicitly granted via Group membership

## Prerequisites
- Connector(s) deployed in the target Remote Network
- Resource address must be resolvable and routable from the Connector(s)
- Port restrictions require all Connectors in Remote Network at **v1.20.0+**

## Configuration Values

| Field | Options/Notes |
|-------|--------------|
| Label | Display name in Admin Console and Client |
| Address | FQDN, wildcard FQDN, IP, CIDR (must be valid, e.g. `10.1.0.0/16` not `10.1.0.1/16`) |
| Alias | Optional extra address; Connector-resolved only |
| Port restrictions | TCP/UDP independently; ICMP toggle; per-port or range |
| Remote Network | Must contain Connectors that can reach the resource |
| Tags | Optional metadata (owner, purpose, location) |
| Client visibility | `Standard Address`, `Browser Address`, `Background Address` |

## Address Resolution Priority (Most → Least Specific)
**IPs**: Single IP > smaller CIDR > larger CIDR
**Domains**: Exact FQDN > wildcard with more non-wildcard chars > broader wildcard

Truly ambiguous addresses (identical specificity) resolve arbitrarily — avoid overlap.

## DNS Best Practices (Private IPs)
1. Configure private DNS — keep resolution internal only
2. Use FQDN-based Resource (public DNS resolving to private IP)
3. Use private IP-based Resource
4. Use CIDR block (least granular)

## Gotchas
- Invalid CIDR notation (host bits set, e.g. `10.1.0.1/16`) returns `Invalid IP or FQDN` error
- Unqualified DNS names (e.g. `host`) require additional Connector configuration + latest client
- DNS rebinding protection on modern systems can break resources defined as IP when DNS resolution is expected — prefer FQDN resources
- Overlapping resources resolved by specificity; ambiguous matches are arbitrary
- Port restrictions unavailable if any Connector in the Remote Network is below v1.20.0
- Hiding resources in Client does not affect Admin Console visibility

## Related Docs
- How DNS Works with Twingate
- Resource Aliases
- Whitelisting Traffic to Public Resources
- Port Restrictions / Upgrading Connectors
- IP Overlap Guide
- Hiding Resources in the Client
## Page Title
Resources

## Summary
A Resource is any network address (FQDN, IP, CIDR, or wildcard) that users access via Twingate. Resources are resolved and routed from the Connector — the end user's device never needs direct routing to the private address. Access is denied by default; users must be in a Group that has been explicitly granted access to the Resource.

## Key Information
- **Address types**: FQDN (`host.autoco.internal`), wildcard FQDN (`*.autoco.internal`), IP address, CIDR range (`10.1.0.0/16`)
- **Wildcard rules**: `*.autoco.internal` matches `host.autoco.internal` and `sub.host.autoco.internal` but NOT `autoco.internal` itself; `*` = 0+ chars, `?` = exactly 1 char
- **CGNAT reservation**: Twingate client reserves `100.96.0.0/12` — resources in that IP range will be blocked
- **Aliases**: resources can have an additional alias address; the Connector resolves it (no DNS setup needed for the alias)
- **Port restrictions**: defaults to all TCP/UDP; can be restricted per resource (ICMP/ping included by default)
- **Tags**: optional metadata for organizing resources
- **Access**: Groups granted access; zero-trust default means no access unless explicitly granted
- **Specificity resolution for overlaps**: single IP > small CIDR > large CIDR; non-wildcard domain > wildcard domain with more literal chars
- **Public IP whitelisting**: route traffic for a public destination through the Connector before exiting to internet

## Prerequisites
- Remote Network with a deployed Connector
- Connector must be able to resolve and route to the resource address

## Step-by-Step
1. Admin Console → Network → Add Resource
2. Enter label (name), address (FQDN/IP/CIDR), optionally alias and port restrictions
3. Select the Remote Network
4. Add one or more Groups — required for the resource to be accessible
5. Optionally add Tags

## Configuration Values
- Default port behavior: all TCP and UDP (including ICMP/ping)
- CGNAT blocked range: `100.96.0.0/12`
- FQDN wildcard characters: `*` (0+), `?` (exactly 1)

## Gotchas
- A resource with no Group assigned is inaccessible to everyone — always add at least one Group
- DNS rebinding protection on modern OS/routers: define DNS resources that resolve to private IPs as FQDN Resources (not IP Resources) to avoid rebinding blocks
- Overlapping Resources: Twingate picks the most specific match — ambiguous overlaps should be avoided
- Unqualified DNS names (e.g. just `host`) require additional Connector configuration and latest Client
- CIDR resources reduce access control granularity — prefer specific FQDNs or IPs where possible

## Related Docs
- `/docs/how-dns-works-with-twingate` — how FQDN resolution works end-to-end
- `/docs/remote-networks` — the Remote Network container resources live in
- `/docs/resource-types-wildcards` — wildcard resource details
- `/docs/resource-types-cidr` — CIDR resource details

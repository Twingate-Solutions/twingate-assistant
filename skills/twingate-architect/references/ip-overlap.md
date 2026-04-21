## Best Practices for Overlapping IP Addresses

IP overlap occurs when two or more assets in different Remote Networks share the same IP address, creating routing ambiguity for Twingate. Three resolution options are available: Resource aliases (recommended), private DNS with per-environment zones, or strict user/group/resource mapping without overlap. No network changes or IP renumbering are required.

**Key Information**
- Ambiguity occurs when a user belongs to two groups that each grant access to an identical IP-style Resource in different Remote Networks
- Overlapping CIDR ranges or wildcard DNS entries across Remote Networks are not recommended -- routing is undefined; more specific definitions always take priority over broader ones
- When a specific Resource definition exists (e.g. `10.0.0.10`) alongside a broader CIDR in a different Remote Network, the specific definition always wins -- there is no way to force traffic to the broader one for that address

**Three Resolution Options**

**Option 1: Resource Aliases (recommended)**
- Add a unique FQDN alias to each overlapping Resource (e.g. `db.dev.autoco.com`, `db.prod.autoco.com`)
- Users connect to the alias; Twingate routes to the correct Remote Network unambiguously
- No DNS infrastructure needed; configured in Admin Console per Resource

**Option 2: Private DNS with Environment Zones**
- Deploy a private DNS server with separate zones per environment (e.g. `*.dev.autoco.com`, `*.prod.autoco.com`)
- Create DNS A records pointing environment FQDNs to the shared IP addresses
- Reconfigure Resources to use FQDNs instead of IPs

**Option 3: Strict Group/Resource Mapping (no overlap)**
- Create separate Resources for each Remote Network with the same IP
- Ensure no user is a member of two groups that both contain Resources with the same IP address
- Requires precise User-Group-Resource mapping; can be managed via the open-source Group Profile Manager (Twingate Labs)

**Gotchas**
- Option 3 breaks if a user is added to both groups -- any team size increase makes this hard to maintain; prefer Options 1 or 2
- CIDR overlap is particularly dangerous: there is no deterministic routing resolution when two Remote Networks have the same CIDR range defined; the more specific definition silently wins

**Related Docs**
- /docs/resource-aliases
- /docs/private-dns-best-practices
- /docs/resources
- /docs/remote-networks

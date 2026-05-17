# Best Practices for Overlapping IP Addresses

## Summary
When multiple assets across different subnets share the same IP address, Twingate cannot automatically determine which Remote Network to route traffic through. Three solutions exist to resolve this ambiguity without changing network infrastructure or IP assignments.

## Key Information
- Resources are attached to Remote Networks and assigned to User Groups
- Ambiguity occurs when a user belongs to groups with Resources pointing to the same IP in different Remote Networks
- Overlapping CIDR ranges and wildcard DNS entries across Remote Networks are not recommended
- More specific Resource definitions (single IP, specific hostname) always take priority over broader ones (CIDR range, wildcard)

## Prerequisites
- Resources must be mapped to distinct Remote Networks
- User-Group-Resource relationships must be clearly defined

## Three Resolution Options

### Option 1: Resource Aliases (Recommended)
Add FQDN aliases to each Resource so routing is determined by alias, not IP:
- `10.1.2.3` (subnet1) → `server.dev.autoco.com`
- `10.1.2.4` (subnet1) → `db.dev.autoco.com`
- `10.1.2.3` (subnet2) → `server.prod.autoco.com`
- `10.1.2.4` (subnet2) → `db.prod.autoco.com`

### Option 2: Private DNS Server
Deploy a private DNS server with per-subnet DNS zones:
- Create zones: `*.dev.autoco.com` → development subnet, `*.prod.autoco.com` → production subnet
- Reconfigure Twingate Resources to use FQDNs instead of IPs
- DNS resolution disambiguates routing automatically

### Option 3: Strict User-Group Separation
Create separate Resources with identical IPs in different Remote Networks, but ensure **no user belongs to two groups that both contain Resources with the same IP**:
- Requires precise User ↔ Group ↔ Resource mapping
- Can be managed via the open-source [Group Profile Manager](https://github.com/Twingate-Labs) (Labs repo)

## Gotchas
- **CIDR/wildcard overlap**: If two Resources in different Remote Networks share overlapping CIDR ranges or wildcard DNS entries and a user has access to both, routing behavior is undefined
- **Specificity priority**: A specific IP (`10.0.0.10`) always wins over a CIDR range (`10.0.0.0/24`); this cannot be overridden — the broader resource becomes unreachable for that specific address
- Option 3 fails silently if user group membership is not carefully maintained — any user in both groups with conflicting IP Resources will experience ambiguity

## Related Docs
- Resource Aliases
- Private DNS configuration
- Remote Networks
- Group Profile Manager (Twingate Labs)
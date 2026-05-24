# Best Practices for Overlapping IP Addresses

## Summary
When multiple assets across different subnets share the same IP address, Twingate cannot automatically determine which Remote Network to route traffic through. Three resolution options exist without requiring network restructuring or IP changes.

## Key Information
- Resources are attached to Remote Networks and assigned to User Groups
- Ambiguity occurs when a user belongs to groups containing Resources with identical IP addresses in different Remote Networks
- Overlapping CIDR ranges and wildcard DNS entries are **not recommended** and have no guaranteed routing behavior
- More specific resource definitions (single IP) always take priority over broader ones (CIDR range)

## Three Resolution Options

### Option 1: Resource Aliases (Recommended)
Assign unique FQDNs as aliases to each Resource, even if underlying IPs are identical:
- `10.1.2.3` (subnet1) → alias `server.dev.autoco.com`
- `10.1.2.3` (subnet2) → alias `server.prod.autoco.com`

Users connect via FQDN; Twingate routes to correct Remote Network automatically.

### Option 2: Private DNS Server
Deploy a private DNS server with environment-specific zones:
- `*.dev.autoco.com` → development subnet records
- `*.prod.autoco.com` → production subnet records

Reconfigure Twingate Resources to use FQDNs instead of IPs.

### Option 3: Strict User/Group/Resource Mapping
Keep duplicate IP Resources in separate Remote Networks, but ensure **no user belongs to two groups** that both contain Resources with the same IP address.
- Requires precise User ↔ Group ↔ Resource mapping
- Can be managed via the open-source [Group Profile Manager](https://github.com/Twingate-Labs) (Twingate Labs)

## Gotchas
- **CIDR/wildcard overlap**: If identical or overlapping CIDR ranges/wildcard DNS entries exist across Remote Networks accessible to the same user, routing is undefined
- **Specificity rule**: A more specific resource (`10.0.0.10`) always overrides a broader one (`10.0.0.0/24`), permanently — you cannot force traffic to the broader resource's network for that specific IP
- Option 3 breaks silently if user group membership is not carefully maintained
- Non-overlapping IPs (e.g., dev `10.1.2.5` vs prod `10.1.2.6`) require no special handling — create separate Resources normally

## Related Docs
- Resource Aliases
- Private DNS Configuration
- Remote Networks
- Twingate Labs / Group Profile Manager
# Best Practices for Overlapping IP Addresses

## Summary
When multiple assets across different network subnets share the same IP address, Twingate cannot automatically determine which Remote Network to route traffic through. Three resolution options exist that avoid network restructuring. Overlapping CIDR ranges and wildcard DNS entries are explicitly unsupported.

## Key Information
- Resources are attached to Remote Networks and assigned to User Groups
- Ambiguity occurs when a user belongs to groups containing Resources with identical IP addresses in different Remote Networks
- More specific Resource definitions (single IP) always take priority over broader ones (CIDR range, wildcard DNS)
- Overlapping CIDR ranges or wildcard DNS entries across Remote Networks produce undefined routing behavior

## Resolution Options

### Option 1: Resource Aliases (Recommended)
Assign unique FQDNs as aliases to Resources with overlapping IPs:
- `10.1.2.3` (dev subnet) → alias `server.dev.autoco.com`
- `10.1.2.3` (prod subnet) → alias `server.prod.autoco.com`
- Users connect via FQDN; Twingate routes to correct Remote Network automatically

### Option 2: Private DNS Server
- Deploy private DNS with separate zones per subnet (e.g., `*.dev.autoco.com`, `*.prod.autoco.com`)
- Create DNS records mapping FQDNs to overlapping IPs within each zone
- Redefine Twingate Resources using FQDNs instead of IP addresses

### Option 3: Strict User/Group Segmentation
- Create separate Resources (same IP, different Remote Networks) in different Groups
- Ensure no user belongs to two Groups that both contain Resources with the same IP
- Can be managed via the open-source [Group Profile Manager](https://github.com/Twingate-Labs) (Twingate Labs)

## Gotchas
- **CIDR/wildcard overlap is unsupported**: No guaranteed routing behavior if two Resources in different Remote Networks share identical or overlapping CIDR ranges or wildcard DNS entries
- **Specificity wins**: A specific IP `10.0.0.10` always overrides a CIDR `10.0.0.0/24` match—there is no way to force traffic through the broader-scoped Resource once a specific match exists
- **Option 3 fragility**: Any user added to multiple groups with overlapping IP Resources immediately creates ambiguity; requires ongoing access management discipline
- Non-overlapping IPs (e.g., dev at `10.1.2.5`, prod at `10.1.2.6`) require no special handling—create two standard Resources

## Prerequisites
- Understanding of Twingate Remote Networks, Resources, and Groups model
- For Option 2: ability to deploy and manage internal DNS infrastructure
- For Option 3: disciplined group membership management

## Related Docs
- Resource Aliases
- Private DNS Server configuration
- DNS Zones
- Group Profile Manager (Twingate Labs repository)
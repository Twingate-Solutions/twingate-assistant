---
source: https://www.twingate.com/docs/ip-overlap
type: docs
fetched: 2026-08-14
source_version: 785bd165f419e3de9d2485f29c14af07054c194e367eb4e20be3d51f42a4d915
---

# Best Practices for Overlapping IP Addresses

## Summary
When multiple assets across different subnets share the same IP address, Twingate cannot automatically determine which Remote Network to route traffic through. Three resolution options exist that avoid network restructuring: resource aliases, private DNS, or strict user-group-resource mapping.

## Key Information
- Resources are attached to Remote Networks; when two Resources share an IP across different Remote Networks, ambiguity occurs if a user has access to both
- Overlapping CIDR ranges and wildcard DNS entries are **not recommended** and have no guaranteed routing behavior
- More specific resource definitions (single IP, specific hostname) always take priority over broader CIDR/wildcard definitions
- A user belonging to two groups that each contain a Resource with the same IP address will experience routing ambiguity

## Three Resolution Options

### Option 1: Resource Aliases (Recommended)
Assign unique FQDNs as aliases to Resources with overlapping IPs:
- `10.1.2.3` (subnet1) → alias `server.dev.autoco.com`
- `10.1.2.3` (subnet2) → alias `server.prod.autoco.com`
- Users connect via alias; Twingate routes to correct Remote Network automatically

### Option 2: Private DNS Server
- Deploy a private DNS server with per-subnet DNS zones (e.g., `*.dev.autoco.com`, `*.prod.autoco.com`)
- Create DNS records mapping FQDNs to overlapping IPs per zone
- Redefine Twingate Resources using FQDNs instead of IPs

### Option 3: Strict User-Group-Resource Mapping
- Create separate Resources with identical IPs in different Remote Networks
- Ensure **no user belongs to two groups** that each have access to Resources with the same IP
- Can be managed via the open-source [Group Profile Manager](https://github.com/Twingate-Labs) (Labs)

## Gotchas
- **CIDR/wildcard overlap**: If two Resources in different Remote Networks share CIDR ranges or wildcard DNS, routing is undefined for users with access to both
- **Specificity rule**: A narrower resource (`10.0.0.10`) always wins over a broader one (`10.0.0.0/24`); there is no way to force traffic to the broader resource while both exist
- Option 3 breaks down the moment any user is added to multiple groups with conflicting IP-based Resources—requires disciplined access management
- Non-overlapping IPs (e.g., dev fileshare `10.1.2.5` vs prod `10.1.2.6`) require no special handling

## Prerequisites
- Understanding of Twingate Resources, Remote Networks, and Groups model
- For Option 2: infrastructure to deploy a private DNS server with configurable zones
- For Option 3: process controls to prevent ambiguous group memberships

## Related Docs
- Resource Aliases
- Private DNS Server configuration
- Group Profile Manager (Twingate Labs)
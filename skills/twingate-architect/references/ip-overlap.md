# Best Practices for Overlapping IP Addresses

## Summary
When multiple assets across different subnets share the same IP address, Twingate cannot automatically determine which Remote Network to route traffic through. Three resolution options exist, none requiring network restructuring or IP changes.

## Key Information
- Resources attach to Remote Networks and are assigned to User Groups
- Ambiguity occurs when a user belongs to multiple Groups, each containing a Resource with the same IP address in different Remote Networks
- Overlapping CIDR ranges and wildcard DNS entries are **not recommended**
- More specific Resource definitions (single IP, specific hostname) always take priority over broader definitions (CIDR range, wildcard DNS)

## Resolution Options

### Option 1: Resource Aliases (Recommended)
Add FQDN aliases to disambiguate Resources with identical IPs:
- `10.1.2.3` (subnet1) → `server.dev.autoco.com`
- `10.1.2.3` (subnet2) → `server.prod.autoco.com`
- Each alias ties routing to a specific Remote Network automatically

### Option 2: Private DNS Server
Deploy a private DNS server with per-subnet DNS zones:
- Create zones like `*.dev.autoco.com` and `*.prod.autoco.com`
- Add DNS records mapping FQDNs to overlapping IPs per environment
- Reconfigure Twingate Resources to use FQDNs instead of IPs

### Option 3: Strict User-Group-Resource Mapping
Create separate Resources with the same IP in different Remote Networks, but ensure **no user belongs to two Groups that both contain Resources with the same IP address**.
- Can be managed via the open-source [Group Profile Manager](https://github.com/Twingate-Labs/twingate-group-profile-manager) (Twingate Labs)

## Gotchas
- If a user is in two Groups each containing a Resource at the same IP → ambiguity, undefined routing behavior
- Overlapping CIDR ranges or wildcard DNS across Remote Networks produce unpredictable routing with no workaround
- When a specific IP/hostname conflicts with a broader CIDR/wildcard, the specific definition always wins — traffic **cannot** be forced to the broader Resource
- Non-overlapping IPs (e.g., dev `10.1.2.5` vs prod `10.1.2.6`) require no special handling; create separate Resources normally

## Configuration Values
| Approach | Resource Definition |
|---|---|
| Alias | Add FQDN alias per Resource in Twingate admin |
| Private DNS | FQDN-style Resource (e.g., `server.dev.autoco.com`) |
| Group mapping | IP-style Resource, strict Group membership control |

## Related Docs
- Resource Aliases documentation
- Private DNS server setup
- Remote Networks configuration
- [Twingate Labs Group Profile Manager](https://github.com/Twingate-Labs)
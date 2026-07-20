# Best Practices for Overlapping IP Addresses

## Summary
When multiple assets across different subnets share the same IP address, Twingate cannot automatically determine which Remote Network to route traffic through. Three options resolve this without changing network infrastructure. Overlapping CIDR ranges and wildcard DNS entries should always be avoided.

## Key Information
- Resources are attached to Remote Networks and assigned to User Groups
- Ambiguity occurs when a user belongs to groups containing Resources with identical IP addresses in different Remote Networks
- More specific Resource definitions (single IP) always take priority over broader ones (CIDR range, wildcard DNS)
- Overlapping CIDR ranges or wildcard DNS entries provide no routing guarantee

## Three Resolution Options

### Option 1: Resource Aliases (Recommended)
Add DNS aliases directly to each Twingate Resource to disambiguate routing:
- `10.1.2.3` (dev subnet) → alias `server.dev.autoco.com`
- `10.1.2.3` (prod subnet) → alias `server.prod.autoco.com`
- Users connect via alias; Twingate routes to correct Remote Network automatically

### Option 2: Private DNS Server
Deploy a private DNS server with per-subnet DNS zones:
- Create zones: `*.dev.autoco.com` → dev subnet, `*.prod.autoco.com` → prod subnet
- Redefine Twingate Resources using FQDNs instead of IP addresses
- DNS resolution eliminates routing ambiguity

### Option 3: Strict User→Group→Resource Mapping
Keep duplicate IP Resources in separate Remote Networks but enforce strict group membership:
- No user may belong to two groups that each contain a Resource with the same IP
- Requires precise access control management
- Can be automated via the open source [Group Profile Manager](https://github.com/Twingate-Labs) (Labs repo)

## Gotchas
- **CIDR/wildcard overlap**: If a user has access to two Remote Networks with identical CIDR ranges or wildcard DNS entries, routing behavior is undefined
- **Specificity rule**: A specific Resource (`10.0.0.10`) always overrides a broader CIDR (`10.0.0.0/24`) — traffic to that IP can never be forced through the broader-range Remote Network while both exist
- **Option 3 limitation**: Breaks if group membership is not carefully controlled; any user in two groups with same-IP Resources creates ambiguity
- Changing IP addresses or restructuring networks is not required for any option

## Configuration Values
| Concept | Example |
|---|---|
| Dev alias pattern | `*.dev.<domain>.com` |
| Prod alias pattern | `*.prod.<domain>.com` |
| Overlapping IP example | `10.1.2.3`, `10.1.2.4` |
| Conflicting CIDR example | `10.0.0.0/24` in two Remote Networks |

## Prerequisites
- Twingate Resources configured with Remote Networks
- For Option 2: ability to deploy and manage a private DNS server
- For Option 3: administrative control over User Group assignments

## Related Docs
- Resource Aliases
- Private DNS Server configuration
- DNS Zones
- [Group Profile Manager (Labs)](https://github.com/Twingate-Labs)
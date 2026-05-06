# Best Practices for Overlapping IP Addresses

## Summary
IP overlap occurs when assets in different network subnets share the same IP address, creating routing ambiguity in Twingate. Three resolution options exist without requiring network restructuring or IP changes. Overlapping CIDR ranges and wildcard DNS entries should always be eliminated.

## Key Information
- Resources are attached to Remote Networks and assigned to User Groups
- Twingate auto-routes connection requests based on IP/FQDN — users never select the Remote Network manually
- Ambiguity occurs when a user belongs to 2+ groups, each containing a Resource with the same IP address
- More specific Resource definitions (single IP, specific hostname) always take priority over broader ones (CIDR range, wildcard DNS)

## Three Resolution Options

### Option 1: Resource Aliases (Recommended)
Add FQDN aliases to each overlapping Resource — each alias maps to one Resource, which maps to one Remote Network.
- `10.1.2.3` in dev subnet → alias `server.dev.autoco.com`
- `10.1.2.3` in prod subnet → alias `server.prod.autoco.com`

### Option 2: Private DNS Server
Deploy a private DNS server with per-subnet DNS zones:
- `*.dev.autoco.com` zone → resolves to dev subnet IPs
- `*.prod.autoco.com` zone → resolves to prod subnet IPs
- Reconfigure Twingate Resources to use FQDNs instead of IPs

### Option 3: Strict User-Group-Resource Mapping
Create separate Resources with same IP in different Remote Networks, but ensure **no user belongs to two groups** that both contain Resources with identical IPs.
- Can be managed via the open-source [Group Profile Manager](https://github.com/Twingate-Labs/twingate-group-profile-manager) (Twingate Labs)

## Gotchas
- **Overlapping CIDR ranges and wildcard DNS entries are not recommended** — routing behavior is not guaranteed when ambiguity exists
- A more specific definition (`10.0.0.10`) always wins over a broader one (`10.0.0.0/24`), and there is **no way to override this** to force traffic through the broader Resource
- Option 3 breaks if group membership isn't carefully controlled — one user in two conflicting groups causes ambiguity
- Non-overlapping IPs (different addresses per environment) require no special handling — create separate Resources normally

## Configuration Values
| Concept | Notes |
|---|---|
| Resource alias | FQDN added to a Resource; resolves routing without changing underlying IP |
| DNS zone scope | Should map one-to-one with subnets containing overlapping resources |
| CIDR specificity | More specific prefix/hostname always takes routing priority |

## Related Docs
- Resource aliases configuration
- Private DNS server setup
- Remote Networks
- Group Profile Manager (Twingate Labs repository)
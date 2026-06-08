# Best Practices for Overlapping IP Addresses

## Summary
When multiple assets across different network subnets share the same IP address, Twingate cannot automatically determine which Remote Network to route traffic through. Three options resolve this without changing network infrastructure or IP assignments.

## Key Information
- Resources attach to Remote Networks and are assigned to User Groups
- Twingate auto-routes based on IP/FQDN — ambiguity occurs when a user belongs to groups with identical IP resources in different Remote Networks
- Overlapping CIDR ranges and wildcard DNS entries are **not recommended**
- More specific resource definitions (single IP, specific hostname) always take priority over broader ones (CIDR range, wildcard domain)

## Three Resolution Options

### Option 1: Resource Aliases (Recommended)
Assign unique aliases (FQDNs) to each resource with a duplicate IP:
- `10.1.2.3` (dev subnet) → alias `server.dev.autoco.com`
- `10.1.2.3` (prod subnet) → alias `server.prod.autoco.com`
- Users connect via alias; Twingate routes to correct Remote Network

### Option 2: Private DNS Server
Deploy a private DNS server with per-subnet DNS zones:
- Zone `*.dev.autoco.com` → resolves to dev subnet IPs
- Zone `*.prod.autoco.com` → resolves to prod subnet IPs
- Reconfigure Twingate Resources to use FQDNs instead of IP addresses

### Option 3: Strict User-Group-Resource Mapping
Create separate Resources with identical IPs in different Remote Networks, but ensure **no user belongs to two groups that both contain resources with the same IP**.
- Manageable via the open-source [Group Profile Manager](https://github.com/Twingate-Labs/twingate-group-profile-manager) (Twingate Labs)

## Gotchas
- **CIDR/wildcard overlap**: If two Remote Networks have identical CIDR ranges or wildcard DNS entries and a user has access to both, routing behavior is undefined
- **Specificity rule**: A specific IP (`10.0.0.10`) or hostname always overrides a broader CIDR/wildcard — this cannot be reversed while the ambiguity exists
- Option 3 breaks if group membership is imprecise — any user in multiple groups with duplicate IP resources will experience ambiguous routing

## Prerequisites
- Resources must be defined and attached to Remote Networks before applying these strategies
- For Option 2: private DNS infrastructure must be deployed and accessible via Twingate Connectors

## Related Docs
- Resource Aliases
- Private DNS configuration
- Remote Networks
- [Twingate Labs - Group Profile Manager](https://github.com/Twingate-Labs)
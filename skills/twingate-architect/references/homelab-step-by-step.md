# How to Protect Your Home Lab with Twingate

## Summary
Step-by-step guide for securing a home lab using Twingate to provide remote access without opening router ports or running a traditional VPN. Covers Connector deployment, Resource creation, multi-user access with Groups, and Security Policies.

## Key Information
- Twingate replaces port forwarding and VPN server setups entirely
- Connectors deployed in pairs (2 per Remote Network) provide HA and load balancing automatically
- Zero trust by default: no permissions granted until explicitly configured
- Resources identified by IP/CIDR, FQDN, or DNS pattern + port combinations
- Groups act as roles; Resources are assigned to Groups, not individual users

## Prerequisites
- Free Twingate account registered
- Twingate Client installed on admin device
- At least one device in home lab for Connector deployment (NAS, Raspberry Pi, Linux/Windows machine)
- Connector hardware requirements: 2GB RAM, 2 vCPUs

## Step-by-Step

1. **Create Remote Network**: Admin Console → Network → Remote Networks → `+ Remote Network` → select `On Premise` → name it (e.g., "Home Lab")
2. **Deploy Connector**: Click connector in Remote Network → choose deployment method (Docker container or systemd) → follow console instructions
3. **Verify Connector**: Confirm it shows as connected to Controller and Relay network
4. **Create initial Resource**: Network → Resources → `Add Resource` → use CIDR (`192.168.100.0/24`) or DNS pattern (`*.int`) → assign to `Everyone` group
5. **Invite Users**: Team → Add User → enter email addresses
6. **Create Groups**: Team → Groups → Add Group (e.g., Standard Users, Power Users, Admin Users) → assign users
7. **Map services to groups**: List all `host:port` combinations, determine which groups need access
8. **Create granular Resources**: One Resource per logical service grouping (combine if same host + same group access) → assign to specific Groups (not `Everyone`)
9. **Delete broad Resource**: Remove the initial "Everything" resource
10. **Disable router VPN/port forwarding**: Remove now-unnecessary open ports and forwarding rules

## Configuration Values

| Parameter | Example Value | Notes |
|-----------|--------------|-------|
| Remote Network Location | `On Premise` | Required for home lab |
| CIDR Range | `192.168.100.0/24` | Match your router subnet |
| DNS Pattern | `*.int` | Alternative to CIDR if using private DNS |
| Connector RAM | 2GB | Minimum requirement |
| Connector vCPUs | 2 | Minimum requirement |

## Resource vs Access Mapping
- Use **IP-style Resources** if users connect via IP addresses
- Use **DNS-style Resources** if users connect via FQDNs
- Use **both** if users do both (e.g., same RDP service defined twice)

## Gotchas
- Connectors are per-Remote-Network, NOT per-Resource — one Connector serves all Resources in the network
- `Everyone` group is default; must explicitly deselect it when creating granular Resources
- Docker on Windows is noted as unstable — prefer Linux-based Connector deployment
- Private DNS domain resources require the Twingate Client to intercept DNS traffic — both IP and DNS Resources may be needed for same service
- Users see 0 Resources after initial setup — expected until Resources are explicitly assigned

## Security Policies (Optional)
- Policies control: authentication frequency, 2FA requirements, device posture checks
- Assigned at Group level, protecting all Resources the Group accesses
- Default policy auto-assigned to all Groups

## Related Docs
- [Connector deployment options](https://www.twingate.com/docs/connector)
- [Security Policies](https://www.twingate.com/docs/security-policies)
- [Twingate Client download](https://www.twingate.com/docs/client)
# How to Protect Your Home Lab with Twingate

## Summary
Step-by-step guide for securing a home lab using Twingate to provide remote access without opening router ports or running a traditional VPN. Covers setup for multi-user environments with granular access control using Groups and Resources.

## Key Information
- Replaces port forwarding and VPN server with Twingate Connectors
- Zero trust model: no permissions granted by default
- Connectors deployed in pairs for HA/load balancing (single Connector works but pairs recommended)
- Connector footprint: 2GB RAM, 2 vCPUs minimum
- Resources identified by IP/CIDR or FQDN + port

## Prerequisites
- Free Twingate account
- Twingate Client installed on admin device
- At least one device in home lab to host a Connector (NAS, Raspberry Pi, Linux/Windows machine)

## Step-by-Step

1. **Create Remote Network**: Admin Console → Network → Remote Networks → `+ Remote Network` → Select `On Premise` → Name it (e.g., "Home Lab")
2. **Deploy Connector**: Click Remote Network → select a Connector → choose deployment method (Docker container or systemd) → follow console instructions
3. **Verify Connector**: Confirm Connector shows connected status in Admin Console
4. **Create Initial Resource**: Network → Resources → `Add Resource` → use CIDR (`192.168.100.0/24`) or DNS pattern (`*.int`) → assign to `Everyone` group
5. **Invite Users**: Team tab → `Add User` → enter email addresses
6. **Create Groups**: Team → Groups → `Add Group` → suggested: Standard Users, Power Users, Admin Users
7. **Map Services to Resources**: Create per-service or per-server Resources with specific ports
8. **Assign Groups to Resources**: Ensure `Everyone` group is NOT selected for granular Resources
9. **Delete broad Resource**: Remove the initial "Everything" resource
10. **Disable router VPN/port forwarding**: No longer needed

## Configuration Values

| Field | Example Value |
|-------|--------------|
| Remote Network Location | `On Premise` |
| CIDR Resource | `192.168.100.0/24` |
| DNS Pattern Resource | `*.int` |
| Connector RAM | 2GB |
| Connector vCPUs | 2 |

**Resource Types**: IP (use when users connect via IP addresses), DNS (use when users connect via FQDNs), or both

## Gotchas
- Twingate Client intercepts traffic based on Resource definitions—if users connect via both IP and FQDN, create Resources for both
- Do NOT check `Everyone` group when creating granular per-service Resources
- Docker on Windows can be unstable; prefer Linux-based Connector deployment
- Single Connector is functional but two are recommended for HA
- No permissions exist by default—users see nothing until Resources are assigned to their Group

## Related Docs
- [Connector deployment options](https://www.twingate.com/docs/) 
- [Security Policies](https://www.twingate.com/docs/access-policies)
- Twingate Client download page
- Private DNS configuration
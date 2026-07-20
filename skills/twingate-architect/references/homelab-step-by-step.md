# How to Protect Your Home Lab with Twingate

## Summary
Step-by-step guide to securing a home lab using Twingate, enabling remote access for family/friends without opening router ports or running a traditional VPN. Covers Connector deployment, Resource creation, user/group management, and access policies.

## Key Information
- No open ports required — replaces port forwarding and VPN server entirely
- Connector minimum footprint: 2GB RAM, 2 vCPUs
- Deployment options: Docker container, systemd (Linux/Raspberry Pi), Hyper-V VM
- Two Connectors per Remote Network recommended (auto HA + load balancing); only one required
- Resources defined by IP/CIDR range or DNS pattern (FQDN/wildcard)
- Zero trust default: no permissions granted until explicitly assigned
- Groups function as roles; Resources are assigned to Groups, not individual users

## Prerequisites
- Twingate free account registered
- Twingate Client installed on admin device
- At least one device in home lab for Connector deployment

## Step-by-Step

1. **Create Remote Network**: Admin Console → Network → Remote Networks → `+ Remote Network` → select "On Premise" → name it (e.g., "Home Lab")
2. **Deploy Connector**: Click a Connector in the Remote Network → choose deployment method → follow console instructions → verify Connector shows as connected
3. **Sign into Twingate Client** on your device
4. **Create initial Resource**: Network → Resources → `Add Resource` → CIDR (e.g., `192.168.100.0/24`) or DNS pattern (e.g., `*.int`) → assign to "Everyone" group
5. **Disable router VPN/port forwarding** once connectivity is confirmed
6. **Invite users**: Team → Add User → enter email addresses
7. **Create Groups**: Team → Groups → `Add Group` (e.g., Standard Users, Power Users, Admin Users) → add users
8. **Map services to groups**: List all `host:port` services → determine per-service group access
9. **Create granular Resources**: One Resource per service or logical grouping → assign correct Groups → do NOT assign "Everyone"
10. **Delete the broad "Everything" Resource**
11. **Configure Security Policies** (optional): assign to Groups to enforce 2FA, auth frequency, device requirements

## Configuration Values

| Field | Example Value |
|---|---|
| Remote Network Location | On Premise |
| CIDR Resource | `192.168.100.0/24` |
| DNS Resource | `*.int` |
| Connector RAM | 2GB |
| Connector vCPUs | 2 |

## Gotchas
- If users connect via both IP and FQDN for the same host, create two separate Resources (one per addressing method)
- Docker on Windows is noted as "not always very stable" — prefer Linux-based Connector deployment
- Do not assign sensitive Resources to the "Everyone" group; create explicit groups
- Twingate Client must re-authenticate or be restarted to see newly added Resources
- One Connector covers all Resources in a Remote Network — no per-Resource Connector needed

## Related Docs
- [Connector Deployment Options](https://www.twingate.com/docs/connector)
- [Security Policies](https://www.twingate.com/docs/security-policies)
- [Download Twingate Client](https://www.twingate.com/download)
- [Register for Free Account](https://auth.twingate.com/signup)
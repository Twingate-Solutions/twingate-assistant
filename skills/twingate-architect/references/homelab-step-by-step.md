# How to Protect Your Home Lab with Twingate

## Summary
Step-by-step guide for securing a home lab using Twingate instead of open ports or traditional VPN. Covers deploying Connectors, creating Resources, managing multi-user access with Groups, and applying Security Policies. Replaces router port forwarding and VPN server entirely.

## Key Information
- Twingate replaces port forwarding rules and VPN server on home router
- Zero trust model: no permissions granted by default
- Connectors deployed in pairs for high availability and load balancing (single Connector acceptable for home lab)
- Connector footprint: 2GB RAM, 2 vCPUs
- Resources identified by IP address, CIDR range, FQDN, or DNS pattern
- Groups act as roles for access control

## Prerequisites
- Free Twingate account
- Twingate Client installed on admin device
- At least one device in home lab for Connector deployment (NAS, Raspberry Pi, Linux/Windows machine)

## Step-by-Step

1. **Create Remote Network**: Admin Console → Network → Remote Networks → `+ Remote Network` → select `On Premise` → name it (e.g., "Home Lab")
2. **Deploy Connector**: Click Remote Network → select a Connector → choose deployment method (Docker, systemd, Hyper-V) → follow Console instructions
3. **Verify Connector**: Confirm Connector shows connected status in Admin Console
4. **Create initial Resource**: Network → Resources → `Add Resource` → use CIDR (e.g., `192.168.100.0/24`) or DNS pattern (e.g., `*.int`) → assign to `Everyone` group
5. **Test access**: Use alternate internet connection (mobile tether) → connect via Twingate Client → access internal service by IP
6. **Disable router VPN/port forwarding**: Remove all forwarding rules after confirming Twingate access works
7. **Invite users**: Team → `Add User` → enter email addresses
8. **Create Groups**: Team → Groups → `Add Group` → create role-based groups (Standard Users, Power Users, Admin Users) → add members
9. **Map services to Resources**: Create one Resource per service or per logical service bundle (same host + same Group access = can combine)
10. **Assign Groups to Resources**: For each Resource, select appropriate Groups — do **not** assign `Everyone`
11. **Delete broad Resource**: Remove the initial `Everything`/CIDR resource
12. **Configure Policies** (optional): Assign Security Policies to Groups for 2FA, device checks, re-auth frequency

## Configuration Values

| Field | Example Value |
|-------|--------------|
| Remote Network Location | `On Premise` |
| CIDR Resource | `192.168.100.0/24` |
| DNS Pattern Resource | `*.int` |
| Connector RAM | 2 GB |
| Connector vCPUs | 2 |

## Gotchas
- Twingate Client intercepts traffic based on Resource definitions — if users connect via both IP and FQDN, create Resources for both
- Docker on Windows is unstable; prefer Hyper-V VM running Linux for Windows hosts
- Do **not** assign sensitive Resources (SSH, RDP, Portainer, Router UI) to `Everyone` or Standard Users groups
- Default policy is applied to all Groups automatically; customize only if stricter controls needed
- Two Connectors per Remote Network are pre-created but only one is required; second provides HA/load balancing

## Related Docs
- [Connector Deployment Options](https://www.twingate.com/docs/connector)
- [Security Policies](https://www.twingate.com/docs/policies)
- [Private DNS Configuration](https://www.twingate.com/docs/dns)
- [Twingate Client Download](https://www.twingate.com/docs/client)
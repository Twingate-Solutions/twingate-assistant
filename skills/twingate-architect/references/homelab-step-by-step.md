# How to Protect Your Home Lab with Twingate

## Summary
Step-by-step guide for setting up Twingate in a home lab environment to provide secure remote access without opening router ports. Covers single-user and multi-user setups with role-based access control using Groups and Resources.

## Key Information
- Replaces port forwarding, dynamic DNS, and router VPN server entirely
- Connectors deployed in pairs (2 per Remote Network) for HA/load balancing; single Connector is sufficient but not recommended
- Connector requirements: 2GB RAM, 2 vCPUs minimum
- Zero-trust by default — no permissions granted until explicitly configured
- Resources identified by IP address, CIDR range, FQDN, or DNS pattern

## Prerequisites
- Free Twingate account
- Twingate Client installed on admin device
- At least one device in the home lab to host a Connector (NAS, Raspberry Pi, Linux/Windows machine)

## Step-by-Step

1. **Create Remote Network** → Admin Console → Network → Remote Networks → `+ Remote Network` → Select `On Premise`
2. **Deploy Connector** → Click Remote Network → select a Connector → choose deployment method (Docker, systemd, Hyper-V VM)
3. **Verify Connector** is connected to Twingate's Controller and Relay network
4. **Sign into Twingate Client** on your device
5. **Create initial Resource** → Network → Resources → `Add Resource` → use CIDR (e.g., `192.168.100.0/24`) or DNS pattern (e.g., `*.int`) → assign to `Everyone` group
6. **Test access** via alternate internet connection (e.g., mobile tether)
7. **Disable router VPN, remove port forwarding rules**
8. **Invite users** → Team → Add User (by email)
9. **Create Groups** (Standard Users, Power Users, Admin Users) → assign users
10. **Map services to Groups** (host:port → Group combinations)
11. **Create granular Resources** per service or logical grouping → assign correct Groups (exclude `Everyone`)
12. **Delete the broad `Everything` Resource**
13. **Configure Security Policies** if needed (2FA, device trust, re-auth frequency)

## Configuration Values

| Field | Example Value | Notes |
|-------|--------------|-------|
| Remote Network Location | `On Premise` | Home lab type |
| CIDR Resource | `192.168.100.0/24` | Entire home subnet |
| DNS Pattern Resource | `*.int` | Private DNS domain |
| Resource + Port | `192.168.100.5:5001` | Per-service definition |

## Gotchas
- **IP vs DNS Resources**: Define both if users connect via both methods (e.g., RDP via IP and FQDN)
- **Docker on Windows** can be unstable — prefer Hyper-V Linux VM for Windows Connector hosts
- **Everyone Group**: Must explicitly deselect when creating granular Resources
- **Same server, same Groups** → can combine multiple ports into one Resource
- Twingate Client only intercepts traffic matching defined Resource patterns

## Related Docs
- [Connector Deployment Options](https://www.twingate.com/docs/connector)
- [Security Policies](https://www.twingate.com/docs/policies)
- [Twingate Client Download](https://www.twingate.com/docs/client)
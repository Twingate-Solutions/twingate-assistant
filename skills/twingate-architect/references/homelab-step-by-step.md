# How to Protect Your Home Lab with Twingate

## Summary
Step-by-step guide for securing a home lab using Twingate to replace VPN/port-forwarding. Covers Connector deployment, Resource creation, multi-user access with Groups, and granular permissions. Enables remote access without opening router ports.

## Key Information
- Twingate replaces VPN server + port forwarding rules entirely
- Zero trust model: no permissions granted by default
- Connectors deployed in pairs for HA/load balancing (1 is functional, 2 recommended)
- Connector footprint: 2GB RAM, 2 vCPUs
- Resources identified by IP/CIDR or FQDN + port

## Prerequisites
- Free Twingate account
- Twingate Client installed on admin device
- Device in home lab for Connector deployment (NAS, Raspberry Pi, Linux/Windows machine)

## Step-by-Step

1. **Create Remote Network**: Admin Console → Network → Remote Networks → `+ Remote Network` → Select `On Premise` → Name it
2. **Deploy Connector**: Click Remote Network → select a Connector → choose deployment method (Docker, systemd, Hyper-V) → follow console instructions
3. **Verify Connector**: Confirm it shows connected in Admin Console
4. **Create initial Resource**: Network → Resources → `Add Resource` → CIDR (`192.168.100.0/24`) or DNS pattern (e.g., `*.int`) → assign to `Everyone` group
5. **Test access**: Use alternate internet connection (mobile tether) to verify connectivity
6. **Shut down VPN server**, remove port forwarding rules from router
7. **Invite users**: Team → `Add User` → enter email
8. **Create Groups**: Recommended: `Standard Users`, `Power Users`, `Admin Users`
9. **Map services to groups**: List all `host:port` services, assign each to appropriate group(s)
10. **Create granular Resources**: One Resource per service or per server/group combo; assign correct Groups (not `Everyone`)
11. **Delete `Everything` Resource**
12. **Configure Policies** (optional): Set auth frequency, 2FA requirements, device posture checks

## Configuration Values
| Field | Example Value |
|-------|--------------|
| Remote Network Location | `On Premise` |
| CIDR Resource | `192.168.100.0/24` |
| DNS Pattern Resource | `*.int` |
| Resource types | IP address, CIDR, DNS/FQDN |

## Gotchas
- Resources use Client-side traffic interception: define Resources matching how users actually connect (IP vs. FQDN — may need both)
- Same service may need two Resource entries if users connect via both IP and DNS
- Docker on Windows is unstable; prefer Hyper-V VM for Windows Connector deployment
- One Connector covers all Resources in the Remote Network — no per-Resource Connector needed
- `Everyone` group should be removed from granular Resources

## Related Docs
- [Connector Deployment Options](/docs/connector)
- [Security Policies](/docs/policies)
- [Twingate Client Download](/docs/client)
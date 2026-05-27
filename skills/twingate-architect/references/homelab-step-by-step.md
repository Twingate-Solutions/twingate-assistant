# How to Protect Your Home Lab with Twingate

## Summary
Step-by-step guide for setting up Twingate in a home lab to replace VPN/port forwarding with zero-trust remote access. Covers Connector deployment, Resource creation, multi-user access with Groups, and granular permission mapping. Enables remote access without opening router ports.

## Key Information
- Twingate replaces VPN server + port forwarding rules entirely
- Zero trust model: no permissions granted by default
- Connectors deployed in pairs for HA/load balancing (single is sufficient but not recommended)
- Connector footprint: 2GB RAM, 2 vCPUs
- Resources identified by IP/CIDR or FQDN + port

## Prerequisites
- Free Twingate account
- Twingate Client installed on admin device
- Device in home lab to host Connector (NAS, Raspberry Pi, Linux/Windows machine)

## Step-by-Step

1. **Create Remote Network**: Admin Console → Network → Remote Networks → `+ Remote Network` → Type: `On Premise`
2. **Deploy Connector**: Click Remote Network → select Connector → choose deployment method (Docker container or systemd)
3. **Verify Connector**: Confirm active connection to Controller/Relay in Admin Console
4. **Create initial Resource**: Network → Resources → `Add Resource` → use CIDR (e.g., `192.168.100.0/24`) or DNS pattern (e.g., `*.int`) → assign to `Everyone` group
5. **Test access**: Use alternate internet connection (mobile tether) to verify connectivity
6. **Disable VPN/port forwarding** on router
7. **Invite users**: Team → Add User → enter email
8. **Create Groups**: Groups tab → `Add Group` (e.g., Standard Users, Power Users, Admin Users)
9. **Map services to Groups**: Define host:port Resources per service, assign appropriate Groups
10. **Delete broad "Everything" Resource** after granular Resources created

## Configuration Values

| Setting | Example Value |
|---|---|
| Remote Network type | `On Premise` |
| CIDR Resource | `192.168.100.0/24` |
| DNS pattern Resource | `*.int` |
| Connector RAM | 2GB minimum |
| Connector vCPUs | 2 minimum |

**Deployment methods**: Docker container, systemd (Linux/VM), Hyper-V VM (Windows — Docker on Windows noted as unstable)

## Resource Design Pattern

- Combine services on same host with same Group access into single Resource
- Support both IP and DNS-style Resources if users connect via both methods
- Recommended Group structure: Standard Users / Power Users / Admin Users
- Restrict sensitive ports (SSH :22, RDP :3389, Portainer :9000) to Admin Users only

## Gotchas
- Client intercepts traffic based on Resource definitions — must cover all access methods (IP + FQDN) users actually use
- Do **not** assign granular Resources to `Everyone` group — select specific Groups
- Docker on Windows is noted as unstable for Connector deployment
- Two Connectors created by default per Remote Network; only one required but HA requires two
- After switching to granular Resources, delete the broad CIDR "Everything" Resource

## Related Docs
- [Connector deployment options](https://www.twingate.com/docs/) — additional deployment methods
- [Security Policies](https://www.twingate.com/docs/) — 2FA, device posture, auth frequency per Group
- Twingate Client download page
- Private DNS configuration docs
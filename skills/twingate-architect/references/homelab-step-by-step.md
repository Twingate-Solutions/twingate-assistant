---
source: https://www.twingate.com/docs/homelab-step-by-step
type: docs
fetched: 2026-08-14
source_version: b312f50ba2d2df81b10e919e95c50a034caaac1c4b47d78fbc39b21aad5a6931
---

# How to Protect Your Home Lab with Twingate

## Summary
Step-by-step guide for securing a home lab using Twingate to replace VPN/port forwarding with zero-trust access. Covers Connector deployment, Resource creation, multi-user access control via Groups, and Security Policies for a typical home lab environment.

## Key Information
- Twingate replaces router VPN, port forwarding, and dynamic DNS entirely
- Uses zero-trust model: no permissions granted by default
- Connectors deployed in pairs for HA/load balancing (single Connector works but not recommended)
- Connector footprint: 2GB RAM, 2 vCPUs minimum
- Resources identified by IP/CIDR, FQDN, or DNS pattern + optional port restrictions
- Traffic interception determined by Resource definitions in the Client

## Prerequisites
- Free Twingate account registered
- Twingate Client installed on admin device
- Device to host Connector (NAS, Raspberry Pi, Linux machine, Windows with Docker/Hyper-V)

## Step-by-Step

1. **Create Remote Network**: Admin Console → Network → Remote Networks → `+ Remote Network` → Select `On Premise` → Name it (e.g., "Home Lab")
2. **Deploy Connector**: Click Remote Network → select a Connector → choose deployment method (Docker, systemd, etc.) → follow console instructions → verify Connected status
3. **Create initial Resource**: Network → Resources → `Add Resource` → label "Everything" → CIDR `192.168.100.0/24` (or DNS pattern `*.int`) → assign to `Everyone` Group
4. **Test access**: Use alternate internet (mobile tether) → verify internal services reachable
5. **Shut down VPN server**, close its port, remove port forwarding rules from router
6. **Invite users**: Team → Add User → enter email for each
7. **Create Groups** (suggested roles):
   - `Standard Users` – basic service access only
   - `Power Users` – elevated but non-admin access
   - `Admin Users` – full access including SSH, RDP, router UI
8. **Map services to Groups** (see table below)
9. **Create granular Resources**: Replace "Everything" with per-service Resources, assign correct Groups, exclude `Everyone` Group
10. **Delete "Everything" Resource**
11. **(Optional)** Configure Security Policies for 2FA, device posture, re-auth frequency

## Configuration Values

| Setting | Example Value |
|---|---|
| Remote Network location | `On Premise` |
| CIDR Resource | `192.168.100.0/24` |
| DNS pattern Resource | `*.int` |
| Connector RAM | 2GB |
| Connector vCPUs | 2 |

## Service-to-Group Mapping Example

| Service | Port | Groups |
|---|---|---|
| NAS UI, Plex, Calibre, Jellyfin | various | Standard, Power, Admin |
| NAS Home Assistant, Router UI | 8123, 8001 | Standard, Power |
| Win RDP, Linux SSH, Portainer | 3389, 22, 9000 | Admin only |

## Gotchas
- Resources must be explicitly assigned to Groups — zero permissions by default
- If users connect via both IP and FQDN, create separate Resources for each
- Docker on Windows can be unstable; prefer Hyper-V Linux VM for Windows hosts
- Do **not** assign granular Resources to the `Everyone` Group (only initial test Resource)
- Two Connectors per Remote Network provide automatic HA — deploying one works but is single point of failure

## Related Docs
- [Connector deployment options](https://www.twingate.com/docs/connector)
- [Security Policies](https://www.twingate.com/docs/policies)
- [Twingate Client download](https://www.twingate.com/docs/client)
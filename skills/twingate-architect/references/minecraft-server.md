---
source: https://www.twingate.com/docs/minecraft-server
type: docs
fetched: 2026-08-05
source_version: f8eae94bbfac4a63444238ae0cdf1db5473913844d74ee3976bf2e29d46b8342
---

# Minecraft Server with Twingate

## Summary
Run a private Minecraft Java Edition server using Docker Compose with a Twingate Connector, eliminating the need for port forwarding. Players connect via the Twingate Client using the server's private Docker network IP. No public ports are exposed.

## Key Information
- Uses `itzg/minecraft-server` Docker image with Twingate Connector in Docker Compose
- Server fixed at `172.30.0.10` on private bridge network `172.30.0.0/24`
- Java Edition uses TCP port `25565` only (no UDP needed)
- Connector makes outbound-only connections; no inbound ports required on router
- Twingate Client must remain connected throughout the Minecraft session

## Prerequisites
- Machine: 2 GB RAM minimum (4+ GB for mods), 2 CPU cores, 10 GB disk
- Docker Engine and Docker Compose installed
- Twingate account with Admin Console access
- Terminal access to host machine

## Step-by-Step

1. **Create Remote Network** in Admin Console → Remote Networks → Add Remote Network
2. **Generate Connector tokens** → select Docker deployment → Generate Tokens → copy Access Token and Refresh Token
3. **Create `docker-compose.yml`** with minecraft and twingate-connector services
4. **Start containers**: `docker compose up -d`
5. **Verify Connector** shows Controller and Relay as "Connected" in Admin Console
6. **Add Resource**: Address `172.30.0.10`, TCP port `25565`, assign to Group
7. **Players install Twingate Client**, sign in, then connect to `172.30.0.10` in Minecraft Multiplayer

## Configuration Values

### Docker Compose Environment Variables
| Variable | Value | Description |
|---|---|---|
| `EULA` | `"TRUE"` | Accept Minecraft EULA (required) |
| `MEMORY` | `"2G"` | Java heap size |
| `TYPE` | `"VANILLA"` | Server type: `VANILLA`, `PAPER`, `FORGE`, `FABRIC` |
| `VERSION` | `"LATEST"` | Minecraft version |
| `DIFFICULTY` | `"normal"` | `peaceful`, `easy`, `normal`, `hard` |
| `MAX_PLAYERS` | `"10"` | Max concurrent players |
| `TWINGATE_NETWORK` | `<network-name>` | Twingate network subdomain |
| `TWINGATE_ACCESS_TOKEN` | `<token>` | From Admin Console |
| `TWINGATE_REFRESH_TOKEN` | `<token>` | From Admin Console |

### Network
- Subnet: `172.30.0.0/24`
- Minecraft container IP: `172.30.0.10`
- Connector image: `twingate/connector:1`
- Minecraft image: `itzg/minecraft-server:latest`

## Gotchas
- **Do not reuse tokens** across Connectors — each requires unique Access/Refresh token pair
- `network_mode: host` is intentionally avoided; breaks on Docker Desktop (macOS/Windows)
- World data in `./data:/data` volume — deleting this directory loses all world data
- Heavy modpacks may need 6–8 GB RAM; adjust `MEMORY` and ensure host has sufficient free RAM
- Bedrock Edition uses UDP/19132, not covered by this guide

## Troubleshooting
- **Can't connect**: Check Client toggle is green, Resource appears in Client, address matches `172.30.0.10`
- **Server crashes**: Check `docker compose logs minecraft` — likely insufficient `MEMORY`
- **Connector offline**: Verify all three `TWINGATE_*` env vars are correct; check outbound internet access

## Related Docs
- [Linux native install version](https://www.twingate.com/docs/minecraft-server) (linked as "Linux version")
- Bedrock Edition guide
- Forge (modded) guide
- itzg/minecraft-server documentation
- Twingate Security Policies
- Protect Your Home Lab guide
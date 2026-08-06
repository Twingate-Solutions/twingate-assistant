---
source: https://www.twingate.com/docs/minecraft-bedrock-server
type: docs
fetched: 2026-08-05
source_version: 8a3d8c1ef64330fcab35a357eeb076db14e2e6e82ea8161d744063468dda505f
---

# Minecraft Bedrock Server with Twingate

## Summary
Deploy a private Minecraft Bedrock Edition server using Docker Compose with a Twingate Connector, eliminating the need for port forwarding. Players connect via Twingate Client which tunnels UDP traffic to the server's private Docker network IP. Supports Windows, iOS, Android, and ChromeOS players only (no console support).

## Key Information
- Bedrock server runs on UDP port **19132** (critical: must configure Resource as UDP, not TCP)
- Server pinned to fixed Docker IP `172.30.0.10` on bridge network `minecraft-net`
- No ports published to host — traffic flows through Twingate tunnel only
- ARM machines supported via `box64` emulation layer in `itzg/minecraft-bedrock-server` image
- Console players (Xbox, PlayStation, Switch) cannot use Twingate — local network only

## Prerequisites
- Machine: 1 GB RAM, 2 CPU cores, 10 GB disk
- Docker Engine + Docker Compose installed
- Twingate account with Admin Console access
- Terminal access to host machine

## Step-by-Step

1. **Create Remote Network** in Admin Console → Remote Networks → Add Remote Network
2. **Generate Connector Tokens** — select Docker deployment, copy Access Token + Refresh Token
3. **Create `docker-compose.yml`** (see configuration below)
4. **Start containers**: `docker compose up -d`
5. **Verify Connector** shows `Connected` in Admin Console
6. **Add Resource**: Address `172.30.0.10`, Protocol UDP port `19132`
7. **Grant access** to Group (e.g., `Everyone` or custom `Minecraft Players`)
8. **Players install Twingate Client**, sign in, then add server at `172.30.0.10:19132` in Minecraft

## Configuration Values

### Docker Compose Environment Variables
| Variable | Value | Notes |
|----------|-------|-------|
| `EULA` | `"TRUE"` | Required — accepts Minecraft EULA |
| `TWINGATE_NETWORK` | `<network_name>` | e.g., `mynetwork` |
| `TWINGATE_ACCESS_TOKEN` | `<token>` | From Admin Console |
| `TWINGATE_REFRESH_TOKEN` | `<token>` | From Admin Console |

### Bedrock Server Tuning Variables
| Variable | Default | Options |
|----------|---------|---------|
| `GAMEMODE` | `survival` | `survival`, `creative`, `adventure` |
| `DIFFICULTY` | `easy` | `peaceful`, `easy`, `normal`, `hard` |
| `MAX_PLAYERS` | `10` | Integer |
| `VERSION` | `LATEST` | e.g., `1.21.30.03` |
| `LEVEL_SEED` | random | Any string |
| `SERVER_PORT` | `19132` | UDP port |

### Network Config
- Subnet: `172.30.0.0/24`
- Bedrock server IP: `172.30.0.10`
- Docker network name: `minecraft-net`

## Gotchas
- **UDP is mandatory** — TCP-only Resource causes "Unable to connect to world" error
- **Tokens are not reusable** — each Connector needs unique Access + Refresh Token pair
- **`network_mode: host`** does not work on Docker Desktop (macOS/Windows) — use bridge network
- **ARM overhead** — emulation (`box64`) adds CPU cost; keep player count low on Raspberry Pi
- **Twingate Client must stay connected** throughout the entire Minecraft session
- Bedrock has no configurable heap size (unlike Java Edition); OOM = increase host RAM

## Troubleshooting
- "Unable to connect": Check Client is connected → Resource appears in Client → Resource is UDP → container is `Up` → IP/port match
- Connector offline: Verify env vars, check outbound internet, run `docker compose logs twingate-connector`
- Server crashes: Run `docker compose logs bedrock`, check memory and architecture compatibility

## Related Docs
- [Minecraft Java Edition guide](https://www.twingate.com/docs) — for Java Edition servers
- [itzg/minecraft-bedrock-
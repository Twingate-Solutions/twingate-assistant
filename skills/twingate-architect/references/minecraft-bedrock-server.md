# Minecraft Bedrock Server with Twingate

## Summary
Host a private Minecraft Bedrock Edition server using Docker Compose with a Twingate Connector, eliminating the need for port forwarding. Traffic routes through an encrypted Twingate tunnel using a fixed Docker bridge network IP. Supports Windows, iOS, Android, and ChromeOS players only (no console support).

## Key Information
- Uses `itzg/minecraft-bedrock-server` Docker image with Twingate Connector in Docker Compose
- Server pinned to `172.30.0.10` on a user-defined bridge network (`minecraft-net`)
- **No ports published to host** — Connector reaches server directly over Docker bridge
- Bedrock uses **UDP port 19132** (not TCP)
- Multi-arch image supports ARM (Apple Silicon, Raspberry Pi) via `box64` emulation layer
- Hardware minimum: 1 GB RAM, 2 CPU cores, 10 GB disk

## Prerequisites
- Docker Engine + Docker Compose installed
- Twingate account with Admin Console access
- Terminal access to host machine

## Step-by-Step

1. **Admin Console** → Remote Networks → Add Remote Network
2. Add Connector → Select Docker → Generate Tokens → copy Access Token + Refresh Token
3. Create project directory and `docker-compose.yml` (see config below)
4. Replace placeholders → `docker compose up -d`
5. **Admin Console** → Resources → Add Resource → set address `172.30.0.10`, **UDP port 19132**
6. Assign Group access to Resource
7. Players install Twingate Client, sign in, then add server at `172.30.0.10:19132` in Minecraft

## Configuration Values

### Docker Compose Environment Variables
| Variable | Value | Notes |
|---|---|---|
| `TWINGATE_NETWORK` | `<network_name>` | Without `.twingate.com` |
| `TWINGATE_ACCESS_TOKEN` | `<token>` | Unique per Connector |
| `TWINGATE_REFRESH_TOKEN` | `<token>` | Unique per Connector |
| `EULA` | `TRUE` | Required to start server |
| `SERVER_NAME` | `"Private Bedrock Server"` | Shown in server list |
| `GAMEMODE` | `survival` | `survival`/`creative`/`adventure` |
| `DIFFICULTY` | `normal` | `peaceful`/`easy`/`normal`/`hard` |
| `MAX_PLAYERS` | `10` | |
| `VERSION` | `LATEST` | Pin with e.g. `1.21.30.03` |
| `LEVEL_SEED` | *(random)* | |

### Docker Images
- `itzg/minecraft-bedrock-server:latest`
- `twingate/connector:1`

### Network
- Subnet: `172.30.0.0/24`
- Server fixed IP: `172.30.0.10`

## Gotchas
- **UDP not TCP**: Configuring the Twingate Resource with TCP causes "Unable to connect to world" error
- **Console players unsupported**: Xbox, PlayStation, Switch have no Twingate Client
- **Twingate must stay connected** during entire Minecraft session
- `network_mode: host` does not work on Docker Desktop for macOS/Windows
- Each Connector requires its own unique token pair — never reuse tokens
- ARM emulation adds CPU overhead; keep player counts low on Raspberry Pi

## Troubleshooting
- "Unable to connect": Check Twingate Client connected, Resource in client list, UDP protocol set, server running (`docker compose ps`), correct IP/port in Minecraft
- Connector offline: Verify all three `TWINGATE_*` env vars, outbound internet access, check `docker compose logs twingate-connector`

## Related Docs
- [Minecraft Java Edition Guide](https://www.twingate.com/docs/minecraft-java-server)
- [Linux native install version](https://www.twingate.com/docs/minecraft-bedrock-server) (linked as "Linux version")
- [itzg/minecraft-bedrock-server documentation](https://github.com/itzg/docker-minecraft-bed
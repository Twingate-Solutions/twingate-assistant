<!-- triage: unassigned URL: https://www.twingate.com/docs/minecraft-bedrock-server -->

# Minecraft Bedrock Server with Twingate

## Summary
Hosts a private Minecraft Bedrock Edition server using Docker Compose with a Twingate Connector, eliminating the need for port forwarding. Players connect via Twingate Client using the server's private Docker bridge IP. Console players (Xbox, PlayStation, Switch) are not supported.

## Key Information
- Bedrock server pinned to `172.30.0.10` on Docker bridge network `minecraft-net` (subnet `172.30.0.0/24`)
- Bedrock uses **UDP port 19132** — must be configured as UDP in Twingate Resource (not TCP)
- No ports published to host; Connector reaches server directly over private bridge
- `itzg/minecraft-bedrock-server` image is multi-arch (includes box64 emulation for ARM)
- Twingate Connector adds <256 MB RAM overhead

## Prerequisites
- Machine: 1 GB RAM, 2 CPU cores, 10 GB disk
- Docker Engine + Docker Compose installed
- Twingate account with Admin Console access
- Terminal access to host machine

## Step-by-Step

1. **Create Remote Network** in Twingate Admin Console → Add Connector → Select Docker → Generate Tokens → copy Access Token and Refresh Token
2. **Create project directory** and `docker-compose.yml` (see config below)
3. **Start containers**: `docker compose up -d`
4. **Verify Connector** in Admin Console shows Controller and Relay as `Connected`
5. **Add Resource**: Address `172.30.0.10`, Protocol UDP port `19132`
6. **Grant access** to a Group (e.g., `Everyone` or custom `Minecraft Players`)
7. **Players install Twingate Client**, sign in, then add server `172.30.0.10:19132` in Minecraft

## Configuration Values

**docker-compose.yml environment variables:**

| Variable | Value |
|---|---|
| `TWINGATE_NETWORK` | `<your-network-name>` |
| `TWINGATE_ACCESS_TOKEN` | `<access-token>` |
| `TWINGATE_REFRESH_TOKEN` | `<refresh-token>` |
| `EULA` | `"TRUE"` |
| `SERVER_NAME` | `"Private Bedrock Server"` |
| `GAMEMODE` | `survival` / `creative` / `adventure` |
| `DIFFICULTY` | `peaceful` / `easy` / `normal` / `hard` |
| `MAX_PLAYERS` | `10` |
| `VERSION` | `LATEST` or specific (e.g., `1.21.30.03`) |
| `LEVEL_SEED` | *(random)* |
| `SERVER_PORT` | `19132` |

**Docker images:**
- `itzg/minecraft-bedrock-server:latest`
- `twingate/connector:1`

## Gotchas
- **UDP required**: Configuring Resource as TCP causes "Unable to connect to world" error
- **Twingate Client must stay connected** throughout the entire Minecraft session
- **Console platforms unsupported**: Xbox, PlayStation, Switch have no Twingate Client
- **ARM overhead**: box64 emulation works but reduces performance on low-powered ARM hardware (e.g., Raspberry Pi)
- **Token reuse**: Each Connector requires unique Access/Refresh token pair
- **`network_mode: host`** does not work on Docker Desktop for macOS/Windows

## Related Docs
- [Minecraft Java Edition guide](https://www.twingate.com/docs/minecraft-java-server)
- [Linux native install version](https://www.twingate.com/docs/minecraft-bedrock-server-linux)
- [itzg/minecraft-bedrock-server docs](https://github.com/itzg/docker-minecraft-bedrock-server)
- Twingate Security Policies, Resources configuration, Protect Your Home Lab
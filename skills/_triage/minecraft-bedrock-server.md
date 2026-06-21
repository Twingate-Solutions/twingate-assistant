<!-- triage: unassigned URL: https://www.twingate.com/docs/minecraft-bedrock-server -->

# Minecraft Bedrock Server with Twingate

## Summary
Host a private Minecraft Bedrock Edition server using Docker Compose with a Twingate Connector, eliminating the need for port forwarding. Players connect via the Twingate Client using the server's private Docker network IP. Console platforms (Xbox, PlayStation, Switch) are not supported.

## Key Information
- Uses `itzg/minecraft-bedrock-server` Docker image with Twingate Connector in same Docker Compose stack
- Server pinned to fixed IP `172.30.0.10` on a shared bridge network (`minecraft-net`, subnet `172.30.0.0/24`)
- Bedrock uses **UDP port 19132** (not TCP — common misconfiguration)
- Multi-arch image supports ARM (Apple Silicon, Raspberry Pi) via `box64` emulation
- No ports published to host; Connector handles all inbound player traffic

## Prerequisites
- Machine: 1 GB RAM, 2 CPU cores, 10 GB disk
- Docker Engine + Docker Compose installed
- Twingate account with Admin Console access
- Terminal access to host machine

## Step-by-Step

1. **Create Remote Network** in Twingate Admin Console → Remote Networks → Add Remote Network
2. **Generate Connector tokens** → select Docker deployment → Generate Tokens → copy Access Token and Refresh Token
3. **Deploy stack** — create `docker-compose.yml`, substitute tokens, run `docker compose up -d`
4. **Verify Connector** shows Controller and Relay both `Connected` in Admin Console
5. **Add Resource**: Address `172.30.0.10`, Protocol **UDP port 19132**
6. **Grant access** to a Group (default: `Everyone`, or create `Minecraft Players` group)
7. **Players**: Install Twingate Client → sign in → add server at `172.30.0.10:19132` in Minecraft

## Configuration Values

| Variable | Default | Description |
|---|---|---|
| `EULA` | — | Must be `"TRUE"` |
| `SERVER_NAME` | `Dedicated Server` | Display name |
| `GAMEMODE` | `survival` | `survival`, `creative`, `adventure` |
| `DIFFICULTY` | `easy` | `peaceful`, `easy`, `normal`, `hard` |
| `MAX_PLAYERS` | `10` | Max concurrent players |
| `LEVEL_SEED` | random | World seed |
| `VERSION` | `LATEST` | e.g., `1.21.30.03` |
| `SERVER_PORT` | `19132` | UDP listen port |

**Twingate Connector env vars:**
- `TWINGATE_NETWORK` — network name (e.g., `mynetwork`)
- `TWINGATE_ACCESS_TOKEN`
- `TWINGATE_REFRESH_TOKEN`

## Gotchas
- **UDP required**: Configuring Resource as TCP causes "Unable to connect to world" with no other indication
- **Twingate Client must stay connected** throughout play session
- **Console players cannot use Twingate** — no client available for Xbox/PlayStation/Switch
- **Do not reuse tokens** across multiple Connectors
- `network_mode: host` does not work on Docker Desktop (macOS/Windows); use bridge network instead
- ARM emulation adds CPU overhead — keep player count low on Raspberry Pi

## Related Docs
- [Minecraft Java Edition guide](https://www.twingate.com/docs) — for Java Edition setup
- [itzg/minecraft-bedrock-server docs](https://github.com/itzg/docker-minecraft-bedrock-server) — full env var reference
- Twingate Security Policies — MFA/device trust for players
- Linux native install version available (linked in source)
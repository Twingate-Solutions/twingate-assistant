# Minecraft Server with Twingate

## Summary
Host a private Minecraft Java Edition server using Docker Compose with a Twingate Connector, eliminating the need for port forwarding. Players connect via Twingate Client, routing traffic through an encrypted tunnel to the server's private Docker network IP. No public ports are exposed.

## Key Information
- Uses `itzg/minecraft-server` Docker image with Twingate Connector in same Docker Compose stack
- Server fixed at `172.30.0.10` on private bridge network `172.30.0.0/24`
- Java Edition uses TCP port `25565` only (no UDP needed)
- Connector adds <256 MB RAM overhead; vanilla server needs 2 GB minimum
- Players must keep Twingate Client connected for entire session

## Prerequisites
- Machine: 2 GB RAM, 2 CPU cores, 10 GB disk (4+ GB RAM for mods)
- Docker Engine + Docker Compose installed
- Twingate account with Admin Console access
- Terminal access to host machine

## Step-by-Step

1. **Create Remote Network** in Admin Console → Remote Networks → Add Remote Network
2. **Generate Connector tokens**: Click Connector → Docker → Generate Tokens → copy Access Token + Refresh Token
3. **Create `docker-compose.yml`** with minecraft + twingate-connector services (see config below)
4. **Start containers**: `docker compose up -d`
5. **Verify Connector** shows Controller + Relay as "Connected" in Admin Console
6. **Add Resource**: Address `172.30.0.10`, TCP port `25565`, assign to a Group
7. **Players install** Twingate Client, sign in, add `172.30.0.10` as Minecraft server address

## Configuration Values

**Docker Compose environment variables:**

| Variable | Value | Description |
|----------|-------|-------------|
| `EULA` | `"TRUE"` | Accept Minecraft EULA |
| `MEMORY` | `"2G"` | Java heap size |
| `TYPE` | `"VANILLA"` | Server type: `VANILLA`, `PAPER`, `FORGE`, `FABRIC` |
| `VERSION` | `"LATEST"` | Minecraft version |
| `DIFFICULTY` | `"normal"` | `peaceful/easy/normal/hard` |
| `MAX_PLAYERS` | `"10"` | Max concurrent players |
| `TWINGATE_NETWORK` | `<network-name>` | Your Twingate network name |
| `TWINGATE_ACCESS_TOKEN` | `<token>` | From Admin Console |
| `TWINGATE_REFRESH_TOKEN` | `<token>` | From Admin Console |

**Network:** `subnet: 172.30.0.0/24`, server at `172.30.0.10`

## Gotchas
- **Do not reuse tokens** across Connectors — each requires unique Access/Refresh token pair
- **`network_mode: host` not used** — incompatible with Docker Desktop on macOS/Windows
- World data stored in `./data:/data` volume — deleting this directory loses all world data
- Heavy modpacks may need 6–8 GB RAM; set `MEMORY` accordingly
- After any `docker-compose.yml` changes: `docker compose down && docker compose up -d`

## Related Docs
- [Bedrock Edition guide](https://www.twingate.com/docs) — uses UDP port 19132
- [Forge (modded) guide](https://www.twingate.com/docs)
- [Linux native install guide](https://www.twingate.com/docs)
- [itzg/minecraft-server documentation](https://github.com/itzg/docker-minecraft-server)
- [Twingate Security Policies](https://www.twingate.com/docs/security-policies)
- [Protect Your Home Lab](https://www.twingate.com/docs)
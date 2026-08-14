---
source: https://www.twingate.com/docs/minecraft-server
type: docs
fetched: 2026-08-14
source_version: 8f11a2bc08b34de80ade380df9e106a1ff0169fe4f417e846794e12d6e120970
---

# Minecraft Server with Twingate

## Summary
Host a private Minecraft Java Edition server using Docker Compose with a Twingate Connector, eliminating the need for port forwarding. Players connect via the Twingate Client using the server's private Docker network IP. No public ports are exposed.

## Key Information
- Uses `itzg/minecraft-server` Docker image with Twingate Connector in same Docker Compose stack
- Minecraft server gets fixed IP `172.30.0.10` on a private bridge network (`172.30.0.0/24`)
- Connector makes outbound-only encrypted tunnel; no inbound ports opened on router
- Java Edition uses TCP port `25565` only (no UDP needed)
- Supports Vanilla, Paper, Forge, and Fabric via `TYPE` env var

## Prerequisites
- Machine: ≥2 GB RAM, ≥2 CPU cores, ≥10 GB disk (4+ GB RAM for mods)
- Docker Engine + Docker Compose installed
- Twingate account with Admin Console access
- Twingate Access Token and Refresh Token (generated per Connector)

## Step-by-Step

1. **Create Remote Network** in Admin Console → Remote Networks → Add Remote Network
2. **Generate Connector Tokens** → select Docker deployment → Generate Tokens → copy Access Token and Refresh Token
3. **Deploy Docker Compose** with Minecraft server + Connector containers
4. **Verify** Connector shows Controller and Relay as Connected in Admin Console
5. **Add Resource**: Address `172.30.0.10`, Protocol TCP port `25565`
6. **Grant Access** to a Group (e.g., "Minecraft Players")
7. **Players install Twingate Client**, sign in, then add `172.30.0.10` in Minecraft Multiplayer

## Configuration Values

### Docker Compose Environment Variables
| Variable | Value | Description |
|---|---|---|
| `TWINGATE_NETWORK` | `<network-name>` | Your Twingate network subdomain |
| `TWINGATE_ACCESS_TOKEN` | `<token>` | Connector access token |
| `TWINGATE_REFRESH_TOKEN` | `<token>` | Connector refresh token |
| `EULA` | `"TRUE"` | Accepts Minecraft EULA |
| `MEMORY` | `"2G"` | Java heap size |
| `TYPE` | `"VANILLA"` | Server type: `VANILLA`, `PAPER`, `FORGE`, `FABRIC` |
| `VERSION` | `"LATEST"` | Minecraft version |
| `DIFFICULTY` | `"normal"` | `peaceful`, `easy`, `normal`, `hard` |
| `MAX_PLAYERS` | `"10"` | Max concurrent players |
| `OPS` | _(none)_ | Comma-separated operator usernames |
| `SEED` | _(random)_ | World generation seed |

### Resource Config
- **Address**: `172.30.0.10`
- **Protocol**: TCP, port `25565`

## Gotchas
- `network_mode: host` intentionally avoided—doesn't work on Docker Desktop (macOS/Windows)
- Each Connector requires its **own unique** token pair; do not reuse tokens
- Twingate Client must remain connected for entire play session
- World data persists to `./data` host directory; deleting it loses the world
- Memory crashes are common cause of server instability—increase `MEMORY` and ensure host has free RAM

## Troubleshooting
- **Can't connect**: Check Client toggle is green, Resource appears in Client, both containers show `Up`, address matches `172.30.0.10`
- **Server crashes**: `docker compose logs minecraft` — usually insufficient RAM
- **Connector offline**: Verify all three `TWINGATE_*` env vars; check outbound internet; run `docker compose logs twingate-connector`

## Related Docs
- [Bedrock Edition guide](https://www.twingate.com/docs/minecraft-bedrock)
- [Forge/modded guide](https://www.twingate.com/docs/minecraft-forge)
- [Linux native install](https://www.twingate.com/docs/minecraft-linux)
- [itzg/minecraft
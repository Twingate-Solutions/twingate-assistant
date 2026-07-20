# Minecraft Server with Twingate

## Summary
Host a private Minecraft Java Edition server via Docker Compose with zero port forwarding. Twingate Connector creates an outbound-only encrypted tunnel; players use the Twingate Client to reach the server's private IP. Port 25565 is never exposed to the public internet.

## Key Information
- Uses `itzg/minecraft-server` Docker image (supports Vanilla, Paper, Forge, Fabric)
- Server fixed at `172.30.0.10` on private Docker bridge network `172.30.0.0/24`
- Minecraft Java Edition: TCP port `25565` only (no UDP needed)
- Connector overhead: <256 MB RAM, negligible CPU
- Vanilla server for ≤10 players: 2 GB RAM minimum; modded: 4–8+ GB

## Prerequisites
- Machine: 2 GB RAM, 2 CPU cores, 10 GB disk (Linux/macOS/Windows)
- Docker Engine + Docker Compose installed
- Twingate account with Admin Console access
- Terminal access

## Step-by-Step

1. **Admin Console → Remote Networks → Add Remote Network** (e.g., "Home Lab")
2. **Add Connector → Select Docker → Generate Tokens** → copy Access Token + Refresh Token
3. Create `~/minecraft-server/docker-compose.yml` (see config below)
4. Replace placeholders → `docker compose up -d`
5. Verify: `docker compose logs minecraft -f` → wait for `Done (...s)! For help, type "help"`
6. Confirm Connector shows `Controller` and `Relay` both **Connected** in Admin Console
7. **Admin Console → Resources → Add Resource**: Address `172.30.0.10`, TCP port `25565`
8. Assign Resource to a Group (e.g., `Everyone` or custom `Minecraft Players`)
9. Players install Twingate Client, sign in, then add `172.30.0.10` in Minecraft → Multiplayer

## Configuration Values

**Docker Compose environment variables:**

| Variable | Value | Notes |
|---|---|---|
| `TWINGATE_NETWORK` | `<your-network-name>` | e.g., `mynetwork` (no `.twingate.com`) |
| `TWINGATE_ACCESS_TOKEN` | `<token>` | From Admin Console |
| `TWINGATE_REFRESH_TOKEN` | `<token>` | From Admin Console |
| `EULA` | `"TRUE"` | Required; implies EULA acceptance |
| `MEMORY` | `"2G"` | Java heap size |
| `TYPE` | `"VANILLA"` | `VANILLA`, `PAPER`, `FORGE`, `FABRIC` |
| `VERSION` | `"LATEST"` | Or pin e.g. `"1.21.1"` |
| `DIFFICULTY` | `"normal"` | `peaceful`/`easy`/`normal`/`hard` |
| `MAX_PLAYERS` | `"10"` | |
| `OPS` | *(none)* | Comma-separated operator usernames |
| `SEED` | *(random)* | World generation seed |

**Fixed network:** `172.30.0.10` (minecraft container), subnet `172.30.0.0/24`

## Gotchas
- **Do not reuse tokens** across Connectors — each needs unique Access/Refresh Token pair
- `network_mode: host` is intentionally avoided (breaks Docker Desktop on macOS/Windows)
- Twingate Client must remain connected for entire play session
- World data lives in `./data` volume — deleting it loses the world; back up regularly
- Modded servers (Forge/Fabric) may need 6–8+ GB RAM; raise `MEMORY` accordingly
- Bedrock Edition uses UDP/19132 — this guide is Java Edition only

## Troubleshooting
- **Can't connect**: Check Client toggle is green; verify player is in correct Group; confirm `172.30.0.10` matches Resource address
- **Server crashes**: Check `docker compose logs minecraft` — likely insufficient `MEMORY`
- **Connector offline**: Verify all three `TWINGATE_*` env vars;
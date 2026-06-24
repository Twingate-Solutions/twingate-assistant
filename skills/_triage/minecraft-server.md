<!-- triage: unassigned URL: https://www.twingate.com/docs/minecraft-server -->

# Minecraft Server with Twingate

## Summary
Host a private Minecraft Java Edition server using Docker Compose with a Twingate Connector, eliminating the need for port forwarding. Players connect via the Twingate Client using the server's private Docker network IP. No public IP exposure or inbound firewall rules required.

## Key Information
- Uses `itzg/minecraft-server` Docker image with Twingate Connector in Docker Compose
- Minecraft server assigned fixed IP `172.30.0.10` on private bridge network `172.30.0.0/24`
- Java Edition only (TCP 25565); Bedrock uses different protocol/port
- Connector overhead: <256 MB RAM, negligible CPU
- Vanilla server for ≤10 players: 2 GB RAM minimum; heavy modpacks may need 6–8 GB

## Prerequisites
- Machine: 2 GB RAM, 2 CPU cores, 10 GB disk (Linux/macOS/Windows)
- Docker Engine + Docker Compose installed
- Twingate account with Admin Console access
- Terminal access

## Step-by-Step

1. **Create Remote Network** → Admin Console → Remote Networks → Add Remote Network
2. **Generate Connector tokens** → select Connector → Docker → Generate Tokens → copy Access Token and Refresh Token
3. **Create `docker-compose.yml`** with minecraft and twingate-connector services (see config below)
4. **Start containers**: `docker compose up -d`
5. **Verify Connector** in Admin Console shows Controller + Relay as `Connected`
6. **Add Resource**: Address `172.30.0.10`, Protocol TCP port `25565`
7. **Assign Group access** to Resource
8. **Players install Twingate Client**, sign in, then add `172.30.0.10` as Minecraft server address

## Configuration Values

### Docker Compose Environment Variables

| Variable | Value | Notes |
|---|---|---|
| `TWINGATE_NETWORK` | `<network-name>` | e.g., `mynetwork` (no `.twingate.com`) |
| `TWINGATE_ACCESS_TOKEN` | `<token>` | From Admin Console |
| `TWINGATE_REFRESH_TOKEN` | `<token>` | From Admin Console |
| `EULA` | `"TRUE"` | Required; implies EULA acceptance |
| `MEMORY` | `"2G"` | Java heap size |
| `TYPE` | `"VANILLA"` | Options: `VANILLA`, `PAPER`, `FORGE`, `FABRIC` |
| `VERSION` | `"LATEST"` | Or pin e.g. `"1.21.1"` |
| `DIFFICULTY` | `"normal"` | `peaceful`/`easy`/`normal`/`hard` |
| `MAX_PLAYERS` | `"10"` | |
| `OPS` | (none) | Comma-separated operator usernames |
| `SEED` | (random) | World generation seed |

### Network
- Subnet: `172.30.0.0/24`
- Minecraft container fixed IP: `172.30.0.10`
- No host port publishing (no `ports:` mapping)

## Gotchas
- **Tokens are unique per Connector** — never reuse Access/Refresh token pairs
- **`network_mode: host` not used** — incompatible with Docker Desktop on macOS/Windows
- **Twingate Client must stay connected** during entire Minecraft session
- **World data loss**: `./data:/data` volume must not be deleted; back up `~/minecraft-server/data` regularly
- After any `docker-compose.yml` change, run `docker compose down && docker compose up -d`
- Server ready when logs show: `Done (Xs)! For help, type "help"`

## Related Docs
- [Bedrock Edition guide](https://www.twingate.com/docs/minecraft-bedrock)
- [Forge (modded) guide](https://www.twingate.com/docs/minecraft-forge)
- [Linux native install version](https://www.twingate.com/docs/minecraft-linux)
- [itzg/minecraft-server documentation](https://github.com/itz
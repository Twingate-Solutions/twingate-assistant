# Modded Minecraft Server (Forge) with Twingate

## Summary
Hosts a private Forge modded Minecraft server using Docker Compose with a Twingate Connector sidecar. Supports both CurseForge modpack auto-install and manual mod placement. Players connect via Twingate Client to a private IP with no port forwarding required.

## Key Information
- Server pinned to `172.30.0.10` on internal bridge network `172.30.0.0/24`
- No host port published; Connector reaches server directly over Docker bridge
- Minecraft port: TCP `25565`
- Both containers share `minecraft-net` bridge network
- CurseForge API key required for modpack auto-download (free at console.curseforge.com)
- First startup can take 10+ minutes (downloads Forge + all mods)

## Prerequisites
- Machine: 4+ GB RAM (6-8 GB for large packs), 2 CPU cores, 20 GB disk
- Docker Engine + Docker Compose installed
- Twingate account with Admin Console access
- Terminal access to host machine
- CurseForge API key (Option A only)

## Step-by-Step

1. **Create Remote Network + Connector tokens** — Follow Step 1 of vanilla Minecraft guide
2. **Deploy server** — Create `docker-compose.yml` (see configs below), run `docker compose up -d`
3. **Add Resource** — Address: `172.30.0.10`, Protocol: TCP port `25565`
4. **Grant access** — Assign Group to Resource in Admin Console
5. **Players install** — Twingate Client + same modpack/mods as server
6. **Connect** — Multiplayer → Add Server → `172.30.0.10`

## Configuration Values

### Option A: CurseForge Modpack
| Variable | Value/Description |
|---|---|
| `TYPE` | `AUTO_CURSEFORGE` |
| `CF_PAGE_URL` | Full CurseForge modpack URL |
| `CF_API_KEY` | CurseForge API key (escape `$` as `$$`) |
| `CF_SLUG` | Alternative to `CF_PAGE_URL` |
| `CF_FILE_ID` | Pin specific modpack version |
| `MEMORY` | `6G` recommended |

### Option B: Manual Mods
| Variable | Value/Description |
|---|---|
| `TYPE` | `FORGE` |
| `VERSION` | e.g., `1.20.1` (must match mods) |
| `FORGE_VERSION` | Usually auto-detected |
| `MEMORY` | `4G` minimum |

### Common Variables
| Variable | Default | Description |
|---|---|---|
| `EULA` | — | Must be `"TRUE"` |
| `MAX_PLAYERS` | `20` | Concurrent player limit |
| `MOTD` | none | Server browser message |
| `OPS` | none | Comma-separated operator usernames |

### Twingate Connector
| Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Your network address |
| `TWINGATE_ACCESS_TOKEN` | From Admin Console |
| `TWINGATE_REFRESH_TOKEN` | From Admin Console |

## Gotchas
- **CurseForge API key dollar signs**: Keys start with `$2a$10$`; escape every `$` as `$$` in `docker-compose.yml` or key is silently corrupted → misleading "forbidden or rate-limit" error
- **Mod version mismatch**: Server rejects clients with missing/wrong mod versions — all players need identical mod files and versions
- **`network_mode: host`** only works on native Linux; use bridge network for cross-platform compatibility
- **RAM overhead**: A `6G` heap uses 7+ GB total; JVM + Forge add significant overhead
- **Some CurseForge mods** are marked "not allowed for third-party distribution" — must be downloaded manually to `./data/mods/`
- Mods must match both Minecraft `VERSION` and Forge version

## Related Docs
- [Vanilla Minecraft Guide](https://www.twingate.com/
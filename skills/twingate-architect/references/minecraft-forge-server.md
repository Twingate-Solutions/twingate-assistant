# Modded Minecraft Server (Forge) with Twingate

## Summary
Deploy a private Forge modded Minecraft server using Docker Compose with a Twingate Connector for secure private access. Supports both CurseForge modpack (recommended) and manual mod installation. Players connect via Twingate Client using the server's private IP with no port forwarding required.

## Key Information
- Uses `itzg/minecraft-server` Docker image with Forge support
- Server pinned to `172.30.0.10` on isolated bridge network (`172.30.0.0/24`)
- No host port published; Connector reaches server directly over Docker bridge network
- All players must have identical mods and versions, or connection is rejected
- First startup with `AUTO_CURSEFORGE` downloads all mods; expect 10+ minutes on slow connections

## Prerequisites
- Machine: 4+ GB RAM, 2+ CPU cores, 20+ GB disk (6-8 GB RAM for large modpacks)
- Docker Engine + Docker Compose installed
- Twingate account with Admin Console access
- CurseForge API key (free, from `console.curseforge.com`) — Option A only

## Step-by-Step

1. Create Remote Network and Connector tokens (follow vanilla Minecraft guide Step 1)
2. Create project directory; write `docker-compose.yml` (Option A or B)
3. Run `docker compose up -d`; wait for `Done (Xs)! For help, type "help"` in logs
4. Verify Connector shows `Connected` in Admin Console
5. Add Resource: Address `172.30.0.10`, TCP port `25565`
6. Grant access to player Group
7. Players install Twingate Client + same mods; connect to `172.30.0.10` in Minecraft

## Configuration Values

### CurseForge Modpack (Option A)
| Variable | Description |
|---|---|
| `TYPE` | `AUTO_CURSEFORGE` |
| `CF_PAGE_URL` | Full CurseForge modpack page URL |
| `CF_API_KEY` | CurseForge API key (escape `$` as `$$`) |
| `CF_SLUG` | Alternative to `CF_PAGE_URL` |
| `CF_FILE_ID` | Pin specific modpack version |

### Manual Mods (Option B)
| Variable | Value |
|---|---|
| `TYPE` | `FORGE` |
| `VERSION` | e.g., `1.20.1` |
| `FORGE_VERSION` | Usually auto-detected |

### Common Variables
| Variable | Default | Description |
|---|---|---|
| `EULA` | — | Must be `"TRUE"` |
| `MEMORY` | `1G` | Set `4G`–`8G` for modded |
| `MAX_PLAYERS` | `20` | Concurrent player limit |
| `OPS` | — | Comma-separated operator usernames |

### Twingate Connector
- `TWINGATE_NETWORK`
- `TWINGATE_ACCESS_TOKEN`
- `TWINGATE_REFRESH_TOKEN`

## Gotchas
- **CurseForge API key dollar signs**: Keys start with `$2a$10$`; escape every `$` as `$$` in `docker-compose.yml` or it silently corrupts — server fails with misleading "forbidden/rate-limited" error
- **Mod version mismatch**: Players see "Mod Rejections" screen; both sides need identical `.jar` files and versions
- **`network_mode: host`**: Only works on native Linux — breaks on Docker Desktop for macOS/Windows; use bridge network instead
- **OOM crashes**: Increase `MEMORY`; JVM+Forge overhead means a `6G` heap uses 7+ GB actual RAM
- **Third-party distribution restriction**: Some CurseForge mods can't be auto-downloaded; place them manually in `./data/mods/`
- **Slow startup is normal**: Large modpacks (200+ mods) take 3-5 minutes; first run with `AUTO_CURSEFORGE` longer

## Related Docs
- [Vanilla Java Minecraft Guide](https://www.twingate.com/
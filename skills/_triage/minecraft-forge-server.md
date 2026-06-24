<!-- triage: unassigned URL: https://www.twingate.com/docs/minecraft-forge-server -->

# Modded Minecraft Server (Forge) with Twingate

## Summary
Deploy a private Forge modded Minecraft server using Docker Compose with a Twingate Connector, keeping it off the public internet. Supports CurseForge modpacks (recommended) or manual mod installation. Players connect via Twingate Client using the server's private IP.

## Key Information
- Uses `itzg/minecraft-server` Docker image with Forge support
- Server pinned to `172.30.0.10` on internal bridge network (`172.30.0.0/24`)
- No host ports published; Connector accesses server directly over Docker bridge network
- Works on Linux, macOS, and Windows (unlike `network_mode: host`)
- All players must have identical mods/versions; server rejects mismatched clients

## Prerequisites
- Machine: 4 GB RAM minimum (6-8 GB for large modpacks), 2 CPU cores, 20 GB disk
- Docker Engine + Docker Compose installed
- Twingate account with Admin Console access
- CurseForge API key (free at `console.curseforge.com`) if using modpacks
- Twingate Connector tokens (from Remote Network setup)

## Step-by-Step

1. **Create Remote Network & Connector tokens** — Follow vanilla Minecraft guide Step 1
2. **Deploy server** — Create `docker-compose.yml`, run `docker compose up -d`
3. **Add Resource** — Address: `172.30.0.10`, Protocol: TCP port `25565`
4. **Grant access** — Assign Group to Resource in Admin Console
5. **Connect players** — Install Twingate Client + matching mods; connect to `172.30.0.10`

## Configuration Values

### CurseForge Modpack (Option A)
| Variable | Description |
|----------|-------------|
| `TYPE` | `AUTO_CURSEFORGE` |
| `CF_PAGE_URL` | Full CurseForge modpack URL |
| `CF_API_KEY` | CurseForge API key (**escape `$` as `$$`**) |
| `CF_SLUG` | Alternative to `CF_PAGE_URL` |
| `CF_FILE_ID` | Pin specific modpack version |

### Manual Mods (Option B)
| Variable | Value |
|----------|-------|
| `TYPE` | `FORGE` |
| `VERSION` | e.g., `1.20.1` |

### Common Variables
| Variable | Default | Notes |
|----------|---------|-------|
| `MEMORY` | `1G` | Set `4G`–`8G` for modded |
| `MAX_PLAYERS` | `20` | — |
| `EULA` | — | Must be `"TRUE"` |
| `OPS` | — | Comma-separated operator usernames |

## Gotchas
- **CurseForge API key dollar signs**: Keys starting with `$2a$10$` must have every `$` escaped as `$$` in `docker-compose.yml`; unescaped keys cause silent corruption with a misleading "forbidden/rate-limit" error
- **RAM overhead**: JVM + Forge add overhead; a `6G` heap may use 7+ GB total; Connector adds <256 MB
- **First startup time**: `AUTO_CURSEFORGE` downloads all mods — can take 10+ minutes on slow connections
- **Mod version matching**: Both mod files AND versions must be identical on client and server; mismatch shows "Mod rejections" screen
- **Some CurseForge mods** block third-party distribution; must be downloaded manually to `./data/mods/`
- **Forge startup is slow**: Large modpacks (200+ mods) take 3–5 minutes; wait for `Done! For help, type "help"` in logs

## Related Docs
- [Vanilla Minecraft guide](https://www.twingate.com/docs/minecraft)
- [Bedrock Edition guide](https://www.twingate.com/docs/minecraft-bedrock)
- [itzg/minecraft-server Forge docs](https://docker-minecraft-server.readthedocs.io/)
- [Twingate Security Policies](https
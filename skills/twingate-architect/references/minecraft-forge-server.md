---
source: https://www.twingate.com/docs/minecraft-forge-server
type: docs
fetched: 2026-08-05
source_version: ad484d120f340411296c78927685b211097f17d8da1d33ca91678158c9999449
---

# Modded Minecraft Server (Forge) with Twingate

## Summary
Deploy a private Forge modded Minecraft server using Docker Compose with a Twingate Connector for secure access. Supports CurseForge modpack auto-install or manual mod placement. Players connect via Twingate Client using the server's private IP with no public port forwarding.

## Key Information
- Uses `itzg/minecraft-server` Docker image with Forge support
- Server pinned to `172.30.0.10` on internal bridge network `172.30.0.0/24`
- Port 25565 TCP — no host port published
- CurseForge API key required for modpack auto-install (free at console.curseforge.com)
- All players must have identical mods + versions; server rejects mismatches
- First startup: 2–5 min (manual mods), 10+ min (CurseForge download)

## Prerequisites
- Host: 4 GB RAM min (6–8 GB for large packs), 2 CPU cores, 20 GB disk
- Docker Engine + Docker Compose installed
- Twingate account with Admin Console access
- CurseForge API key (Option A only)
- Connector tokens from Twingate Admin Console

## Step-by-Step

1. Create Remote Network + generate Connector tokens (follow vanilla Minecraft guide Step 1)
2. Create project directory: `mkdir -p ~/minecraft-forge && cd ~/minecraft-forge`
3. Create `docker-compose.yml` (see Configuration Values below)
4. Start: `docker compose up -d`
5. Monitor: `docker compose logs minecraft -f` — wait for `Done (...s)! For help, type "help"`
6. Verify Connector in Admin Console: Controller + Relay both show **Connected**
7. Add Resource: Address `172.30.0.10`, TCP port `25565`
8. Assign Resource to player Group
9. Players install Twingate Client + same mods, connect to `172.30.0.10`

## Configuration Values

### Option A — CurseForge Modpack
```yaml
TYPE: "AUTO_CURSEFORGE"
CF_PAGE_URL: "https://www.curseforge.com/minecraft/modpacks/<slug>"
CF_API_KEY: "<YOUR_API_KEY>"   # escape $ as $$ (see Gotchas)
MEMORY: "6G"
```

### Option B — Manual Mods
```yaml
TYPE: "FORGE"
VERSION: "1.20.1"
MEMORY: "4G"
```
Place `.jar` files in `./data/mods/`

### General Variables
| Variable | Default | Description |
|---|---|---|
| `EULA` | — | Must be `"TRUE"` |
| `MEMORY` | `1G` | JVM heap; set 4–8G for modded |
| `MAX_PLAYERS` | `20` | Concurrent player limit |
| `MOTD` | none | Server browser message |
| `OPS` | none | Comma-separated operator usernames |
| `CF_FILE_ID` | — | Pin specific modpack version |
| `FORGE_VERSION` | auto | Specific Forge build |

### Twingate Connector
```yaml
TWINGATE_NETWORK: "<network>.twingate.com"
TWINGATE_ACCESS_TOKEN: "<token>"
TWINGATE_REFRESH_TOKEN: "<token>"
```

## Gotchas
- **`$` in CurseForge API keys**: Keys start with `$2a$10$...` — escape every `$` as `$$` in `docker-compose.yml` or the key is silently corrupted; error appears as "Access forbidden" not key error
- **`network_mode: host`** only works on native Linux; bridge network used here works cross-platform
- **JVM overhead**: A `6G` heap uses 7+ GB total RAM in practice
- **Mod version mismatch**: Players see "Mod rejections" screen; both mod files AND versions must match exactly
- **Some CurseForge mods** block third-party distribution — must download manually to `./data/mods/`
- **`EULA:
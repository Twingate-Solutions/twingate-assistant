---
source: https://www.twingate.com/docs/minecraft-forge-server
type: docs
fetched: 2026-08-14
source_version: 72bc3c29c104a2863a7c70ba3c01730918384a81881f119d4a9b4bd592b0238b
---

# Modded Minecraft Server (Forge) with Twingate

## Summary
Deploy a private Forge modded Minecraft server using Docker Compose with a Twingate Connector sidecar. Players connect via Twingate Client to a private IP, keeping the server off the public internet. Supports both CurseForge modpack auto-install and manual mod placement.

## Key Information
- Uses `itzg/minecraft-server` Docker image with `TYPE: AUTO_CURSEFORGE` or `TYPE: FORGE`
- Server pinned to `172.30.0.10` on private bridge network `172.30.0.0/24`
- No host ports published; Connector reaches server directly over Docker bridge
- All players must have identical mods (same files, same versions) as the server
- CurseForge modpacks auto-sync client/server mod lists via launcher

## Prerequisites
- Host: 4+ GB RAM (6-8 GB for large modpacks), 2 CPU cores, 20 GB disk
- Docker Engine + Docker Compose installed
- Twingate account with Admin Console access
- CurseForge API key (free, from `console.curseforge.com`) — Option A only
- Connector tokens from Twingate Admin Console

## Step-by-Step

1. **Create Remote Network & Connector tokens** — follow vanilla Minecraft guide Step 1
2. **Deploy server + Connector** — create `docker-compose.yml` (see configs below), run `docker compose up -d`
3. **Add Resource in Admin Console** — Address: `172.30.0.10`, TCP port `25565`
4. **Grant access** — assign Group to Resource
5. **Players install Twingate Client** + same modpack/mods, connect to `172.30.0.10` in-game

## Configuration Values

### Option A: CurseForge Modpack
| Variable | Value |
|---|---|
| `TYPE` | `AUTO_CURSEFORGE` |
| `CF_PAGE_URL` | Full modpack URL (e.g., `https://www.curseforge.com/minecraft/modpacks/all-the-mods-10`) |
| `CF_API_KEY` | Your CurseForge API key |
| `CF_FILE_ID` | (Optional) Pin specific modpack version |
| `MEMORY` | `6G` (adjust per modpack size) |

### Option B: Manual Mods
| Variable | Value |
|---|---|
| `TYPE` | `FORGE` |
| `VERSION` | e.g., `1.20.1` |
| `FORGE_VERSION` | (Optional) specific Forge build |
| `MEMORY` | `4G` minimum |

### Twingate Connector
| Variable | Value |
|---|---|
| `TWINGATE_NETWORK` | Your network subdomain |
| `TWINGATE_ACCESS_TOKEN` | From Admin Console |
| `TWINGATE_REFRESH_TOKEN` | From Admin Console |

## Gotchas
- **Dollar sign escaping**: CurseForge API keys start with `$2a$10$`. Escape every `$` as `$$` in `docker-compose.yml` or the key is silently corrupted. Error manifests as a misleading "forbidden/rate-limit" API error.
- **Mod version matching**: Client and server must have identical mod files/versions. Mismatch shows "Mod rejections" screen listing differences.
- **Startup time**: First launch takes 2-5 minutes (Forge install); CurseForge modpacks add 10+ minutes for downloads on slow connections.
- **RAM overhead**: JVM + Forge use ~1 GB above heap size (e.g., `6G` heap → ~7 GB actual). Connector adds <256 MB.
- **`network_mode: host`**: Only works on native Linux — use bridge network for macOS/Windows Docker Desktop compatibility.
- **Manual mods directory**: May not exist after first start; create with `mkdir -p ./data/mods` before copying jars.
- **Third-party distribution restrictions**: Some CurseForge mods block API download; must be manually placed in `./data/mods/`.

## Related Docs
- [Vanilla
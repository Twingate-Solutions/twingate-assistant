---
source: https://www.twingate.com/docs/minecraft-forge-server
type: docs
fetched: 2026-11-22
source_version: f8768df6bc4ee451ea7072c0bfe8b0c68e14c898cbfcc7d132df593748100d78
trust: official
---

# Modded Minecraft Server (Forge) with Twingate

## Summary
Guide to hosting a private Forge-modded Minecraft server using Docker Compose, with a Twingate Connector on the same bridge network so players reach the server at a private IP (`172.30.0.10`) through the Twingate Client. No ports are published to the host or the public internet. Works on Linux, macOS, and Windows.

## Key Information
- Two server setup paths: **Option A** CurseForge modpack (recommended, `TYPE=AUTO_CURSEFORGE`) or **Option B** manual mods (`TYPE=FORGE`).
- Server image: `itzg/minecraft-server:latest`. Connector image: `twingate/connector:1`.
- Both containers share the `minecraft-net` bridge (subnet `172.30.0.0/24`). The server is pinned to `172.30.0.10`, with no host port published.
- Avoid `network_mode: host`. It only works on native Linux and breaks on Docker Desktop for macOS and Windows.
- Every player must have identical mods and versions on the client, or they get a "Mod rejections" screen.
- First startup takes 2-5 minutes, and 10+ minutes for a large modpack on a slow connection.

## Prerequisites
- 4 GB RAM minimum, 2 CPU cores, 20 GB disk. Large packs (200+ mods) need 6-8 GB. The JVM uses more than the heap, so a `6G` heap can use 7 GB or more. The Connector adds under 256 MB.
- Docker Engine and Docker Compose.
- A Twingate account with Admin Console access.
- Terminal access.
- For Option A: a free CurseForge API key from console.curseforge.com.

## Step-by-Step
1. Create a Remote Network and generate Connector tokens (Step 1 of the vanilla Minecraft guide).
2. Create `~/minecraft-forge` and a `docker-compose.yml` with a `minecraft` service and a `twingate-connector` service on `minecraft-net`.
   - Option A: set `CF_PAGE_URL`, `CF_API_KEY`, and `MEMORY`.
   - Option B: set `VERSION` and `MEMORY`. Run `docker compose up -d && sleep 30 && docker compose down` once, then `mkdir -p ./data/mods` and copy the `.jar` files into it.
3. Run `docker compose up -d`, then `docker compose logs minecraft -f`. Wait for `For help, type "help"`.
4. In the Admin Console, verify the Connector shows Controller and Relay as Connected.
5. Add a Resource: name `Forge Server`, address `172.30.0.10`, protocol TCP port `25565`. Grant access to a Group.
6. Players install the Twingate Client, install matching mods, then add `172.30.0.10` in Multiplayer.
   - Modpack: use the CurseForge App, Prism Launcher, or ATLauncher.
   - Manual: use the Forge installer (Install client) and copy the same mods into the client `mods/` folder.

## Configuration Values
- Connector: `TWINGATE_NETWORK`, `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`
- Server: `EULA` ("TRUE" means agreeing to the Minecraft EULA), `TYPE`, `VERSION` (default LATEST; pin to match mods, e.g. `1.20.1`), `FORGE_VERSION` (auto), `MEMORY` (default 1G; use 4G-8G), `MAX_PLAYERS` (default 20), `MOTD`, `OPS`
- CurseForge: `CF_PAGE_URL`, `CF_SLUG` (alternative to `CF_PAGE_URL`), `CF_API_KEY` (required), `CF_FILE_ID` (pins a modpack version)
- After config changes: `docker compose down && docker compose up -d`

## Gotchas
- **Escape `$` as `$$` in `CF_API_KEY`.** Keys start with `$2a$10$`, and Docker Compose treats `$` as a variable reference. An unescaped key causes a misleading "Access to https://api.curseforge.com is forbidden or rate-limit has been exceeded" error. Example: `"$$2a$$10$$AbCdEf..."`.
- Mixing Minecraft and Forge versions is the most common cause of startup crashes.
- Some mods are marked "not allowed for third-party distribution". The image logs these, and you must download them manually into `./data/mods/`.
- On an out-of-memory crash (`java.lang.OutOfMemoryError`), raise `MEMORY` and make sure the host has that much RAM free.
- Check `./data/logs/latest.log` for crashes and mod conflicts.
- If the Connector shows offline, verify the tokens, outbound internet access, and `docker compose logs twingate-connector`.

## Related Docs
- Vanilla Minecraft guide (https://www.twingate.com/docs/minecraft-server)
- Linux Forge version (https://www.twingate.com/docs/minecraft-forge-server-linux)
- Bedrock guide (https://www.twingate.com/docs/minecraft-bedrock-server)
- All Minecraft guides (https://www.twingate.com/docs/minecraft-guides)
- Resources (https://www.twingate.com/docs/resources)
- Security Policies (https://www.twingate.com/docs/security-policies)
- itzg Forge/CurseForge docs (https://docker-minecraft-server.readthedocs.io/en/latest/types-and-platforms/mod-platforms/auto-curseforge/)
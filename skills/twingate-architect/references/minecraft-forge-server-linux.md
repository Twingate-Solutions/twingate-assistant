---
source: https://www.twingate.com/docs/minecraft-forge-server-linux
type: docs
fetched: 2026-08-14
source_version: e76fcaf91c6821bc30b27eb3858e6f698f8d48ad3753e1794756b35e84fd95a1
---

# Modded Minecraft Forge Server with Twingate (Linux)

## Summary
Sets up a private Forge modded Minecraft server on bare-metal Linux with Twingate for secure remote access. Players connect via Twingate Client using the server's private IP—no port forwarding required. Unlike the Docker guide, this approach requires manual Forge installation and mod management.

## Key Information
- Forge installer creates `run.sh` and `user_jvm_args.txt`; edit the latter for JVM memory settings
- All players must have identical mods (same files, same versions) or connection is rejected
- Twingate Connector installs alongside Forge on same host; adds <256 MB RAM overhead
- First startup takes 2–5 minutes; large modpacks (200+ mods) can take up to 10 minutes
- Server directory: `/opt/minecraft-forge/server/`; runs as dedicated `minecraft` system user

## Prerequisites
- Linux machine: Ubuntu 22.04/24.04 or Debian 12; ≥4 GB RAM, ≥2 CPU cores, ≥20 GB disk
- Java 17 (Minecraft 1.20.x) or Java 21 (Minecraft 1.21+)
- Twingate account with Admin Console access
- SSH/terminal access to server

## Step-by-Step

1. Create Remote Network and generate Connector tokens (see vanilla guide Step 1)
2. Create system user: `sudo useradd -r -m -d /opt/minecraft-forge -s /bin/bash minecraft`
3. Install Java: `sudo apt install -y openjdk-17-jre-headless` (or `openjdk-21-jre-headless`)
4. Download Forge installer from `files.minecraftforge.net`, run with `--installServer`
5. Accept EULA: `echo "eula=true" > eula.txt`
6. Add mod `.jar` files to `/opt/minecraft-forge/server/mods/`
7. Set memory in `user_jvm_args.txt`: `-Xmx4G -Xms2G`
8. Create systemd service at `/etc/systemd/system/minecraft-forge.service`
9. `sudo systemctl daemon-reload && sudo systemctl enable --now minecraft-forge`
10. Install Twingate Connector via setup script
11. Add Resource in Admin Console: TCP port `25565`, server's private IP
12. Players install matching mods + Twingate Client, connect via private IP

## Configuration Values

| File | Setting | Default/Example |
|------|---------|-----------------|
| `server.properties` | `server-port` | `25565` |
| `server.properties` | `max-players` | `20` |
| `server.properties` | `online-mode` | `true` |
| `server.properties` | `view-distance` | `10` |
| `user_jvm_args.txt` | heap size | `-Xmx4G -Xms2G` |

**Connector env vars:** `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`, `TWINGATE_NETWORK`

**Client mod paths:**
- Windows: `%appdata%\.minecraft\mods\`
- macOS: `~/Library/Application Support/minecraft/mods/`
- Linux: `~/.minecraft/mods/`

## Gotchas
- Mod version mismatch → "Mod Rejections" screen; filenames must be identical on server and client
- `run.sh` may not be executable after install: `sudo chmod +x run.sh`
- `Unsupported class file major version` = wrong Java version installed
- `OutOfMemoryError` on startup → increase `-Xmx` in `user_jvm_args.txt` (6–8G for large packs)
- Do NOT edit `run.sh` for memory; use `user_jvm_args.txt`
- CurseForge auto-install is Docker-only; manual mod management required here

## Related Docs
- [Vanilla Java guide](https://www.twingate.com/docs/minecraft-java-server-linux)
- [Bedrock guide](https://www.twin
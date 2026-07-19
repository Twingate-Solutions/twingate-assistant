# Modded Minecraft Server (Forge) with Twingate (Linux)

## Summary
Guide for hosting a private Forge modded Minecraft server on bare-metal Linux with Twingate for secure access. Covers native Forge installation, systemd service setup, and Twingate Connector deployment. Players must have identical mods installed client-side to connect.

## Key Information
- Native Linux installation (no Docker); no CurseForge auto-install (use Docker guide for that)
- Twingate setup is identical to vanilla Minecraft — Connector on same host, Resource on port 25565
- All players must have matching mod `.jar` files and versions or connections are rejected
- Forge startup takes 2–5 minutes; large modpacks (200+ mods) up to 5+ minutes

## Prerequisites
- Linux machine: Ubuntu 22.04/24.04 or Debian 12; min 4 GB RAM, 2 CPU cores, 20 GB disk
- Java 17 (Minecraft 1.20.x) or Java 21 (Minecraft 1.21+)
- Twingate account with Admin Console access
- SSH/terminal access to the host

## Step-by-Step

1. **Create Remote Network & Connector tokens** — Follow vanilla Minecraft guide Step 1
2. **Create server user**: `sudo useradd -r -m -d /opt/minecraft-forge -s /bin/bash minecraft`
3. **Install Java**: `sudo apt install -y openjdk-17-jre-headless` (or `openjdk-21` for 1.21+)
4. **Download & run Forge installer** from `files.minecraftforge.net` with `--installServer`
5. **Accept EULA**: `echo "eula=true" > /opt/minecraft-forge/server/eula.txt`
6. **Add mods**: Copy `.jar` files to `/opt/minecraft-forge/server/mods/`
7. **Set memory**: Edit `user_jvm_args.txt` (e.g., `-Xmx4G -Xms2G`)
8. **Create systemd service** at `/etc/systemd/system/minecraft-forge.service`
9. **Start server**: `sudo systemctl enable --now minecraft-forge`; watch logs for `For help, type "help"`
10. **Install Twingate Connector** via setup script with tokens
11. **Add Resource** in Admin Console: private IP, TCP port 25565
12. **Players install same mods + Twingate Client**, connect via private IP

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Server port | `25565` (TCP) |
| Server directory | `/opt/minecraft-forge/server` |
| JVM args file | `user_jvm_args.txt` |
| Default memory | `-Xmx4G -Xms2G`; large packs: `-Xmx6G` or `-Xmx8G` |
| Mod directory | `/opt/minecraft-forge/server/mods/` |
| Mod config directory | `/opt/minecraft-forge/server/config/` |
| Systemd service | `minecraft-forge` |
| Server user | `minecraft` |

**Connector env vars**: `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`, `TWINGATE_NETWORK`

## Gotchas
- Edit `user_jvm_args.txt` for memory — do NOT modify `run.sh` directly
- `run.sh` may not be executable after install: `sudo chmod +x run.sh`
- `Unsupported class file major version` = wrong Java version
- `OutOfMemoryError` = increase `-Xmx` in `user_jvm_args.txt`
- Mod version mismatches show as "Mod rejections" screen on client
- First-world-generation startup is significantly slower than subsequent starts

## Related Docs
- [Vanilla Minecraft Guide](https://www.twingate.com/docs/minecraft-java-server-linux)
- [Forge Docker Guide](https://www.twingate.com/docs/minecraft-forge-server-docker)
- [Bedrock Edition Guide](https://www.twin
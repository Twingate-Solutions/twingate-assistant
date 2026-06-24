<!-- triage: unassigned URL: https://www.twingate.com/docs/minecraft-forge-server-linux -->

# Modded Minecraft Server (Forge) with Twingate (Linux)

## Summary
Hosts a private Forge modded Minecraft server on bare-metal Linux with Twingate for secure access. Installs a native Twingate Connector alongside the Forge server; players connect via private IP without port forwarding. All players must have identical mods and versions installed client-side.

## Key Information
- Native Linux installation (no Docker); mods added manually
- Docker guide provides automated CurseForge modpack install; this guide does not
- Forge server runs on port **25565** (TCP)
- Connector adds <256 MB RAM overhead
- Forge startup takes 2–5 minutes on first launch; large packs (200+ mods) up to 5 minutes

## Prerequisites
- Linux machine: 4+ GB RAM, 2+ CPU cores, 20+ GB disk (Ubuntu 22.04/24.04 or Debian 12)
- Java 17 for Minecraft 1.20.x; Java 21 for Minecraft 1.21+
- Twingate account with Admin Console access
- SSH/terminal access

## Step-by-Step

1. **Create Remote Network & Connector tokens** — follow Step 1 of vanilla Minecraft guide
2. **Create server user**: `sudo useradd -r -m -d /opt/minecraft-forge -s /bin/bash minecraft`
3. **Install Java**: `sudo apt install -y openjdk-17-jre-headless` (or `openjdk-21-jre-headless`)
4. **Download Forge installer** from `files.minecraftforge.net`, run with `--installServer`
5. **Accept EULA**: `echo "eula=true" > /opt/minecraft-forge/server/eula.txt`
6. **Add mods**: copy `.jar` files to `/opt/minecraft-forge/server/mods/`
7. **Set memory**: edit `user_jvm_args.txt` (e.g., `-Xmx4G -Xms2G`)
8. **Create systemd service** at `/etc/systemd/system/minecraft-forge.service`
9. **Start server**: `sudo systemctl enable --now minecraft-forge`; confirm ready via `journalctl -u minecraft-forge -f` (look for "For help, type help")
10. **Install Twingate Connector** via setup script with tokens
11. **Add Resource** in Admin Console: private IP, TCP port 25565
12. **Players install**: Twingate Client + matching Forge version + identical mod `.jar` files

## Configuration Values

| File | Setting | Example |
|------|---------|---------|
| `user_jvm_args.txt` | Memory | `-Xmx4G -Xms2G` (6–8G for large packs) |
| `server.properties` | `server-port` | `25565` |
| `server.properties` | `online-mode` | `true` |
| Connector env | `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`, `TWINGATE_NETWORK` | from Admin Console |

**Systemd service**: `ExecStart=/opt/minecraft-forge/server/run.sh --nogui`, `User=minecraft`

## Gotchas
- **Mod version mismatch** causes "Mod Rejections" on connect — filenames and versions must be identical on server and all clients
- Edit `user_jvm_args.txt` for memory, **not** `run.sh` directly
- `run.sh` may not be executable after install: `sudo chmod +x /opt/minecraft-forge/server/run.sh`
- Wrong Java version causes `Unsupported class file major version` crash
- `OutOfMemoryError` on startup = increase `-Xmx` in `user_jvm_args.txt`

## Related Docs
- [Vanilla Java Minecraft guide](https://www.twingate.com/docs/minecraft)
- [Bedrock Edition guide](https://www.twingate.com/docs/minecraft-bedrock)
- [Forge Docker guide](https://www.twingate.com/docs/minecraft-forge-server-docker)
- [T
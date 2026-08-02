# Modded Minecraft Server (Forge) with Twingate (Linux)

## Summary
Hosts a private Forge modded Minecraft server on bare-metal Linux with Twingate for secure access. Players connect via private IP through Twingate Client without port forwarding. All players must have identical mods installed client-side.

## Key Information
- Port: TCP 25565
- Forge server user: `minecraft` (system user at `/opt/minecraft-forge`)
- JVM args controlled via `user_jvm_args.txt`, not `run.sh`
- Twingate Connector runs natively alongside the Forge server
- Docker alternative offers automated CurseForge modpack installation; native does not

## Prerequisites
- Linux host (Ubuntu 22.04/24.04 or Debian 12), 4GB+ RAM, 2+ CPU cores, 20GB disk
- Java 17 (Minecraft 1.20.x) or Java 21 (Minecraft 1.21+)
- Twingate account with Admin Console access
- SSH/terminal access to host

## Step-by-Step

1. **Create Remote Network & Connector tokens** — follow vanilla Minecraft guide Step 1
2. **Create server user**: `sudo useradd -r -m -d /opt/minecraft-forge -s /bin/bash minecraft`
3. **Install Java**: `sudo apt install -y openjdk-17-jre-headless` (or `openjdk-21`)
4. **Download Forge installer** from `files.minecraftforge.net`, run with `--installServer`
5. **Accept EULA**: `echo "eula=true" > eula.txt`
6. **Add mods**: copy `.jar` files to `/opt/minecraft-forge/server/mods/`
7. **Set memory**: edit `user_jvm_args.txt` (e.g., `-Xmx4G -Xms2G`)
8. **Make executable**: `sudo chmod +x /opt/minecraft-forge/server/run.sh`
9. **Create systemd service** at `/etc/systemd/system/minecraft-forge.service`
10. **Start**: `sudo systemctl enable --now minecraft-forge`
11. **Install Twingate Connector** via setup script with tokens
12. **Add Resource** in Admin Console: private IP, TCP 25565
13. **Players**: install matching mods + Twingate Client, connect via private IP

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Server directory | `/opt/minecraft-forge/server` |
| Service name | `minecraft-forge` |
| Default port | `25565` |
| Memory config file | `user_jvm_args.txt` |
| Mod directory | `/opt/minecraft-forge/server/mods/` |
| Mod config directory | `/opt/minecraft-forge/server/config/` |
| `TWINGATE_ACCESS_TOKEN` | From Admin Console |
| `TWINGATE_REFRESH_TOKEN` | From Admin Console |
| `TWINGATE_NETWORK` | Your network name |

**RAM recommendations**: 4GB (small packs), 6-8GB (200+ mods)

## Gotchas
- **Mod version mismatch** = "Mod Rejections" on connect — server and all clients need identical `.jar` files
- First startup takes 2-5 minutes (3-5 min for large packs); >10 min indicates a hanging mod
- `OutOfMemoryError` on startup → increase `-Xmx` in `user_jvm_args.txt`
- `Unsupported class file major version` → wrong Java version installed
- Forge installer version in URL must match your mods' requirements exactly
- CurseForge auto-install only available in Docker version

## Related Docs
- [Vanilla Minecraft Guide](https://www.twingate.com/docs/minecraft)
- [Bedrock Edition Guide](https://www.twingate.com/docs/minecraft-bedrock)
- [Forge Docker Guide](https://www.twingate.com/docs/minecraft-forge-server-docker)
- [Twingate Resources Configuration](https://www.twingate.com/docs/resources)
- [
# Modded Minecraft Server (Forge) with Twingate (Linux)

## Summary
Guide for hosting a private Forge modded Minecraft server on bare-metal Linux with Twingate for secure access. Covers native Forge installation, systemd service setup, and Twingate Connector installation. Players must have matching mods installed client-side to connect.

## Key Information
- Native Linux install (no Docker); no automated CurseForge modpack installation (use Docker guide for that)
- Twingate Connector runs alongside Forge server on same host
- Players connect via private IP through Twingate Client—no port forwarding required
- All players must have identical mod `.jar` files and versions as the server

## Prerequisites
- Linux machine: Ubuntu 22.04/24.04 or Debian 12; min 4 GB RAM, 2 CPU cores, 20 GB disk
- Java 17 (Minecraft 1.20.x) or Java 21 (Minecraft 1.21+)
- Twingate account with Admin Console access
- SSH/terminal access to server

## Step-by-Step

1. **Create Remote Network & Connector tokens** — Follow vanilla Minecraft guide Step 1
2. **Create server user**: `sudo useradd -r -m -d /opt/minecraft-forge -s /bin/bash minecraft`
3. **Install Java**: `sudo apt install -y openjdk-17-jre-headless` (or `openjdk-21` for 1.21+)
4. **Download & run Forge installer** from `files.minecraftforge.net` with `--installServer` flag
5. **Accept EULA**: `echo "eula=true" > /opt/minecraft-forge/server/eula.txt`
6. **Add mods**: Copy `.jar` files to `/opt/minecraft-forge/server/mods/`
7. **Set memory**: Edit `user_jvm_args.txt` (e.g., `-Xmx4G -Xms2G`)
8. **Create systemd service** at `/etc/systemd/system/minecraft-forge.service`
9. **Start server**: `sudo systemctl enable --now minecraft-forge`
10. **Install Twingate Connector** via setup script with tokens
11. **Add Resource** in Admin Console: server private IP, TCP port 25565
12. **Players install Twingate Client + matching mods**, connect via private IP

## Configuration Values

| File | Key | Value |
|------|-----|-------|
| `server.properties` | `server-port` | `25565` |
| `server.properties` | `online-mode` | `true` |
| `server.properties` | `max-players` | `20` |
| `user_jvm_args.txt` | JVM flags | `-Xmx4G -Xms2G` |

**Connector install env vars:**
- `TWINGATE_ACCESS_TOKEN`
- `TWINGATE_REFRESH_TOKEN`
- `TWINGATE_NETWORK`

## Gotchas
- Forge startup: 2–5 min normal, 3–5 min for large packs (200+ mods); >10 min indicates error
- `run.sh` may not be executable after install—run `chmod +x` manually
- Edit `user_jvm_args.txt` for memory, **not** `run.sh` directly
- Large modpacks (200+ mods) need 6–8 GB RAM; check modpack description
- `Unsupported class file major version` = wrong Java version
- Mod config files live in `/opt/minecraft-forge/server/config/`

## Related Docs
- [Vanilla Java Minecraft Guide](https://www.twingate.com/docs/minecraft)
- [Bedrock Edition Guide](https://www.twingate.com/docs/minecraft-bedrock)
- [Forge Docker Guide](https://www.twingate.com/docs/minecraft-forge-server-docker)
- [Twingate Resources Configuration](https://www.twingate.com/docs/resources)
- [Security Policies](https://www.twingate.com/docs/security-policies)
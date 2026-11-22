---
source: https://www.twingate.com/docs/minecraft-forge-server-linux
type: docs
fetched: 2026-11-22
source_version: 3a52e14c9cf38b848450c531add14ce46d499e2ec6426f703a250b3884e9555e
trust: official
---

# Modded Minecraft Server (Forge) with Twingate (Linux)

## Summary
Guide to hosting a private Forge-modded Minecraft server on bare-metal Linux (no Docker) and exposing it only through Twingate. A native Twingate Connector runs on the same host, and players reach the server's private IP on TCP 25565 via the Twingate Client. Mods are added manually; CurseForge auto-install is only available in the Docker guide.

## Key Information
- Every player must have identical mods and versions on their client, or they get a "Mod rejections" screen.
- Twingate setup is identical to vanilla: one Resource, TCP 25565, no port forwarding.
- Tested on Ubuntu 22.04, Ubuntu 24.04, Debian 12.
- Server runs as a dedicated `minecraft` user under systemd (`minecraft-forge.service`).
- First Forge launch takes 2-5 minutes; large packs (200+ mods) can take 3-5 minutes.
- Connector adds under 256 MB RAM.

## Prerequisites
- Linux host: 4 GB RAM minimum, 2 CPU cores, 20 GB free disk. Large packs need 6-8 GB.
- Java 17 (Minecraft 1.20.x) or Java 21 (1.21+).
- Twingate account with Admin Console access.
- SSH/terminal access.

## Step-by-Step
1. **Remote Network and Connector tokens**: follow Step 1 of the vanilla Linux guide (https://www.twingate.com/docs/minecraft-server-linux#step-1-create-a-remote-network-and-generate-connector-tokens).
2. **Create user/dir**: `useradd -r -m -d /opt/minecraft-forge -s /bin/bash minecraft`; create `/opt/minecraft-forge/server` and chown it.
3. **Install Java**: `openjdk-17-jre-headless` or `openjdk-21-jre-headless` via apt; verify with `java -version`.
4. **Install Forge**: pick the version at files.minecraftforge.net (https://files.minecraftforge.net), download the installer jar, run `java -jar <installer> --installServer`, then delete the installer.
5. **Accept EULA**: write `eula=true` to `eula.txt`.
6. **Add mods**: copy jars into `/opt/minecraft-forge/server/mods/` and chown to `minecraft`.
7. **Configure** `server.properties` and `user_jvm_args.txt`; `chmod +x run.sh`.
8. **Create systemd service** with `ExecStart=/opt/minecraft-forge/server/run.sh --nogui`, `Restart=on-failure`; then `systemctl daemon-reload` and `systemctl enable --now minecraft-forge`.
9. **Watch logs**: `journalctl -u minecraft-forge -f` until `For help, type "help"` appears.
10. **Install Twingate Connector** using the setup script from binaries.twingate.com with the three env vars below. Check `systemctl status twingate-connector` shows `active (running)`, and in Admin Console confirm Controller and Relay show Connected.
11. **Create Resource**: get the IP with `hostname -I | awk '{print $1}'`. In Admin Console add Resource "Forge Server", address = private IP, protocol TCP 25565, then grant access to a Group.
12. **Players**: install the Twingate Client, install matching Forge and mods (manually or via a CurseForge-compatible launcher), add the server by private IP.

## Configuration Values
- Connector env vars: `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`, `TWINGATE_NETWORK`
- `user_jvm_args.txt`: `-Xmx4G -Xms2G` (raise to 6G/8G for big packs)
- `server.properties`: `server-port=25565`, `max-players`, `difficulty`, `gamemode`, `motd`, `online-mode=true`, `view-distance` (lower to reduce RAM)
- Mod configs: `/opt/minecraft-forge/server/config/`
- Logs: `/opt/minecraft-forge/server/logs/latest.log`

## Gotchas
- Edit `user_jvm_args.txt` for memory, not `run.sh`.
- `run.sh` may not be executable; fix with `chmod +x`.
- Mixed Minecraft/Forge/mod versions are the top cause of startup crashes.
- `OutOfMemoryError` means increase `-Xmx`.
- `Unsupported class file major version` means wrong Java version.
- Restart the service after changing properties, mods, or configs.
- Removing a mod requires players to remove it client-side too.
- Connector offline: verify tokens, outbound internet, and `journalctl -u twingate-connector -f`.

## Related Docs
- Minecraft guides index (https://www.twingate.com/docs/minecraft-guides)
- Vanilla Java guide (https://www.twingate.com/docs/minecraft-server)
- Bedrock guide (https://www.twingate.com/docs/minecraft-bedrock-server)
- Forge Docker guide (https://www.twingate.com/docs/minecraft-forge-server)
- Resources (https://www.twingate.com/docs/resources)
- Security Policies (https://www.twingate.com/docs/security-policies)
- Protect Your Home Lab (https://www.twingate.com/docs/homelab-step-by-step)
- Linux Client install guide (https://www.twingate.com/docs/linux)
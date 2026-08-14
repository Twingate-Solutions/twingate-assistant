---
source: https://www.twingate.com/docs/minecraft-server-linux
type: docs
fetched: 2026-08-14
source_version: 5a0ec180c5c4329f6ce4e9c37201ddf5e2f8650a0875f59742513eb0bf7729ee
---

# Minecraft Server with Twingate (Linux)

## Summary
Deploy a private Minecraft Java Edition server on bare-metal Linux using systemd and OpenJDK 21, secured via Twingate Connector instead of port forwarding. Players connect through the Twingate Client using the server's private IP, keeping port 25565 off the public internet entirely.

## Key Information
- Minecraft Java Edition uses TCP port 25565 only (no UDP needed)
- Twingate Connector creates outbound-only tunnel — no inbound firewall/router changes required
- Server binds to `0.0.0.0:25565` by default, accessible to Connector on same host without internet exposure
- Twingate Client must remain connected for entire play session
- Connector overhead: <256 MB RAM, negligible CPU

## Prerequisites
- Linux machine (Ubuntu 22.04/24.04 or Debian 12 tested): 2+ GB RAM, 2+ CPU cores, 10+ GB disk
- Java 21 (OpenJDK) — installed via `apt`
- Twingate account with Admin Console access
- SSH/terminal access with `sudo`

## Step-by-Step

**1. Twingate Setup**
- Admin Console → Remote Networks → Add Remote Network → Add Connector → Select Linux → Generate Tokens
- Copy Access Token and Refresh Token

**2. Server Setup**
```bash
sudo useradd -r -m -U -d /opt/minecraft -s /bin/bash minecraft
sudo mkdir -p /opt/minecraft/server
sudo chown -R minecraft:minecraft /opt/minecraft
sudo apt update && sudo apt install -y openjdk-21-jre-headless
sudo -u minecraft -s
cd /opt/minecraft/server
wget https://piston-data.mojang.com/v1/objects/[VERSION_HASH]/server.jar  # get URL from minecraft.net
echo "eula=true" > eula.txt
exit
```

**3. systemd Service** (`/etc/systemd/system/minecraft.service`):
```ini
[Unit]
Description=Minecraft Server
After=network.target
[Service]
Type=simple
User=minecraft
WorkingDirectory=/opt/minecraft/server
ExecStart=/usr/bin/java -Xmx2G -Xms1G -jar server.jar nogui
Restart=on-failure
RestartSec=10
[Install]
WantedBy=multi-user.target
```
```bash
sudo systemctl daemon-reload && sudo systemctl enable --now minecraft
```

**4. Install Connector**
```bash
curl "https://binaries.twingate.com/connector/setup.sh" | \
sudo TWINGATE_ACCESS_TOKEN="<TOKEN>" \
TWINGATE_REFRESH_TOKEN="<REFRESH>" \
TWINGATE_NETWORK="<NETWORK>" bash
```

**5. Add Resource** — Admin Console → Resources → Add Resource → TCP port 25565 → server private IP (`hostname -I | awk '{print $1}'`)

**6. Player Setup** — Install Twingate Client, sign in, connect, then add server IP in Minecraft Multiplayer

## Configuration Values

| Parameter | Value |
|-----------|-------|
| `server-port` | 25565 |
| `max-players` | 10 (default 20) |
| `difficulty` | `peaceful/easy/normal/hard` |
| `gamemode` | `survival/creative/adventure/spectator` |
| `-Xmx` / `-Xms` | 2G/1G (increase for mods: 4-8G) |

## Gotchas
- Download URL for `server.jar` changes each release — always get from [minecraft.net](https://minecraft.net/en-us/download/server)
- Each Connector needs unique tokens — never reuse token sets
- Heavy modpacks may need 6-8 GB RAM; adjust `-Xmx` in service file + `daemon-reload`
- Port conflict check: `sudo ss -tlnp | grep 25565`
- World data stored in `/opt/minecraft/server/` — back up regularly; deletion = data loss

## Troubleshooting Commands
```bash
sudo systemctl status minecraft
sudo journal
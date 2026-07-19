# Minecraft Server with Twingate (Linux)

## Summary
Hosts a vanilla Minecraft Java Edition server on bare-metal Linux using systemd, secured via Twingate instead of port forwarding. The Connector creates an outbound-only encrypted tunnel so port 25565 is never exposed to the internet. Players install the Twingate Client and connect using the server's private IP.

## Key Information
- Covers native Linux installation (no Docker); separate guides exist for Bedrock, Forge, and Docker versions
- Architecture: Player → Twingate Client → Twingate Cloud → Connector → Minecraft Server (port 25565)
- No inbound firewall rules or router port forwarding required
- Minecraft Java Edition uses **TCP only** on port 25565 (Bedrock uses UDP 19132)
- Twingate Connector overhead: <256 MB RAM, negligible CPU

## Prerequisites
- Linux machine: Ubuntu 22.04/24.04 or Debian 12; ≥2 GB RAM, 2 CPU cores, 10 GB disk
- Java 21 (OpenJDK) — installed in Step 2
- Twingate account with Admin Console access
- SSH/terminal access with sudo privileges

## Step-by-Step

**Step 1: Twingate Setup**
1. Admin Console → Remote Networks → Add Remote Network → name it → Save
2. Click undeployed Connector → Select Linux → Generate Tokens
3. Copy Access Token and Refresh Token

**Step 2: Install Server**
```bash
# Create user/directory
sudo useradd -r -m -U -d /opt/minecraft -s /bin/bash minecraft
sudo mkdir -p /opt/minecraft/server
sudo chown -R minecraft:minecraft /opt/minecraft

# Install Java
sudo apt update && sudo apt install -y openjdk-21-jre-headless

# Download server JAR (get current URL from minecraft.net/en-us/download/server)
sudo -u minecraft -s
cd /opt/minecraft/server
wget https://piston-data.mojang.com/v1/objects/[VERSION_HASH]/server.jar
echo "eula=true" > eula.txt
exit

# Install Twingate Connector
curl "https://binaries.twingate.com/connector/setup.sh" | \
  sudo TWINGATE_ACCESS_TOKEN="<TOKEN>" \
  TWINGATE_REFRESH_TOKEN="<TOKEN>" \
  TWINGATE_NETWORK="<NETWORK>" bash
```

**Step 3: Add Resource**
- Admin Console → Resources → Add Resource
- Address: server's private IP (`hostname -I | awk '{print $1}'`)
- Protocol: TCP port 25565
- Grant access to desired Group

**Step 4: Player Setup**
- Install Twingate Client → sign in → connect
- Minecraft → Multiplayer → Add Server → enter private IP (port 25565 is default)

**Step 5: Access Control**
- Admin Console → Team → Add User (sends email invite)
- Create Group "Minecraft Players" → assign users → assign to Resource
- Remove from group to instantly revoke access

## Configuration Values

| Parameter | Value |
|-----------|-------|
| `server-port` | 25565 |
| `max-players` | 10 (default 20) |
| `-Xmx` / `-Xms` | 2G / 1G (increase for mods) |
| Connector env vars | `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`, `TWINGATE_NETWORK` |

**RAM sizing:** vanilla ≤10 players = 2 GB; heavy modpacks = 6–8 GB+

## Gotchas
- Server JAR URL changes with each Minecraft release — always get current URL from minecraft.net
- Each Connector requires its own unique token pair (never reuse)
- Twingate Client must remain connected for entire play session
- Crashes most commonly caused by insufficient memory — increase `-Xmx` in systemd service
- After editing `server.properties`, run `sudo systemctl restart minecraft`
- Run `sudo systemctl daemon-reload` after any systemd service file changes

## Troubleshooting Commands
```bash
sudo systemctl
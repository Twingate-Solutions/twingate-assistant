---
source: https://www.twingate.com/docs/minecraft-server-linux
type: docs
fetched: 2026-11-22
source_version: 4969e3e5f2be23424553720143a53bc886166b791befa2b6b890c5502bf8e192
trust: official
---

# Minecraft Server with Twingate (Linux)

## Summary
Guide to hosting a private vanilla Java Edition Minecraft server on bare-metal Linux (Java + systemd) with a natively installed Twingate Connector. Players reach the server's private IP through the Twingate Client, so no port forwarding or public exposure of port 25565 is needed.

## Key Information
- Architecture: Player (Twingate Client) → Twingate Cloud → Connector (outbound-only tunnel) → Minecraft server on TCP 25565.
- Java Edition uses TCP 25565 only. Bedrock uses UDP 19132 and is covered in a separate guide.
- The server binds to 0.0.0.0:25565 by default. This is reachable by the local Connector and not exposed to the internet if the router does not forward it.
- Access is controlled with Twingate Groups instead of Minecraft allowlists.
- Connector overhead: under 256 MB RAM.

## Prerequisites
- Linux host (Ubuntu 22.04/24.04 or Debian 12 tested): 2 GB RAM, 2 CPU cores, 10 GB disk.
- OpenJDK 21, installed in Step 2.
- Twingate account with Admin Console access.
- Terminal/SSH access with sudo.

## Step-by-Step
1. **Admin Console:** Remote Networks → Add Remote Network (e.g., On Premise) → add Connector → choose Linux → Generate Tokens. Copy the Access Token and Refresh Token.
2. **Server setup:**
   - Create user and directory: `sudo useradd -r -m -U -d /opt/minecraft -s /bin/bash minecraft`, then `sudo mkdir -p /opt/minecraft/server` and `sudo chown -R minecraft:minecraft /opt/minecraft`.
   - Install Java: `sudo apt install -y openjdk-21-jre-headless`.
   - As the minecraft user in `/opt/minecraft/server`, download server.jar from the official Minecraft download page (the URL changes each release).
   - Write `eula=true` to `eula.txt` (this accepts Mojang's EULA).
   - Create `server.properties`.
   - Create `/etc/systemd/system/minecraft.service` with `ExecStart=/usr/bin/java -Xmx2G -Xms1G -jar server.jar nogui`, `User=minecraft`, `Restart=on-failure`.
   - Run `sudo systemctl daemon-reload && sudo systemctl enable --now minecraft`.
   - Watch for "For help, type "help"" in `journalctl -u minecraft -f`.
3. **Connector:** Run the official installer from binaries.twingate.com with the three env vars below. The source shows a piped one-liner, so follow the Connector Linux deployment option in the Admin Console for the exact command. Verify with `systemctl status twingate-connector` and confirm Controller and Relay show Connected.
4. **Resource:** Find the private IP with `hostname -I | awk '{print $1}'`. Add a Resource with the name Minecraft Server, that IP as the address, and TCP 25565. Grant access to a Group.
5. **Players:** Install the Twingate Client, sign in to `yournetwork.twingate.com`, then in Minecraft go to Multiplayer → Add Server using the private IP.
6. **Access control:** Invite users under Team, create a "Minecraft Players" Group, assign it to the Resource, and remove Everyone.

## Configuration Values
- Connector env vars: `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`, `TWINGATE_NETWORK`.
- `server.properties`: server-port (25565), max-players, difficulty, gamemode, motd, view-distance (10), level-seed, white-list, pvp.
- JVM: `-Xmx`/`-Xms` in the systemd unit. Use 4 GB or more for mods, and 6-8 GB or more for heavy modpacks.

## Gotchas
- Each Connector needs its own unique token pair.
- Players must keep the Twingate Client connected during play.
- If you change the port, update the Twingate Resource to match.
- Crashes are usually caused by low memory, so raise `-Xmx` and restart.
- Back up `/opt/minecraft/server/`, since it holds the world data.
- Port conflict check: `sudo ss -tlnp | grep 25565`.
- Connector offline: check the tokens, outbound internet access, and `journalctl -u twingate-connector`.
- Revoking access: remove the user from the Group.

## Related Docs
- [All Minecraft guides](https://www.twingate.com/docs/minecraft-guides)
- [Bedrock](https://www.twingate.com/docs/minecraft-bedrock-server)
- [Forge (modded)](https://www.twingate.com/docs/minecraft-forge-server)
- [Docker version](https://www.twingate.com/docs/minecraft-server)
- [Resources](https://www.twingate.com/docs/resources)
- [Security Policies](https://www.twingate.com/docs/security-policies)
- [Deploy a second Connector](https://www.twingate.com/docs/deploy-connector-with-docker-compose)
- [Protect Your Home Lab](https://www.twingate.com/docs/homelab-step-by-step)
- [Linux Client install guide](https://www.twingate.com/docs/linux)
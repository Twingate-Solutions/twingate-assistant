# Minecraft Server with Twingate (Linux)

## Page Title
Minecraft Server with Twingate (Linux) — Vanilla Java Edition, Native Install

## Summary
Deploy a private Minecraft Java Edition server on bare-metal Linux using systemd and OpenJDK, secured via a Twingate Connector instead of port forwarding. Players authenticate through Twingate Client before traffic reaches the server, eliminating public exposure of port 25565. No router configuration or inbound firewall rules required.

## Key Information
- Vanilla Java Edition only; separate guides exist for Bedrock, Forge, and Docker
- Twingate Connector creates outbound-only encrypted tunnel — no inbound ports needed
- Server binds to `0.0.0.0:25565` by default but remains inaccessible without Twingate auth
- Twingate Client must remain connected for the entire Minecraft session
- Connector overhead: <256 MB RAM, negligible CPU

## Prerequisites
- Linux machine: Ubuntu 22.04/24.04 or Debian 12 (tested)
- Minimum: 2 GB RAM, 2 CPU cores, 10 GB disk (4+ GB RAM for mods)
- Java 21 (OpenJDK) — installed in Step 2
- Twingate account with Admin Console access
- SSH/terminal with `sudo` privileges

## Step-by-Step

1. **Admin Console**: Create Remote Network → Add Connector → Select Linux → Generate Tokens → copy Access Token and Refresh Token
2. **System user**: `sudo useradd -r -m -U -d /opt/minecraft -s /bin/bash minecraft`
3. **Install Java**: `sudo apt install -y openjdk-21-jre-headless`
4. **Download server JAR**: Get current URL from `minecraft.net/en-us/download/server`
5. **Accept EULA**: `echo "eula=true" > eula.txt`
6. **Create systemd service** at `/etc/systemd/system/minecraft.service`
7. **Start server**: `sudo systemctl daemon-reload && sudo systemctl enable --now minecraft`
8. **Install Connector**: One-line curl installer with tokens
9. **Add Resource**: Private IP, TCP port 25565, assign Group access
10. **Players**: Install Twingate Client → sign in → connect → add server IP in Minecraft Multiplayer

## Configuration Values

**systemd service (ExecStart):**
```
/usr/bin/java -Xmx2G -Xms1G -jar server.jar nogui
```

**Connector installer env vars:**
```
TWINGATE_ACCESS_TOKEN="<token>"
TWINGATE_REFRESH_TOKEN="<token>"
TWINGATE_NETWORK="<network-name>"
```

**Key `server.properties` values:**
| Property | Default | Notes |
|---|---|---|
| `server-port` | `25565` | TCP only (Java Edition) |
| `max-players` | `20` | |
| `difficulty` | `easy` | peaceful/easy/normal/hard |
| `white-list` | `false` | Use Twingate Groups instead |

## Gotchas
- Each Connector requires **unique** Access/Refresh token pair — do not reuse
- Java Edition uses **TCP 25565**; Bedrock uses UDP 19132 — different setup required
- Increase `-Xmx` for mods: heavy modpacks may need 6–8 GB
- World data lives in `/opt/minecraft/server/` — no built-in backup; manual backup required
- Server JAR download URL changes with each release — always get current link from minecraft.net
- `eula=true` constitutes agreement to Minecraft EULA

## Troubleshooting
| Issue | Fix |
|---|---|
| Players can't connect | Check Client shows "Connected"; verify Group assignment; check `systemctl status minecraft` |
| Server crashes | `journalctl -u minecraft -n 100`; increase `-Xmx` |
| Connector offline | Verify tokens; check outbound internet; `journalctl -u twingate-connector -n 50` |
| Port in use | `sudo ss -tlnp \| grep 25565` |
| Permission errors | `
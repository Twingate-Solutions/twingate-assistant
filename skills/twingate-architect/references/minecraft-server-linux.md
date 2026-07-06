# Minecraft Server with Twingate (Linux)

## Summary
Hosts a vanilla Minecraft Java Edition server on bare-metal Linux using Java and systemd, secured via Twingate instead of port forwarding. The Twingate Connector creates an outbound-only encrypted tunnel, eliminating public internet exposure of port 25565. Players connect using the server's private IP through the Twingate Client.

## Key Information
- No port forwarding or inbound firewall rules required
- Connector uses outbound-only tunnel to Twingate Cloud
- Java Edition only (TCP 25565); Bedrock uses UDP 19132 on different guide
- Connector overhead: <256 MB RAM, negligible CPU
- World data stored in `/opt/minecraft/server/` — back up regularly

## Prerequisites
- Linux machine: Ubuntu 22.04/24.04 or Debian 12 (tested)
- Minimum: 2 GB RAM, 2 CPU cores, 10 GB disk
- Java 21 (OpenJDK) — installed in Step 2
- Twingate account with Admin Console access
- SSH/terminal access with sudo privileges

## Step-by-Step

1. **Admin Console**: Create Remote Network → Add Connector → Select Linux → Generate Tokens → copy Access Token and Refresh Token
2. **System setup**: Create `minecraft` system user, install OpenJDK 21, download server JAR from minecraft.net, accept EULA (`eula=true`)
3. **systemd service**: Create `/etc/systemd/system/minecraft.service`, enable and start
4. **Install Connector**: Run one-line installer with tokens
5. **Create Resource**: Private IP, TCP port 25565, assign Group access
6. **Players**: Install Twingate Client, sign in, add server by private IP in Minecraft Multiplayer

## Configuration Values

| Parameter | Value |
|-----------|-------|
| `TWINGATE_ACCESS_TOKEN` | From Admin Console token generation |
| `TWINGATE_REFRESH_TOKEN` | From Admin Console token generation |
| `TWINGATE_NETWORK` | Your network name (e.g., `yournetwork`) |
| `-Xmx` / `-Xms` | `2G` / `1G` default; increase for mods |
| `server-port` | `25565` |
| `max-players` | `10` (configured) / `20` (default) |

**Connector install command:**
```bash
curl "https://binaries.twingate.com/connector/setup.sh" | \
sudo TWINGATE_ACCESS_TOKEN="<TOKEN>" \
TWINGATE_REFRESH_TOKEN="<TOKEN>" \
TWINGATE_NETWORK="<NETWORK>" bash
```

**Systemd ExecStart:**
```
/usr/bin/java -Xmx2G -Xms1G -jar server.jar nogui
```

## Gotchas
- Tokens are single-use per Connector — never reuse across Connectors
- Server JAR URL changes each release; get current link from minecraft.net
- Twingate Client must remain connected during entire play session
- Server binds to `0.0.0.0` but this does NOT expose to internet without port forwarding
- Heavy modpacks may need 6–8 GB RAM — adjust `-Xmx` accordingly
- After editing `server.properties` or service file, run `systemctl daemon-reload` before restart

## Troubleshooting
- **Can't connect**: Check Client shows "Connected", verify Resource assigned to player's Group
- **Crash on start**: Increase `-Xmx` value, check `journalctl -u minecraft -n 100`
- **Connector offline**: Verify tokens and outbound internet; check `journalctl -u twingate-connector -n 50`
- **Port in use**: `sudo ss -tlnp | grep 25565`

## Related Docs
- Bedrock Edition guide
- Forge (modded) guide
- Docker version guide
- Twingate Security Policies (MFA, device trust)
- Minecraft Wiki server.properties reference
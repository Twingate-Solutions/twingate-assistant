<!-- triage: unassigned URL: https://www.twingate.com/docs/minecraft-server-linux -->

# Minecraft Server with Twingate (Linux)

## Summary
Hosts a private Minecraft Java Edition server on bare-metal Linux using systemd, with Twingate replacing port forwarding. Players connect via Twingate Client using the server's private IP—no public ports exposed.

## Key Information
- Minecraft Java Edition only (TCP 25565); Bedrock uses UDP 19132 (separate guide)
- Twingate Connector creates outbound-only tunnel; router needs zero inbound rules
- Connector overhead: <256 MB RAM, negligible CPU
- Tested on Ubuntu 22.04, 24.04, Debian 12

## Prerequisites
- Linux machine: 2GB RAM min (4GB+ for mods), 2 CPU cores, 10GB disk
- Java 21 (OpenJDK): `sudo apt install -y openjdk-21-jre-headless`
- Twingate account with Admin Console access
- SSH/sudo access to host

## Step-by-Step

1. **Admin Console**: Create Remote Network → Add Connector → Generate Access + Refresh Tokens
2. **System user**: `sudo useradd -r -m -U -d /opt/minecraft -s /bin/bash minecraft`
3. **Download server JAR** from minecraft.net/en-us/download/server to `/opt/minecraft/server/`
4. **Accept EULA**: `echo "eula=true" > eula.txt`
5. **Create systemd service** at `/etc/systemd/system/minecraft.service`
6. **Start**: `sudo systemctl daemon-reload && sudo systemctl enable --now minecraft`
7. **Verify startup**: `sudo journalctl -u minecraft -f` — wait for `Done...! For help, type "help"`
8. **Install Connector**: one-line curl script with tokens
9. **Add Resource** in Admin Console: private IP, TCP port 25565
10. **Players**: Install Twingate Client, sign in, add server IP in Minecraft Multiplayer

## Configuration Values

**systemd service (`/etc/systemd/system/minecraft.service`)**:
```
ExecStart=/usr/bin/java -Xmx2G -Xms1G -jar server.jar nogui
User=minecraft
WorkingDirectory=/opt/minecraft/server
```

**Connector installer env vars**:
```
TWINGATE_ACCESS_TOKEN="<token>"
TWINGATE_REFRESH_TOKEN="<token>"
TWINGATE_NETWORK="<network-name>"
```

**Key `server.properties` values**:
| Property | Default | Notes |
|----------|---------|-------|
| `server-port` | `25565` | Must match Twingate Resource |
| `max-players` | `20` | |
| `-Xmx` flag | `2G` | Increase for mods (6-8G for heavy modpacks) |

## Gotchas
- Tokens are single-use per Connector; never reuse across Connectors
- Twingate Client must remain connected for entire play session
- Server JAR URL changes each release—get current link from minecraft.net
- Port 25565 binds to `0.0.0.0` by default but doesn't require firewall changes—it's only reachable via Twingate tunnel
- `-Xmx` must match available host RAM; crashes often caused by insufficient memory

## Troubleshooting Quick Reference
- Server crash → check `sudo journalctl -u minecraft -n 100`, increase `-Xmx`
- Connector offline → verify tokens and outbound internet; check `sudo journalctl -u twingate-connector -n 50`
- Port in use → `sudo ss -tlnp | grep 25565`
- Permission errors → `sudo chown -R minecraft:minecraft /opt/minecraft`

## Related Docs
- Bedrock Edition guide, Forge (modded) guide, Docker Compose version
- Twingate Security Policies (MFA/device trust)
- High availability: Deploy a Second Connector
- Minecraft Wiki server.properties reference
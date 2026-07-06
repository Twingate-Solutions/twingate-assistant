# Minecraft Bedrock Server with Twingate (Linux)

## Summary
Hosts a private Minecraft Bedrock Dedicated Server on Linux using Twingate to avoid public port exposure. Players connect via Twingate Client using the server's private IP instead of port forwarding UDP 19132. Supports Windows, iOS, Android, and ChromeOS players only (no console support).

## Key Information
- Server runs on UDP port **19132** (not TCP)
- Requires x86_64/AMD64 hardware — native binary won't run on ARM (use Docker guide for ARM)
- Twingate Connector opens outbound connections only; no inbound firewall rules needed
- Console players (Xbox, PlayStation, Switch) cannot use Twingate

## Prerequisites
- Linux machine: Ubuntu 22.04/24.04 or Debian 12, x86_64, 1GB+ RAM, 2 CPU cores, 10GB disk
- Twingate account with Admin Console access
- SSH/terminal access to Linux machine
- Packages: `curl`, `unzip`, `libcurl4`, `openssl`

## Step-by-Step

1. **Create Remote Network** in Admin Console → Remote Networks → Add Remote Network
2. **Generate Connector Tokens** → select Linux deployment → Generate Tokens → save Access Token + Refresh Token
3. **Create minecraft user**: `sudo useradd -r -m -d /opt/minecraft-bedrock -s /bin/bash minecraft`
4. **Download & extract** Bedrock server binary from [minecraft.net](https://minecraft.net) into `/opt/minecraft-bedrock/server/`
5. **Configure** `/opt/minecraft-bedrock/server/server.properties`
6. **Create systemd service** at `/etc/systemd/system/minecraft-bedrock.service` with `LD_LIBRARY_PATH=/opt/minecraft-bedrock/server`
7. **Start server**: `sudo systemctl enable --now minecraft-bedrock`
8. **Install Connector**:
   ```bash
   curl "https://binaries.twingate.com/connector/setup.sh" | \
   sudo TWINGATE_ACCESS_TOKEN="<token>" \
   TWINGATE_REFRESH_TOKEN="<token>" \
   TWINGATE_NETWORK="<network>" bash
   ```
9. **Add Resource** in Admin Console: Address = server private IP, Protocol = **UDP port 19132**
10. **Assign Group** access to the Resource
11. Players install Twingate Client, sign in, then add server IP in Minecraft → Servers tab

## Configuration Values

| Parameter | Value |
|-----------|-------|
| `TWINGATE_ACCESS_TOKEN` | From Admin Console |
| `TWINGATE_REFRESH_TOKEN` | From Admin Console |
| `TWINGATE_NETWORK` | `yournetwork.twingate.com` |
| `server-port` | `19132` (UDP) |
| `LD_LIBRARY_PATH` | `/opt/minecraft-bedrock/server` |

**Key `server.properties` fields:** `server-name`, `gamemode`, `difficulty`, `max-players`, `level-seed`, `online-mode`

## Gotchas
- **Must use UDP** for the Twingate Resource — TCP-only causes "Unable to connect to world" even if everything else is correct
- Token sets are unique per Connector — never reuse across Connectors
- Twingate Client must remain connected for entire play session
- ARM hardware requires Docker-based guide (uses box64 emulation)
- After editing `server.properties`, restart: `sudo systemctl restart minecraft-bedrock`

## Troubleshooting Commands
```bash
sudo journalctl -u minecraft-bedrock -n 100      # Server logs
sudo systemctl status twingate-connector          # Connector status
sudo ss -ulpn | grep 19132                        # Port conflicts
sudo chown -R minecraft:minecraft /opt/minecraft-bedrock  # Fix permissions
```

## Related Docs
- [Docker-based Bedrock Guide](https://www.twingate.com/docs) — for ARM or containerized deployments
- [Java Edition Guide](https://www.twingate.com/docs)
- Twingate Security Policies, Resources configuration, Deploy Second
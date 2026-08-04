# Minecraft Bedrock Server with Twingate (Linux)

## Summary
Guide for hosting a private Minecraft Bedrock Dedicated Server on bare-metal Linux (x86_64) using Twingate to avoid port forwarding. The Twingate Connector tunnels UDP traffic so port 19132 never needs to be publicly exposed. Supports Windows, iOS, Android, and ChromeOS players only (no console support).

## Key Information
- Bedrock server listens on **UDP port 19132** (not TCP)
- Architecture requirement: **x86_64 only** — ARM (Raspberry Pi, Apple Silicon) requires the Docker-based guide with box64 emulation
- No router port forwarding required
- Twingate Client must remain connected during entire play session
- Console platforms (Xbox, PlayStation, Switch) cannot use Twingate

## Prerequisites
- Linux machine: Ubuntu 22.04/24.04 or Debian 12, x86_64, ≥1 GB RAM, ≥2 CPU cores, ≥10 GB disk
- Twingate account with Admin Console access
- SSH/terminal access to Linux machine
- Packages: `curl`, `unzip`, `libcurl4`, `openssl`

## Step-by-Step

1. **Create Remote Network** in Admin Console → Generate Connector Access Token + Refresh Token
2. **Create system user**: `sudo useradd -r -m -d /opt/minecraft-bedrock -s /bin/bash minecraft`
3. **Download Bedrock server** from [minecraft.net](https://minecraft.net), extract to `/opt/minecraft-bedrock/server/`
4. **Configure** `server.properties` as needed
5. **Create systemd service** at `/etc/systemd/system/minecraft-bedrock.service` with `LD_LIBRARY_PATH=/opt/minecraft-bedrock/server`
6. **Start server**: `sudo systemctl enable --now minecraft-bedrock`
7. **Install Connector**:
   ```bash
   curl "https://binaries.twingate.com/connector/setup.sh" | \
   sudo TWINGATE_ACCESS_TOKEN="<token>" \
   TWINGATE_REFRESH_TOKEN="<token>" \
   TWINGATE_NETWORK="<network>" bash
   ```
8. **Add Resource** in Admin Console: private IP, **UDP port 19132**
9. **Assign Group** access to Resource
10. **Players**: Install Twingate Client → sign in → add server by private IP in Minecraft

## Configuration Values

| Property | Default | Notes |
|---|---|---|
| `server-port` | `19132` | UDP only |
| `gamemode` | `survival` | survival/creative/adventure |
| `difficulty` | `easy` | peaceful/easy/normal/hard |
| `max-players` | `10` | |
| `online-mode` | `true` | Xbox Live validation |
| `tick-distance` | `4` | Range: 4–12 |

**Connector env vars**: `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`, `TWINGATE_NETWORK`

## Gotchas
- **Must use UDP** for the Twingate Resource — TCP-only causes "Unable to connect to world" even if everything else is correct
- Each Connector needs its own unique token pair — do not reuse tokens
- Connector tokens are one-time: copy immediately after generation
- ARM hardware silently fails with architecture errors on native install
- If missing `.so` files: `sudo apt install --reinstall libcurl4 openssl`

## Troubleshooting Commands
```bash
sudo journalctl -u minecraft-bedrock -f          # Server logs
sudo journalctl -u twingate-connector -n 100     # Connector logs
sudo ss -ulpn | grep 19132                       # Check port conflicts
sudo chown -R minecraft:minecraft /opt/minecraft-bedrock  # Fix permissions
```

## Related Docs
- [Docker-based Bedrock guide](https://www.twingate.com/docs) (ARM support)
- [Java Edition guide](https://www.twingate.com/docs)
- Twingate Security Policies (MFA, device trust)
- Deploy a Second
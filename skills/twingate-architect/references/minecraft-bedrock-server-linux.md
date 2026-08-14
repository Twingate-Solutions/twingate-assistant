---
source: https://www.twingate.com/docs/minecraft-bedrock-server-linux
type: docs
fetched: 2026-08-14
source_version: c5bf42fdebc64e6951b7cb902f3d5e77f01970fe7e2cc2919b68b25d3aff9f80
---

# Minecraft Bedrock Server with Twingate (Linux)

## Summary
Guide for hosting a private Minecraft Bedrock Dedicated Server on Linux (x86_64) using Twingate instead of port forwarding. The Twingate Connector tunnels UDP traffic so port 19132 never needs to be publicly exposed. Supports Windows, iOS, Android, and ChromeOS players only (no console support).

## Key Information
- Bedrock server listens on **UDP port 19132** (not TCP)
- Architecture requirement: **x86_64 only** — ARM (Raspberry Pi, Apple Silicon) requires the Docker-based guide with box64 emulation
- Connector adds <256 MB RAM overhead; 1 GB total RAM handles ~10 players
- Twingate Client must remain connected for entire Minecraft session

## Prerequisites
- Linux machine: Ubuntu 22.04/24.04 or Debian 12, x86_64, ≥1 GB RAM, ≥2 CPU cores, ≥10 GB disk
- Twingate account with Admin Console access
- SSH/terminal access to Linux machine
- Packages: `curl`, `unzip`, `libcurl4`, `openssl`

## Step-by-Step

1. **Create Remote Network** in Admin Console → Remote Networks → Add Remote Network
2. **Generate Connector Tokens** (Access Token + Refresh Token) from the Connector config
3. **Create minecraft system user**: `sudo useradd -r -m -d /opt/minecraft-bedrock -s /bin/bash minecraft`
4. **Download & extract** Bedrock Dedicated Server from [minecraft.net](https://minecraft.net) to `/opt/minecraft-bedrock/server/`
5. **Configure** `/opt/minecraft-bedrock/server/server.properties`
6. **Create systemd service** at `/etc/systemd/system/minecraft-bedrock.service` (see config below)
7. **Start server**: `sudo systemctl enable --now minecraft-bedrock`
8. **Install Connector** via setup script
9. **Add Resource** in Admin Console: private IP, UDP port 19132
10. **Assign Group access** to Resource
11. Players install Twingate Client, sign in, then add server by private IP in Minecraft

## Configuration Values

**systemd service** (`/etc/systemd/system/minecraft-bedrock.service`):
```ini
[Service]
User=minecraft
WorkingDirectory=/opt/minecraft-bedrock/server
ExecStart=/opt/minecraft-bedrock/server/bedrock_server
Environment=LD_LIBRARY_PATH=/opt/minecraft-bedrock/server
```

**Connector install env vars**:
```
TWINGATE_ACCESS_TOKEN=<token>
TWINGATE_REFRESH_TOKEN=<token>
TWINGATE_NETWORK=<yournetwork>
```

**Key `server.properties` settings**:
| Property | Default | Notes |
|---|---|---| 
| `server-port` | `19132` | UDP |
| `max-players` | `10` | |
| `online-mode` | `true` | Xbox Live validation |
| `tick-distance` | `4` | Range: 4–12 |

## Gotchas
- **UDP not TCP**: Resource must be configured as UDP 19132 — TCP causes "Unable to connect to world"
- **ARM hardware**: Native binary will fail; use Docker guide with box64 instead
- **Console players**: Xbox/PlayStation/Switch have no Twingate Client — cannot connect through Twingate
- **Token reuse**: Each Connector requires unique Access/Refresh token pair
- **File ownership**: All files under `/opt/minecraft-bedrock` must be owned by `minecraft:minecraft`

## Troubleshooting Commands
```bash
sudo systemctl status minecraft-bedrock
sudo journalctl -u minecraft-bedrock -n 100
sudo journalctl -u twingate-connector -n 100
sudo ss -ulpn | grep 19132  # check port conflicts
sudo chown -R minecraft:minecraft /opt/minecraft-bedrock  # fix permissions
```

## Related Docs
- Docker-based Bedrock guide (ARM support)
- Minecraft Java Edition guide
- Twingate Security Policies (MFA, device
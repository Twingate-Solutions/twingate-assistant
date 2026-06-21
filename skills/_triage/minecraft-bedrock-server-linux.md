<!-- triage: unassigned URL: https://www.twingate.com/docs/minecraft-bedrock-server-linux -->

# Minecraft Bedrock Server with Twingate (Linux)

## Summary
Guide for hosting a private Minecraft Bedrock Dedicated Server on bare-metal Linux (x86_64) with Twingate securing access. Players connect via Twingate Client instead of public port forwarding. Supports Windows, iOS, Android, and ChromeOS — not consoles.

## Key Information
- Bedrock server uses **UDP port 19132** (not TCP)
- Server is **x86_64 only** — ARM hardware requires the Docker-based guide (uses box64 emulation)
- No inbound router ports needed; Connector makes outbound connection to Twingate Cloud
- Twingate Client must remain connected throughout play session

## Prerequisites
- Linux machine: x86_64, ≥1 GB RAM, ≥2 CPU cores, ≥10 GB disk
- Tested on Ubuntu 22.04/24.04, Debian 12
- Twingate account with Admin Console access
- SSH/terminal access to Linux machine
- Dependencies: `curl unzip libcurl4 openssl`

## Step-by-Step

1. **Create Remote Network** in Admin Console → Remote Networks → Add Remote Network
2. **Generate Connector Tokens** (Access Token + Refresh Token) from the Connector page
3. **Create minecraft user**: `sudo useradd -r -m -d /opt/minecraft-bedrock -s /bin/bash minecraft`
4. **Download & extract** Bedrock server binary to `/opt/minecraft-bedrock/server`
5. **Configure** `/opt/minecraft-bedrock/server/server.properties`
6. **Create systemd service** at `/etc/systemd/system/minecraft-bedrock.service`
7. **Start server**: `sudo systemctl enable --now minecraft-bedrock`
8. **Install Connector** via setup script with tokens
9. **Add Resource** in Admin Console: private IP, UDP port 19132
10. **Assign Group access** to Resource
11. Players install Twingate Client, sign in, add server by private IP in Minecraft

## Configuration Values

**Connector install:**
```bash
curl "https://binaries.twingate.com/connector/setup.sh" | \
sudo TWINGATE_ACCESS_TOKEN="<token>" \
TWINGATE_REFRESH_TOKEN="<token>" \
TWINGATE_NETWORK="<network>" bash
```

**Key server.properties settings:**
| Property | Default | Notes |
|---|---|---|
| `server-port` | `19132` | UDP only |
| `gamemode` | `survival` | survival/creative/adventure |
| `max-players` | `10` | |
| `online-mode` | `true` | Xbox Live validation |

**systemd environment:** `LD_LIBRARY_PATH=/opt/minecraft-bedrock/server`

## Gotchas
- **UDP not TCP**: Resource must be configured for UDP 19132 — TCP causes "Unable to connect to world"
- **ARM incompatibility**: Native binary won't run on Raspberry Pi or Apple Silicon; use Docker guide
- **Console players unsupported**: Xbox, PlayStation, Switch have no Twingate Client
- **Token reuse**: Each Connector requires unique token pair
- **File ownership**: `/opt/minecraft-bedrock` must be owned by `minecraft:minecraft`

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
- Twingate Security Policies (MFA, device trust)
- Deploy a Second Connector (HA)
# Minecraft Bedrock Server with Twingate (Linux)

## Summary
Guide for hosting a private Minecraft Bedrock Edition server on bare-metal x86_64 Linux using Twingate instead of port forwarding. The Twingate Connector tunnels UDP traffic so port 19132 never needs to be publicly exposed. Supports Windows, iOS, Android, and ChromeOS players (not consoles).

## Key Information
- Bedrock server listens on **UDP port 19132** (not TCP)
- Architecture: Player → Twingate Client → Twingate Cloud → Connector → Bedrock Server
- No inbound firewall rules or port forwarding required
- Console players (Xbox, PlayStation, Switch) cannot use Twingate

## Prerequisites
- Linux x86_64 machine (Ubuntu 22.04/24.04 or Debian 12 tested)
- **ARM not supported** for native install; use Docker-based guide with box64 emulation instead
- Minimum: 1 GB RAM, 2 CPU cores, 10 GB disk
- Twingate account with Admin Console access
- SSH/terminal access

## Step-by-Step

1. **Create Remote Network** in Admin Console → Remote Networks → Add Remote Network
2. **Generate Connector tokens** (Access Token + Refresh Token) from the Connector settings
3. **Create minecraft user/directory**:
   ```bash
   sudo useradd -r -m -d /opt/minecraft-bedrock -s /bin/bash minecraft
   sudo mkdir -p /opt/minecraft-bedrock/server
   sudo chown -R minecraft:minecraft /opt/minecraft-bedrock
   ```
4. **Install dependencies**: `sudo apt install -y curl unzip libcurl4 openssl`
5. **Download and extract** Bedrock server binary from minecraft.net Ubuntu link
6. **Configure** `/opt/minecraft-bedrock/server/server.properties`
7. **Create systemd service** at `/etc/systemd/system/minecraft-bedrock.service`
8. **Start server**: `sudo systemctl enable --now minecraft-bedrock`
9. **Install Connector**:
   ```bash
   curl "https://binaries.twingate.com/connector/setup.sh" | \
   sudo TWINGATE_ACCESS_TOKEN="<token>" \
   TWINGATE_REFRESH_TOKEN="<token>" \
   TWINGATE_NETWORK="<network>" bash
   ```
10. **Add Resource** in Admin Console: private IP, UDP port 19132
11. **Assign Group access** to Resource
12. Players install Twingate Client, sign in, add server by private IP in Minecraft

## Configuration Values

| Parameter | Value |
|-----------|-------|
| `TWINGATE_ACCESS_TOKEN` | From Admin Console |
| `TWINGATE_REFRESH_TOKEN` | From Admin Console |
| `TWINGATE_NETWORK` | e.g., `yournetwork.twingate.com` |
| `server-port` | `19132` |
| `LD_LIBRARY_PATH` | `/opt/minecraft-bedrock/server` (required in systemd) |
| Resource protocol | **UDP** 19132 |

## Gotchas
- **Must use UDP** for Resource config — TCP-only causes "Unable to connect to world"
- Token sets are unique per Connector; never reuse across Connectors
- Bedrock binary is x86_64 only; ARM requires Docker + box64
- Twingate Client must remain connected for entire play session
- Find conflicting port: `sudo ss -ulpn | grep 19132`
- Fix permissions: `sudo chown -R minecraft:minecraft /opt/minecraft-bedrock`

## Related Docs
- [Docker-based Bedrock guide](https://www.twingate.com/docs) — ARM support via box64
- [Java Edition guide](https://www.twingate.com/docs)
- [Deploy a Second Connector](https://www.twingate.com/docs) — high availability
- [Security Policies](https://www.twingate.com/docs) — MFA, device trust
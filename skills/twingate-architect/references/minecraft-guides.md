# Minecraft Server Guides

## Summary
Index page for hosting private Minecraft servers using Twingate to avoid port forwarding. Covers Java (Vanilla), Java (Forge/modded), and Bedrock editions with both Docker Compose and Linux bare metal deployment options. All setups use a Twingate Connector that creates outbound-only connections, keeping servers off the public internet.

## Key Information
- Six total guides: 3 editions × 2 deployment methods (Docker Compose, Linux bare metal)
- No ports exposed to internet; players connect via private IP through Twingate Client
- Connector opens outbound connection to Twingate Cloud (no inbound firewall rules needed)
- Docker guides use `itzg/minecraft-server` (Java) and `itzg/minecraft-bedrock-server` (Bedrock) images
- Forge Docker guide supports automated CurseForge modpack installation

## Comparison Table

| | Java Vanilla | Java Forge | Bedrock |
|---|---|---|---|
| Protocol | TCP 25565 | TCP 25565 | UDP 19132 |
| Min RAM | 2 GB | 4–8 GB | 1 GB |
| Platforms | Win/Mac/Linux | Win/Mac/Linux | Win/iOS/Android/ChromeOS |
| Mod support | No | Yes | No |

## Prerequisites
- Twingate account (free tier available)
- Twingate Client installed on each player's device
- **Docker guides:** Docker + Docker Compose on host (Linux, macOS, or Windows)
- **Linux guides:** Ubuntu 22.04/24.04 or Debian 12; Java installed (Java editions); x86_64 arch (Bedrock); systemd

## Architecture
```
[Player Device + Twingate Client] → [Twingate Cloud] → [Twingate Connector] → [Minecraft Server]
```
- Connector and server run as either Docker containers (Compose) or systemd services (bare metal)
- Players connect using server's **private IP address**, not public IP or hostname

## Gotchas
- Bedrock edition is **UDP 19132**, not TCP — relevant for Connector/Resource configuration
- Bedrock Linux guide requires **x86_64** architecture only (no ARM support noted)
- Forge requires significantly more RAM (4–8 GB) vs vanilla (2 GB); check specific guide before provisioning
- RAM/disk requirements vary by edition — index page doesn't specify disk; check individual guides

## Related Docs
- Vanilla Java Docker guide
- Vanilla Java Linux guide
- Forge Docker guide
- Forge Linux guide
- Bedrock Docker guide
- Bedrock Linux guide
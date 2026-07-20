# Minecraft Server Guides

## Page Title
Minecraft Server Guides - Private Minecraft Server Hosting with Twingate

## Summary
Index page for hosting private Minecraft servers using Twingate without port forwarding. Covers three server editions (Java Vanilla, Java Forge, Bedrock) with two deployment options each (Docker Compose or bare metal Linux). The Twingate Connector handles outbound-only connections, keeping the server off the public internet.

## Key Information
- 6 total guides: 3 editions × 2 deployment methods
- No ports exposed to internet; Connector makes outbound connections to Twingate Cloud
- Players connect via private IP using Twingate Client

## Edition Comparison

| | Java Vanilla | Java Forge | Bedrock |
|---|---|---|---|
| Protocol | TCP 25565 | TCP 25565 | UDP 19132 |
| Min RAM | 2 GB | 4–8 GB | 1 GB |
| Platforms | Win/Mac/Linux | Win/Mac/Linux | Win/iOS/Android/ChromeOS |
| Mod Support | No | Yes | No |

## Prerequisites
- Twingate account (free tier available)
- Twingate Client installed on each player's device
- **Docker guides**: Docker + Docker Compose (Linux/macOS/Windows host)
- **Linux guides**: Ubuntu 22.04/24.04 or Debian 12; Java (Vanilla/Forge) or Bedrock binary (x86_64 only); systemd

## Architecture
```
[Player Device] → Twingate Client → [Twingate Cloud] ↔ [Twingate Connector] → [Minecraft Server]
```

## Deployment Options by Edition
- **Java Vanilla Docker**: `itzg/minecraft-server` image
- **Java Vanilla Linux**: Native install + systemd
- **Forge Docker**: Auto-downloads CurseForge modpacks or manual mods
- **Forge Linux**: Manual Forge install + systemd
- **Bedrock Docker**: `itzg/minecraft-bedrock-server` image
- **Bedrock Linux**: Native install + systemd

## Gotchas
- Bedrock uses **UDP** 19132, not TCP — relevant for firewall/connector config
- Bedrock Linux bare metal is **x86_64 only**
- Forge RAM requirement (4–8 GB) is significantly higher than Vanilla
- RAM/disk specifics vary per guide — check individual guides before provisioning

## Related Docs
- Individual guides linked from this index (not URLs provided)
- Twingate Connector setup (implied prerequisite)
- Twingate Client installation
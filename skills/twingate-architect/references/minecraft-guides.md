# Minecraft Server Guides

## Page Title
Twingate Minecraft Server Guides (Index/Overview)

## Summary
Index page for hosting private Minecraft servers using Twingate without port forwarding. Covers three server types (Java Vanilla, Java Forge, Bedrock) each with Docker Compose and Linux bare metal deployment options. The Twingate Connector opens outbound-only connections, keeping the server off the public internet.

## Key Information
- **Three server editions**: Java Vanilla, Java Forge (modded), Bedrock
- **Two deployment methods each**: Docker Compose or Linux bare metal (systemd)
- **No port forwarding required**: Connector uses outbound connections to Twingate Cloud
- Players connect via private IP through Twingate Client

## Prerequisites
- Twingate account (free tier available)
- Twingate Client installed on each player's device
- **Docker path**: Docker + Docker Compose on host (Linux/macOS/Windows supported)
- **Linux path**: Ubuntu 22.04/24.04 or Debian 12 + systemd

## Configuration Values / Comparison Table

| Property | Java Vanilla | Java Forge | Bedrock |
|----------|-------------|------------|---------|
| Protocol | TCP 25565 | TCP 25565 | UDP 19132 |
| Min RAM | 2 GB | 4–8 GB | 1 GB |
| Platforms | Win/Mac/Linux | Win/Mac/Linux | Win/iOS/Android/ChromeOS |
| Mod support | No | Yes | No |
| Docker image | `itzg/minecraft-server` | `itzg/minecraft-server` | `itzg/minecraft-bedrock-server` |

## Architecture
```
[Player's Device + Twingate Client]
         ↕ Twingate Cloud ↕
[Twingate Connector] ↔ [Minecraft Server]
```

## Gotchas
- Bedrock uses **UDP** 19132 (not TCP); ensure Connector/network config supports UDP
- Forge minimum RAM is 4–8 GB vs 2 GB for Vanilla — plan host resources accordingly
- Bedrock Linux bare metal is **x86_64 only** (no ARM support)
- Bedrock supports cross-platform play; Java does not (no mobile/console)
- Docker Compose Forge guide supports automated CurseForge modpack downloads; Linux guide is manual only

## Related Docs
- Java Vanilla: Docker Compose guide | Linux guide
- Java Forge: Docker Compose guide | Linux guide
- Bedrock: Docker Compose guide | Linux guide
- Twingate Connector setup documentation
- Twingate Client installation
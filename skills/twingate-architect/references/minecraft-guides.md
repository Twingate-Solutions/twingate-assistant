---
source: https://www.twingate.com/docs/minecraft-guides
type: docs
fetched: 2026-08-14
source_version: 9b558f6b007a76018f3ce8017aff2c1c33166025bdf93d118138eb1d4462b0c8
---

# Minecraft Server Guides

## Page Title
Minecraft Server Guides (Twingate)

## Summary
Index page for hosting private Minecraft servers secured with Twingate, eliminating public port forwarding. Covers three server editions (Java Vanilla, Java Forge, Bedrock) with two deployment methods each (Docker Compose and bare-metal Linux). Players connect via Twingate Client; no ports are exposed to the internet.

## Key Information
- **6 total guides**: 3 editions × 2 deployment methods
- Architecture: Player → Twingate Client → Twingate Cloud → Connector → Minecraft Server (outbound-only connection)
- Connector runs alongside Minecraft server (as container or systemd service)
- Players use server's **private IP address** to connect (not public IP)

## Prerequisites
- Twingate account (free tier available)
- Twingate Client installed on each player's device
- **Docker guides**: Docker + Docker Compose on host (Linux/macOS/Windows)
- **Linux guides**: Ubuntu 22.04/24.04 or Debian 12; systemd; Java (Java editions) or Bedrock binary (x86_64 only)

## Edition Comparison

| | Java Vanilla | Java Forge | Bedrock |
|---|---|---|---|
| Protocol | TCP 25565 | TCP 25565 | **UDP 19132** |
| Min RAM | 2 GB | 4–8 GB | 1 GB |
| Platforms | Win/Mac/Linux | Win/Mac/Linux | Win/iOS/Android/ChromeOS |
| Mod support | No | Yes | No |

## Deployment Options

| Edition | Docker Image | Linux Method |
|---|---|---|
| Java Vanilla | `itzg/minecraft-server` | systemd native |
| Java Forge | `itzg/minecraft-server` (CurseForge auto-download) | Manual Forge + systemd |
| Bedrock | `itzg/minecraft-bedrock-server` | systemd native (x86_64 only) |

## Configuration Values
- Java port: `25565/TCP`
- Bedrock port: `19132/UDP`
- Bedrock Linux: x86_64 architecture required

## Gotchas
- Bedrock uses **UDP**, not TCP — firewall/Twingate Resource rules must specify UDP 19132
- Bedrock bare-metal requires x86_64 (no ARM support noted)
- Forge RAM minimum (4–8 GB) is significantly higher; modpack requirements vary
- Players must have Twingate Client installed **before** attempting to connect

## Related Docs
- Java Vanilla: Docker Compose guide, Linux guide
- Java Forge: Docker Compose guide (CurseForge modpacks), Linux guide
- Bedrock: Docker Compose guide, Linux guide
- Twingate Connector setup documentation
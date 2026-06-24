<!-- triage: unassigned URL: https://www.twingate.com/docs/minecraft-guides -->

# Minecraft Server Guides

## Page Title
Minecraft Server Guides – Private Minecraft Server with Twingate

## Summary
Index page for hosting private Minecraft servers secured with Twingate, eliminating the need for port forwarding. Covers three server editions (Java Vanilla, Java Forge, Bedrock) each with Docker Compose or Linux bare-metal deployment options. Players connect via Twingate Client; no ports are exposed to the internet.

## Key Information
- **6 total guides**: 3 editions × 2 deployment methods each
- **Docker guides**: Use `itzg/minecraft-server` (Java) or `itzg/minecraft-bedrock-server` (Bedrock) images via Docker Compose
- **Linux guides**: Native install managed with systemd; Ubuntu 22.04/24.04 or Debian 12
- Twingate Connector makes **outbound-only connections** — no inbound port exposure

## Edition Comparison

| | Java Vanilla | Java Forge | Bedrock |
|---|---|---|---|
| Protocol | TCP 25565 | TCP 25565 | UDP 19132 |
| Min RAM | 2 GB | 4–8 GB | 1 GB |
| Platforms | Win/Mac/Linux | Win/Mac/Linux | Win/iOS/Android/ChromeOS |
| Mod support | No | Yes | No |

## Prerequisites
- Twingate account (free tier available)
- Twingate Client installed on each player's device
- **Docker path**: Docker + Docker Compose on host (Linux, macOS, or Windows)
- **Linux path**: Linux machine (Ubuntu 22.04/24.04 or Debian 12), Java (for Java/Forge) or Bedrock binary (x86_64 only), systemd

## Architecture
```
[Player Device + Twingate Client] → [Twingate Cloud] → [Twingate Connector] → [Minecraft Server]
```
Connector runs alongside the Minecraft server (as a container or systemd service). Players connect using the server's **private IP address**.

## Gotchas
- Bedrock uses **UDP** 19132, not TCP — relevant for Connector/firewall configuration
- Bedrock Linux install is **x86_64 only** (no ARM)
- Forge requires significantly more RAM (4–8 GB minimum vs. 2 GB for Vanilla)
- Docker Forge guide supports automated CurseForge modpack download; Linux Forge requires manual mod setup

## Related Docs
- Java Vanilla: Docker Compose guide, Linux guide
- Java Forge: Docker Compose guide, Linux guide
- Bedrock: Docker Compose guide, Linux guide
- Twingate sign-up (free)
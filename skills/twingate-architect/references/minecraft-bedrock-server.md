---
source: https://www.twingate.com/docs/minecraft-bedrock-server
type: docs
fetched: 2026-08-14
source_version: 5751c672a9655bcd78e4605e7d7e6f1b13553754315de2a1aba6c092d8403ff2
---

# Minecraft Bedrock Server with Twingate

## Summary
Deploy a private Minecraft Bedrock Edition server using Docker Compose with a Twingate Connector, eliminating the need for port forwarding. Players connect via Twingate Client on Windows, iOS, Android, or ChromeOS. Console platforms (Xbox, PlayStation, Switch) are not supported.

## Key Information
- Uses `itzg/minecraft-bedrock-server` Docker image with Twingate Connector in Docker Compose
- Server pinned to fixed Docker bridge IP `172.30.0.10`; no host port published
- Bedrock uses **UDP port 19132** (not TCP)
- Multi-arch image supports ARM (Apple Silicon, Raspberry Pi) via box64 emulation
- Minimum specs: 1 GB RAM, 2 CPU cores, 10 GB disk

## Prerequisites
- Docker Engine + Docker Compose installed
- Twingate account with Admin Console access
- Twingate Access Token and Refresh Token (generated per Connector)

## Step-by-Step

1. **Create Remote Network** in Twingate Admin Console → Remote Networks → Add Remote Network
2. **Generate Connector Tokens** → select Connector → Docker → Generate Tokens → copy Access Token + Refresh Token
3. **Deploy via Docker Compose** (see config below) → `docker compose up -d`
4. **Verify Connector** shows Controller + Relay as `Connected` in Admin Console
5. **Add Resource**: Address `172.30.0.10`, Protocol UDP port `19132`
6. **Grant Access** to Group (default: Everyone, or create `Minecraft Players` group)
7. **Players**: Install Twingate Client → sign in → add server at `172.30.0.10:19132` in Minecraft

## Configuration Values

**docker-compose.yml environment variables:**

| Variable | Value |
|---|---|
| `TWINGATE_NETWORK` | `<your-network-name>` |
| `TWINGATE_ACCESS_TOKEN` | `<access-token>` |
| `TWINGATE_REFRESH_TOKEN` | `<refresh-token>` |
| `EULA` | `"TRUE"` |
| `SERVER_NAME` | Custom name |
| `GAMEMODE` | `survival` / `creative` / `adventure` |
| `DIFFICULTY` | `peaceful` / `easy` / `normal` / `hard` |
| `MAX_PLAYERS` | `10` |
| `VERSION` | `LATEST` or specific (e.g., `1.21.30.03`) |
| `LEVEL_SEED` | Random or specified |

**Network:** Docker bridge `minecraft-net`, subnet `172.30.0.0/24`, server at `172.30.0.10`

**Docker images:**
- `itzg/minecraft-bedrock-server:latest`
- `twingate/connector:1`

## Gotchas
- **UDP only**: Resource must be configured as UDP port 19132; TCP misconfiguration causes "Unable to connect to world"
- **Console unsupported**: Xbox/PlayStation/Switch have no Twingate Client
- **Tokens are unique**: Never reuse Access/Refresh token pairs across Connectors
- **Twingate must stay connected** for entire session
- **ARM overhead**: Bedrock is x86_64 binary; emulation works but limits player count on low-powered ARM hardware
- `network_mode: host` does not work on Docker Desktop (macOS/Windows); use bridge network instead

## Troubleshooting
- "Unable to connect": Check Twingate Client connected, Resource in player's list, UDP configured, server running (`docker compose ps`), correct IP/port in Minecraft
- Connector offline: Verify env vars, outbound internet, check `docker compose logs twingate-connector`
- Crashes/memory: Check `docker compose logs bedrock`; Bedrock has no configurable heap size

## Related Docs
- [Minecraft Java Edition guide](https://www.twingate.com/docs/minecraft-java-server)
- [itzg/minecraft-bedrock-server documentation](https://github.com/itzg/docker-minecraft-bedrock-server)
- Twingate Security Policies, Resources configuration, Protect Your Home
---
source: https://www.twingate.com/docs/minecraft-server
type: docs
fetched: 2026-11-22
source_version: 0d3680d5d6505ec198be1108c6a21178fc47871ef8c8c091ba4b585e2c97afa4
trust: official
---

# Minecraft Server with Twingate (Docker Compose, Java Edition)

## Summary
Guide to hosting a private vanilla Minecraft Java Edition server using Docker Compose, with a Twingate Connector running alongside it. Players reach the server over an outbound-only encrypted tunnel via the Twingate Client, so no port forwarding or public exposure of port 25565 is needed.

## Key Information
- Architecture: Player device (Twingate Client) → Twingate Cloud → Twingate Connector → Minecraft server (25565).
- Both containers share a private bridge network `minecraft-net` (subnet `172.30.0.0/24`); the Minecraft container has the fixed IP `172.30.0.10`.
- No ports are published to the host. `network_mode: host` is avoided because it breaks on Docker Desktop (macOS/Windows).
- Java Edition uses TCP 25565 only (Bedrock uses UDP 19132).
- Minecraft image: `itzg/minecraft-server:latest`. Connector image: `twingate/connector:1`.
- Access is managed with Twingate Groups instead of Minecraft allowlists.
- Connector overhead: under 256 MB RAM.

## Prerequisites
- Machine with 2 GB RAM, 2 CPU cores, 10 GB disk (4 GB+ for mods or more players; heavy modpacks may need 6-8 GB+).
- Docker Engine and Docker Compose.
- Twingate account with Admin Console access.
- Terminal access.

## Step-by-Step
1. **Admin Console:** Remote Networks → Add Remote Network (e.g., On Premise) → add Connector → choose Docker → Generate Tokens. Copy the Access and Refresh Tokens. Each Connector needs its own unique token set.
2. **Compose file:** Create `~/minecraft-server/docker-compose.yml` with a `minecraft` service (env vars below, `./data:/data` volume, static IP `172.30.0.10`, `restart: unless-stopped`) and a `twingate-connector` service on the same network. Define the `minecraft-net` network with the IPAM subnet.
3. Replace the placeholders with your network name and tokens, then run `docker compose up -d`.
4. Verify with `docker compose ps` (both `Up`) and `docker compose logs minecraft -f` (wait for `For help, type "help"`).
5. In the Admin Console, confirm the Connector's Controller and Relay both show Connected.
6. **Create the Resource:** Name `Minecraft Server`, address `172.30.0.10`, protocol TCP 25565. Grant access to a Group.
7. **Players:** Install the Twingate Client, sign in to your network, then in Minecraft go to Multiplayer → Add Server → `172.30.0.10`.
8. **Access control:** Invite users (Team → Add User), create a `Minecraft Players` Group, assign it to the Resource, and remove `Everyone`.

## Configuration Values
Connector env vars: `TWINGATE_NETWORK`, `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`

Minecraft env vars (itzg image):
- `EULA` ("TRUE" required)
- `MEMORY` (default 2G)
- `TYPE` (VANILLA, PAPER, FORGE, FABRIC)
- `VERSION` (LATEST or e.g. 1.21.1)
- `DIFFICULTY`
- `MAX_PLAYERS` (10)
- `MOTD`
- `OPS`
- `SEED`

Apply changes with `docker compose down && docker compose up -d`.

## Gotchas
- Setting `EULA: "TRUE"` means you accept the Minecraft EULA.
- Players must keep the Twingate Client connected during play.
- Deleting `./data` or removing the volume mount loses world data. Back it up.
- Crashes are usually insufficient `MEMORY`; also make sure the host has that much free RAM.
- Connector offline: check the tokens and network name, outbound internet access, and `docker compose logs twingate-connector`.
- Bedrock players cannot use this setup (different protocol and port).
- If the Resource doesn't appear for a player, check their Group membership.
- Revoking access: remove the user from the Group.

## Related Docs
- Linux native version (https://www.twingate.com/docs/minecraft-server-linux)
- All Minecraft guides (https://www.twingate.com/docs/minecraft-guides)
- Bedrock (https://www.twingate.com/docs/minecraft-bedrock-server)
- Forge (modded) (https://www.twingate.com/docs/minecraft-forge-server)
- Resources (https://www.twingate.com/docs/resources)
- Security Policies (https://www.twingate.com/docs/security-policies)
- Protect Your Home Lab (https://www.twingate.com/docs/homelab-step-by-step)
- itzg/minecraft-server documentation (https://docker-minecraft-server.readthedocs.io/)
- Linux Client install guide (https://www.twingate.com/docs/linux)
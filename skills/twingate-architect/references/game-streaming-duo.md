# Duo Multi-User Remote Game Streaming with Twingate

## Summary
Duo enables multiple users to play different games simultaneously on one Windows PC via virtual sessions. This guide configures Duo with Twingate Zero Trust access so remote users can stream without port forwarding or router exposure. Moonlight is used as the streaming client on remote devices.

## Key Information
- Free tier: limited to 30fps; Patreon ($10 lifetime) unlocks unlimited sessions and 60+ fps
- Each user requires a separate Windows user account and virtual session
- Twingate Connector creates outbound-only connection—no inbound ports needed
- Moonlight client handles the actual game streaming protocol

## Prerequisites
- Windows 11 (23H2 or newer) — Windows 10 not supported
- Gaming GPU (Nvidia/AMD/Intel for hardware encoding)
- Twingate account with Admin Console access
- WSL (Ubuntu) or Docker Desktop for Connector deployment
- Moonlight client on remote devices

## Step-by-Step

1. **Install Duo** — Run installer as Administrator, select all components, reboot
2. **Configure Duo** — Access `http://localhost:47990`, set GPU encoder (NVENC/AMF/QuickSync)
3. **Create Windows user** — `net user "RemoteUser" "Password!" /add` + add to Users group
4. **Create virtual session** — Duo web UI → Sessions Management → Add New Virtual Session
5. **Deploy Twingate Connector** — WSL (recommended) or Docker on gaming PC
6. **Add Duo as Twingate Resource** — Private IP, TCP `47984-47990`, UDP `47998-48010`
7. **Assign group access** — Resource → Access → Add Access → select group
8. **Install Twingate Client** on each remote device, sign in, connect
9. **Install Moonlight** on each remote device
10. **Pair Moonlight** — Add PC by private IP, enter PIN in Duo web UI → PIN section

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Duo Web UI | `http://localhost:47990` |
| TCP Ports | `47984-47990` |
| UDP Ports | `47998-48010` |
| Minimum RAM/session | 4GB (8GB recommended) |
| Minimum CPU/session | 2 cores (4 recommended) |

**Service check commands:**
- `sc query DuoService`
- `sc query TermWrap`

## Gotchas
- TermWrap service must be running for virtual sessions to start
- Windows Remote Desktop must be enabled (Settings → System → Remote Desktop)
- Some anti-cheat systems are incompatible with virtual sessions
- Free tier hard-capped at 30Hz regardless of hardware
- Twingate Connector must stay running; WSL/Docker keeps it persistent
- Try `127.0.0.1` if Moonlight can't connect via private IP

## Related Docs
- [Sunshine Remote Streaming](https://www.twingate.com/docs/sunshine) — Single-user streaming
- [Apollo Remote Streaming](https://www.twingate.com/docs/apollo) — Automatic virtual displays
- [Game Streaming Overview](https://www.twingate.com/docs/game-streaming) — Compare options
- [Connector Deployment Guides](https://www.twingate.com/docs/connector)
- [Resource Access Configuration](https://www.twingate.com/docs/access-control)
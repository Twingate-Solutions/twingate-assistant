# Duo Multi-User Remote Game Streaming with Twingate

## Summary
Configure Duo multi-user game streaming software on a Windows 11 gaming PC with Twingate Zero Trust access, enabling multiple family members to game simultaneously without port forwarding. Each user gets an isolated virtual Windows session accessible via Moonlight client through an encrypted Twingate tunnel.

## Key Information
- Duo runs multiple concurrent virtual Windows sessions on one PC, each user gets dedicated resources
- Free tier: 30Hz max, limited users. Patreon ($10 lifetime): unlimited users, 60+ fps, HDR
- Moonlight is the streaming client; Duo is the server (compatible with Sunshine/Moonlight ecosystem)
- No inbound ports required — Twingate Connector uses outbound-only connections

## Prerequisites
- Windows 11 23H2 or newer (Windows 10 not supported)
- Gaming GPU (Nvidia/AMD/Intel for hardware encoding)
- Twingate account with admin access
- WSL (Ubuntu) or Docker Desktop for Connector deployment
- Moonlight client on remote devices

## Step-by-Step

1. **Install Duo** — Run installer as Administrator, select all components, reboot
2. **Configure Duo** — Access `http://localhost:47990`, set GPU encoder (NVENC/AMF/QuickSync)
3. **Create Windows user accounts** — `net user "RemoteUser" "Password!" /add` + add to Users group
4. **Create virtual sessions** — In Duo web UI → Sessions Management → Add New Virtual Session, assign user account
5. **Deploy Twingate Connector** — Via WSL (recommended) or Docker on the gaming PC
6. **Add Duo as Twingate Resource** — Use PC's private IP with specified port ranges
7. **Assign access** — Add user groups to resource in Twingate Admin Console
8. **Install Twingate Client** on each remote device, sign in, connect
9. **Install Moonlight** on remote devices
10. **Pair Moonlight** — Enter PC's private IP, exchange 4-digit PIN via Duo web UI → PIN section

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Duo Web UI | `http://localhost:47990` |
| TCP Ports | `47984-47990` (Web UI + HTTPS) |
| UDP Ports | `47998-48010` (streaming, multi-session) |
| Duo service name | `DuoService` |
| TermWrap service | `TermWrap` |

**GPU Encoder mapping:**
- Nvidia → NVENC
- AMD → AMF  
- Intel → QuickSync

## Gotchas
- First virtual session start is slow — Windows initializing new session environment
- Anti-cheat systems may not work in virtual sessions
- Twingate Connector must stay running; WSL/Docker handles persistence
- Free tier hard-limited to 30fps regardless of hardware
- `sc query DuoService` / `sc query TermWrap` to verify services are running if connection fails
- Alternative: try `127.0.0.1` instead of LAN IP if Moonlight can't connect

## Resource Planning
| RAM | CPU Cores | GPU | Concurrent Sessions |
|-----|-----------|-----|---------------------|
| 16GB | 8-core | RTX 3070 | 2–4 |
| 32GB | 12-core | RTX 4080 | 4–6 |
- Per session minimum: 4GB RAM, 2 CPU cores (8GB / 4 cores recommended)

## Related Docs
- [Sunshine Remote Streaming](https://www.twingate.com/docs/game-streaming-sunshine) — single-user streaming
- [Apollo Remote Streaming](https://www.twingate.com/docs/game-streaming-apollo) — automatic virtual displays
- [Connector Deployment Guides](https://www.twingate.com/docs/connector)
- [Resource Access Configuration](https://www.twingate.com/docs/access-configuration)
- [Duo GitHub Repository](https://github.com/blackseraph/duo)
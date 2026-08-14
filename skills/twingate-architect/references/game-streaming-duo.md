---
source: https://www.twingate.com/docs/game-streaming-duo
type: docs
fetched: 2026-08-14
source_version: 47bf59c54a19fb047b3c4ddd6833f57a2f3c593eeb9c4d57dbb7e5fb322b3543
---

# Duo Multi-User Remote Game Streaming with Twingate

## Page Title
Duo Multi-User Remote Game Streaming with Twingate

## Summary
Duo enables multiple users to game simultaneously on a single Windows 11 PC via virtual sessions. This guide covers integrating Duo with Twingate Zero Trust access so remote family members can stream securely without port forwarding. Setup targets under 30 minutes.

## Key Information
- Duo creates isolated virtual Windows sessions per user; each gets dedicated resources
- Twingate replaces port forwarding with outbound-only encrypted tunnel
- Free tier: 30Hz max; Patreon ($10 lifetime): unlimited users + 60+ fps + HDR
- Streaming protocol uses Moonlight client connecting to Duo (Sunshine-compatible API)
- Each virtual session requires its own Windows user account

## Prerequisites
- Windows 11 (23H2 or newer) — Windows 10 not supported
- Gaming GPU (Nvidia/AMD/Intel for hardware encoding)
- Twingate account with Admin Console access
- WSL (Ubuntu) or Docker for Connector deployment
- Moonlight client on each remote device

## Step-by-Step

1. **Install Duo** — Download `Duo.exe`, run as Administrator, select all components, reboot
2. **Configure Duo** — Access `http://localhost:47990`, set GPU encoder (NVENC/AMF/QuickSync)
3. **Create Windows user**: `net user "RemoteUser" "Password!" /add` + add to Users group
4. **Create virtual session** in Duo web UI → Sessions Management → Add New Virtual Session
5. **Deploy Twingate Connector** on gaming PC via WSL (recommended) or Docker
6. **Add Duo as Twingate Resource** with gaming PC private IP
7. **Assign group access** to the resource in Admin Console
8. **Install Twingate Client** on each remote device, sign in, connect
9. **Install Moonlight** on remote devices
10. **Pair Moonlight** — enter PC IP, get 4-digit PIN, enter PIN in Duo web UI → PIN section

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Duo Web UI | `http://localhost:47990` |
| TCP Ports | `47984-47990` (Web UI + HTTPS) |
| UDP Ports | `47998-48010` (streaming, multi-session) |
| Resource Address | PC private IPv4 (e.g., `192.168.1.100`) |
| WSL install | `wsl --install` |
| Add Windows user | `net user "Name" "Pass!" /add` |
| Verify Duo service | `sc query DuoService` |
| Verify TermWrap | `sc query TermWrap` |

## Gotchas
- Virtual sessions won't start if Remote Desktop is disabled: Settings → System → Remote Desktop → Enable
- Some anti-cheat systems are incompatible with virtual sessions
- 30Hz cap is hard limit on free tier; requires Patreon link to unlock higher framerates
- Twingate Connector must stay running (WSL/Docker keeps it alive in background)
- Per-session minimums: 4GB RAM, 2 CPU cores — monitor Task Manager before adding sessions
- UDP range 47998-48010 covers multiple concurrent sessions; single-port config will break multi-user

## Related Docs
- [Sunshine Remote Streaming](https://www.twingate.com/docs/game-streaming-sunshine) — single-user
- [Apollo Remote Streaming](https://www.twingate.com/docs/game-streaming-apollo) — auto virtual displays
- [Game Streaming Overview](https://www.twingate.com/docs/game-streaming)
- [Connector Deployment Guides](https://www.twingate.com/docs/connector)
- [Resource Access Configuration](https://www.twingate.com/docs/resources)
- [Duo GitHub Repository](https://github.com/blackseraph/duo)
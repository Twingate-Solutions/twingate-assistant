# Duo Multi-User Remote Game Streaming with Twingate

## Summary
Duo enables multiple users to stream different games simultaneously from a single Windows 11 PC, each in isolated virtual sessions. This guide integrates Twingate Zero Trust access to eliminate port forwarding requirements while enabling secure remote streaming via the Moonlight client.

## Key Information
- Free tier: unlimited users (limited to 30Hz/30fps), Patreon ($10 lifetime) unlocks 60+ fps, HDR, custom refresh rates
- Each concurrent user requires a separate Windows user account and virtual session in Duo
- Moonlight is the streaming client; Duo acts as the server (Sunshine-compatible API)
- Twingate Connector runs on the gaming PC; no inbound ports needed

## Prerequisites
- Windows 11 (23H2 or newer) — Windows 10 not supported
- Gaming GPU (Nvidia/AMD/Intel for hardware encoding)
- Twingate account with Admin Console access
- WSL (Ubuntu) or Docker for Connector deployment

## Step-by-Step

1. **Install Duo** — Download `Duo.exe`, run as Administrator, select all components, reboot
2. **Configure Duo** — Access `http://localhost:47990`, set GPU encoder (NVENC/AMF/QuickSync)
3. **Create Windows user** per streaming session:
   ```
   net user "RemoteUser" "StrongPassword123!" /add
   net localgroup "Users" "RemoteUser" /add
   ```
4. **Create virtual session** in Duo UI → Sessions Management → Add New Virtual Session
5. **Deploy Twingate Connector** on gaming PC via WSL (recommended) or Docker
6. **Add Duo as Twingate Resource** with gaming PC's private IP
7. **Install Twingate Client** on each remote device; sign in and connect
8. **Install Moonlight** on remote devices; add PC by private IP; enter pairing PIN in Duo UI

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Duo Web UI | `http://localhost:47990` |
| TCP Ports | `47984-47990` (Web UI + HTTPS) |
| UDP Ports | `47998-48010` (streaming, multi-session) |
| Connector deployment | Linux (WSL Ubuntu) or Docker |

## Gotchas
- **Windows 11 only** — 23H2 minimum; no Windows 10 support
- Free tier hard-capped at 30Hz — Patreon required for 60+ fps
- Anti-cheat systems may fail in virtual sessions
- Connector must stay running; WSL/Docker keeps it persistent in background
- When pairing Moonlight, PIN must be entered in Duo UI while already connected via Twingate
- `TermWrap` service must be running for virtual sessions; check with `sc query TermWrap`
- Per-session minimums: 4GB RAM, 2 CPU cores — monitor Task Manager before adding sessions

## Related Docs
- [Sunshine Remote Streaming](https://www.twingate.com/docs/game-streaming-sunshine) — single-user streaming
- [Apollo Remote Streaming](https://www.twingate.com/docs/game-streaming-apollo) — automatic virtual displays
- [Game Streaming Overview](https://www.twingate.com/docs/game-streaming) — compare options
- [Connector Deployment Guides](https://www.twingate.com/docs/connector)
- [Resource Access Configuration](https://www.twingate.com/docs/access-control)
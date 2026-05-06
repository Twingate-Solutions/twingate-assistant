# Duo Multi-User Remote Game Streaming with Twingate

## Summary
Configures Duo (multi-user game streaming platform) with Twingate Zero Trust access so multiple family members can stream games simultaneously from one Windows PC. Replaces port forwarding with a Twingate Connector for secure, private remote access. Full setup takes ~30 minutes.

## Key Information
- Duo enables multiple concurrent virtual Windows sessions on one gaming PC
- Free tier: 30fps max, limited users. Patreon ($10 lifetime): unlimited sessions, 60+ fps, HDR
- Streaming uses Moonlight client to connect to Duo (Sunshine-compatible protocol)
- No inbound ports required; Connector makes outbound-only connections

## Prerequisites
- Windows 11 23H2+ gaming PC with dedicated GPU
- Twingate account with Admin Console access
- WSL (Ubuntu) or Docker for Connector deployment
- Remote devices with Twingate Client + Moonlight installed

## Step-by-Step

1. **Install Duo** — Download `Duo.exe`, run as Administrator, select all components, reboot
2. **Configure Duo** — Open `http://localhost:47990`, set GPU encoder (NVENC/AMF/QuickSync)
3. **Create Windows user accounts** per session: `net user "RemoteUser" "Password!" /add`
4. **Create virtual sessions** in Duo UI → Sessions Management → Add New Virtual Session
5. **Deploy Twingate Connector** on gaming PC via WSL (recommended) or Docker
6. **Add Duo as Twingate Resource** with gaming PC's private IP
7. **Assign resource access** to appropriate user groups in Admin Console
8. **Install Twingate Client** on each remote device, sign in, connect
9. **Install Moonlight** on remote devices, add PC via private IP, enter pairing PIN in Duo UI

## Configuration Values

| Setting | Value |
|---|---|
| Duo Web UI | `http://localhost:47990` |
| TCP Ports | `47984-47990` (Web UI + HTTPS) |
| UDP Ports | `47998-48010` (streaming, multi-session) |
| Resource Address | Gaming PC private IP (e.g., `192.168.1.100`) |

## Gotchas
- **Windows 11 23H2+ only** — Windows 10 not supported
- Free tier hard-locked to 30Hz regardless of client/network capability
- Some anti-cheat systems incompatible with virtual sessions
- Moonlight pairing PIN must be entered in Duo UI while Twingate is connected
- Try `127.0.0.1` in Moonlight if private IP connection fails
- Check `TermWrap` service is running if virtual sessions won't start: `sc query TermWrap`
- Per-session minimums: 4GB RAM, 2 CPU cores; monitor Task Manager before adding sessions

## Related Docs
- [Sunshine Remote Streaming](https://www.twingate.com/docs/game-streaming-sunshine) — single-user alternative
- [Apollo Remote Streaming](https://www.twingate.com/docs/game-streaming-apollo) — automatic virtual displays
- [Game Streaming Overview](https://www.twingate.com/docs/game-streaming) — compare options
- [Connector Deployment Guides](https://www.twingate.com/docs/connector)
- [Resource Access Configuration](https://www.twingate.com/docs/access-control)
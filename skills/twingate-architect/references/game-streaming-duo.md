# Duo Multi-User Remote Game Streaming with Twingate

## Summary
Duo enables multiple users to game simultaneously on a single Windows 11 PC using virtual sessions. This guide configures Twingate as the secure access layer, replacing port forwarding with Zero Trust tunneling. Moonlight is used as the streaming client on remote devices.

## Key Information
- Free tier: 30fps, limited sessions; Patreon ($10 lifetime): unlimited sessions, 60+ fps, HDR
- Each virtual session requires a dedicated Windows user account
- Moonlight client handles the actual streaming; Twingate handles secure network access
- Architecture: Remote Device → Twingate Client → Twingate Cloud → Connector on Gaming PC → Duo Service

## Prerequisites
- Windows 11 23H2 or newer with gaming GPU (Nvidia/AMD/Intel)
- Twingate account with Admin Console access
- WSL (Ubuntu) or Docker Desktop for Connector deployment
- Moonlight client on each remote device

## Step-by-Step

1. **Install Duo** – Download `Duo.exe`, run as Administrator, select all components, reboot
2. **Configure Duo** – Access `http://localhost:47990`, set GPU encoder (NVENC/AMF/QuickSync)
3. **Create Windows user** per session:
   ```
   net user "RemoteUser" "StrongPassword123!" /add
   net localgroup "Users" "RemoteUser" /add
   ```
4. **Create virtual session** in Duo web UI → Sessions Management → Add New Virtual Session
5. **Deploy Twingate Connector** on gaming PC via WSL (recommended) or Docker
6. **Add Duo as Twingate Resource** with private IP address
7. **Install Twingate Client** on all remote devices, sign in, connect
8. **Install Moonlight** on remote devices, add PC by private IP, complete PIN pairing via Duo web UI
9. **Select virtual session** in Moonlight to start gaming

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Duo Web UI | `http://localhost:47990` |
| TCP Ports | `47984-47990` (Web UI + HTTPS) |
| UDP Ports | `47998-48010` (streaming, multi-session) |
| Connector deployment | WSL Ubuntu (recommended) or Docker |
| Check Duo service | `sc query DuoService` |
| Check TermWrap service | `sc query TermWrap` |

## Resource Planning
- **Per session minimum**: 4GB RAM, 2 CPU cores (recommended: 8GB, 4 cores)
- **16GB/8-core/RTX 3070**: 2–3 concurrent sessions
- **32GB/12-core/RTX 4080**: 4–5 concurrent sessions

## Gotchas
- Windows 10 is **not supported**; requires Windows 11 23H2+
- Free tier hard-limited to 30Hz; 60+ fps requires Patreon activation
- Some anti-cheat systems do not work in virtual sessions
- Connector must remain running continuously for remote access
- If connection fails in Moonlight, try `127.0.0.1` instead of private IP
- Remote Desktop must be enabled: Settings → System → Remote Desktop

## Related Docs
- [Sunshine Remote Streaming](https://www.twingate.com/docs/game-streaming-sunshine) – single-user streaming
- [Apollo Remote Streaming](https://www.twingate.com/docs/game-streaming-apollo) – automatic virtual displays
- [Game Streaming Overview](https://www.twingate.com/docs/game-streaming) – compare options
- [Connector Deployment Guides](https://www.twingate.com/docs/connector)
- [Resource Access Configuration](https://www.twingate.com/docs/access-control)
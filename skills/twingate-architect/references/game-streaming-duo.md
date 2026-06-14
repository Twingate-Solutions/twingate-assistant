# Duo Multi-User Remote Game Streaming with Twingate

## Summary
Duo enables multiple users to play different games simultaneously on one Windows PC using virtual sessions. This guide covers integrating Duo with Twingate Zero Trust access so remote users can stream securely without port forwarding. Setup takes approximately 30 minutes.

## Key Information
- Duo creates isolated virtual Windows sessions per user, each with dedicated resources
- Twingate replaces port forwarding with encrypted outbound-only tunnels
- Free tier: 30fps max, limited sessions; Patreon ($10 lifetime): unlimited sessions, 60+ fps, HDR
- Moonlight is the streaming client used to connect to Duo sessions
- Windows 11 23H2+ required; Windows 10 not supported

## Prerequisites
- Windows 11 (23H2 or newer) PC with dedicated gaming GPU
- Twingate account with Admin Console access
- WSL (Ubuntu) or Docker Desktop for Connector deployment
- Moonlight client on each remote device
- Twingate client on each remote device

## Step-by-Step

1. **Install Duo** — Download `Duo.exe`, run as Administrator, select all components, reboot
2. **Configure Duo** — Access `http://localhost:47990`, set GPU encoder (NVENC/AMF/QuickSync)
3. **Create virtual sessions** — Create Windows user accounts via PowerShell, then create sessions in Duo web UI
4. **Deploy Twingate Connector** — Via WSL (recommended) or Docker on the gaming PC
5. **Add Duo as Twingate Resource** — Private IP with specific TCP/UDP port ranges
6. **Assign access** — Add user groups to the resource in Admin Console
7. **Install clients** — Twingate Client + Moonlight on each remote device
8. **Pair Moonlight** — Enter gaming PC IP, complete 4-digit PIN pairing in Duo web UI

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Duo Web UI | `http://localhost:47990` |
| TCP Ports | `47984-47990` (Web UI + HTTPS) |
| UDP Ports | `47998-48010` (streaming, multi-session) |
| Add Windows user | `net user "Username" "Password!" /add` |
| Add to Users group | `net localgroup "Users" "Username" /add` |
| Check Duo service | `sc query DuoService` |
| Check TermWrap | `sc query TermWrap` |

## Gotchas
- Each virtual session requires a **separate Windows user account**
- Anti-cheat systems may not work in virtual sessions
- Connector must remain running continuously for streaming to work
- First session start may be slow (Windows initializes new virtual environment)
- Free tier hard-limited to 30Hz — requires Patreon link to unlock 60+ fps
- Per session minimum: 4GB RAM, 2 CPU cores (8GB/4 cores recommended)
- Some games require windowed mode if fullscreen causes issues

## Resource Planning
| Hardware | Estimated Sessions |
|----------|-------------------|
| 16GB RAM, 8-core, RTX 3070 | 2–4 sessions |
| 32GB RAM, 12-core, RTX 4080 | 4–6 sessions |

## Related Docs
- [Sunshine Remote Streaming](https://www.twingate.com/docs/game-streaming-sunshine) — single-user streaming
- [Apollo Remote Streaming](https://www.twingate.com/docs/game-streaming-apollo) — automatic virtual displays
- [Game Streaming Overview](https://www.twingate.com/docs/game-streaming) — compare options
- [Connector Deployment Guides](https://www.twingate.com/docs/connector)
- [Resource Access Configuration](https://www.twingate.com/docs/access-configuration)
- [Duo GitHub Repository](https://github.com/blackseraph/duo)
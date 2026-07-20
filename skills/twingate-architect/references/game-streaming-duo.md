# Duo Multi-User Remote Game Streaming with Twingate

## Summary
Duo enables multiple users to stream different games simultaneously from a single Windows 11 PC. This guide covers integrating Duo with Twingate for secure Zero Trust remote access, eliminating port forwarding requirements. Setup targets under 30 minutes.

## Key Information
- Free tier: limited to 30Hz/30fps, limited concurrent users
- Patreon tier ($10 lifetime): unlimited simultaneous sessions, 60+ fps, HDR
- Moonlight is the streaming client used on remote devices
- Twingate Connector creates outbound-only connection; no inbound ports needed
- Each concurrent user requires a separate Windows user account and Duo virtual session

## Prerequisites
- Windows 11 (23H2 or newer) — Windows 10 not supported
- Gaming GPU (Nvidia/AMD/Intel)
- Twingate account
- WSL (Ubuntu) or Docker for Connector deployment
- Moonlight client on each remote device

## Step-by-Step

1. **Install Duo** — Run installer as Administrator, select all components, reboot
2. **Configure Duo** — Access `http://localhost:47990`, set GPU encoder (NVENC/AMF/QuickSync)
3. **Create Windows user accounts** — One per streaming user via PowerShell:
   ```
   net user "RemoteUser" "Password!" /add
   net localgroup "Users" "RemoteUser" /add
   ```
4. **Create virtual sessions** — In Duo web UI → Sessions Management → Add New Virtual Session
5. **Deploy Twingate Connector** — Via WSL (recommended) or Docker on gaming PC
6. **Add Duo as Twingate Resource**:
   - Address: gaming PC private IP
   - TCP ports: `47984-47990`
   - UDP ports: `47998-48010`
7. **Install Twingate Client** on each remote device, sign in, connect
8. **Install Moonlight** on each remote device
9. **Pair Moonlight** — Add PC by private IP, enter 4-digit PIN in Duo web UI → PIN section

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Duo Web UI | `http://localhost:47990` |
| TCP Ports | `47984-47990` |
| UDP Ports | `47998-48010` |
| Nvidia encoder | NVENC |
| AMD encoder | AMF |
| Intel encoder | QuickSync |

## Gotchas
- Virtual sessions require `TermWrap` service running (`sc query TermWrap`)
- Windows Remote Desktop must be enabled for virtual sessions to start
- Some anti-cheat systems incompatible with virtual sessions
- 30Hz cap is hard-limited on free tier; requires Patreon link to unlock
- Twingate Connector must stay running continuously for remote access to work
- Each additional user needs: Windows account + Duo session + Moonlight pairing

## Resource Planning
| RAM | CPU | GPU | Sessions |
|-----|-----|-----|----------|
| 16GB | 8-core | RTX 3070 | 2–4 |
| 32GB | 12-core | RTX 4080 | 4–6 |
- Minimum per session: 4GB RAM, 2 CPU cores

## Related Docs
- [Sunshine Remote Streaming](https://www.twingate.com/docs) — single-user streaming
- [Apollo Remote Streaming](https://www.twingate.com/docs) — automatic virtual displays
- [Connector Deployment Guides](https://www.twingate.com/docs)
- [Duo GitHub Repository](https://github.com)
- [Moonlight Releases](https://github.com/moonlight-stream)
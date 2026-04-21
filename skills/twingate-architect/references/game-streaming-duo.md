## Duo Multi-User Remote Game Streaming with Twingate

Duo enables multiple users to game simultaneously on one Windows PC by creating isolated virtual Windows sessions, each with dedicated resources. The free tier supports 30fps and limited sessions; a one-time $10 Patreon pledge unlocks unlimited simultaneous sessions and 60+ fps. Twingate provides secure access without port forwarding.

**Key Information**
- Requires Windows 11 23H2 or newer -- Windows 10 is not supported
- Free tier: 30Hz/30fps limit; Patreon ($10 lifetime): unlimited sessions, 60+ fps, HDR
- Twingate Resource ports: TCP 47984-47990, UDP 47998-48010 (wider UDP range for multiple concurrent sessions)
- Each virtual session requires a dedicated Windows local user account
- Per-session minimums: 4GB RAM (8GB recommended), 2 CPU cores (4 recommended)
- Connector on gaming PC: WSL (recommended) or Docker Desktop
- Client: Moonlight on all platforms; each user has their own Twingate account and Moonlight client
- Duo web UI: `http://localhost:47990`; pairing via 4-digit PIN in web UI

**Prerequisites**
- Windows 11 23H2 or newer with gaming-capable GPU
- Twingate account (one per streaming user)
- Duo installed (free from GitHub releases or Patreon)

**Step-by-Step**
1. Install Duo as Administrator (select all components); reboot
2. For each user: `net user "Username" "Password" /add` and `net localgroup "Users" "Username" /add`
3. In Duo web UI -> Sessions Management -> Add New Virtual Session; assign Windows user; set resolution; Start
4. Deploy Twingate Connector via WSL or Docker; create Resource (TCP 47984-47990, UDP 47998-48010); assign to group
5. Each family member: install Twingate Client, sign in, connect; install Moonlight; add PC by private IP; pair via PIN
6. For Patreon features: link Patreon in Duo web UI -> Settings -> Patreon

**Configuration Values**
- Check Duo service: `sc query DuoService`
- Check TermWrap service (required for virtual sessions): `sc query TermWrap`
- Enable Remote Desktop: Settings -> System -> Remote Desktop -> Enable

**Gotchas**
- Windows 11 23H2 is a hard requirement; Windows 10 is not compatible
- Free tier is hard-capped at 30Hz -- this is expected behavior, not a bug
- Anti-cheat systems (Easy Anti-Cheat, BattleEye) may not work in virtual sessions
- Monitor session resources via Task Manager; start with 2 sessions and scale gradually

**Related Docs**
- /docs/game-streaming-remote
- /docs/game-streaming-sunshine
- /docs/game-streaming-apollo

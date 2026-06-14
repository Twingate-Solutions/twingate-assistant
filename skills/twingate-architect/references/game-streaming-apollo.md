# Apollo Remote Game Streaming with Twingate

## Page Title
Apollo Remote Game Streaming with Twingate

## Summary
Apollo extends Sunshine with automatic virtual display management (via SudoVDA), enabling headless PC game streaming without a physical monitor. Combined with Twingate, streaming is secured via Zero Trust access—no port forwarding required. Setup takes under 30 minutes.

## Key Information
- Apollo auto-creates virtual displays matching client resolution via SudoVDA
- Twingate Connector makes outbound-only connections; no inbound ports exposed
- Works with Moonlight clients (all platforms) or Artemis (Android, enhanced features)
- SudoVDA must be selected during Apollo installation or virtual displays won't work

## Prerequisites
- Windows PC with gaming GPU (Nvidia/AMD/Intel)
- Twingate account
- Remote streaming device (laptop/phone/tablet)
- WSL (recommended) or Docker for Connector deployment

## Step-by-Step

1. **Install Apollo** — Download from Apollo Releases, run as Administrator, check "SudoVDA Virtual Display Driver", reboot
2. **Configure Apollo** — Access `http://localhost:47990`, set encoder per GPU (NVENC/AMF/QuickSync)
3. **Deploy Twingate Connector** — Create Remote Network in Admin Console, deploy via WSL (recommended) or Docker
4. **Create Twingate Resource** — Add gaming PC's private IP with required ports
5. **Install Twingate Client** — On remote device, sign in, connect
6. **Install Moonlight or Artemis** — On streaming device
7. **Pair client** — Add PC by private IP in Moonlight, enter 4-digit PIN in Apollo web UI at PIN section

## Configuration Values

**Apollo Ports (Twingate Resource):**
| Protocol | Ports | Purpose |
|----------|-------|---------|
| TCP | 47984-47990 | Web UI + HTTPS |
| UDP | 47998-48000 | Streaming |

**Apollo Web UI:** `http://localhost:47990` (local only by default)

**GPU Encoder Settings:**
- Nvidia → NVENC
- AMD → AMF
- Intel → QuickSync

**Check Apollo service:**
```
sc query ApolloService
```

**Find local IP:**
```
ipconfig
```

## Gotchas
- SudoVDA must be checked at install time; if missed, fully uninstall/reinstall Apollo and reboot
- Apollo web UI (port 47990) is local-only; add TCP 47990 to Twingate Resource only if remote web UI access needed
- Connector must stay running for streaming to work; WSL/Docker handle background persistence
- Always use the PC's **private IP** in Moonlight/Artemis even when streaming remotely (Twingate handles routing)
- Recommended starting bitrate: 15–20 Mbps for 1080p; use wired ethernet on gaming PC

## Related Docs
- [Sunshine Remote Streaming](https://www.twingate.com/docs) — traditional display streaming
- [Duo Remote Streaming](https://www.twingate.com/docs) — multi-user simultaneous gaming
- [Game Streaming Overview](https://www.twingate.com/docs) — compare all options
- [Connector Deployment Guides](https://www.twingate.com/docs)
- [Resource Access Configuration](https://www.twingate.com/docs)
- [Apollo GitHub Repository](https://github.com/ClassicOldSong/Apollo)
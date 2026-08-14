---
source: https://www.twingate.com/docs/game-streaming-apollo
type: docs
fetched: 2026-08-14
source_version: 6822f70e55a4760ce08881aa6370d2bc2a78791a4c665f7b8e637149b7fa35de
---

# Apollo Remote Game Streaming with Twingate

## Page Title
Apollo Remote Game Streaming with Twingate

## Summary
Apollo extends Sunshine with automatic virtual display management via SudoVDA, enabling headless PC game streaming without a physical monitor. Combined with Twingate Zero Trust access, it eliminates port forwarding requirements while providing secure remote streaming. Setup takes under 30 minutes.

## Key Information
- Apollo automatically creates virtual displays matching client resolution via SudoVDA
- No port forwarding or inbound firewall rules needed — Twingate uses outbound-only connections
- Compatible with Moonlight clients (all platforms) and Artemis (Android-enhanced client)
- Web UI (port 47990) is local-only by default; add it to Twingate Resource only if remote config needed

## Prerequisites
- Windows PC with gaming GPU (Nvidia/AMD/Intel)
- Twingate account
- Remote streaming device (laptop, phone, tablet)
- WSL (Ubuntu) or Docker Desktop for Connector deployment

## Step-by-Step

1. **Install Apollo** — Download `Apollo-x.x.x.exe`, run as Administrator, ensure "SudoVDA Virtual Display Driver" is checked, reboot
2. **Configure Apollo** — Open `http://localhost:47990`, set encoder: NVENC (Nvidia), AMF (AMD), QuickSync (Intel)
3. **Deploy Twingate Connector** — Create Remote Network in Admin Console, deploy Connector via WSL (recommended) or Docker on gaming PC
4. **Create Twingate Resource** — Add gaming PC's private IP with specified ports (see below)
5. **Install Twingate Client** — On remote device, sign in, connect, verify Apollo resource appears
6. **Install Moonlight/Artemis** — On remote device
7. **Pair client** — Add PC by private IP, enter 4-digit PIN in Apollo web UI at PIN section

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Apollo Web UI | `http://localhost:47990` |
| TCP Ports (Resource) | `47984-47990` (Web UI + HTTPS) |
| UDP Ports (Resource) | `47998-48000` (Streaming) |
| WSL install command | `wsl --install` |
| Check Apollo service | `sc query ApolloService` |
| Find local IP | `ipconfig` (look for IPv4 under active adapter) |

## Gotchas
- **SudoVDA must be selected during installation** — cannot be added after; requires full reinstall if missed
- Reboot required after Apollo installation for SudoVDA driver to initialize
- Connector must remain running continuously for remote streaming to work
- Always use the PC's **private IP** in Moonlight/Artemis even when streaming remotely (Twingate handles routing)
- WSL preferred over Docker Desktop to avoid VM overhead and additional background services
- Verify correct Remote Network is selected when assigning Resources if multiple networks exist

## Troubleshooting
- **Can't connect**: Check Twingate shows "Connected", verify `sc query ApolloService`
- **Virtual display missing**: Device Manager → Display adapters → should show "SudoVDA Virtual Display"
- **Poor performance**: Start at 15-20 Mbps for 1080p, use wired ethernet on gaming PC
- **Pairing fails**: Restart pairing process, restart Apollo from system tray

## Related Docs
- [Sunshine Remote Streaming](https://www.twingate.com/docs) — traditional display streaming
- [Duo Remote Streaming](https://www.twingate.com/docs) — multi-user simultaneous gaming
- [Connector Deployment Guides](https://www.twingate.com/docs)
- [Resource Access Configuration](https://www.twingate.com/docs)
- [Apollo GitHub Repository](https://github.com/apolloapp/apollo)
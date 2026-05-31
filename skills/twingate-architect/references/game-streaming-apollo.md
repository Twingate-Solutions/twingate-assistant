# Apollo Remote Game Streaming with Twingate

## Page Title
Apollo Remote Game Streaming with Twingate

## Summary
Apollo extends Sunshine with automatic virtual display management (via SudoVDA), enabling headless PC game streaming without a physical monitor. This guide configures Apollo on a Windows gaming PC with Twingate Zero Trust access, eliminating port forwarding requirements. Setup takes approximately 30 minutes.

## Key Information
- Apollo includes SudoVDA for automatic virtual display creation matching client resolution
- Twingate Connector creates outbound-only encrypted tunnel — no inbound ports or port forwarding needed
- Compatible streaming clients: Moonlight (all platforms) and Artemis (Android-only, enhanced features)
- Apollo web UI (port 47990) is local-only by default

## Prerequisites
- Windows PC with Nvidia/AMD/Intel gaming GPU
- Twingate account with Admin Console access
- Remote device for streaming (laptop, phone, tablet)
- WSL (Ubuntu) or Docker Desktop for Connector deployment

## Step-by-Step

1. **Install Apollo** — Download `Apollo-x.x.x.exe`, run as Administrator, ensure "SudoVDA Virtual Display Driver" is checked, reboot
2. **Configure Apollo** — Access `http://localhost:47990`, set encoder per GPU (NVENC/AMF/QuickSync)
3. **Deploy Twingate Connector** — Create/select Remote Network in Admin Console, deploy via WSL (recommended) or Docker on gaming PC
4. **Create Twingate Resource** — Add gaming PC private IP with specified ports
5. **Install Twingate Client** — On remote/streaming device, sign in and connect
6. **Install Moonlight or Artemis** — On streaming device
7. **Pair client** — Add PC by private IP in Moonlight, enter 4-digit PIN in Apollo web UI under PIN section

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Apollo Web UI | `http://localhost:47990` |
| TCP ports (Resource) | `47984-47990` (Web UI + HTTPS) |
| UDP ports (Resource) | `47998-48000` (Streaming) |
| Apollo service check | `sc query ApolloService` |
| Find local IP | `ipconfig` (look for IPv4 under active adapter) |
| Encoder - Nvidia | NVENC |
| Encoder - AMD | AMF |
| Encoder - Intel | QuickSync |

## Gotchas
- **SudoVDA must be selected during installation** — cannot be added after; requires full reinstall if missed
- Connector must remain running continuously for remote streaming
- Always use the PC's **private IP** in Moonlight/Artemis — Twingate handles routing even remotely
- Add TCP 47990 to Resource only if remote web UI access is needed (security consideration)
- Poor performance: start at 15-20 Mbps for 1080p; use wired ethernet on gaming PC

## Troubleshooting Quick Reference
- Virtual display missing: Device Manager → Display adapters → verify "SudoVDA Virtual Display" present
- Can't connect: verify Twingate Client shows "Connected" and resource is visible
- Pairing fails: restart Apollo from system tray, generate new PIN

## Related Docs
- [Sunshine Remote Streaming](https://www.twingate.com/docs) — traditional display streaming alternative
- [Duo Remote Streaming](https://www.twingate.com/docs) — multi-user simultaneous gaming
- [Connector Deployment Guides](https://www.twingate.com/docs) — detailed installation options
- [Resource Access Configuration](https://www.twingate.com/docs) — managing permissions
- [Apollo GitHub Repository](https://github.com) — upstream documentation
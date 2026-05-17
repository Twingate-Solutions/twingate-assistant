# Apollo Remote Game Streaming with Twingate

## Summary
Apollo is a game streaming server (extends Sunshine) with built-in SudoVDA for automatic virtual display management, enabling headless PC game streaming. Combined with Twingate, it provides secure remote streaming without port forwarding. Setup takes ~30 minutes.

## Key Information
- Apollo automatically creates virtual displays matching client resolution via SudoVDA
- No physical monitor required; no inbound ports or port forwarding needed
- Compatible with Moonlight clients (all platforms) and Artemis (Android-enhanced client)
- Twingate Connector creates outbound-only encrypted tunnel; gaming PC stays private

## Prerequisites
- Windows PC with gaming GPU (Nvidia/AMD/Intel)
- Twingate account with Admin Console access
- Remote device (laptop/phone/tablet) for streaming
- WSL (Ubuntu) or Docker Desktop for Connector deployment

## Step-by-Step

1. **Install Apollo** — Download `Apollo-x.x.x.exe`, run as Administrator, ensure **SudoVDA Virtual Display Driver** is checked, reboot
2. **Configure Apollo** — Access `http://localhost:47990`, set encoder (NVENC/AMF/QuickSync) per GPU
3. **Deploy Twingate Connector** — Create Remote Network in Admin Console; deploy via WSL (recommended) or Docker on gaming PC
4. **Create Twingate Resource** — Add gaming PC private IP with specified ports; assign group access
5. **Install Twingate Client** on remote device; sign in and connect
6. **Install Moonlight or Artemis** on remote device
7. **Pair client** — Add PC by private IP in Moonlight, enter 4-digit PIN in Apollo web UI at `/PIN`

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Apollo Web UI | `http://localhost:47990` |
| TCP ports (Resource) | `47984-47990` (Web UI + HTTPS) |
| UDP ports (Resource) | `47998-48000` (Streaming) |
| Check Apollo service | `sc query ApolloService` |
| Nvidia encoder | NVENC |
| AMD encoder | AMF |
| Intel encoder | QuickSync |

## Gotchas
- **SudoVDA must be selected during installation** — cannot be added after; requires full reinstall if missed
- Verify in Device Manager → Display adapters → "SudoVDA Virtual Display" after reboot
- Apollo web UI (port 47990) is local-only by default; add TCP 47990 to Resource only if remote config access is needed
- Use gaming PC's **private IP** in Moonlight even when streaming remotely (Twingate handles routing)
- Connector must remain running; WSL/Docker runs it as background service
- Start streaming bitrate at 15–20 Mbps for 1080p; use wired ethernet on gaming PC

## Related Docs
- [Sunshine Remote Streaming](https://www.twingate.com/docs) — traditional display streaming alternative
- [Duo Remote Streaming](https://www.twingate.com/docs) — multi-user simultaneous gaming
- [Connector Deployment Guides](https://www.twingate.com/docs)
- [Apollo GitHub Repository](https://github.com/LizardByte/Apollo) — full Apollo documentation
# Apollo Remote Game Streaming with Twingate

## Page Title
Apollo Remote Game Streaming with Twingate

## Summary
Apollo extends Sunshine with automatic virtual display management (via SudoVDA), enabling headless PC game streaming without a physical monitor. This guide configures Apollo on a Windows gaming PC with Twingate Zero Trust access, eliminating port forwarding requirements. Setup takes under 30 minutes.

## Key Information
- Apollo auto-creates virtual displays matching client resolution via SudoVDA
- No inbound ports or port forwarding needed — Twingate Connector uses outbound connections only
- Compatible with Moonlight clients (all platforms) and Artemis (Android-only enhanced client)
- Apollo web UI (port 47990) is local-only by default

## Prerequisites
- Windows PC with gaming GPU (Nvidia, AMD, or Intel)
- Twingate account with Admin Console access
- Remote device for streaming (laptop, phone, tablet)
- WSL (Ubuntu) or Docker Desktop for Connector deployment

## Step-by-Step

1. **Install Apollo** — Download `Apollo-x.x.x.exe`, run as Administrator, ensure **SudoVDA Virtual Display Driver** is checked, reboot
2. **Configure Apollo** — Access `http://localhost:47990`, set encoder (NVENC/AMF/QuickSync) per GPU type
3. **Deploy Twingate Connector** — Create Remote Network in Admin Console; deploy via WSL (recommended) or Docker on gaming PC
4. **Create Twingate Resource** — Add gaming PC's private IP with specified ports (see below)
5. **Assign Access** — Add user group to resource in Admin Console
6. **Install Twingate Client** — On remote/streaming device; sign in and connect
7. **Install Moonlight or Artemis** — On remote device
8. **Pair client** — Add PC by private IP in Moonlight, enter 4-digit PIN in Apollo web UI under PIN section

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Apollo Web UI | `http://localhost:47990` |
| TCP Ports (Resource) | `47984-47990` (Web UI + HTTPS) |
| UDP Ports (Resource) | `47998-48000` (Streaming) |
| Nvidia encoder | NVENC |
| AMD encoder | AMF |
| Intel encoder | QuickSync |
| Apollo service check | `sc query ApolloService` |
| WSL install command | `wsl --install` |

## Gotchas
- **SudoVDA must be selected during installation** — if missed, fully uninstall and reinstall Apollo; a reboot is required after install
- Connector must remain running continuously for remote streaming to work
- Always use the PC's **private IP** in Moonlight/Artemis even when streaming remotely (Twingate handles routing)
- If remote web UI access is needed, explicitly add TCP port 47990 to the Twingate Resource
- Start bitrate at 15–20 Mbps for 1080p; wired ethernet recommended on gaming PC
- Verify SudoVDA appears in Device Manager → Display adapters as "SudoVDA Virtual Display"

## Related Docs
- [Sunshine Remote Streaming](https://www.twingate.com/docs/) — traditional display streaming alternative
- [Duo Remote Streaming](https://www.twingate.com/docs/) — multi-user simultaneous gaming
- [Connector Deployment Guides](https://www.twingate.com/docs/) — detailed installation options
- [Resource Access Configuration](https://www.twingate.com/docs/) — managing permissions
- [Apollo GitHub Repository](https://github.com/) — upstream documentation and community support
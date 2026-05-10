# Apollo Remote Game Streaming with Twingate

## Summary
Apollo extends Sunshine with automatic virtual display management via SudoVDA, enabling headless PC game streaming without a physical monitor. Combined with Twingate, it provides secure remote access without port forwarding. Setup takes ~30 minutes.

## Key Information
- Apollo auto-creates virtual displays matching client resolution via SudoVDA
- No port forwarding or inbound firewall rules required
- Twingate Connector makes outbound-only connections
- Works with Moonlight clients (all platforms) and Artemis (Android-only enhanced client)

## Prerequisites
- Windows PC with Nvidia/AMD/Intel gaming GPU
- Twingate account with Admin Console access
- Remote device for streaming (any platform)
- WSL (Ubuntu) or Docker Desktop for Connector deployment

## Step-by-Step

1. **Install Apollo** — Download `Apollo-x.x.x.exe`, run as Administrator, ensure **SudoVDA Virtual Display Driver** is checked, reboot
2. **Verify Apollo** — Check Device Manager → Display adapters for "SudoVDA Virtual Display"; access web UI at `http://localhost:47990`
3. **Configure encoder** — Set GPU encoder in Apollo UI: Nvidia→NVENC, AMD→AMF, Intel→QuickSync
4. **Deploy Twingate Connector** — Create/select Remote Network in Admin Console; deploy via WSL (recommended) or Docker on gaming PC
5. **Create Twingate Resource** — Add resource with gaming PC's private IP and ports below
6. **Assign access** — Add user group to resource in Admin Console Access tab
7. **Install Twingate Client** on remote device, sign in, connect
8. **Install Moonlight or Artemis** on remote device
9. **Pair client** — Add PC by private IP in Moonlight/Artemis, enter 4-digit PIN at `http://localhost:47990` → PIN section

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Apollo Web UI | `http://localhost:47990` |
| TCP Ports (Resource) | `47984-47990` (Web UI + HTTPS) |
| UDP Ports (Resource) | `47998-48000` (Streaming) |
| Apollo service check | `sc query ApolloService` |
| Recommended starting bitrate | 15-20 Mbps for 1080p |

## Gotchas
- **SudoVDA must be selected during install** — cannot add after the fact without full reinstall + reboot
- Apollo web UI (47990) is local-only by default; add TCP 47990 to Twingate Resource only if remote web UI access needed
- Connector must stay running continuously — WSL/Docker handle background persistence
- Always use the PC's **private IP** in Moonlight/Artemis even when streaming remotely (Twingate handles routing)
- Correct Remote Network must be selected when creating Resource if multiple exist

## Troubleshooting Quick Reference
- **Can't connect**: Verify Twingate shows "Connected" and run `sc query ApolloService`
- **SudoVDA missing**: Device Manager → Display adapters; reinstall Apollo if absent
- **Pairing fails**: Restart pairing flow, verify Apollo service running
- **Poor performance**: Use wired ethernet on gaming PC, reduce bitrate, check hardware encoding config

## Related Docs
- [Sunshine Remote Streaming](https://www.twingate.com/docs/sunshine-streaming) — traditional display streaming alternative
- [Duo Remote Streaming](https://www.twingate.com/docs/duo-streaming) — multi-user simultaneous gaming
- [Game Streaming Overview](https://www.twingate.com/docs/game-streaming) — compare all options
- [Connector Deployment Guides](https://www.twingate.com/docs/connector) — detailed installation
- [Apollo GitHub Repository](https://github.com/ClassicOldSong/Apollo) — upstream documentation
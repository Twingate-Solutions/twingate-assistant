# Apollo Remote Game Streaming with Twingate

## Summary
Apollo extends Sunshine with automatic virtual display management (SudoVDA), enabling headless PC game streaming. Combined with Twingate, it eliminates port forwarding by routing streaming traffic through encrypted Zero Trust tunnels. Setup takes ~30 minutes.

## Key Information
- Apollo auto-creates virtual displays matching client resolution via SudoVDA — no physical monitor required
- Twingate Connector makes outbound-only connections; no inbound ports exposed
- Compatible with Moonlight clients (all platforms) and Artemis (Android-only enhanced client)
- Apollo web UI (port 47990) is local-only by default

## Prerequisites
- Windows PC with Nvidia/AMD/Intel gaming GPU
- Twingate account with Admin Console access
- Remote device for streaming (any platform)
- WSL (Ubuntu) or Docker Desktop for Connector deployment

## Step-by-Step

1. **Install Apollo** — Download `Apollo-x.x.x.exe`, run as Administrator, ensure **SudoVDA Virtual Display Driver** is checked, reboot
2. **Verify SudoVDA** — Device Manager → Display adapters → confirm "SudoVDA Virtual Display" appears
3. **Configure Apollo** — `http://localhost:47990` → Configuration → select GPU encoder (NVENC/AMF/QuickSync)
4. **Deploy Twingate Connector** — Create/select Remote Network in Admin Console; deploy via WSL (recommended) or Docker on gaming PC
5. **Create Twingate Resource** — Add gaming PC private IP with streaming port ranges
6. **Assign access** — Add user group to resource in Admin Console
7. **Install Twingate Client** on remote device, sign in, connect
8. **Install Moonlight or Artemis** on remote device
9. **Pair client** — Add PC by private IP in client, enter 4-digit PIN in Apollo web UI under PIN section
10. **Stream** — Select Desktop or game; Apollo auto-creates virtual display

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
| Recommended starting bitrate | 15–20 Mbps for 1080p |

## Gotchas
- **SudoVDA must be selected during installation** — reinstall required if missed; cannot add after the fact without full uninstall
- Reboot required after Apollo install to initialize SudoVDA driver
- Twingate Connector must stay running continuously (WSL/Docker handle this)
- Always use the PC's **private IP** in Moonlight/Artemis, even when streaming remotely over Twingate
- Add TCP 47990 to Twingate Resource only if remote web UI access is needed
- Select correct Remote Network when creating the Resource if multiple exist

## Related Docs
- [Sunshine Remote Streaming](https://www.twingate.com/docs) — traditional display streaming alternative
- [Duo Remote Streaming](https://www.twingate.com/docs) — multi-user simultaneous gaming
- [Connector Deployment Guides](https://www.twingate.com/docs) — detailed installation options
- [Resource Access Configuration](https://www.twingate.com/docs) — managing permissions
- [Apollo GitHub Repository](https://github.com) — upstream documentation and community support
# Apollo Remote Game Streaming with Twingate

## Summary
Apollo extends Sunshine with automatic virtual display management via SudoVDA, enabling headless PC game streaming. This guide sets up Apollo on a Windows gaming PC with Twingate Zero Trust access, eliminating port forwarding requirements. Total setup time: ~30 minutes.

## Key Information
- Apollo auto-creates virtual displays matching client resolution via SudoVDA driver
- No physical monitor required on host PC
- Uses outbound-only Twingate tunnel — no exposed ports or port forwarding
- Compatible with Moonlight clients (all platforms) and Artemis (Android-only enhanced client)

## Prerequisites
- Windows PC with Nvidia/AMD/Intel gaming GPU
- Twingate account with Admin Console access
- Remote device for streaming (any platform)
- WSL (Ubuntu) or Docker Desktop for Connector deployment

## Step-by-Step

1. **Install Apollo** — Download from Apollo Releases, run as Administrator, ensure **SudoVDA Virtual Display Driver** is checked, reboot
2. **Configure Apollo** — Access `http://localhost:47990`, set encoder (NVENC/AMF/QuickSync per GPU)
3. **Deploy Twingate Connector** — Create Remote Network in Admin Console, deploy Connector via WSL (`wsl --install`) or Docker on gaming PC
4. **Create Twingate Resource** — Add gaming PC private IP with TCP `47984-47990` and UDP `47998-48000`; assign group access
5. **Install Twingate Client** — On remote/streaming device, sign in, connect
6. **Install Moonlight or Artemis** — On streaming device
7. **Pair client** — Add PC by private IP in Moonlight, enter PIN in Apollo web UI at `http://localhost:47990` → PIN section

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Apollo Web UI | `http://localhost:47990` |
| TCP Ports (Resource) | `47984-47990` |
| UDP Ports (Resource) | `47998-48000` |
| Web UI port (optional remote) | `47990` TCP |
| Check Apollo service | `sc query ApolloService` |
| Nvidia encoder | NVENC |
| AMD encoder | AMF |
| Intel encoder | QuickSync |

## Gotchas
- **SudoVDA must be selected during installation** — cannot add afterward without full reinstall
- Twingate Connector must stay running; WSL/Docker handles background persistence
- Always use the PC's **private IP** in Moonlight even when streaming remotely (Twingate handles routing)
- Apollo Web UI is local-only by default; add TCP `47990` to Resource only if remote config access needed
- Starting bitrate recommendation: 15-20 Mbps for 1080p; wired ethernet strongly recommended on host
- Virtual display missing → Device Manager → Display adapters should show "SudoVDA Virtual Display"

## Related Docs
- [Sunshine Remote Streaming](https://www.twingate.com/docs/) — traditional display streaming alternative
- [Duo Remote Streaming](https://www.twingate.com/docs/) — multi-user simultaneous gaming
- [Connector Deployment Guides](https://www.twingate.com/docs/) — detailed Connector installation
- [Resource Access Configuration](https://www.twingate.com/docs/) — managing permissions
- [Apollo GitHub Repository](https://github.com/) — upstream documentation
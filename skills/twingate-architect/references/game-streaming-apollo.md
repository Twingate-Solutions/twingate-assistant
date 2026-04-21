## Apollo Remote Game Streaming with Twingate

Apollo is a Sunshine fork that adds automatic virtual display management via SudoVDA, enabling headless game streaming without a physical monitor. The gaming PC runs Apollo + a Twingate Connector (via WSL or Docker); remote devices run the Twingate Client + Moonlight (or Artemis on Android) to stream over the encrypted tunnel with no port forwarding.

**Key Information**
- Twingate Resource ports: TCP 47984-47990 (web UI + HTTPS streaming), UDP 47998-48000 (stream data)
- Apollo web UI: `http://localhost:47990` (local only by default; add TCP 47990 to Resource for remote admin)
- SudoVDA must be selected during Apollo installation for automatic virtual displays -- cannot be added later without reinstall
- Reboot required after installation to initialize SudoVDA
- Connector on gaming PC: WSL (recommended, low overhead) or Docker Desktop
- Encoder selection in Apollo web UI: NVENC (Nvidia), AMF (AMD), QuickSync (Intel)
- Client apps: Moonlight (all platforms) or Artemis (Android only, adds clipboard sync and advanced permissions)
- Pairing: Moonlight shows a 4-digit PIN; enter it in Apollo web UI -> PIN section

**Prerequisites**
- Windows PC with gaming-capable GPU (Nvidia, AMD, or Intel)
- Twingate account
- WSL or Docker Desktop for Connector deployment
- Remote device (laptop, phone, tablet) for streaming

**Step-by-Step**
1. Install Apollo as Administrator; check "SudoVDA Virtual Display Driver" during install; reboot
2. Open Apollo web UI at `http://localhost:47990`; create admin credentials; set GPU encoder
3. Deploy Twingate Connector via WSL (`wsl --install` then run Linux Connector command) or Docker
4. Create Twingate Resource: gaming PC private IP, TCP 47984-47990, UDP 47998-48000; assign to group
5. Install Twingate Client on remote device; sign in and connect
6. Install Moonlight on remote device; add PC by private IP; enter pairing PIN in Apollo web UI

**Configuration Values**
- Verify SudoVDA: Device Manager -> Display adapters -> "SudoVDA Virtual Display"
- Check Apollo service: `sc query ApolloService`

**Gotchas**
- SudoVDA is not installed by default in all Apollo builds -- explicitly check the box during installation
- Without SudoVDA, a physical monitor must be connected for streaming to work
- Connector must remain running; use WSL or Docker (not a PowerShell window that might close)
- Apollo web UI port 47990 is local-only by default; expose it via Twingate only if remote config is needed

**Related Docs**
- /docs/game-streaming-remote
- /docs/game-streaming-sunshine
- /docs/game-streaming-duo

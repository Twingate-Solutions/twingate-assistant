## Sunshine Remote Game Streaming with Twingate

Sunshine is an open-source, self-hosted game streaming server (maintained by LizardByte) that implements the Nvidia GameStream protocol, paired with the Moonlight client. The gaming PC runs Sunshine + a Twingate Connector (via WSL or Docker); remote devices use Twingate Client + Moonlight over an encrypted tunnel with no port forwarding.

**Key Information**
- Twingate Resource ports: TCP 47984-47990 (web UI + HTTPS streaming), UDP 47998-48000 (stream data)
- Sunshine web UI: `http://localhost:47990` (local only by default)
- Install via winget: `winget install LizardByte.Sunshine` or manual installer from Sunshine Releases
- Connector on gaming PC: WSL (recommended) or Docker Desktop
- Encoder selection in Sunshine web UI: NVENC (Nvidia), AMF (AMD), QuickSync (Intel) -- hardware encoder required
- Requires a physical monitor connected unless a virtual display driver (IddSampleDriver) is set up separately
- Client: Moonlight on all platforms
- Pairing: Moonlight shows a 4-digit PIN; enter it in Sunshine web UI -> PIN section

**Prerequisites**
- Windows PC with gaming-capable GPU
- Twingate account
- WSL or Docker Desktop for Connector deployment
- Remote device for streaming

**Step-by-Step**
1. Install Sunshine: `winget install LizardByte.Sunshine` (or manual installer)
2. Open Sunshine web UI at `http://localhost:47990`; create admin credentials; set GPU encoder under Configuration -> Video/Audio
3. Deploy Twingate Connector via WSL (`wsl --install` then run Linux Connector command) or Docker
4. Get gaming PC's private IP: `ipconfig` in PowerShell
5. Create Twingate Resource: private IP, TCP 47984-47990, UDP 47998-48000; assign to group
6. Install Twingate Client on remote device; sign in and connect
7. Install Moonlight; add PC by private IP; Moonlight shows PIN; enter in Sunshine web UI -> PIN

**Configuration Values**
- Check Sunshine service: `sc query SunshineService`
- Streaming bitrate: start with 15-20 Mbps for 1080p in Moonlight settings

**Gotchas**
- Sunshine requires a physical monitor or virtual display driver (IddSampleDriver) for headless use -- use Apollo instead for automatic headless support
- Connector must stay running; use WSL or Docker (not a window that could close)
- Hardware encoder must be selected; Sunshine defaults may not auto-detect the GPU

**Related Docs**
- /docs/game-streaming-remote
- /docs/game-streaming-apollo
- /docs/game-streaming-duo

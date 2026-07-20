# Apollo Remote Game Streaming with Twingate

## Summary
Apollo is a game streaming server (extending Sunshine) that includes SudoVDA for automatic virtual display management, enabling headless PC game streaming. This guide covers setting up Apollo with Twingate Zero Trust access, eliminating port forwarding requirements. Setup takes approximately 30 minutes.

## Key Information
- Apollo automatically creates virtual displays matching client resolution via SudoVDA
- Twingate replaces port forwarding with encrypted outbound tunnels
- Compatible with Moonlight clients (all platforms) and Artemis (Android only)
- Web UI (port 47990) is local-only by default

## Prerequisites
- Windows PC with Nvidia/AMD/Intel gaming GPU
- Twingate account with Admin Console access
- Remote device for streaming (any platform)
- WSL or Docker for Connector deployment

## Step-by-Step

### 1. Install Apollo
- Download `Apollo-x.x.x.exe` from [Apollo Releases](https://github.com)
- Run as Administrator; **ensure SudoVDA Virtual Display Driver is checked**
- Reboot after installation
- Verify: Device Manager → Display Adapters → "SudoVDA Virtual Display"
- Access web UI: `http://localhost:47990`
- Set encoder: NVENC (Nvidia), AMF (AMD), QuickSync (Intel)

### 2. Deploy Twingate Connector
- Admin Console → Remote Networks → Add/select network
- Add Connector; deploy via WSL (recommended) or Docker
- WSL install: `wsl --install`, then Ubuntu from Microsoft Store
- Run generated token command in WSL terminal
- Verify green "Online" status in Admin Console

### 3. Create Twingate Resource
- Admin Console → Resources → Add Resource
- Configure with gaming PC's private IP (`ipconfig` to find)
- Assign access to appropriate group

### 4. Install Twingate Client on Remote Device
- Connect and verify "Apollo Gaming PC" resource is visible

### 5. Install Streaming Client
- Moonlight (all platforms) or Artemis (Android, adds clipboard sync)

### 6. Pair and Stream
- Connect Twingate client first
- In Moonlight/Artemis: Add PC → enter gaming PC's private IP
- Enter 4-digit PIN at `http://localhost:47990` → PIN section
- Select Desktop or game to start streaming

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Apollo Web UI | `http://localhost:47990` |
| TCP Ports (Resource) | `47984-47990` |
| UDP Ports (Resource) | `47998-48000` |
| Check Apollo service | `sc query ApolloService` |

## Gotchas
- **SudoVDA must be selected during installation** — reinstall required if missed; without it a physical monitor is required
- Twingate Connector must remain running continuously for remote access
- Always use the PC's **private IP** in Moonlight/Artemis even when streaming remotely
- Web UI port 47990 is included in TCP range but is local-only by default; explicitly add it to the Resource if remote config access is needed
- Wired ethernet on gaming PC strongly recommended for performance

## Troubleshooting
- Poor performance: Start at 15-20 Mbps for 1080p; use wired connection
- Virtual display missing: Reinstall Apollo with SudoVDA checked, then reboot
- Pairing fails: Restart Apollo from system tray, retry PIN

## Related Docs
- [Sunshine Remote Streaming](#) — traditional display streaming
- [Duo Remote Streaming](#) — multi-user simultaneous gaming
- [Connector Deployment Guides](#)
- [Resource Access Configuration](#)
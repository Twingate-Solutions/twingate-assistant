# Sunshine Remote Game Streaming with Twingate

## Page Title
Sunshine Remote Game Streaming with Twingate

## Summary
Sunshine is an open-source self-hosted game streaming server (Nvidia GameStream protocol) used with the Moonlight client. This guide configures Sunshine on a Windows gaming PC secured via Twingate, eliminating port forwarding by routing traffic through an encrypted Twingate Connector tunnel.

## Key Information
- Sunshine runs on Windows; Moonlight is the client (Windows/Mac/Linux/iOS/Android)
- Twingate Connector deployed on gaming PC creates outbound-only connection — no inbound ports needed
- Connector recommended via WSL (Ubuntu); Docker Desktop is alternative
- Hardware encoding required: NVENC (Nvidia), AMF (AMD), QuickSync (Intel)

## Prerequisites
- Windows PC with Nvidia/AMD/Intel GPU
- Twingate account with admin access
- Remote device with Twingate Client + Moonlight installed
- WSL (Ubuntu) or Docker Desktop on gaming PC

## Step-by-Step

1. **Install Sunshine**: `winget install LizardByte.Sunshine` or manual installer; access web UI at `http://localhost:47990`
2. **Configure encoder**: Web UI → Configuration → Video/Audio → select GPU-appropriate encoder
3. **Deploy Twingate Connector**: Admin Console → Remote Networks → Connectors → deploy via WSL or Docker
4. **Add Twingate Resource**: Resources → Add Resource with gaming PC's private IP
5. **Assign access**: Resource → Access → Add group
6. **Install Twingate Client** on remote device; connect and verify resource appears
7. **Install Moonlight** on remote device
8. **Pair**: Moonlight → Add PC → enter private IP → enter 4-digit PIN in Sunshine web UI (`http://localhost:47990` → PIN section)

## Configuration Values

| Setting | Value |
|---|---|
| Sunshine Web UI | `http://localhost:47990` |
| TCP Ports (Resource) | `47984-47990` |
| UDP Ports (Resource) | `47998-48000` |
| WSL install command | `wsl --install` |
| Service check | `sc query SunshineService` |
| Starting bitrate (1080p) | 15–20 Mbps |

## Gotchas
- Connector must stay running at all times for remote streaming to work
- Select correct Remote Network when creating the Resource (must match where Connector is deployed)
- Physical monitor must be connected, or use virtual display driver (IddSampleDriver) for headless setups
- Some games require Sunshine to run as Administrator
- Wired ethernet on gaming PC strongly recommended for performance
- Try `127.0.0.1` instead of private IP if Moonlight can't connect

## Related Docs
- Apollo Remote Streaming (automatic virtual display management)
- Duo Remote Streaming (multi-user simultaneous gaming)
- Game Streaming Overview (compare all options)
- Connector Deployment Guides
- Resource Access Configuration
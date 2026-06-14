# Sunshine Remote Game Streaming with Twingate

## Page Title
Sunshine Remote Game Streaming with Twingate

## Summary
Sunshine is an open-source self-hosted game streaming server (Nvidia GameStream protocol) paired with the Moonlight client. This guide covers installing Sunshine on a Windows gaming PC and securing remote access via Twingate, eliminating port forwarding. The Twingate Connector creates outbound-only encrypted tunnels; no inbound ports are exposed.

## Key Information
- Sunshine implements Nvidia GameStream protocol; works with Moonlight client
- No port forwarding or firewall changes required on home router
- Connector runs on gaming PC (WSL recommended over Docker on Windows)
- Supports Nvidia (NVENC), AMD (AMF), and Intel (QuickSync) hardware encoding

## Prerequisites
- Windows PC with gaming GPU (Nvidia/AMD/Intel)
- Twingate account with Admin Console access
- WSL with Ubuntu (recommended) or Docker Desktop for Connector deployment
- Remote device with Moonlight and Twingate Client installed

## Step-by-Step

1. **Install Sunshine**: `winget install LizardByte.Sunshine` or manual installer; verify at `http://localhost:47990`
2. **Configure encoder**: Admin UI → Configuration → Video/Audio → set GPU-appropriate encoder
3. **Deploy Twingate Connector**: Create/select Remote Network in Admin Console → deploy Connector via WSL (`wsl --install`, then run generated token command)
4. **Add Sunshine as Twingate Resource**: Use PC's private IP with specific port ranges
5. **Assign access**: Resources → your resource → Access → Add Group
6. **Install Twingate Client** on remote device and connect
7. **Install Moonlight** on remote device
8. **Pair**: Add PC by private IP in Moonlight → enter 4-digit PIN in Sunshine web UI at PIN section

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Sunshine Web UI | `http://localhost:47990` |
| TCP ports (Resource) | `47984-47990` |
| UDP ports (Resource) | `47998-48000` |
| Sunshine service name | `SunshineService` |
| Verify service | `sc query SunshineService` |
| Find local IP | `ipconfig` |

## Gotchas
- Connector must remain running continuously; WSL/Docker keeps it running in background
- Hardware encoding must be configured—software encoding insufficient for real-time streaming
- Black screen may occur without physical monitor connected; use virtual display driver for headless setups
- Some games require Sunshine to run as Administrator
- When troubleshooting Moonlight connection, try `127.0.0.1` if private IP fails

## Troubleshooting Reference
- **Can't connect**: Verify Twingate shows Connected; confirm resource visible in client
- **Poor performance**: Start at 15-20 Mbps for 1080p; use wired ethernet on gaming PC
- **Pairing fails**: Confirm Sunshine service running (`sc query SunshineService`); restart from tray

## Related Docs
- [Apollo Remote Streaming](https://www.twingate.com/docs/game-streaming-apollo) — automatic virtual display management
- [Duo Remote Streaming](https://www.twingate.com/docs/game-streaming-duo) — multi-user simultaneous gaming
- [Game Streaming Overview](https://www.twingate.com/docs/game-streaming) — compare all streaming options
- [Connector Deployment Guides](https://www.twingate.com/docs/connector)
- [Sunshine Official Docs](https://docs.lizardbyte.dev/projects/sunshine/)
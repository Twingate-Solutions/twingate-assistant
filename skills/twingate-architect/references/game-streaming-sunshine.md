---
source: https://www.twingate.com/docs/game-streaming-sunshine
type: docs
fetched: 2026-08-14
source_version: a861a469f20d0935afe72536e0676d5e4cb2a9ae03638ecd168c12392592af92
---

# Sunshine Remote Game Streaming with Twingate

## Summary
Sets up Sunshine (open-source GameStream server) on a Windows gaming PC with Twingate Zero Trust access, replacing port forwarding with encrypted tunnel routing. Uses Moonlight client on remote devices to stream games. Total setup time ~30 minutes.

## Key Information
- Sunshine implements Nvidia GameStream protocol; Moonlight is the compatible client
- Twingate Connector runs on gaming PC, creating outbound-only connections (no inbound ports)
- WSL deployment recommended over Docker Desktop for Windows
- Hardware encoding required: NVENC (Nvidia), AMF (AMD), QuickSync (Intel)

## Prerequisites
- Windows PC with gaming GPU (Nvidia/AMD/Intel)
- Twingate account with Admin Console access
- Remote device (laptop/phone/tablet) for streaming
- WSL/Ubuntu or Docker Desktop for Connector deployment

## Step-by-Step

1. **Install Sunshine**: `winget install LizardByte.Sunshine` or download installer; configure encoder in web UI at `http://localhost:47990`
2. **Deploy Twingate Connector**: Create Remote Network in Admin Console → Add Connector → deploy via WSL (recommended) or Docker on gaming PC
3. **Create Twingate Resource**: IP = gaming PC's private IP; TCP ports `47984-47990`; UDP ports `47998-48000`; assign group access
4. **Install Twingate Client** on remote device and connect
5. **Install Moonlight** on remote device
6. **Pair**: Add PC by private IP in Moonlight → enter 4-digit PIN in Sunshine web UI under PIN section

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Sunshine Web UI | `http://localhost:47990` |
| TCP Ports | `47984-47990` |
| UDP Ports | `47998-48000` |
| Sunshine Service Name | `SunshineService` |
| WSL install command | `wsl --install` |

## Gotchas
- Connector must remain running continuously for streaming to work
- If connection fails in Moonlight, try `127.0.0.1` instead of private IP
- Some games require Sunshine to run as administrator
- Headless setups (no monitor) require a virtual display driver (e.g., IddSampleDriver)
- Initial bitrate: start at 15-20 Mbps for 1080p; wired ethernet strongly recommended on gaming PC
- Verify correct Remote Network selected when assigning Connector to Resource

## Troubleshooting Commands
```powershell
# Check Sunshine service status
sc query SunshineService

# Find local IP address
ipconfig
```

## Related Docs
- Apollo Remote Streaming (automatic virtual display management)
- Duo Remote Streaming (multi-user simultaneous gaming)
- Game Streaming Overview
- Connector Deployment Guides
- [Official Sunshine docs](https://docs.lizardbyte.dev/projects/sunshine/)
# Sunshine Remote Game Streaming with Twingate

## Summary
Sets up Sunshine (open-source GameStream server) on a Windows gaming PC with Twingate providing secure remote access. Eliminates port forwarding by routing Moonlight client connections through Twingate's encrypted tunnel. Total setup time ~30 minutes.

## Key Information
- Sunshine implements Nvidia GameStream protocol; Moonlight is the compatible client
- Twingate Connector runs on the gaming PC, creates outbound-only connections (no inbound ports needed)
- WSL deployment recommended over Docker Desktop for Windows (lower overhead)
- Hardware encoding required: NVENC (Nvidia), AMF (AMD), QuickSync (Intel)

## Prerequisites
- Windows PC with gaming GPU (Nvidia/AMD/Intel)
- Twingate account with Admin Console access
- Remote device (laptop/phone/tablet) for streaming
- Active internet on both ends

## Step-by-Step

1. **Install Sunshine** on gaming PC: `winget install LizardByte.Sunshine` or manual installer
2. **Configure Sunshine** at `http://localhost:47990` — set hardware encoder for your GPU
3. **Deploy Twingate Connector** on gaming PC via WSL (recommended) or Docker
4. **Create Twingate Resource** pointing to gaming PC's private IP
5. **Install Twingate Client** on remote device; sign in and connect
6. **Install Moonlight** on remote device
7. **Pair Moonlight**: enter PC's private IP → get 4-digit PIN → enter PIN in Sunshine web UI at `http://localhost:47990` → PIN section

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Sunshine Web UI | `http://localhost:47990` |
| TCP Ports (Resource) | `47984-47990` (Web UI + HTTPS) |
| UDP Ports (Resource) | `47998-48000` (Streaming) |
| WSL install | `wsl --install` |

## Gotchas
- Twingate Connector must remain running continuously for streaming to work
- Gaming PC needs a connected monitor OR virtual display driver for headless setups (black screen otherwise)
- Some games require Sunshine to run as Administrator
- Start Moonlight bitrate at 15-20 Mbps for 1080p; tune down if performance is poor
- If connection fails, try `127.0.0.1` instead of private IP in Moonlight
- Select correct Remote Network when creating the Resource (matters if multiple networks exist)

## Troubleshooting Quick Reference
- **Can't connect**: Verify Twingate shows "Connected," Sunshine service running (`sc query SunshineService`)
- **Pairing fails**: Restart Sunshine from system tray; verify Twingate connected before pairing
- **Poor performance**: Wired ethernet on gaming PC, lower bitrate/resolution, close bandwidth apps
- **Games won't launch**: Check executable path and working directory in Sunshine Applications

## Related Docs
- [Apollo Remote Streaming](https://www.twingate.com/docs) — automatic virtual display management
- [Duo Remote Streaming](https://www.twingate.com/docs) — multi-user simultaneous gaming
- [Connector Deployment Guides](https://www.twingate.com/docs)
- [Resource Access Configuration](https://www.twingate.com/docs)
- [Official Sunshine Docs](https://docs.lizardbyte.dev/projects/sunshine/)
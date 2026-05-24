# Sunshine Remote Game Streaming with Twingate

## Page Title
Sunshine Remote Game Streaming with Twingate

## Summary
Sets up Sunshine (open-source GameStream server) on a Windows gaming PC and secures remote access via Twingate Zero Trust, eliminating port forwarding. Moonlight client connects through Twingate's encrypted tunnel to stream games from anywhere.

## Key Information
- Sunshine implements Nvidia GameStream protocol; pairs with Moonlight client
- Twingate Connector creates outbound-only connection — no inbound ports or port forwarding required
- Connector recommended via WSL on Windows (lighter than Docker Desktop)
- Hardware encoding required: NVENC (Nvidia), AMF (AMD), QuickSync (Intel)

## Prerequisites
- Windows PC with Nvidia/AMD/Intel GPU
- Twingate account with Admin Console access
- Remote device (Windows/Mac/iOS/Android) for streaming

## Step-by-Step

1. **Install Sunshine** — `winget install LizardByte.Sunshine` or manual installer; configure encoder at `http://localhost:47990`
2. **Deploy Twingate Connector** — Create Remote Network in Admin Console; deploy Connector via WSL (`wsl --install`) or Docker on gaming PC
3. **Create Twingate Resource** — Add gaming PC's private IP as resource with specific port ranges
4. **Install Twingate Client** — On remote device; sign in and connect
5. **Install Moonlight** — On remote device
6. **Pair Moonlight to Sunshine** — Add PC by private IP in Moonlight; enter 4-digit PIN in Sunshine web UI under PIN section

## Configuration Values

| Setting | Value |
|---|---|
| Sunshine Web UI | `http://localhost:47990` |
| TCP Ports (Resource) | `47984-47990` |
| UDP Ports (Resource) | `47998-48000` |
| Service name | `SunshineService` |

## Gotchas
- Twingate Connector must stay running for streaming to work — WSL/Docker handles persistence
- A physical or virtual monitor must be connected; headless setups need IddSampleDriver
- If IP-based connection fails in Moonlight, try `127.0.0.1`
- Some games require Sunshine to run as Administrator
- Wired ethernet on gaming PC strongly recommended for performance
- Start bitrate at 15–20 Mbps for 1080p; adjust down if performance is poor

## Troubleshooting Quick Reference
- **Can't connect**: Verify Twingate Client shows "Connected"; confirm resource visible in client
- **Pairing fails**: Check `sc query SunshineService`; restart from system tray
- **Black screen**: Connect monitor or configure virtual display driver
- **Games won't launch**: Verify executable path and working directory in Sunshine Applications

## Related Docs
- [Apollo Remote Streaming](https://www.twingate.com/docs) — automatic virtual display management
- [Duo Remote Streaming](https://www.twingate.com/docs) — multi-user simultaneous gaming
- [Game Streaming Overview](https://www.twingate.com/docs) — compare all streaming options
- [Connector Deployment Guides](https://www.twingate.com/docs)
- [Resource Access Configuration](https://www.twingate.com/docs)
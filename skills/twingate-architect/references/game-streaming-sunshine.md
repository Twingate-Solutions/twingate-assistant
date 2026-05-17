# Sunshine Remote Game Streaming with Twingate

## Summary
Configure Sunshine (open-source GameStream server) on a Windows gaming PC with Twingate Zero Trust access for secure remote streaming via Moonlight client. Eliminates port forwarding by routing traffic through Twingate Connector's outbound-only encrypted tunnel.

## Key Information
- Sunshine implements Nvidia GameStream protocol; Moonlight is the compatible client
- Twingate Connector creates outbound-only connection—no inbound ports or firewall changes needed
- Connector deployed on gaming PC via WSL (recommended) or Docker
- Total setup time: ~30 minutes

## Prerequisites
- Windows PC with GPU (Nvidia/AMD/Intel)
- Twingate account with admin access
- WSL/Ubuntu or Docker Desktop for Connector deployment
- Remote device (any platform) for streaming

## Step-by-Step

1. **Install Sunshine**: `winget install LizardByte.Sunshine` or download installer from GitHub releases
2. **Configure Sunshine** at `http://localhost:47990`: set encoder (NVENC/AMF/QuickSync per GPU)
3. **Deploy Twingate Connector** on gaming PC via WSL (`wsl --install`) using tokens from Admin Console
4. **Create Twingate Resource**: gaming PC's private IP, TCP `47984-47990`, UDP `47998-48000`
5. **Assign group access** to the resource in Admin Console
6. **Install Twingate Client** on remote device and connect
7. **Install Moonlight** on remote device; add PC by private IP
8. **Pair**: enter 4-digit PIN from Moonlight into Sunshine web UI at `http://localhost:47990` → PIN section

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Sunshine Web UI | `http://localhost:47990` |
| TCP Ports (Resource) | `47984-47990` |
| UDP Ports (Resource) | `47998-48000` |
| Nvidia Encoder | NVENC |
| AMD Encoder | AMF |
| Intel Encoder | QuickSync |
| Sunshine Service name | `SunshineService` |

## Gotchas
- Hardware encoding must be selected—software encoding is insufficient for real-time streaming
- Connector must remain running; WSL/Docker handles background persistence
- If Moonlight can't connect, try `127.0.0.1` instead of private IP
- Headless streaming (no monitor) requires virtual display driver (IddSampleDriver)
- Some games need Sunshine running as administrator to launch
- Verify correct Remote Network is selected when creating the Resource

## Troubleshooting Quick Reference
- **Can't connect**: Check Twingate Client shows "Connected"; verify Sunshine service running (`sc query SunshineService`)
- **Poor performance**: Start at 15-20 Mbps for 1080p; use wired ethernet on gaming PC
- **Black screen**: Attach monitor or configure virtual display driver

## Related Docs
- [Apollo Remote Streaming](https://www.twingate.com/docs) — automatic virtual display management
- [Duo Remote Streaming](https://www.twingate.com/docs) — multi-user simultaneous gaming
- [Connector Deployment Guides](https://www.twingate.com/docs)
- [Resource Access Configuration](https://www.twingate.com/docs)
- [Official Sunshine Documentation](https://docs.lizardbyte.dev/projects/sunshine/)
# Sunshine Remote Game Streaming with Twingate

## Summary
Sets up Sunshine (open-source GameStream server) on a Windows gaming PC with Twingate Zero Trust access for secure remote streaming via Moonlight client. Eliminates port forwarding by routing all traffic through Twingate Connector outbound connections. Target setup time: ~30 minutes.

## Key Information
- Sunshine implements Nvidia GameStream protocol; pairs with Moonlight client
- Twingate Connector creates outbound-only encrypted tunnel — no inbound ports required
- Connector deployed on gaming PC via WSL (recommended) or Docker Desktop
- Supported encoders: NVENC (Nvidia), AMF (AMD), QuickSync (Intel)

## Prerequisites
- Windows PC with gaming GPU (Nvidia/AMD/Intel)
- Twingate account with Admin Console access
- Remote device (laptop/phone/tablet) for streaming
- WSL + Ubuntu **or** Docker Desktop (for Connector deployment)

## Step-by-Step

1. **Install Sunshine** — `winget install LizardByte.Sunshine` or manual installer from GitHub releases
2. **Configure Sunshine** — Set encoder at `http://localhost:47990` → Configuration → Video/Audio
3. **Deploy Twingate Connector** on gaming PC via WSL or Docker; verify green "Online" status
4. **Create Twingate Resource** pointing to gaming PC's private IP
5. **Assign Resource access** to appropriate user group in Admin Console
6. **Install Twingate Client** on remote device; sign in and connect
7. **Install Moonlight** on remote device
8. **Pair**: Add PC by private IP in Moonlight → enter 4-digit PIN in Sunshine web UI → confirm pairing

## Configuration Values

| Parameter | Value |
|---|---|
| Sunshine Web UI | `http://localhost:47990` |
| TCP Ports (Resource) | `47984-47990` |
| UDP Ports (Resource) | `47998-48000` |
| Get local IP | `ipconfig` → IPv4 Address |
| Pairing alternative address | `127.0.0.1` |
| Check service status | `sc query SunshineService` |

## Gotchas
- Hardware encoding must be selected manually — don't use software encoding for game streaming
- Connector must remain running continuously; WSL/Docker runs it in background
- A physical or virtual monitor must be connected to gaming PC (black screen otherwise); use IddSampleDriver for headless
- Some games require Sunshine running as administrator
- Start Moonlight bitrate at 15–20 Mbps for 1080p; tune down if performance is poor
- Verify correct Remote Network selected when creating Resource if multiple exist

## Related Docs
- [Apollo Remote Streaming](https://www.twingate.com/docs) — automatic virtual display management
- [Duo Remote Streaming](https://www.twingate.com/docs) — multi-user simultaneous gaming
- [Connector Deployment Guides](https://www.twingate.com/docs)
- [Resource Access Configuration](https://www.twingate.com/docs)
- [Sunshine Official Docs](https://docs.lizardbyte.dev/projects/sunshine/)
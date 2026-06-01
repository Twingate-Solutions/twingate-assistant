# Sunshine Remote Game Streaming with Twingate

## Summary
Sets up Sunshine (open-source GameStream server) on a Windows gaming PC and secures remote access via Twingate, eliminating port forwarding. Moonlight client connects through Twingate's encrypted tunnel to stream games remotely. Total setup time ~30 minutes.

## Key Information
- Sunshine implements Nvidia GameStream protocol; pairs with Moonlight client
- Twingate Connector creates outbound-only connection—no inbound ports exposed
- WSL deployment recommended over Docker Desktop for Windows (lower overhead)
- Hardware encoding required: NVENC (Nvidia), AMF (AMD), QuickSync (Intel)

## Prerequisites
- Windows PC with gaming GPU (Nvidia/AMD/Intel)
- Twingate account with admin access
- Remote device with Moonlight and Twingate Client installed

## Step-by-Step

1. **Install Sunshine**: `winget install LizardByte.Sunshine` or manual installer; configure encoder at `http://localhost:47990`
2. **Deploy Twingate Connector**: Create Remote Network in Admin Console → add Connector → deploy via WSL (`wsl --install`) or Docker on gaming PC
3. **Create Twingate Resource**: Private IP of gaming PC with TCP `47984-47990` and UDP `47998-48000`
4. **Assign Access**: Add group access to the resource in Admin Console
5. **Install Twingate Client** on remote device and connect
6. **Install Moonlight** on remote device; add PC by private IP
7. **Pair**: Enter 4-digit PIN from Moonlight into Sunshine web UI at `http://localhost:47990` → PIN section

## Configuration Values

| Setting | Value |
|---|---|
| Sunshine Web UI | `http://localhost:47990` |
| TCP Ports | `47984-47990` |
| UDP Ports | `47998-48000` |
| Recommended starting bitrate | 15–20 Mbps for 1080p |

## Gotchas
- Twingate Connector must stay running continuously; WSL/Docker keep it in background
- If Moonlight can't connect, try `127.0.0.1` instead of private IP
- Headless setups (no monitor) require a virtual display driver (e.g., IddSampleDriver)
- Some games require Sunshine to run as Administrator
- Connector must be on the correct Remote Network matching the Resource

## Troubleshooting Quick Reference
- **Pairing fails**: Verify Sunshine service running via `sc query SunshineService`
- **Poor performance**: Use wired ethernet on gaming PC; lower bitrate/resolution in Moonlight
- **Black screen**: Connect physical monitor or configure virtual display driver

## Related Docs
- Apollo Remote Streaming (auto virtual display management)
- Duo Remote Streaming (multi-user simultaneous gaming)
- Game Streaming Overview (compare all options)
- Connector Deployment Guides
- [Sunshine Official Docs](https://docs.lizardbyte.dev/projects/sunshine/)
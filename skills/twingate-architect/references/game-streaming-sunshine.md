# Sunshine Remote Game Streaming with Twingate

## Page Title
Sunshine Remote Game Streaming with Twingate

## Summary
Guides setup of Sunshine (open-source GameStream server) on a Windows gaming PC with Twingate Zero Trust access replacing port forwarding. Moonlight client connects to Sunshine through an encrypted Twingate tunnel. Total setup time ~30 minutes.

## Key Information
- Sunshine implements Nvidia GameStream protocol; pairs with Moonlight client
- Twingate Connector creates outbound-only connection — no inbound ports needed
- Architecture: Remote Device → Twingate Client → Twingate Cloud → Connector → Sunshine

## Prerequisites
- Windows PC with GPU (Nvidia/AMD/Intel)
- Twingate account with Admin Console access
- Remote device (Windows/Mac/iOS/Android) for streaming to

## Step-by-Step

1. **Install Sunshine**: `winget install LizardByte.Sunshine` or manual installer
2. **Configure encoder** at `http://localhost:47990`: NVENC (Nvidia), AMF (AMD), QuickSync (Intel)
3. **Deploy Twingate Connector** on gaming PC via WSL (recommended) or Docker
4. **Add Sunshine as Twingate Resource** using PC's private IP
5. **Install Twingate Client** on remote device and connect
6. **Install Moonlight** on remote device
7. **Pair**: Enter PC private IP in Moonlight → enter PIN in Sunshine web UI (`/PIN` section)

## Configuration Values

**Sunshine ports (Resource config):**
| Protocol | Ports | Purpose |
|----------|-------|---------|
| TCP | 47984-47990 | Web UI + HTTPS |
| UDP | 47998-48000 | Streaming |

**Sunshine web UI:** `http://localhost:47990`

**WSL Connector install:**
```bash
wsl --install  # then Ubuntu from Microsoft Store
# Run generated token command in WSL Ubuntu terminal
```

**Check Sunshine service:**
```powershell
sc query SunshineService
```

**Get PC IP:**
```powershell
ipconfig  # look for IPv4 under active adapter
```

## Gotchas
- Hardware encoder must be selected — software encoding insufficient for real-time streaming
- Connector must stay running (WSL/Docker keeps it in background)
- Pairing PIN must be entered while connected via Twingate
- Headless PCs need a physical monitor or virtual display driver (IddSampleDriver)
- Poor performance: start at 15-20 Mbps bitrate for 1080p; use wired ethernet on gaming PC
- If IP connection fails, try `127.0.0.1` in Moonlight
- Some games require Sunshine run as administrator

## Related Docs
- [Apollo Remote Streaming](https://www.twingate.com/docs) — automatic virtual display management
- [Duo Remote Streaming](https://www.twingate.com/docs) — multi-user simultaneous gaming
- [Game Streaming Overview](https://www.twingate.com/docs) — compare all options
- [Connector Deployment Guides](https://www.twingate.com/docs)
- [Official Sunshine Docs](https://docs.lizardbyte.dev/projects/sunshine/)
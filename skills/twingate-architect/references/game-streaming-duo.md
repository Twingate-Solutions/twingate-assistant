# Duo Multi-User Remote Game Streaming with Twingate

## Summary
Configures Duo (multi-user game streaming platform) with Twingate Zero Trust access so multiple family members can stream games simultaneously from one Windows PC without port forwarding. Each user gets an isolated virtual Windows session. Twingate replaces exposed ports with encrypted outbound-only tunnels.

## Key Information
- Duo enables concurrent virtual Windows sessions on one GPU-equipped PC
- Free tier: 30fps max, limited users; Patreon ($10 lifetime): unlimited users, 60+ fps, HDR
- Moonlight is the client-side streaming application; Duo is the server component
- Twingate Connector runs on the gaming PC (WSL recommended on Windows)
- Each concurrent session needs ~4–8GB RAM and 2–4 CPU cores

## Prerequisites
- Windows 11 23H2 or newer (Windows 10 not supported)
- Gaming GPU (Nvidia/AMD/Intel)
- Twingate account with Admin Console access
- WSL + Ubuntu (recommended for Connector deployment)

## Step-by-Step

1. **Install Duo** – Run installer as Administrator, select all components, reboot
2. **Configure Duo** – Open `http://localhost:47990`, set GPU encoder (NVENC/AMF/QuickSync)
3. **Create Windows user accounts** per session via PowerShell: `net user "Username" "Pass!" /add`
4. **Create virtual sessions** in Duo web UI → Sessions Management → Add New Virtual Session
5. **Deploy Twingate Connector** on gaming PC via WSL: `wsl --install`, install Ubuntu, run connector command from Admin Console
6. **Add Duo as Twingate Resource** with gaming PC's private IP
7. **Install Twingate Client** on each remote device, sign in, connect
8. **Install Moonlight** on remote devices, add PC by private IP, complete PIN pairing via Duo web UI
9. **Select virtual session** in Moonlight to begin streaming

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Duo Web UI | `http://localhost:47990` |
| TCP Ports | `47984–47990` (Web UI + HTTPS) |
| UDP Ports | `47998–48010` (streaming, multi-session) |
| Resource Address | Gaming PC private IPv4 (e.g., `192.168.1.100`) |

## Gotchas
- Virtual sessions won't start without TermWrap service running: `sc query TermWrap`
- Some anti-cheat systems are incompatible with virtual sessions
- Free tier hard-capped at 30fps regardless of hardware
- Twingate Connector must stay running for remote access to function
- Each remote device user needs their own Twingate account with resource access granted
- Try `127.0.0.1` in Moonlight if private IP connection fails while on Twingate

## Troubleshooting Commands
```powershell
sc query DuoService      # Verify Duo running
sc query TermWrap        # Verify virtual session service
ipconfig                 # Find PC's private IP
```

## Related Docs
- [Sunshine Remote Streaming](https://www.twingate.com/docs/game-streaming-sunshine) – Single-user streaming
- [Apollo Remote Streaming](https://www.twingate.com/docs/game-streaming-apollo) – Auto virtual displays
- [Game Streaming Overview](https://www.twingate.com/docs/game-streaming) – Compare options
- [Connector Deployment Guides](https://www.twingate.com/docs/connector)
- [Resource Access Configuration](https://www.twingate.com/docs/access-control)
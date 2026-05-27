# Remote Game Streaming with Twingate

## Summary
Overview page for setting up remote PC game streaming using Twingate's Zero Trust network with Sunshine, Apollo, or Duo streaming software. Eliminates port forwarding by routing all traffic through Twingate's encrypted tunnel. Serves as an index to three specific setup guides.

## Key Information
- Three supported streaming servers: **Sunshine** (general), **Apollo** (headless/virtual display), **Duo** (multi-user)
- Client application: **Moonlight** on the remote device
- Twingate Connector runs on gaming PC, establishes outbound-only connection — no inbound ports needed
- All traffic is authenticated, encrypted, and auditable with optional MFA

## Prerequisites
- Windows PC with gaming-capable GPU (Nvidia/AMD/Intel)
- Twingate account (free tier available)
- Remote streaming device (laptop, phone, tablet)
- Stable internet at both ends
- Wired ethernet on gaming PC (strongly recommended)

## Architecture
1. Streaming server (Sunshine/Apollo/Duo) runs on gaming PC
2. Twingate Connector on gaming PC makes outbound-only connection to Twingate Cloud
3. Remote device connects via Twingate Client
4. Moonlight streams game video over encrypted Twingate tunnel

## Configuration Values (Performance Targets)
| Parameter | Value |
|-----------|-------|
| Bandwidth (1080p60) | 15–20 Mbps |
| Bandwidth (4K60) | 25–40 Mbps |
| Target latency | <50ms |
| Encoding | Hardware only: NVENC / AMF / QuickSync |

## Solution Comparison
| Feature | Sunshine | Apollo | Duo |
|---------|----------|--------|-----|
| Setup complexity | Easy | Easy | Moderate |
| Virtual displays | Manual | Auto (SudoVDA) | Automatic |
| Multi-user | No | No | Yes (Patreon) |
| Cost | Free | Free | Free (limited) |

## Gotchas
- Multi-user (Duo) and HDR in Duo require Patreon subscription
- Software encoders insufficient for real-time streaming — hardware encoder required
- This page links to sub-guides; no standalone setup steps here

## Related Docs
- Sunshine Remote Streaming guide
- Apollo Remote Streaming guide
- Duo Remote Streaming guide
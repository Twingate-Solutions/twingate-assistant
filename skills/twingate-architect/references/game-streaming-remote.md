# Remote Game Streaming with Twingate

## Page Title
Remote Game Streaming with Twingate

## Summary
Overview page for setting up remote PC game streaming secured by Twingate's Zero Trust network. Covers three streaming solutions (Sunshine, Apollo, Duo) that work with Moonlight client, eliminating port forwarding requirements. All setups route traffic through Twingate Connector for authenticated, encrypted access.

## Key Information
- Three supported streaming servers: **Sunshine** (general), **Apollo** (headless/virtual display), **Duo** (multi-user)
- Client-side uses **Moonlight** app on remote device
- No port forwarding required — Connector uses outbound-only connections
- All traffic is authenticated, encrypted, and auditable with optional MFA

## Prerequisites
- Windows PC with gaming-capable GPU (Nvidia/AMD/Intel)
- Twingate account (free tier available)
- Remote device (laptop, phone, tablet)
- Stable internet at both locations
- Wired ethernet on gaming PC (strongly recommended)

## Architecture
1. Streaming server (Sunshine/Apollo/Duo) runs on gaming PC
2. Twingate Connector establishes outbound-only connection to Twingate Cloud
3. Remote user connects via Twingate Client
4. Moonlight streams over the encrypted Twingate tunnel

## Configuration Values / Performance Targets
| Parameter | Value |
|-----------|-------|
| Bandwidth (1080p60) | 15–20 Mbps |
| Bandwidth (4K60) | 25–40 Mbps |
| Target latency | <50ms |
| Encoding | Hardware only (NVENC/AMF/QuickSync) |

## Solution Comparison
| Feature | Sunshine | Apollo | Duo |
|---------|----------|--------|-----|
| Setup | Easy | Easy | Moderate |
| Virtual Displays | Manual | Automatic (SudoVDA) | Automatic |
| Multi-User | No | No | Yes (Patreon) |
| Cost | Free | Free | Free (limited) |

## Gotchas
- Software encoding not viable for real-time streaming — hardware encoder required
- Duo multi-user and HDR features require Patreon subscription
- Apollo's key differentiator is SudoVDA for headless PCs (no physical monitor needed)
- Each solution has its own dedicated quick start guide (not covered on this page)

## Related Docs
- Sunshine Remote Streaming guide
- Apollo Remote Streaming guide
- Duo Remote Streaming guide
- Twingate Connector setup
- Twingate Client installation
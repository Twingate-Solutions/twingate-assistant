# Remote Game Streaming with Twingate

## Page Title
Remote Game Streaming with Twingate

## Summary
Overview page for setting up remote game streaming (Sunshine, Apollo, or Duo) secured via Twingate's Zero Trust network. Eliminates port forwarding by routing streaming traffic through Twingate's encrypted tunnel. Acts as an index to three specific solution guides.

## Key Information
- Three supported streaming servers: **Sunshine**, **Apollo**, **Duo** (all use Moonlight client on remote device)
- Architecture: Streaming server → Twingate Connector (outbound-only) → Twingate Cloud → Client device → Moonlight
- Gaming PC is never exposed to the internet; no port forwarding required

## Prerequisites
- Windows PC with gaming-capable GPU (Nvidia, AMD, or Intel)
- Twingate account (free tier available)
- Remote device (laptop, phone, tablet)
- Stable internet at both ends
- Wired ethernet on gaming PC (strongly recommended)

## Solution Comparison

| Feature | Sunshine | Apollo | Duo |
|---|---|---|---|
| Setup Complexity | Easy | Easy | Moderate |
| Virtual Displays | Manual | Automatic (SudoVDA) | Automatic |
| Multi-User | No | No | Yes (Patreon) |
| HDR Support | Yes | Yes | Yes (Patreon) |
| Cost | Free | Free | Free (limited) |

## Use Case Selection
- **Sunshine**: General streaming, simple setup, established community (LizardByte/open-source)
- **Apollo**: Headless PCs (no monitor), automatic virtual display/resolution management
- **Duo**: Families or shared PCs needing simultaneous multi-user streaming

## Performance Requirements
- **1080p60**: 15–20 Mbps
- **4K60**: 25–40 Mbps
- **Target latency**: <50ms for responsive gameplay
- **Encoding**: Hardware encoders required — NVENC (Nvidia), AMF (AMD), QuickSync (Intel)

## Gotchas
- Duo's multi-user and HDR features require Patreon subscription
- Software encoding is not sufficient for real-time game streaming; hardware encoder mandatory
- Wireless connections on the gaming PC will degrade performance significantly

## Related Docs
- Sunshine Remote Streaming guide
- Apollo Remote Streaming guide
- Duo Remote Streaming guide
- Twingate Connector setup documentation
# Remote Game Streaming with Twingate

## Page Title
Remote Game Streaming with Twingate

## Summary
Overview page for setting up remote game streaming (Sunshine, Apollo, or Duo) secured via Twingate's Zero Trust network. Eliminates port forwarding by routing streaming traffic through Twingate's encrypted tunnel. Serves as an index to three solution-specific guides.

## Key Information
- Three supported streaming solutions: **Sunshine**, **Apollo**, **Duo**
- Client: **Moonlight** streams games over the Twingate tunnel
- Architecture: Streaming server → Twingate Connector (outbound-only) → Twingate Cloud → Client device
- Gaming PC remains hidden from internet; no open router ports required

## Prerequisites
- Windows PC with gaming-capable GPU (Nvidia, AMD, or Intel)
- Twingate account (free tier available)
- Remote device (laptop, phone, tablet)
- Stable internet at both endpoints
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
- **Sunshine** – General/traditional streaming, established community support
- **Apollo** – Headless PCs (no monitor), automatic virtual display/resolution management
- **Duo** – Families or shared PCs requiring simultaneous multi-user streaming

## Performance Requirements
- **1080p60**: 15–20 Mbps
- **4K60**: 25–40 Mbps
- **Target latency**: <50ms for responsive gameplay
- **Encoding**: Hardware encoders required (NVENC / AMF / QuickSync)

## Gotchas
- Duo multi-user and HDR features require Patreon subscription
- Software encoding is insufficient for real-time game streaming — GPU hardware encoder mandatory
- Virtual display setup is manual with Sunshine; use Apollo for headless scenarios

## Related Docs
- Sunshine Remote Streaming guide
- Apollo Remote Streaming guide
- Duo Remote Streaming guide
- Twingate Connector setup documentation
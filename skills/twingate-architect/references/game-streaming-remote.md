# Remote Game Streaming with Twingate

## Page Title
Remote Game Streaming with Twingate

## Summary
Overview page for setting up remote PC game streaming secured by Twingate's Zero Trust network. Covers three streaming software options (Sunshine, Apollo, Duo) that work with Moonlight client. Eliminates need for port forwarding by routing traffic through Twingate's encrypted tunnel.

## Key Information
- Three supported streaming servers: **Sunshine**, **Apollo**, **Duo**
- Client: **Moonlight** on remote device
- Architecture: Streaming server → Twingate Connector (outbound-only) → Twingate Cloud → Twingate Client → Moonlight
- Gaming PC remains hidden from internet; no open ports required

## Prerequisites
- Windows PC with gaming-capable GPU (Nvidia/AMD/Intel)
- Twingate account (free tier available)
- Remote device (laptop, phone, tablet)
- Stable internet at both ends
- Wired ethernet on gaming PC recommended

## Solution Comparison

| Feature | Sunshine | Apollo | Duo |
|---|---|---|---|
| Setup Complexity | Easy | Easy | Moderate |
| Virtual Displays | Manual | Automatic (SudoVDA) | Automatic |
| Multi-User | No | No | Yes (Patreon) |
| HDR Support | Yes | Yes | Yes (Patreon) |
| Cost | Free | Free | Free (limited) |

**Choose by use case:**
- **Sunshine** – General streaming, established community
- **Apollo** – Headless PCs (no monitor), automatic resolution matching
- **Duo** – Multiple simultaneous users on one PC

## Performance Requirements
- **1080p60:** 15–20 Mbps
- **4K60:** 25–40 Mbps
- **Latency target:** <50ms for responsive gameplay
- **Encoding:** Hardware encoder required (NVENC/AMF/QuickSync)

## Gotchas
- Software encoding will not perform adequately; hardware encoder (NVENC/AMF/QuickSync) is mandatory
- Duo multi-user and HDR require paid Patreon tier
- Apollo's automatic virtual display uses SudoVDA — relevant when no physical monitor is attached
- This page is an index only; actual setup steps are in individual guides per solution

## Related Docs
- Sunshine Remote Streaming guide
- Apollo Remote Streaming guide
- Duo Remote Streaming guide
# Remote Game Streaming with Twingate

## Page Title
Remote Game Streaming with Twingate

## Summary
Overview page for setting up remote PC game streaming secured by Twingate's Zero Trust network. Covers three streaming solutions (Sunshine, Apollo, Duo) that eliminate port forwarding requirements. All solutions use Moonlight client on the remote device and a Twingate-secured tunnel.

## Key Information
- **Architecture**: Streaming server → Twingate Connector (outbound-only) → Twingate Cloud → Client device → Moonlight streams over encrypted tunnel
- **Three supported streaming servers**:
  - **Sunshine**: Open-source, simple setup, general use
  - **Apollo**: Includes SudoVDA for automatic virtual display (headless PCs)
  - **Duo**: Multi-user simultaneous streaming (Patreon features required for full access)
- Gaming PC stays fully hidden from internet; no open router ports required

## Prerequisites
- Windows PC with gaming-capable GPU (Nvidia, AMD, or Intel)
- Twingate account (free tier available)
- Remote streaming client device (laptop, phone, tablet)
- Stable internet at both locations
- Moonlight client on the remote device

## Configuration Values / Performance Requirements
| Parameter | Value |
|-----------|-------|
| 1080p60 bandwidth | 15–20 Mbps |
| 4K60 bandwidth | 25–40 Mbps |
| Target latency | < 50ms |
| Encoder requirement | Hardware only: NVENC, AMF, or QuickSync |
| Recommended connection | Wired ethernet on gaming PC |

## Solution Comparison

| Feature | Sunshine | Apollo | Duo |
|---------|----------|--------|-----|
| Setup Complexity | Easy | Easy | Moderate |
| Virtual Displays | Manual | Automatic (SudoVDA) | Automatic |
| Multi-User | No | No | Yes (Patreon) |
| HDR Support | Yes | Yes | Yes (Patreon) |
| Cost | Free | Free | Free (limited) |

## Gotchas
- Duo's multi-user and HDR features require Patreon subscription
- Software encoders are **not** supported for real-time streaming; hardware GPU encoder required
- Wired ethernet is strongly recommended on the gaming PC side; Wi-Fi may cause latency/quality issues
- This page is an index only — each solution has its own dedicated setup guide

## Related Docs
- Sunshine Remote Streaming guide (linked, URL not provided)
- Apollo Remote Streaming guide (linked, URL not provided)
- Duo Remote Streaming guide (linked, URL not provided)
- Twingate Connector setup (implied prerequisite)
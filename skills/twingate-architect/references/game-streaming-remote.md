---
source: https://www.twingate.com/docs/game-streaming-remote
type: docs
fetched: 2026-08-14
source_version: c83b552efe73032c9fd7c1d36de4a5f7f98682284f33dcec8445bdf7ba34ed6a
---

# Remote Game Streaming with Twingate

## Page Title
Remote Game Streaming with Twingate

## Summary
This page is an index/overview for setting up remote PC game streaming using Twingate's Zero Trust network as a secure transport layer. It covers three streaming solutions (Sunshine, Apollo, Duo) that work with Moonlight client, eliminating port forwarding requirements. All setups use outbound-only Twingate Connectors so the gaming PC remains hidden from the internet.

## Key Information
- Three supported streaming servers: **Sunshine** (general use), **Apollo** (headless/virtual display), **Duo** (multi-user)
- Moonlight is the client used on the remote device for all three solutions
- Architecture: Streaming server → Twingate Connector (outbound-only) → Twingate Cloud → Twingate Client → Moonlight

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

## Configuration Values / Performance Requirements
- **1080p60**: 15–20 Mbps bandwidth
- **4K60**: 25–40 Mbps bandwidth
- **Target latency**: <50ms for responsive gameplay
- **Encoding**: Hardware encoders required — NVENC (Nvidia), AMF (AMD), QuickSync (Intel)

## Gotchas
- Duo multi-user and HDR support require Patreon subscription
- Software encoding is insufficient for real-time game streaming; hardware encoder mandatory
- This page links to individual setup guides but does not contain step-by-step instructions itself
- No port forwarding needed or recommended — opening ports defeats the security model

## Use Case Selection Guide
- **Sunshine** → Standard gaming PC with monitor attached, simple setup
- **Apollo** → Headless PC (no monitor), needs automatic virtual display via SudoVDA
- **Duo** → Shared household or multiple simultaneous users on one PC

## Related Docs
- Sunshine Remote Streaming guide (linked, separate page)
- Apollo Remote Streaming guide (linked, separate page)
- Duo Remote Streaming guide (linked, separate page)
- Twingate Connector setup (implied prerequisite)
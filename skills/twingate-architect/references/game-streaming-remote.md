# Remote Game Streaming with Twingate

## Summary
Overview page for setting up remote game streaming (Sunshine, Apollo, or Duo) secured via Twingate's Zero Trust network. Eliminates port forwarding by routing all traffic through Twingate's encrypted tunnel. Three streaming solutions are supported, each suited to different use cases.

## Key Information
- **No port forwarding required** — Twingate Connector uses outbound-only connections
- **Client**: Moonlight used on remote device to receive stream
- **Three server options**: Sunshine, Apollo, Duo
- All traffic is authenticated, encrypted, and auditable with optional MFA

## Prerequisites
- Windows PC with gaming-capable GPU (Nvidia, AMD, or Intel)
- Twingate account (free tier available)
- Remote device (laptop, phone, tablet)
- Stable internet at both ends
- Wired ethernet on gaming PC strongly recommended

## Architecture
1. Streaming server (Sunshine/Apollo/Duo) runs on gaming PC
2. Twingate Connector establishes outbound-only tunnel to Twingate Cloud
3. Remote device connects via Twingate Client
4. Moonlight client streams over encrypted Twingate tunnel

## Solution Comparison

| Feature | Sunshine | Apollo | Duo |
|---|---|---|---|
| Setup Complexity | Easy | Easy | Moderate |
| Virtual Displays | Manual | Automatic (SudoVDA) | Automatic |
| Multi-User | No | No | Yes (Patreon) |
| HDR Support | Yes | Yes | Yes (Patreon) |
| Cost | Free | Free | Free (limited) |

## Performance Requirements
- **1080p60**: 15–20 Mbps
- **4K60**: 25–40 Mbps
- **Latency target**: <50ms for responsive gameplay
- **Encoding**: Hardware encoders required (NVENC/AMF/QuickSync)

## Use Case Selection
- **Sunshine**: General streaming, simple setup, established community (LizardByte)
- **Apollo**: Headless PCs without monitor, automatic virtual display/resolution via SudoVDA
- **Duo**: Families or shared PCs needing simultaneous multi-user access

## Gotchas
- Duo multi-user and HDR require Patreon subscription
- Virtual displays on Sunshine require manual configuration (unlike Apollo/Duo)
- Hardware encoder required — software encoding insufficient for real-time game streaming

## Related Docs
- Sunshine Remote Streaming guide
- Apollo Remote Streaming guide
- Duo Remote Streaming guide
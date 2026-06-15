# Remote Game Streaming with Twingate

## Summary
Overview page for setting up remote PC game streaming secured by Twingate's Zero Trust network. Covers three streaming solutions (Sunshine, Apollo, Duo) that eliminate port forwarding by routing traffic through Twingate's encrypted tunnel. Serves as a navigation hub to individual solution guides.

## Key Information
- Twingate replaces port forwarding and traditional VPN for game streaming
- Uses Moonlight client on remote devices to receive the stream
- Streaming server runs on gaming PC; Twingate Connector makes outbound-only connections
- Gaming PC remains hidden from public internet

## Prerequisites
- Windows PC with gaming-capable GPU (Nvidia, AMD, or Intel)
- Twingate account (free tier available)
- Remote streaming client device (laptop, phone, tablet)
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

**Choose by use case:**
- **Sunshine** — General streaming, established community, open-source (LizardByte)
- **Apollo** — Headless PCs (no monitor), automatic virtual display/resolution management
- **Duo** — Multiple simultaneous users on one PC (families, shared setups)

## Architecture
1. Streaming server (Sunshine/Apollo/Duo) runs on gaming PC
2. Twingate Connector establishes outbound-only tunnel to Twingate Cloud
3. Remote device connects via Twingate Client
4. Moonlight client streams over the encrypted Twingate tunnel

## Performance Requirements

| Metric | Target |
|---|---|
| 1080p60 bandwidth | 15–20 Mbps |
| 4K60 bandwidth | 25–40 Mbps |
| Max latency | <50ms for responsive gameplay |
| Encoding | Hardware required: NVENC / AMF / QuickSync |

## Gotchas
- Software encoding is not viable for real-time game streaming — hardware encoder (NVENC/AMF/QuickSync) is required
- Duo multi-user and HDR features require Patreon subscription
- Wireless connections on the gaming PC will degrade performance significantly
- MFA can be enforced via Twingate but must be configured separately

## Related Docs
- Sunshine Remote Streaming guide
- Apollo Remote Streaming guide
- Duo Remote Streaming guide
- Twingate Connector setup
- Twingate Client setup
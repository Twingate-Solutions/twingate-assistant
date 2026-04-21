## Remote Game Streaming with Twingate -- Overview

Index and comparison page for the three Twingate-secured game streaming options: Sunshine (simplest, traditional), Apollo (headless with automatic virtual displays), and Duo (multi-user simultaneous sessions). All three use the same Twingate architecture: a Connector on the gaming PC plus the Moonlight client on remote devices; no port forwarding required.

**Key Information**
- Common architecture: streaming server (Sunshine/Apollo/Duo) + Twingate Connector on gaming PC; Moonlight + Twingate Client on remote device
- Common hardware requirement: Windows PC with gaming-capable GPU (Nvidia/AMD/Intel for NVENC/AMF/QuickSync)
- Streaming performance targets: 15-20 Mbps for 1080p60; 25-40 Mbps for 4K60; under 50ms latency
- Wired ethernet on gaming PC strongly recommended
- Hardware encoders (NVENC/AMF/QuickSync) required for real-time streaming -- software encoding insufficient

**Comparison**

| Feature | Sunshine | Apollo | Duo |
|---|---|---|---|
| Setup complexity | Easy | Easy | Moderate |
| Virtual displays | Manual (IddSampleDriver) | Automatic (SudoVDA) | Automatic |
| Multi-user | No | No | Yes (Patreon) |
| HDR | Yes | Yes | Yes (Patreon) |
| Cost | Free | Free | Free (limited) |
| Best for | General streaming | Headless PCs | Families/shared PCs |

**Prerequisites**
- Windows gaming PC with GPU
- Twingate account (free tier supported)
- Stable internet at both locations

**Gotchas**
- All three solutions require hardware GPU encoding -- software encoding is too slow for game streaming
- Wired ethernet on the gaming PC is strongly recommended; Wi-Fi introduces variable latency
- Choose Apollo over Sunshine if the PC has no monitor (headless); Apollo's SudoVDA handles virtual displays automatically

**Related Docs**
- /docs/game-streaming-sunshine
- /docs/game-streaming-apollo
- /docs/game-streaming-duo

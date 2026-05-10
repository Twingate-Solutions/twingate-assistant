# Twingate Performance

## Summary
Twingate uses peer-to-peer connections between Clients and Connectors to minimize overhead, typically reducing throughput by only 5–15%. Benchmarks show Twingate performs within 1–4% of baseline, significantly outperforming self-hosted WireGuard and OpenVPN on equivalent hardware.

## Key Information
- **P2P overhead**: 5–15% throughput reduction (peer-to-peer)
- **Relay fallback**: 200–250 Mbps consistently when P2P unavailable
- **Split-tunnel design**: only Resource-bound traffic goes through tunnel; other traffic (video calls, etc.) bypasses it
- **Benchmark hardware**: 1 vCPU, 2GB RAM VPS with 1Gbps NIC

| Test | Baseline | Twingate | WireGuard | OpenVPN (UDP) |
|------|----------|----------|-----------|---------------|
| Speedtest.net | 943 Mbps | 906 Mbps (-4%) | 148 Mbps (-84%) | 120 Mbps (-87%) |
| 1.8GB File Transfer | 600 Mbps | 600 Mbps (0%) | 224 Mbps (-63%) | 208 Mbps (-66%) |
| LAN Speed Test | 459 Mbps | 455 Mbps (-1%) | 166 Mbps (-64%) | 133 Mbps (-71%) |

## Prerequisites for Self-Testing
- Separate Remote Network from user's local network (cloud or data center)
- Remote Network internet connection of **≥1 Gbps** recommended
- Twingate Admin Console access
- Prior approval required before **publicly publishing** benchmark results

## Step-by-Step: Speedtest.net Performance Test
1. Log into Admin Console → **Resources** → **Add Resource**
2. Select target Remote Network; set label (e.g., "Speedtest.net Test")
3. Set DNS Address to `*speedtest*` (wildcard captures all speedtest domains)
4. Click **Add Resource** → assign to a Group (create isolated test Group if needed)
5. Have user run Speedtest.net **without** Twingate Client connected → record baseline
6. Have user connect Twingate Client → run Speedtest.net again
7. Verify egress IP in results matches Remote Network location
8. Compare results; ≤5% delta is expected for healthy P2P connection

## Configuration Values
- DNS wildcard syntax: `*speedtest*` (asterisks required for wildcard matching)
- File transfer test tools: `rsync --v --stats --progress` (macOS/Linux), Robocopy/Teracopy (Windows)
- LAN Speed Test minimum dataset: **1GB** for accurate results

## Gotchas
- **Storage I/O is often the real bottleneck** in file transfer tests—HDD-based RAID will cap results well below network capacity; use NVMe storage for accurate network benchmarking
- **Relay vs. P2P**: check Admin Console Activity Logs to confirm connection type; relay connections cap at ~200–250 Mbps
- **Local network as confounding factor**: always use a Remote Network physically/logically separate from the user's network
- LAN Speed Test is outdated (no recent updates) and less accurate than raw file transfers
- Public benchmarking requires **Twingate's prior written approval**

## Related Docs
- Wildcard Resource addressing
- Twingate Relays
- Admin Console Activity Logs
- Group and Resource management
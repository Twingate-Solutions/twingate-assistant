# Twingate Performance

## Page Title
Evaluating Twingate Performance

## Summary
Twingate uses peer-to-peer connections between Clients and Connectors, resulting in 5-15% throughput reduction versus baseline. Benchmarks show Twingate significantly outperforms self-hosted WireGuard and OpenVPN on equivalent hardware. Relay fallback connections deliver 200-250 Mbps consistently.

## Key Information
- **P2P overhead**: 5-15% throughput reduction typical
- **Relay fallback**: 200-250 Mbps when P2P unavailable
- **Split-tunnel design**: Only Resource-bound traffic goes through tunnel; other traffic (video calls, etc.) bypasses Twingate entirely
- **Benchmark results** (1 vCPU, 2GB RAM VPS):

| Test | Baseline | Twingate | WireGuard | OpenVPN (UDP) |
|------|----------|----------|-----------|---------------|
| Speedtest.net | 943 Mbps | 906 Mbps (-4%) | 148 Mbps (-84%) | 120 Mbps (-87%) |
| 1.8GB File Transfer | 600 Mbps | 600 Mbps (0%) | 224 Mbps (-63%) | 208 Mbps (-66%) |
| LAN Speed Test | 459 Mbps | 455 Mbps (-1%) | 166 Mbps (-64%) | 133 Mbps (-71%) |

## Prerequisites
- Separate Remote Network (cloud/datacenter) with ≥1 Gbps internet connection for testing
- Twingate Client installed on test user device
- Resource and Group configured in Admin Console
- Check activity logs to confirm P2P vs. Relay connection type

## Step-by-Step: Speedtest.net Performance Test
1. Run baseline Speedtest.net with Twingate Client **disconnected**
2. In Admin Console → Resources → **Add Resource**
3. Select Remote Network; set DNS Address to `*speedtest*` (wildcard)
4. Assign Resource to a test Group (isolate from production users)
5. Connect Twingate Client; run Speedtest.net again
6. Verify egress IP changed (confirms traffic routes through Remote Network)
7. Compare results — expect ≤5% degradation on P2P connection

## Configuration Values
- **Wildcard DNS address**: `*speedtest*` — captures all domains containing "speedtest"
- **Recommended file size for LAN Speed Test**: ≥1 GB dataset for accuracy
- **rsync flags for macOS**: `--v --stats --progress`
- **Windows file transfer tools**: Teracopy, Robocopy
- **Linux file transfer**: rsync

## Gotchas
- **Publishing benchmarks requires Twingate's prior approval**
- File transfer tests are usually bottlenecked by storage I/O (HDD RAID << NVMe), not the network
- Remote Network must be physically separate from user's local network — testing on same LAN skips P2P path
- Remote Network internet speed must not be the bottleneck (use ≥1 Gbps)
- LAN Speed Test tool is outdated and less accurate than direct file transfers
- Low baseline speeds indicate ISP/local network issues, not Twingate

## Related Docs
- Wildcard Resources documentation
- Activity logs (Admin Console) — verify P2P vs. Relay connection
- Twingate Relay documentation
- Remote Network Connector setup
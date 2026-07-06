# Twingate Performance

## Summary
Twingate uses peer-to-peer connections between Clients and Connectors to minimize overhead, typically resulting in only 5-15% throughput reduction. Performance benchmarks show Twingate significantly outperforms self-hosted WireGuard and OpenVPN on equivalent hardware. Relay fallback connections deliver 200-250Mbps consistently.

## Key Information
- **P2P overhead**: 1-5% throughput reduction (tested on 1 vCPU / 2GB RAM VPS)
- **Relay fallback**: 200-250Mbps consistent throughput when P2P unavailable
- **Split-tunnel design**: Only Resource-bound traffic goes through tunnel; other traffic (e.g., video calls) bypasses it
- **Relay vs P2P detection**: Check Admin Console activity logs

## Performance Benchmark Results (1Gbps connections, 1 vCPU / 2GB RAM)

| Test | Baseline | Twingate | WireGuard | OpenVPN (UDP) |
|------|----------|----------|-----------|---------------|
| Speedtest.net (multi) | 943Mbps | 906Mbps (-4%) | 148Mbps (-84%) | 120Mbps (-87%) |
| 1.8GB File Transfer (Samba) | 600Mbps | 600Mbps (0%) | 224Mbps (-63%) | 208Mbps (-66%) |
| LAN Speed Test (1GB) | 459Mbps | 455Mbps (-1%) | 166Mbps (-64%) | 133Mbps (-71%) |

## Prerequisites for Own Testing
- Separate Remote Network from user's local network (isolates test from LAN bottlenecks)
- Remote Network internet connection: **minimum 1Gbps recommended**
- NVMe storage on file server to avoid I/O bottleneck skewing results
- Twingate Admin Console access to add Resources

## Step-by-Step: Speedtest.net Performance Test

1. Run baseline Speedtest.net in browser with Twingate **disconnected**
2. In Admin Console → **Resources** → **Add Resource**
3. Select target Remote Network; set DNS Address to `*speedtest*` (wildcard)
4. Assign Resource to a test Group (optionally isolated to avoid affecting other users)
5. Log into Twingate Client; re-run Speedtest.net
6. Verify egress IP changed (lower-left of result) confirming traffic routes through Remote Network

## Configuration Values
- **Wildcard DNS pattern**: `*speedtest*` — captures any domain containing "speedtest"
- **File transfer flags (rsync/macOS)**: `--v --stats --progress`
- **LAN Speed Test minimum dataset**: 1GB for accurate results

## Gotchas
- File transfer tests are almost always bottlenecked by storage I/O (HDD RAID arrays will be far slower than NVMe)
- LAN Speed Test tool is outdated and less accurate than raw file transfers
- Opening firewall ports for baseline testing carries security risk — do cautiously
- Public release of benchmarking results **requires Twingate's prior approval**
- OpenVPN requires ~12MHz per Mbps; achieving 1Gbps needs a modern 4-core 3GHz CPU

## Related Docs
- [Wildcard Resources](https://www.twingate.com/docs) — DNS wildcard addressing
- Admin Console Activity Logs — determining P2P vs Relay connections
- Troubleshooting guide — for results significantly below baseline
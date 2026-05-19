# Twingate Performance

## Summary
Twingate uses peer-to-peer connections between Clients and Connectors to minimize throughput overhead, typically 5–15% reduction vs baseline. Benchmarks show Twingate significantly outperforms self-hosted WireGuard and OpenVPN on equivalent hardware. Relay fallback connections deliver 200–250Mbps consistently.

## Key Information
- **P2P overhead**: 1–5% throughput reduction in benchmark tests
- **Relay fallback**: 200–250Mbps consistently when P2P not possible
- **Split-tunnel design**: Only Resource-bound traffic routes through Twingate; other traffic (e.g., video calls) uses direct internet
- **Benchmark hardware**: 1 vCPU, 2GB RAM VPS with 1Gbps NIC

### Benchmark Results vs Baseline
| Test | Twingate | WireGuard | OpenVPN (UDP) |
|------|----------|-----------|---------------|
| Speedtest.net | -4% | -84% | -87% |
| 1.8GB File Transfer (Samba) | 0% | -63% | -66% |
| LAN Speed Test (1GB) | -1% | -64% | -71% |

## Prerequisites for Performance Testing
- Separate Remote Network from user's local network (ensures P2P path is tested)
- Remote Network internet connection: **≥1Gbps recommended**
- Access to Twingate Admin Console with permission to add Resources/Groups

## Step-by-Step: Speedtest.net Performance Test

1. **Admin Console → Resources → Add Resource**
2. Select target Remote Network; set label (e.g., "Speedtest.net Test")
3. DNS Address: `*speedtest*` (wildcard captures all speedtest-related domains)
4. Click **Add Resource** → assign to a Group (create isolated test Group if needed)
5. User runs baseline test with Twingate **disconnected**
6. User runs test again with Twingate **connected**
7. Verify egress IP in results reflects Remote Network location (not local IP)
8. Expected result: ≤5% degradation from baseline on P2P connection

## Configuration Values
- Wildcard DNS resource address: `*speedtest*`
- rsync flags for file transfer testing: `--v --stats --progress`
- LAN Speed Test minimum sample size: **1GB**

## Gotchas
- **Public benchmarking requires Twingate's prior approval** before publishing results
- File transfer tests are bottlenecked by storage I/O (HDD RAID << NVMe); use fast storage to avoid false negatives
- LAN Speed Test is outdated and less accurate; use ≥1GB test files for better results
- Opening firewall ports for baseline testing carries security risk — do with caution
- If egress IP doesn't change between tests, traffic isn't routing through the Remote Network
- P2P vs Relay status visible in **Admin Console → Activity Logs**

## Related Docs
- Wildcard Resource addresses
- Twingate Relay documentation
- Admin Console Activity Logs
- Connector installation/configuration
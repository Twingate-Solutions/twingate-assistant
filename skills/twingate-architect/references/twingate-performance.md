---
source: https://www.twingate.com/docs/twingate-performance
type: docs
fetched: 2026-08-14
source_version: 9a0f891eb2d056eafdf1f5ee14b21b7076020844d46501509a4d159ee8b88573
---

# Twingate Performance

## Summary
Twingate uses peer-to-peer connections between Clients and Connectors to minimize overhead, typically resulting in only 5–15% throughput reduction. Performance benchmarks show Twingate nearly matches baseline speeds, significantly outperforming self-hosted WireGuard and OpenVPN on equivalent hardware.

## Key Information
- **P2P performance**: 1–5% throughput reduction vs. baseline in testing
- **Relay fallback performance**: 200–250 Mbps consistently (when P2P not possible)
- **WireGuard comparison**: 63–84% throughput reduction on same hardware
- **OpenVPN comparison**: 66–87% throughput reduction on same hardware
- **Split-tunnel design**: Only Resource-destined traffic goes through tunnel; all other traffic (video calls, etc.) bypasses Twingate entirely
- **Connector requirements**: Tested on 1 vCPU / 2GB RAM with near-baseline results
- **Public benchmarks**: Require Twingate's prior written approval before publishing

## Benchmark Results (1 vCPU / 2GB RAM VPS)

| Test | Baseline | Twingate | WireGuard | OpenVPN UDP |
|------|----------|----------|-----------|-------------|
| Speedtest.net (multi) | 943 Mbps | 906 Mbps (-4%) | 148 Mbps (-84%) | 120 Mbps (-87%) |
| 1.8GB Samba Transfer | 600 Mbps | 600 Mbps (0%) | 224 Mbps (-63%) | 208 Mbps (-66%) |
| LAN Speed Test (1GB) | 459 Mbps | 455 Mbps (-1%) | 166 Mbps (-64%) | 133 Mbps (-71%) |

## Running Your Own Speed Test (Speedtest.net Method)

1. Go to **Admin Console → Resources → Add Resource**
2. Select target Remote Network (must be network-separated from user's location)
3. Set DNS Address to `*speedtest*` (wildcard captures all speedtest traffic)
4. Assign to a Group (create isolated test group to avoid affecting other users)
5. Have user run Speedtest.net **without** Twingate connected → record baseline
6. Have user run Speedtest.net **with** Twingate connected → compare results
7. Verify egress IP in results shows Remote Network location (confirms P2P routing)

## Configuration Values
- Wildcard resource address: `*speedtest*`
- Recommended test connection speed: **≥1 Gbps** at Remote Network
- File transfer test dataset: **≥1 GB** for accurate LAN Speed Test results
- rsync flags for monitoring: `--v --stats --progress`

## Gotchas
- **Storage I/O is often the bottleneck** for file transfer tests—HDD-based servers will cap results well below network capacity; use NVMe storage for accurate tests
- **Relay fallback** occurs when P2P is not technically feasible; check Admin Console activity logs to determine connection type (P2P vs. Relay)
- **LAN Speed Test tool** is outdated and less accurate than direct file transfers; use 1GB+ dataset to compensate
- Remote Network must be **physically/network separated** from the user's local network for valid P2P testing
- File share testing requires temporarily opening firewall ports for baseline comparison

## Determining Connection Type
Check **Admin Console → Activity Logs** to see whether a connection is peer-to-peer or routed via Relay.

## Related Docs
- Twingate Wildcard Resources
- Twingate Relays
- Remote Network Connector setup
- Troubleshooting connectivity issues
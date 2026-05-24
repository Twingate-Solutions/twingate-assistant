# Twingate Performance

## Summary
Twingate uses peer-to-peer connections between Clients and Connectors to minimize performance overhead, typically reducing throughput by only 5–15%. Benchmark tests show Twingate performs within 1–5% of baseline, significantly outperforming self-hosted WireGuard (63–84% degradation) and OpenVPN (66–87% degradation) on identical hardware.

## Key Information
- **P2P overhead**: 5–15% throughput reduction typical
- **Relay fallback**: 200–250 Mbps consistently when P2P unavailable
- **Split-tunnel design**: Only Resource-destined traffic goes through tunnel; other traffic (video calls, etc.) bypasses Twingate entirely
- **Benchmark hardware**: 1 vCPU, 2GB RAM VPS with 1Gbps connection
- **Benchmark results**:
  - Speedtest: Twingate -4% vs baseline; WireGuard -84%; OpenVPN -87%
  - File transfer (Samba): Twingate 0%; WireGuard -63%; OpenVPN -66%
  - LAN Speed Test: Twingate -1%; WireGuard -64%; OpenVPN -71%

## Prerequisites
- Separate Remote Network (cloud or physically separated data center) for meaningful testing
- Remote Network internet connection ≥ 1 Gbps recommended for testing
- Test user assigned to Group with access to test Resource

## Step-by-Step: Speedtest.net Performance Test
1. Admin Console → Resources → **Add Resource**
2. Select Remote Network; set label (e.g., "Speedtest.net Test")
3. DNS Address: `*speedtest*` (wildcard captures all speedtest traffic)
4. Assign to an isolated Group (optionally create new Group for test user only)
5. Run Speedtest.net **without** Twingate Client connected → record baseline download speed
6. Connect Twingate Client → re-run test → compare results
7. Verify egress IP in results reflects Remote Network location (confirms P2P routing)

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Wildcard DNS for Speedtest | `*speedtest*` |
| Recommended test file size (LAN Speed Test) | ≥ 1 GB |
| rsync flags for file transfer monitoring | `--v --stats --progress` |
| Expected relay throughput | 200–250 Mbps |
| Expected P2P overhead | 5–15% |

## Gotchas
- **Public benchmarks require Twingate approval** before release
- Relay connections are significantly slower than P2P; check Admin Console activity logs to confirm connection type
- File transfer tests are usually bottlenecked by storage I/O (HDD RAID much slower than NVMe), not the network
- Remote Network must be **physically/logically separate** from user's local network for valid P2P testing
- LAN Speed Test tool is outdated and less accurate; use ≥1 GB sample sizes if using it
- Low baseline speeds may indicate user's ISP/local network is the bottleneck, not Twingate

## Related Docs
- [Wildcard Resources](https://www.twingate.com/docs/wildcard-resources)
- Activity Logs (Admin Console) — verify P2P vs Relay connection status
- [Twingate Connectors](https://www.twingate.com/docs/connectors)
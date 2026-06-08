# Twingate Performance

## Summary
Twingate uses peer-to-peer connections between Clients and Connectors to minimize overhead, typically resulting in only 5–15% throughput reduction. Benchmarks show Twingate performs near-baseline (within 5%), significantly outperforming self-hosted WireGuard and OpenVPN on identical hardware. When P2P is unavailable, relay fallback provides 200–250 Mbps.

## Key Information
- **P2P overhead**: 5–15% throughput reduction (often less in practice)
- **Relay fallback**: 200–250 Mbps consistently
- **Split-tunnel design**: only Resource-bound traffic routes through Twingate; other traffic unaffected
- **Benchmark hardware**: 1 vCPU, 2GB RAM VPS with 1Gbps NIC

### Benchmark Results (vs. Baseline)
| Test | Twingate | WireGuard | OpenVPN (UDP) |
|------|----------|-----------|---------------|
| Speedtest.net | -4% | -84% | -87% |
| 1.8GB File Transfer (Samba) | 0% | -63% | -66% |
| LAN Speed Test (1GB) | -1% | -64% | -71% |

## Prerequisites for Performance Testing
- Separate Remote Network (not on same LAN as test user)
- Remote Network internet connection ≥ 1 Gbps recommended
- Twingate Admin Console access to add Resources

## Step-by-Step: Speedtest.net Performance Test

1. **Admin Console** → Resources → Add Resource
2. Set Remote Network to your test environment
3. Set DNS Address to `*speedtest*` (wildcard captures all speedtest traffic)
4. Add Resource to an isolated test Group; add only the test user
5. **Baseline**: Run Speedtest.net with Twingate Client **disconnected**
6. **Connected test**: Log into Twingate Client, run Speedtest.net again
7. Verify egress IP in results confirms traffic routed through Remote Network
8. Check Admin Console activity logs to confirm P2P vs. relay connection

## Configuration Values
- **Wildcard resource address**: `*speedtest*`
- **Recommended test file size** (LAN Speed Test): ≥ 1 GB for accuracy
- **rsync flags for file transfer testing**: `--v --stats --progress`

## Gotchas
- **Public benchmarks require Twingate approval** before publishing
- Relay fallback significantly lowers max throughput (~200–250 Mbps) — check activity logs to identify relay vs. P2P
- File transfer tests are often bottlenecked by storage I/O (HDD RAID much slower than NVMe), not the network
- Test Remote Network must be **physically separate** from user's LAN to validate P2P behavior
- Opening firewall ports for baseline testing carries security risk — do so cautiously

## Related Docs
- Wildcard Resources
- Activity Logs (Admin Console)
- Twingate Relay documentation
- Connector setup/deployment
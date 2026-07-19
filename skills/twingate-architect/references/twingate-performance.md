# Twingate Performance

## Summary
Twingate uses peer-to-peer connections between Clients and Connectors to minimize overhead, typically reducing throughput by only 5–15%. Benchmarks show Twingate performs within 4% of baseline, significantly outperforming self-hosted WireGuard and OpenVPN on equivalent hardware. Relay fallback (when P2P isn't possible) yields 200–250 Mbps consistently.

## Key Information
- **P2P overhead**: 5–15% throughput reduction typical
- **Relay fallback throughput**: 200–250 Mbps
- **Split-tunnel design**: Only Resource-bound traffic goes through tunnel; other traffic (video calls, etc.) uses direct internet
- **Benchmark results** (1 vCPU, 2GB RAM VPS):

| Test | Baseline | Twingate | WireGuard | OpenVPN (UDP) |
|------|----------|----------|-----------|---------------|
| Speedtest.net | 943 Mbps | 906 Mbps (-4%) | 148 Mbps (-84%) | 120 Mbps (-87%) |
| 1.8GB Samba Transfer | 600 Mbps | 600 Mbps (0%) | 224 Mbps (-63%) | 208 Mbps (-66%) |
| LAN Speed Test (1GB) | 459 Mbps | 455 Mbps (-1%) | 166 Mbps (-64%) | 133 Mbps (-71%) |

## Prerequisites
- Remote Network in a physically separate location from test client
- Remote Network internet connection ≥ 1 Gbps for meaningful testing
- Twingate Admin Console access
- Check Admin Console activity logs to confirm P2P vs. Relay connection type

## Step-by-Step: Speedtest.net Performance Test

1. **Baseline**: Run Speedtest.net with Twingate Client disconnected; record download speed
2. **Add Resource**: Admin Console → Resources → Add Resource
3. **Configure wildcard Resource**:
   - Select target Remote Network
   - DNS Address: `*speedtest*` (wildcard captures all speedtest domains)
   - Label: e.g., "Speedtest.net Test"
4. **Assign to Group**: Recommend creating isolated test Group with only test user
5. **Retest**: Connect Twingate Client → run Speedtest.net → compare results
6. **Verify**: Confirm egress IP shown in results matches Remote Network location (confirms traffic routed through Twingate)

## Configuration Values
- Wildcard DNS address format: `*speedtest*` (asterisks required)
- Recommended test dataset size for LAN Speed Test: ≥ 1 GB

## Gotchas
- **Public benchmarking requires Twingate's prior approval** before publishing results
- Storage I/O is often the real bottleneck in file transfer tests (HDD RAID << NVMe)
- Relay vs. P2P significantly affects results; verify connection type in Admin Console activity logs before drawing conclusions
- Test Remote Network must be geographically/network-separated from client to avoid local network being the bottleneck
- LAN Speed Test tool is outdated and less accurate; prefer actual file transfers or Speedtest.net

## Related Docs
- Wildcard Resource configuration
- Twingate Relays documentation
- Activity logs in Admin Console
- Troubleshooting connectivity issues
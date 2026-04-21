## Evaluating Twingate Performance

Covers performance characteristics of Twingate P2P connections compared to WireGuard and OpenVPN, and provides a methodology for running your own throughput tests. Peer-to-peer connections add 5-15% overhead versus baseline; relay fallback yields 200-250 Mbps consistently.

**Key Information:**
- P2P connection overhead: 5-15% throughput reduction vs. baseline
- Relay fallback (when P2P unavailable): 200-250 Mbps
- WireGuard on same hardware: 63-84% throughput reduction vs. baseline
- OpenVPN on same hardware: 66-87% throughput reduction vs. baseline
- Split-tunnel design: only Resource-bound traffic passes through the tunnel; other traffic (video conferencing, etc.) uses direct internet
- Determine P2P vs. relay status from the Admin Console activity logs
- Public release of Twingate benchmark results requires Twingate's prior written approval

**Test Methodology (Speedtest.net):**
1. Create a Remote Network in a physically separate environment from the test client
2. Add a wildcard Resource: address = `*speedtest*` (captures all speedtest domains), assign to a Group
3. Run Speedtest.net baseline with Twingate Client disconnected
4. Run Speedtest.net with Twingate Client connected -- egress IP should change to the Remote Network's location
5. Compare results; within 5% of baseline indicates a healthy P2P connection

**Configuration Values:**
- Wildcard address format: `*speedtest*` (asterisks required)
- Recommended test server upstream: 1 Gbps minimum

**Gotchas:**
- File transfer tests are usually bottlenecked by storage I/O (especially HDD arrays), not the network -- use NVMe-based storage to remove this variable
- LAN Speed Test (totusoft.com) is older and less accurate; use 1 GB+ sample file size for better results
- A significantly lower-than-expected result warrants investigating both the client's local network and the Remote Network's upstream bandwidth

**Related Docs:**
- /docs/connector -- Connector deployment for test Remote Networks
- /docs/remote-networks -- Setting up test Remote Networks
- /docs/resources -- Configuring wildcard Resources

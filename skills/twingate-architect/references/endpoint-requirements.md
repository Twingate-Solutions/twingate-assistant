## Endpoint Requirements

Lists system requirements and outbound firewall rules needed for the Twingate Client. The Client is under 10 MB, uses the OS native VPN interface, and requires no special permissions beyond VPN setup.

**Key Information:**
- App size: under 10 MB; minimal CPU/memory footprint
- Uses OS native VPN (local connection to 127.0.0.1) to intercept Resource-bound traffic -- this is expected behavior
- No special permissions required beyond the VPN interface
- Client download: get.twingate.com (auto-detects platform)

**Required Outbound Firewall Rules:**
- TCP 443 -- communication with Twingate Controller and Relay infrastructure
- TCP 30000-31000 -- fallback Relay connections when P2P is unavailable
- UDP 1-65535 (+ QUIC/HTTP3) -- peer-to-peer connectivity for optimal performance

**Gotchas:**
- Blocking UDP 1-65535 forces all connections through Relay (200-250 Mbps cap) -- open UDP for P2P performance
- Seeing a local VPN connection (127.0.0.1) is expected; it is how Twingate intercepts Resource traffic

**Related Docs:**
- /docs/clients -- Client installation overview
- /docs/twingate-performance -- P2P vs. relay performance comparison
- /docs/local-peer-to-peer-best-practices -- P2P firewall configuration

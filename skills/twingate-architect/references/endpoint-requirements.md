# Endpoint Requirements

## Summary
The Twingate Client must be installed and running on user devices to access protected Resources. It uses the host OS's native VPN functionality to intercept traffic, requiring minimal resources (<10MB). Firewall rules are generally not needed but specific ports must be accessible if connectivity issues arise.

## Key Information
- Client size: <10MB, minimal system resource usage
- Uses native OS VPN functionality — VPN connection activating on device is expected/normal
- Download available at `get.twingate.com` (auto-detects platform)
- Compatible with most MDM/device management solutions

## Prerequisites
- Device must have outbound internet access
- Supported operating system with native VPN capability

## Firewall Rules (Outbound Only)

| Protocol | Port(s) | Purpose |
|----------|---------|---------|
| TCP | 443 | Communication with Twingate Controller and Relay infrastructure |
| TCP | 30000–31000 | Connections to Relay infrastructure (fallback when P2P unavailable) |
| UDP + QUIC/HTTP3 | 1–65535 | Peer-to-peer connectivity for optimal performance |

All rules are **outbound-initiated** — no inbound rules required.

## Gotchas
- VPN connection appearing on the device is **expected behavior**, not an error
- Firewall rules are not typically required; only needed for troubleshooting connectivity issues
- UDP ports 1–65535 are required for P2P; restricting these degrades performance and forces Relay fallback
- TCP 30000–31000 is the Relay fallback path when P2P (UDP) is blocked

## Related Docs
- Download & Installation guide
- Managed Devices section
- QUIC/HTTP3 guide (referenced for UDP port usage)
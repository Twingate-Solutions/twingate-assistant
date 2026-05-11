# Endpoint Requirements

## Summary
The Twingate Client must be installed and running to access protected Resources. It uses the host OS's native VPN functionality to intercept traffic, requiring outbound firewall access on specific ports for Controller, Relay, and peer-to-peer connectivity.

## Key Information
- Client size: <10MB, minimal resource usage
- Download at: `get.twingate.com` (auto-detects platform)
- Native OS VPN activation is expected behavior, not an error
- Compatible with most device management (MDM) solutions

## Prerequisites
- Device with supported OS
- Outbound internet access on required ports
- Admin rights for installation (implied)

## Firewall Rules (Outbound Only)

| Protocol | Port(s) | Purpose |
|----------|---------|---------|
| TCP | 443 | Controller + Relay infrastructure communication |
| TCP | 30000–31000 | Relay fallback (when P2P unavailable) |
| UDP/QUIC (HTTP/3) | 1–65535 | Peer-to-peer connectivity (optimal performance) |

> No special firewall rules are typically required. Use the above list only for troubleshooting connectivity issues.

## Gotchas
- VPN indicator appearing on the device is **expected** — not a sign of misconfiguration
- UDP ports 1–65535 are needed for P2P; restricting these degrades performance but doesn't break connectivity (falls back to TCP Relay on 30000–31000)
- Port 443 TCP is the minimum required for basic functionality

## Related Docs
- Download & Installation guide
- Managed Devices section
- HTTP/3 / QUIC guide (linked in source for UDP/QUIC details)
# Endpoint Requirements

## Page Title
Endpoint Requirements

## Summary
The Twingate Client must be installed and running on a device to access protected Resources. It uses the host OS's native VPN functionality to intercept traffic, so a VPN connection appearing on the device is expected behavior.

## Key Information
- Client size: less than 10MB, minimal resource usage
- Download via: `get.twingate.com` (auto-detects platform)
- Compatible with most device management (MDM) solutions
- Uses native OS VPN stack for traffic interception

## Prerequisites
- Device access to `get.twingate.com` for download
- Outbound firewall rules permitting required ports (see below)

## Configuration Values

### Required Firewall Rules (Outbound Only)
| Protocol | Port(s) | Purpose |
|----------|---------|---------|
| TCP | 443 | Controller and Relay infrastructure communication |
| TCP | 30000–31000 | Relay fallback (when peer-to-peer unavailable) |
| UDP/QUIC (HTTP/3) | 1–65535 | Peer-to-peer connectivity (optimal performance) |

## Gotchas
- A VPN connection activating on the device is **expected** — not a malfunction
- UDP ports 1–65535 are required for peer-to-peer; restricting these degrades performance but doesn't block access (falls back to TCP Relay)
- No special inbound firewall rules are needed
- Standard deployments typically work without any firewall changes; use the port list only for troubleshooting

## Related Docs
- Download & Installation
- Managed Devices
- HTTP/3 / QUIC guide (referenced for UDP/QUIC behavior)
# Endpoint Requirements

## Summary
The Twingate Client must be installed and running on user devices to access protected Resources. It uses the host OS's native VPN functionality to intercept traffic, requiring minimal resources (<10MB). Specific outbound firewall ports are needed for full functionality.

## Key Information
- Client size: <10MB, minimal system resource usage
- Uses native OS VPN functionality — VPN connection activating on device is expected/normal
- Download via `get.twingate.com` (auto-detects platform)
- Compatible with most device management solutions (MDM/EMM)

## Prerequisites
- Device access to install software
- Outbound firewall connectivity on required ports (see below)

## Configuration Values

### Required Firewall Rules (Outbound Only)

| Port/Range | Protocol | Purpose |
|---|---|---|
| `443` | TCP | Communication with Twingate Controller and Relay infrastructure |
| `30000-31000` | TCP | Relay infrastructure connections (fallback when P2P unavailable) |
| `1-65535` | UDP + QUIC/HTTP3 | Peer-to-peer connectivity (optimal performance) |

## Gotchas
- No inbound firewall rules required — all connections are outbound-initiated
- UDP ports `1-65535` are needed for P2P; without them, traffic falls back to Relay (ports `30000-31000`), which still works but is suboptimal
- Special firewall rules are not usually needed; use the port list above only for troubleshooting connectivity issues
- VPN indicator appearing on device is **expected behavior**, not an error

## Related Docs
- Download & Installation
- Managed Devices
- QUIC/HTTP3 guide (referenced for UDP/QUIC details)
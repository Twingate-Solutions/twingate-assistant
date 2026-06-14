# Endpoint Requirements

## Page Title
Endpoint Requirements

## Summary
The Twingate Client must be installed and running on a device to access protected Resources. It uses the host OS's native VPN functionality to intercept traffic, requiring minimal resources (<10MB). Firewall rules may need adjustment if connectivity issues arise.

## Key Information
- Client download available at `get.twingate.com` (auto-detects platform)
- App size: <10MB, minimal system resource usage
- Uses native OS VPN functionality — VPN connection activating on device is expected/normal
- Compatible with most device management (MDM) solutions

## Prerequisites
- Device with supported OS
- Outbound internet access on required ports (see below)

## Configuration Values

### Required Firewall Rules (Outbound Only)

| Protocol | Port(s) | Purpose |
|----------|---------|---------|
| TCP | 443 | Communication with Twingate Controller and Relay infrastructure |
| TCP | 30000–31000 | Relay fallback when peer-to-peer is unavailable |
| UDP/QUIC (HTTP/3) | 1–65535 | Peer-to-peer connectivity (optimal performance) |

## Step-by-Step

1. Navigate to `get.twingate.com` — client downloads automatically for detected platform
2. Install the client application
3. Start the client before attempting to access protected Resources
4. If connectivity issues occur, verify outbound firewall rules match the table above

## Gotchas
- **VPN activation is expected** — the client activates a native OS VPN connection; this is not an error
- **UDP ports 1–65535** must be open for peer-to-peer (P2P); without this, traffic falls back to Relay via TCP 30000–31000, which may reduce performance
- Firewall rules are typically not needed by default, but should be checked first when troubleshooting connectivity
- All connections are **outbound-initiated** — no inbound ports required

## Related Docs
- Download & Installation (detailed install guide)
- Managed Devices (MDM/device management integration)
- HTTP/3 / QUIC guide (linked from firewall section)
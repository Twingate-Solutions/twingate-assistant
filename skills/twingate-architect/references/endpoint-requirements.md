# Endpoint Requirements

## Summary
The Twingate Client must be installed and running on a device to access protected Resources. It uses the host OS's native VPN functionality to intercept traffic, requiring minimal resources (<10MB). Firewall rules may need adjustment if connectivity issues arise.

## Key Information
- Client size: <10MB, minimal system resource usage
- Uses native OS VPN functionality — VPN connection activating on device is expected behavior
- Download at `get.twingate.com` (auto-detects platform)
- Compatible with most device management solutions (MDM/EMM)

## Prerequisites
- Device running a supported OS platform
- Outbound internet access on required ports
- Admin rights to install VPN/network extensions (implied by OS VPN usage)

## Firewall Rules (Outbound Only)

| Protocol | Port(s) | Purpose |
|----------|---------|---------|
| TCP | 443 | Communication with Twingate Controller and Relay infrastructure |
| TCP | 30000–31000 | Relay connections when peer-to-peer is unavailable |
| UDP/QUIC (HTTP/3) | 1–65535 | Peer-to-peer connectivity (optimal performance) |

**Note:** All connections are **outbound-initiated** — no inbound rules required.

## Installation

1. Navigate to `get.twingate.com`
2. Platform is auto-detected; download and install the Client
3. For managed/enterprise deployments, refer to the Managed Devices documentation

## Gotchas
- UDP ports 1–65535 must be open for peer-to-peer (best performance); if blocked, traffic falls back to Relay via TCP 30000–31000
- A VPN indicator appearing on the device is **expected** — not an error
- No special firewall rules are required by default; use the port list only for troubleshooting connectivity issues
- QUIC/HTTP3 is used for UDP transport — may be blocked by some firewalls that restrict UDP broadly

## Related Docs
- Download & Installation (detailed install guide)
- Managed Devices (MDM/device management compatibility)
- QUIC/HTTP3 guide (UDP peer-to-peer connectivity details)
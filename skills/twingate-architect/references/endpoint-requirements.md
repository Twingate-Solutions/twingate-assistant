# Endpoint Requirements

## Page Title
Endpoint Requirements

## Summary
The Twingate Client must be installed and running on devices to access protected Resources. It uses the host OS's native VPN functionality to intercept traffic, so a VPN connection activating on the device is expected behavior.

## Key Information
- Client app size: less than 10MB, minimal resource usage
- Download available at `get.twingate.com` (auto-detects platform)
- Compatible with most device management solutions
- Uses native OS VPN stack — VPN activation is normal, not an error

## Prerequisites
- Device with supported OS
- Outbound internet access on required ports
- Admin/install permissions on the device

## Configuration Values

### Required Firewall Rules (Outbound Only)

| Protocol | Port(s) | Purpose |
|----------|---------|---------|
| TCP | 443 | Communication with Twingate Controller and Relay infrastructure |
| TCP | 30000–31000 | Relay connections when peer-to-peer is unavailable |
| UDP + QUIC (HTTP/3) | 1–65535 | Peer-to-peer connectivity (optimal performance) |

## Step-by-Step

1. Navigate to `get.twingate.com` — client downloads automatically for detected platform
2. Install the Client application
3. Ensure outbound firewall rules are not blocking required ports
4. Connect — a VPN connection activating is expected

## Gotchas
- **No inbound rules needed** — all connections are outbound-initiated; default firewall configs typically work without changes
- **UDP 1–65535 required for P2P** — restricting this port range will degrade performance and fall back to Relay
- **VPN icon is expected** — users may be confused by the OS VPN indicator; this is by design
- Firewall rules are primarily needed for troubleshooting, not standard setup

## Related Docs
- Download & Installation (detailed install instructions)
- Managed Devices (MDM/device management compatibility)
- HTTP/3 / QUIC guide (referenced for UDP/QUIC port usage)
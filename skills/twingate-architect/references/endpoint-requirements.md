# Endpoint Requirements

## Summary
The Twingate Client must be installed and running on user devices to access protected Resources. It uses the host OS's native VPN functionality to intercept traffic, requiring minimal resources (<10MB). Firewall rules are generally not needed but specific ports must be reachable for full functionality.

## Key Information
- Client size: <10MB, minimal system resource usage
- Uses native OS VPN functionality — VPN connection activating on device is expected/normal
- Download available at `get.twingate.com` (auto-detects platform)
- Compatible with most device management (MDM) solutions

## Prerequisites
- Device access to install software
- Outbound internet connectivity on required ports (see below)

## Configuration Values

### Required Firewall Ports (Outbound Only)

| Port/Range | Protocol | Purpose |
|---|---|---|
| `443` | TCP | Communication with Twingate Controller and Relay infrastructure |
| `30000-31000` | TCP | Relay connections when peer-to-peer is unavailable |
| `1-65535` | UDP + QUIC (HTTP/3) | Peer-to-peer connectivity (optimal performance) |

All rules are **outbound-initiated** — no inbound rules required.

## Step-by-Step: Client Installation
1. Navigate to `get.twingate.com`
2. Client auto-downloads for the detected platform
3. Install and run the application
4. For managed/MDM deployment, see Managed Devices documentation

## Gotchas
- A VPN connection appearing in OS network settings is **expected behavior**, not an error
- UDP ports `1-65535` are needed for peer-to-peer; restricting these degrades performance but won't break connectivity (falls back to Relay on TCP `30000-31000`)
- Firewall rules are not required in typical setups — only needed for troubleshooting connectivity issues

## Related Docs
- Download & Installation (detailed install guide)
- Managed Devices (MDM/enterprise deployment)
- HTTP/3 and QUIC guide (UDP/QUIC port details)
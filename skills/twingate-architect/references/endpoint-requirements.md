# Endpoint Requirements

## Page Title
Endpoint Requirements

## Summary
The Twingate Client must be installed and running on a device to access Twingate-protected Resources. It uses the host OS's native VPN functionality to intercept traffic, requiring less than 10MB and minimal system resources.

## Key Information
- Client size: <10MB, minimal resource usage
- Download URL: `get.twingate.com` (auto-detects platform)
- Uses native OS VPN stack — VPN connection activation is expected/normal
- Compatible with most device management (MDM/EMM) solutions

## Prerequisites
- Device running a supported OS
- Outbound internet access on required ports (see below)
- Twingate network/account to connect to

## Configuration Values

### Required Firewall Rules (Outbound Only)

| Protocol | Port(s) | Purpose |
|----------|---------|---------|
| TCP | 443 | Controller and Relay infrastructure communication |
| TCP | 30000–31000 | Relay fallback when peer-to-peer is unavailable |
| UDP/QUIC (HTTP/3) | 1–65535 | Peer-to-peer connectivity (optimal performance) |

- All connections are **outbound-initiated** — no inbound rules required
- UDP/QUIC ports enable best performance; blocking them forces Relay fallback

## Step-by-Step: Client Installation
1. Navigate to `get.twingate.com`
2. Client auto-downloads for the detected platform
3. Install and launch the Client
4. Connect using your Twingate network address

For advanced/managed deployments, refer to the Managed Devices section.

## Gotchas
- A VPN connection appearing in the OS is **expected behavior**, not an error
- Firewall rules are generally not needed in standard environments — only troubleshoot if connectivity issues arise
- UDP ports 1–65535 must be open for peer-to-peer; if blocked, traffic falls back to Relay via TCP 30000–31000 with degraded performance
- QUIC/HTTP/3 UDP traffic uses the full port range — overly restrictive UDP egress policies will impact performance

## Related Docs
- Download & Installation (detailed install guide)
- Managed Devices (MDM/EMM deployment)
- QUIC/HTTP/3 guide (UDP peer-to-peer connectivity details)
---
source: https://www.twingate.com/docs/endpoint-requirements
type: docs
fetched: 2026-08-14
source_version: 8536e1fa217fd08bb185b36b465830393266c1c5f095c1c863f30797aa4dc673
---

# Endpoint Requirements

## Page Title
Endpoint Requirements

## Summary
The Twingate Client must be installed and running on a device to access protected Resources. It uses the host OS's native VPN functionality to intercept traffic, so a VPN connection appearing on the device is expected behavior. The app is under 10MB and lightweight on system resources.

## Key Information
- Client download available at `get.twingate.com` (auto-detects platform)
- Compatible with most device management/MDM solutions
- Uses native OS VPN stack — VPN activation is normal and expected
- No special firewall rules typically required; list below is for troubleshooting

## Prerequisites
- Device must have the Twingate Client installed and running
- Outbound internet connectivity on required ports

## Configuration Values

### Required Firewall Rules (Outbound Only)

| Protocol | Port(s) | Purpose |
|----------|---------|---------|
| TCP | 443 | Communication with Twingate Controller and Relay infrastructure |
| TCP | 30000–31000 | Relay connections when peer-to-peer is unavailable |
| UDP/QUIC (HTTP/3) | 1–65535 | Peer-to-peer connectivity (optimal performance) |

## Gotchas
- **VPN prompt is expected** — the Client activates a VPN connection on the device; this is not an error and should not alarm end users
- **UDP 1–65535** is required for peer-to-peer; blocking this degrades performance but doesn't break connectivity (falls back to Relay via TCP 30000–31000)
- TCP 443 is the minimum required port; without it, the Client cannot communicate at all

## Related Docs
- [Download & Installation](https://www.twingate.com/docs/download-and-installation)
- [Managed Devices](https://www.twingate.com/docs/managed-devices)
- QUIC/HTTP3 guide (linked inline on the docs page)
# Endpoint Requirements

## Summary
The Twingate Client must be installed and running on user devices to access protected Resources. It uses the host OS's native VPN functionality to intercept traffic, requiring minimal resources (<10MB). Firewall rules are generally not needed but specific ports must be reachable for full functionality.

## Key Information
- Client size: <10MB, minimal system resource usage
- Uses native OS VPN functionality — VPN connection activating on device is expected/normal
- Download via `get.twingate.com` (auto-detects platform)
- Compatible with most MDM/device management solutions

## Prerequisites
- Device with supported OS
- Outbound internet connectivity
- Admin rights for installation (implied by VPN functionality usage)

## Firewall Rules (Outbound Only)

| Protocol | Port(s) | Purpose |
|----------|---------|---------|
| TCP | 443 | Communication with Twingate Controller and Relay infrastructure |
| TCP | 30000–31000 | Relay infrastructure connections (fallback when peer-to-peer unavailable) |
| UDP/QUIC (HTTP/3) | 1–65535 | Peer-to-peer connectivity for optimal performance |

## Gotchas
- Firewall rules are **not usually required** — only needed for troubleshooting connectivity issues
- UDP ports 1–65535 required for P2P; restrictive firewalls blocking UDP will fall back to TCP relay (ports 30000–31000)
- If TCP 30000–31000 and UDP are both blocked, only TCP 443 remains — may degrade performance
- Native VPN activation is intentional, not a conflict with existing VPN software (verify compatibility separately)

## Related Docs
- [Download & Installation](#) — detailed installation instructions
- [Managed Devices](#) — MDM/device management compatibility
- [HTTP/3 / QUIC guide](#) — UDP/QUIC configuration details
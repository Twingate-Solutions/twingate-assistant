# Twingate Client Application

## Summary
The Twingate Client enables user access to private network Resources across macOS, Windows, Linux, iOS, and Android/ChromeOS. It establishes a local VPN connection to `127.0.0.1` to intercept traffic to private Resources. Clients older than 12 months lose connectivity to the Twingate service.

## Key Information
- Users enter their organization subdomain (e.g., `autoco` for `autoco.twingate.com`) once on first setup
- No special permissions required, but creates local VPN to `127.0.0.1`
- Clients older than 12 months are unsupported and cannot connect

## Download URLs by Platform

| Platform | URL |
|----------|-----|
| macOS (PKG) | `https://api.twingate.com/download/darwin?installer=pkg` |
| Windows (EXE) | `https://api.twingate.com/download/windows` |
| Windows (MSI) | `https://api.twingate.com/download/windows?installer=msi` |
| iOS | `https://api.twingate.com/download/ios` |
| Android/ChromeOS | `https://api.twingate.com/download/android` |
| Linux | Via public repositories + convenience script |
| End-user self-install | `get.twingate.com` (auto-detects platform) |

## Minimum Supported Versions (as of last update)
- macOS: `2024.57`
- Windows: `2024.51`
- Linux: `2024.63`
- iOS: `2024.57`
- Android: `2024.85`

## Prerequisites
- Organization subdomain on `twingate.com`
- For managed deployments: software distribution tooling (see managed devices docs)

## Gotchas
- Clients older than 12 months **cannot connect** — enforce update policies proactively
- Linux updates come from **public repositories** (not Twingate-hosted), requires separate repo configuration
- Historical versions available via public changelog, but running old versions risks service interruption

## Update Strategy
- **Automatic updates**: Available when local users have elevated permissions; client checks and installs updates automatically
- **Managed/MDM deployments**: Use platform-specific guides for macOS/iOS and Windows distribution
- Reference the [Client changelog](https://www.twingate.com/docs/client-changelog) before updating in production

## Related Docs
- Endpoint Requirements
- Managed Devices deployment guides (macOS/iOS, Windows)
- Linux client source repositories
- Linux convenience install script
- Public Client changelog
# Twingate Client Applications

## Summary
The Twingate Client enables users to access private network Resources and is available on macOS, Windows, Linux, iOS, and Android/ChromeOS. Users authenticate by entering their organization's subdomain (e.g., `autoco` for `autoco.twingate.com`) on first setup. The client creates a local VPN connection to `127.0.0.1` to intercept traffic to private Resources.

## Key Information
- No special permissions required, but sets up local VPN to `127.0.0.1`
- Organization subdomain only needs to be entered once on first use
- Clients older than 12 months cannot connect to Twingate service
- End users can self-install via `get.twingate.com` (auto-detects platform)

## Download Endpoints

| Platform | URL |
|----------|-----|
| macOS (PKG) | `https://api.twingate.com/download/darwin?installer=pkg` |
| Windows (EXE) | `https://api.twingate.com/download/windows` |
| Windows (MSI) | `https://api.twingate.com/download/windows?installer=msi` |
| iOS | `https://api.twingate.com/download/ios` |
| Android/ChromeOS | `https://api.twingate.com/download/android` |
| Linux | Convenience script + public repositories |

## Minimum Supported Versions
Clients below these versions cannot connect:
- **macOS:** 2024.57
- **Windows:** 2024.51
- **Linux:** 2024.63
- **iOS:** 2024.57
- **Android:** 2024.85

## Installation Methods
- **End users:** Browse to `get.twingate.com` for auto-detected platform download
- **Managed devices:** Use platform-specific managed device documentation
- **Linux:** Use published convenience script or configure source repositories

## Updates
- macOS/Windows: Hosted by Twingate, pulled automatically when user has elevated permissions
- Linux: Hosted in public repositories
- iOS/Android: Distributed via App Store / Google Play Store
- Automate updates via software distribution tools (separate guides for macOS/iOS and Windows)

## Gotchas
- Clients older than 12 months are **unsupported and will lose connectivity** — enforce update policies
- Historical versions available in public changelog if pinning is required
- Linux updates come from external repos, not Twingate-hosted endpoints
- Local VPN to `127.0.0.1` may conflict with other VPN software or local network tools

## Related Docs
- Endpoint Requirements
- Managed Devices (platform-specific deployment)
- Linux client source repositories
- Client changelog (version history)
- macOS/iOS deployment guide
- Windows deployment guide
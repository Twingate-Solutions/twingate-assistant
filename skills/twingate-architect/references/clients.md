# Twingate Client Applications

## Summary
The Twingate Client enables users to access private Resources and threat protection across macOS, Windows, Linux, iOS, and Android/ChromeOS. Setup requires entering the organization's subdomain once; the client creates a local VPN to `127.0.0.1` to intercept traffic to private Resources.

## Key Information
- Supported platforms: macOS, Windows, Linux, iOS, Android, ChromeOS
- Organization name = subdomain prefix (e.g., `autoco` for `autoco.twingate.com`)
- No special permissions required; uses local VPN to `127.0.0.1`
- Clients older than 12 months cannot connect to Twingate service

## Download URLs

| Platform | URL |
|----------|-----|
| Auto-detect | `https://get.twingate.com` |
| macOS (PKG) | `https://api.twingate.com/download/darwin?installer=pkg` |
| Windows (EXE) | `https://api.twingate.com/download/windows` |
| Windows (MSI) | `https://api.twingate.com/download/windows?installer=msi` |
| Linux | Convenience script via public repos |
| iOS | `https://api.twingate.com/download/ios` |
| Android/ChromeOS | `https://api.twingate.com/download/android` |

## Minimum Supported Versions
Clients below these versions cannot connect:
- macOS: `2024.57`
- Windows: `2024.51`
- Linux: `2024.63`
- iOS: `2024.57`
- Android: `2024.85`

## Installation Methods
- **End users**: Direct to `get.twingate.com` (auto-detects platform)
- **Managed devices**: Use managed devices documentation for MDM/deployment tools
- **Linux**: Use convenience script for any supported distribution

## Updates
- macOS/Windows: Hosted by Twingate; automatic updates available when users have elevated permissions
- Linux: Hosted in public repositories
- iOS/Android: Distributed via App Store / Google Play Store
- Managed deployment guides available for macOS, iOS, and Windows

## Gotchas
- Clients older than 12 months are **blocked** from connecting — enforce update policies proactively
- Linux updates come from public repos (not Twingate-hosted), so repo access must be maintained
- Automatic updates only work when local users have elevated permissions; otherwise use software distribution tools

## Related Docs
- Endpoint Requirements
- Managed Devices documentation
- Linux client source repositories
- Client public changelog
- macOS/iOS deployment guide
- Windows deployment guide
# Twingate Client Application

## Summary
The Twingate Client provides users access to private Resources and threat protection across macOS, Windows, Linux, iOS, and Android/ChromeOS. Installation requires only the organization subdomain (e.g., `autoco` for `autoco.twingate.com`). The client uses a local VPN connection to `127.0.0.1` to intercept traffic to private Resources.

## Key Information
- No special permissions required on the device
- Local VPN connection established to `127.0.0.1` for traffic interception
- Clients older than 12 months cannot connect to Twingate service
- Organization subdomain only needs to be entered once on first setup

## Download URLs by Platform

| Platform | URL |
|----------|-----|
| Auto-detect | `get.twingate.com` |
| macOS (PKG) | `https://api.twingate.com/download/darwin?installer=pkg` |
| Windows (EXE) | `https://api.twingate.com/download/windows` |
| Windows (MSI) | `https://api.twingate.com/download/windows?installer=msi` |
| Linux | Convenience script + public repos |
| iOS | `https://api.twingate.com/download/ios` |
| Android/ChromeOS | `https://api.twingate.com/download/android` |

## Minimum Supported Versions
Clients below these versions cannot connect:
- **macOS**: 2024.57
- **Windows**: 2024.51
- **Linux**: 2024.63
- **iOS**: 2024.57
- **Android**: 2024.85

## Installation Methods
- **End users**: Direct to `get.twingate.com` (auto-detects platform)
- **Managed devices**: Use platform-specific managed device documentation
- **Linux**: Use published convenience script for any supported distribution

## Updates
- macOS/Windows: Hosted by Twingate, pulled from static URLs above
- Linux: Hosted in public repositories
- iOS: App Store
- Android/ChromeOS: Google Play Store
- Auto-updates available when local users have elevated permissions
- Managed deployment guides available for macOS/iOS and Windows

## Gotchas
- Clients older than 12 months are hard-blocked from connecting — enforce update policies
- Historical versions available via public changelog (MSI/macOS only)
- Linux updates come from external repos, not Twingate-hosted endpoints
- Auto-update requires elevated local user permissions; managed environments need separate deployment tooling

## Related Docs
- Endpoint Requirements
- Managed Devices documentation
- Linux client documentation (source repositories)
- Client changelog
- macOS/iOS deployment guide
- Windows deployment guide
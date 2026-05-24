# Twingate Client Applications

## Summary
The Twingate Client enables users to access private Resources and provides threat protection across macOS, Windows, Linux, iOS, and Android/ChromeOS. Clients connect by entering their organization's subdomain and authenticate via a local VPN to `127.0.0.1` for traffic interception. Clients older than 12 months lose connectivity to the Twingate service.

## Key Information
- Organization name = subdomain prefix (e.g., `autoco` for `autoco.twingate.com`)
- Local VPN established to `127.0.0.1` to intercept Resource traffic
- No special permissions required on endpoint
- Clients >12 months old cannot connect to Twingate service

## Download URLs

| Platform | URL |
|----------|-----|
| Auto-detect | `get.twingate.com` |
| macOS (PKG) | `https://api.twingate.com/download/darwin?installer=pkg` |
| Windows (EXE) | `https://api.twingate.com/download/windows` |
| Windows (MSI) | `https://api.twingate.com/download/windows?installer=msi` |
| Linux | Convenience script + package repos |
| iOS | `https://api.twingate.com/download/ios` |
| Android/ChromeOS | `https://api.twingate.com/download/android` |

## Minimum Supported Versions
Clients below these versions cannot connect:
- **macOS:** 2024.57
- **Windows:** 2024.51
- **Linux:** 2024.63
- **iOS:** 2024.57
- **Android:** 2024.85

## Installation Methods
- **End users (self-managed):** Direct to `get.twingate.com`
- **Managed devices:** Use platform-specific managed device documentation
- **Linux:** Use published convenience script; packages in public repositories
- **macOS/iOS & Windows:** Automated deployment guides available

## Gotchas
- Organization name entry is one-time only on first client setup
- Historical versions available via public changelog (MSI/PKG only; not EXE)
- Automatic updates only work when local users have elevated permissions
- Linux updates come from public repos, not Twingate-hosted like other platforms
- ChromeOS uses Android/Google Play distribution

## Related Docs
- Endpoint Requirements
- Managed Devices documentation
- Linux client source repositories
- Client changelog (version history)
- macOS/iOS deployment guide
- Windows deployment guide
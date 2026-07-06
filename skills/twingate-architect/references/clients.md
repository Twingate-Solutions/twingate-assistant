# Twingate Client Application

## Summary
The Twingate Client provides users access to private Resources and threat protection across major platforms. Users authenticate by entering their organization's subdomain once at initial setup. Clients older than 12 months are blocked from connecting to the service.

## Key Information
- **Supported platforms:** macOS, Windows, Linux, iOS, Android, ChromeOS
- **No special permissions required**, but creates a local VPN connection to `127.0.0.1` to intercept traffic to private Resources
- **Organization name** = subdomain only (e.g., `autoco` for `autoco.twingate.com`)
- Clients older than 12 months cannot connect to Twingate service

## Download URLs

| Platform | URL |
|----------|-----|
| Auto-detect | `https://get.twingate.com` |
| macOS (PKG) | `https://api.twingate.com/download/darwin?installer=pkg` |
| Windows (EXE) | `https://api.twingate.com/download/windows` |
| Windows (MSI) | `https://api.twingate.com/download/windows?installer=msi` |
| Linux | Convenience script + public repos |
| iOS | `https://api.twingate.com/download/ios` |
| Android/ChromeOS | `https://api.twingate.com/download/android` |

## Minimum Supported Versions
| Platform | Minimum Version |
|----------|----------------|
| macOS | 2024.57 |
| Windows | 2024.51 |
| Linux | 2024.63 |
| iOS | 2024.57 |
| Android | 2024.85 |

## Prerequisites
- Valid Twingate account with a configured subdomain
- For managed devices: use managed devices documentation for deployment
- For automatic updates: local users need elevated permissions

## Gotchas
- Clients below minimum version thresholds are **hard-blocked** from connecting — enforce update policies proactively
- Linux updates come from **public repositories**, not Twingate-hosted binaries (unlike other platforms)
- macOS/Windows/iOS/Android historical versions available via the [public changelog](https://www.twingate.com/docs/client-changelog)
- Local VPN to `127.0.0.1` may conflict with other VPN software — check Endpoint Requirements docs

## Related Docs
- Endpoint Requirements
- Managed Devices (platform-specific deployment)
- Linux client source repositories
- Client changelog
- macOS/iOS and Windows automated update guides
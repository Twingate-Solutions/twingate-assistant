# Twingate Client Application

## Summary
The Twingate Client enables users to access private network Resources and runs on macOS, Windows, Linux, iOS, and Android/ChromeOS. It creates a local VPN connection to `127.0.0.1` to intercept traffic to private Resources. Clients older than 12 months cannot connect to the Twingate service.

## Key Information
- Organization name (subdomain) only needs to be entered once during initial setup
- No special permissions required, but local VPN to `127.0.0.1` is established
- Unsupported (>12 month old) clients are blocked from connecting entirely
- Linux updates via public repositories; all other platforms via vendor app stores or Twingate-hosted endpoints

## Prerequisites
- Twingate account subdomain (e.g., `autoco` from `autoco.twingate.com`)
- For managed devices: use managed devices documentation instead of end-user install flow

## Download Endpoints

| Platform | URL |
|----------|-----|
| macOS (PKG) | `https://api.twingate.com/download/darwin?installer=pkg` |
| Windows (EXE) | `https://api.twingate.com/download/windows` |
| Windows (MSI) | `https://api.twingate.com/download/windows?installer=msi` |
| iOS | `https://api.twingate.com/download/ios` |
| Android/ChromeOS | `https://api.twingate.com/download/android` |
| Any user (auto-detect) | `https://get.twingate.com` |
| Linux | Convenience script + source repositories (see Linux docs) |

## Minimum Supported Versions (as of last update)
- macOS: `2024.57`
- Windows: `2024.51`
- Linux: `2024.63`
- iOS: `2024.57`
- Android: `2024.85`

## Update Strategy
- Historical versions available via [public changelog](https://www.twingate.com/docs/client-changelog)
- Automatic updates available when local users have elevated permissions
- MDM/software distribution: use platform-specific managed device guides (macOS/iOS, Windows)

## Gotchas
- Clients older than 12 months **cannot connect** — enforce update policy to prevent service interruption
- Linux does **not** use Twingate-hosted binaries; uses public package repositories
- ChromeOS uses the Android client via Google Play

## Related Docs
- Endpoint Requirements
- Managed Devices documentation
- Linux client / source repositories
- Client changelog
- macOS/iOS managed deployment
- Windows managed deployment
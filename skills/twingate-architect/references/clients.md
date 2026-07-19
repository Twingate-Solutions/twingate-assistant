# Twingate Client Application

## Summary
The Twingate Client provides users access to private network resources across macOS, Windows, Linux, iOS, and Android/ChromeOS. It creates a local VPN connection to `127.0.0.1` to intercept traffic to private resources. Clients older than 12 months cannot connect to the Twingate service.

## Key Information
- Users enter only the subdomain (e.g., `autoco`) on first setup — not the full URL
- No special permissions required, but a local VPN to `127.0.0.1` is established
- Unsupported (old) clients are blocked from connecting entirely
- Updates are auto-hosted by Twingate for macOS/Windows; Linux uses public repositories; iOS/Android via app stores

## Prerequisites
- Twingate account with known subdomain
- For managed deployments: refer to managed devices documentation
- For auto-updates: local users need elevated permissions

## Download Endpoints

| Platform | URL |
|----------|-----|
| macOS (PKG) | `https://api.twingate.com/download/darwin?installer=pkg` |
| Windows (EXE) | `https://api.twingate.com/download/windows` |
| Windows (MSI) | `https://api.twingate.com/download/windows?installer=msi` |
| iOS | `https://api.twingate.com/download/ios` |
| Android/ChromeOS | `https://api.twingate.com/download/android` |
| Linux | Convenience script + source repos (see Linux docs) |
| Any platform (auto-detect) | `get.twingate.com` |

## Minimum Supported Versions
Clients older than these versions cannot connect:
- **macOS**: 2024.57
- **Windows**: 2024.51
- **Linux**: 2024.63
- **iOS**: 2024.57
- **Android**: 2024.85

## Gotchas
- Clients older than 12 months are hard-blocked — plan forced update policies before this threshold is hit
- Linux updates are **not** hosted by Twingate directly; they come from public repositories requiring separate repo configuration
- Historical versions available via public changelog (macOS PKG, Windows MSI only)
- Auto-updates only work when local users have elevated permissions; otherwise use software distribution tools

## Related Docs
- Endpoint Requirements (local VPN behavior details)
- Managed Devices documentation (MDM/enterprise deployment)
- Linux client documentation (source repositories)
- Client changelog (version history)
- macOS & iOS deployment guide
- Windows deployment guide
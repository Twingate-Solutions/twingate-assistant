# Twingate Client Applications

## Summary
The Twingate Client enables user access to private network resources across macOS, Windows, Linux, iOS, and Android/ChromeOS. It establishes a local VPN to `127.0.0.1` to intercept traffic to private resources. Clients older than 12 months cannot connect to the Twingate service.

## Key Information
- No special permissions required for installation
- Local VPN set up to `127.0.0.1` for traffic interception
- Users enter organization subdomain (e.g., `autoco`) on first launch only
- Clients >12 months old are blocked from connecting

## Download URLs by Platform

| Platform | URL |
|----------|-----|
| macOS (PKG) | `https://api.twingate.com/download/darwin?installer=pkg` |
| Windows (EXE) | `https://api.twingate.com/download/windows` |
| Windows (MSI) | `https://api.twingate.com/download/windows?installer=msi` |
| Linux | Convenience script via public repos |
| iOS | `https://api.twingate.com/download/ios` |
| Android/ChromeOS | `https://api.twingate.com/download/android` |
| Auto-detect | `get.twingate.com` |

## Minimum Supported Versions (as of last update)
- **macOS:** 2024.57
- **Windows:** 2024.51
- **Linux:** 2024.63
- **iOS:** 2024.57
- **Android:** 2024.85

## Installation Methods
1. **Self-managed:** Direct users to `get.twingate.com` (auto-detects platform)
2. **Managed devices:** Use platform-specific MDM/deployment docs
3. **Linux:** Use published convenience script for any supported distro

## Gotchas
- Clients older than 12 months will fail to connect — enforce update policy
- Linux updates come from public repositories, not hosted by Twingate directly
- Historical versions available via public changelog (useful for pinning versions in managed deployments)
- Automatic updates only work when local users have elevated permissions

## Related Docs
- Endpoint Requirements
- Managed Devices deployment guide
- Linux client source repositories
- Client changelog (version history)
- macOS/iOS deployment guide
- Windows deployment guide
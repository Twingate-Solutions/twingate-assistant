# Twingate Client Application

## Summary
The Twingate Client enables user access to private network resources across macOS, Windows, Linux, iOS, and Android/ChromeOS. It creates a local VPN connection to `127.0.0.1` to intercept traffic to private resources. Clients older than 12 months cannot connect to the Twingate service.

## Key Information
- Users enter only the subdomain (e.g., `autoco` for `autoco.twingate.com`) on first setup
- No special permissions required, but a local VPN to `127.0.0.1` is established
- End users can self-install via `get.twingate.com`
- Managed device deployment requires platform-specific documentation

## Download URLs by Platform

| Platform | URL |
|----------|-----|
| macOS (PKG) | `https://api.twingate.com/download/darwin?installer=pkg` |
| Windows (EXE) | `https://api.twingate.com/download/windows` |
| Windows (MSI) | `https://api.twingate.com/download/windows?installer=msi` |
| Linux | Convenience script + public repos |
| iOS | `https://api.twingate.com/download/ios` |
| Android/ChromeOS | `https://api.twingate.com/download/android` |

## Minimum Supported Versions (older versions cannot connect)

| Platform | Minimum Version |
|----------|----------------|
| macOS | 2024.57 |
| Windows | 2024.51 |
| Linux | 2024.63 |
| iOS | 2024.57 |
| Android | 2024.85 |

## Prerequisites
- Valid Twingate account with a configured subdomain
- User rights to install software (or MDM/managed device setup for enterprise)

## Gotchas
- **12-month version cutoff**: Clients older than 12 months are hard-blocked from connecting — enforce update policies
- Linux updates come from public repositories, not Twingate-hosted servers (unlike other platforms)
- macOS and Android/iOS updates are distributed via App Store/Play Store, limiting direct distribution control
- Historical versions available only via the public changelog — direct old-version URLs not provided

## Update Recommendations
- Automate updates wherever possible
- When local users have elevated permissions, client can auto-check and install updates
- For managed/enterprise environments, use platform-specific deployment guides (macOS/iOS, Windows)

## Related Docs
- Endpoint Requirements (local VPN/network details)
- Managed Devices documentation
- Linux client source repositories
- Client public changelog
- macOS/iOS deployment guide
- Windows deployment guide
---
source: https://www.twingate.com/docs/clients
type: docs
fetched: 2026-10-25
source_version: e762a0e34be3eead33546f0380dccd9f93cfd9733fd8722fc62ccec00a541c1d
trust: official
---

# Twingate Client Application

## Summary
The Twingate Client enables users to access private network resources and threat protection across macOS, Windows, Linux, iOS, and Android/ChromeOS. Installation requires only an organization subdomain (e.g., `autoco` for `autoco.twingate.com`). The client creates a local VPN connection to `127.0.0.1` to intercept traffic to private resources.

## Key Information
- No special OS permissions required, but a local VPN connection to `127.0.0.1` is established
- Clients older than 12 months are unsupported and cannot connect to the service
- Mac App Store version is deprecated; use PKG installer instead
- Auto-updates available when local users have elevated permissions

## Download URLs

| Platform | URL |
|----------|-----|
| macOS (PKG) | `https://api.twingate.com/download/darwin?installer=pkg` |
| Windows (EXE) | `https://api.twingate.com/download/windows` |
| Windows (MSI) | `https://api.twingate.com/download/windows?installer=msi` |
| iOS | `https://api.twingate.com/download/ios` |
| Android/ChromeOS | `https://api.twingate.com/download/android` |
| End-user self-install | `https://get.twingate.com` (auto-detects platform) |

- Linux: Published to public repositories; see Linux client docs for repo sources. A convenience script is available — refer to the [Linux client documentation](https://www.twingate.com/docs/linux) rather than running an unverified pipe-to-shell command.

## Prerequisites
- Organization subdomain (entered once on first launch)
- For managed deployments: refer to managed devices documentation
- Elevated local permissions required for automatic client updates

## Configuration Values
- **Organization name field**: subdomain only (e.g., `autoco`, not `autoco.twingate.com`)
- **Local VPN binding**: `127.0.0.1`

## Update Management
- Historical versions (macOS PKG, Windows MSI): available via [public changelog](https://www.twingate.com/docs/client-changelog)
- iOS/Android: distributed via App Store / Google Play Store (no manual URL needed)
- Managed deployment guides exist for macOS/iOS and Windows

## Gotchas
- macOS App Store version is **no longer supported** — must migrate to PKG installer
- Clients >12 months old will be **blocked from connecting** entirely
- Linux updates come from public repos, not Twingate-hosted binaries

## Related Docs
- [Endpoint Requirements](https://www.twingate.com/docs/endpoint-requirements)
- [Managed Devices](https://www.twingate.com/docs/managed-devices)
- [Linux Client / Source Repositories](https://www.twingate.com/docs/linux)
- [Client Changelog](https://www.twingate.com/docs/client-changelog)
- [macOS Managed Deployment](https://www.twingate.com/docs/macos)
- [Windows Managed Deployment](https://www.twingate.com/docs/windows)
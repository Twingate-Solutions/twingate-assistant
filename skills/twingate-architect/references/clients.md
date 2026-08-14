---
source: https://www.twingate.com/docs/clients
type: docs
fetched: 2026-08-14
source_version: 63a890a4c62dafc9c14debc36812343cb02758682ca99d81529143aa76fdf7a2
---

# Twingate Client Application

## Summary
The Twingate Client enables users to access private network resources and is available across major platforms. Users authenticate via their organization's subdomain, and the client creates a local VPN connection to intercept resource traffic. Clients older than 12 months lose connectivity to the Twingate service.

## Key Information
- **Supported platforms:** macOS, Windows, Linux, iOS, Android, ChromeOS
- **Setup:** Users enter organization subdomain (e.g., `autoco` for `autoco.twingate.com`) — one-time configuration
- **Local VPN:** Client binds to `127.0.0.1` to intercept private resource traffic; no special permissions required
- **End-user install URL:** `get.twingate.com` (auto-detects platform)

## Download Endpoints

| Platform | URL |
|----------|-----|
| macOS (PKG) | `https://api.twingate.com/download/darwin?installer=pkg` |
| Windows (EXE) | `https://api.twingate.com/download/windows` |
| Windows (MSI) | `https://api.twingate.com/download/windows?installer=msi` |
| Linux | Convenience script + public repos |
| iOS | `https://api.twingate.com/download/ios` |
| Android/ChromeOS | `https://api.twingate.com/download/android` |

## Minimum Supported Versions (12-month limit)
Clients below these versions **cannot connect**:
- macOS: `2024.57`
- Windows: `2024.51`
- Linux: `2024.63`
- iOS: `2024.57`
- Android: `2024.85`

## Prerequisites
- Organization subdomain on `twingate.com`
- For managed deployments: software distribution tooling (see managed devices docs)

## Gotchas
- Clients older than 12 months are hard-blocked from connecting — enforce update policies proactively
- Historical versions (macOS PKG, Windows MSI) available via public changelog only — direct links always serve latest
- Linux updates come from public repos, not Twingate-hosted binaries; use convenience script or configure source repos directly

## Related Docs
- Endpoint Requirements (local VPN/network details)
- Managed Devices documentation (MDM/enterprise deployment)
- Linux client source repositories
- Client public changelog (historical versions + release notes)
- macOS & iOS deployment guide
- Windows deployment guide
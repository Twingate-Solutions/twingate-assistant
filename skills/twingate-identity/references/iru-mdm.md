---
source: https://www.twingate.com/docs/iru-mdm
type: docs
fetched: 2026-08-14
source_version: 7b62c9e2074ed1e968571543277bc8ac1178f65ddd527ccf158616c25695f60e
---

# Deploying Twingate Clients with Iru (MDM)

## Summary
Guide for deploying Twingate macOS and iOS clients via Iru (formerly Kandji) MDM. macOS deployment is best handled via the Twingate Auto App; iOS requires Apple Business Manager integration.

## Key Information
- **macOS**: Use Twingate Auto App (recommended) — automatically handles notifications, VPN profile, and system extension
- **macOS alternative**: Deploy as custom app using PKG installer (not recommended)
- **iOS**: Requires Apple Business Manager linked to Iru before distribution is possible
- Auto App requires no custom configuration for macOS

## Prerequisites
- Iru (Kandji) account with Library access
- **iOS only**: Devices enrolled in Apple Business Manager; Iru linked to Apple Business Manager
- **macOS custom app**: PKG downloaded from [Twingate download page](https://www.twingate.com/docs/download)

## Step-by-Step

### macOS (Auto App)
1. Sign in to Iru
2. Select **Library** in sidebar
3. Find Twingate Client app for macOS
4. Select and deploy via Auto App

### iOS
1. Add Twingate iOS Client to Apple Business Manager
2. Add devices to Apple Business Manager (follow Iru's official docs)
3. Link Iru with Apple Business Manager
4. Sign in to Iru → **Library** → find Twingate iOS app → distribute

## Configuration Values
- Pre-configuration for macOS via [configuration profiles](https://www.twingate.com/docs/configuration-profiles) — supports:
  - Auto-enable VPN configuration
  - Auto-enable system extension
  - Pre-populate Network name

## Gotchas
- **Manually installed clients must be removed first** — version conflicts can occur if users have pre-existing installations
  - Create a temporary removal policy targeting all devices
  - Deactivate the removal policy before rolling out the MDM-distributed client
- macOS custom app (PKG) deployment does **not** auto-configure VPN profile, notifications, or system extension — requires manual configuration profile setup
- iOS distribution is blocked until Apple Business Manager is fully linked to Iru

## Related Docs
- [Twingate Configuration Profiles](https://www.twingate.com/docs/configuration-profiles)
- [Twingate Download Page](https://www.twingate.com/docs/download)
- Iru official documentation (Apple Business Manager enrollment)
---
source: https://www.twingate.com/docs/kandji-mdm
type: docs
fetched: 2026-08-14
source_version: 7b62c9e2074ed1e968571543277bc8ac1178f65ddd527ccf158616c25695f60e
---

# Deploying Twingate Clients with Iru (Kandji) MDM

## Summary
Guide for deploying Twingate macOS and iOS clients via Iru (formerly Kandji) MDM. macOS deployment uses the Twingate Auto App (recommended) or a custom PKG upload. iOS deployment requires Apple Business Manager integration.

## Key Information
- **macOS recommended method**: Twingate Auto App in Iru library (auto-configures notifications, VPN profile, system extension)
- **macOS alternative**: Custom app via PKG upload from Twingate download page
- **iOS requirement**: Must link Iru with Apple Business Manager before distributing iOS client
- Iru was previously named Kandji

## Prerequisites
- Active Iru (Kandji) account
- **iOS only**: Apple Business Manager account with devices enrolled; Iru linked to Apple Business Manager

## Step-by-Step

### macOS (Auto App - Recommended)
1. Sign in to Iru
2. Select **Library** in sidebar
3. Find Twingate Client app for macOS
4. Select and deploy via Auto App

### macOS (Custom PKG - Alternative)
1. Download PKG installer from Twingate download page
2. Upload PKG as custom app in Iru
3. Deploy to devices

### iOS
1. Add Twingate iOS app to Apple Business Manager
2. Enroll devices in Apple Business Manager (follow Iru's official docs)
3. Link Iru with Apple Business Manager
4. Sign in to Iru → **Library** → find Twingate iOS Client → distribute

## Configuration Values
- No specific env vars or CLI flags
- Pre-configuration via **configuration profiles** guide (separate doc) enables:
  - VPN configuration auto-enable
  - System extension auto-enable
  - Pre-populated Network name

## Gotchas
- **Manually installed clients conflict**: Users with existing manual Twingate installs may experience version conflicts after MDM rollout
  - Fix: Create a temporary removal policy targeting all devices; deactivate policy before rolling out MDM-managed version
- Auto App handles VPN profile and system extension automatically — custom PKG does **not** do this automatically
- iOS distribution is blocked until Apple Business Manager linkage is confirmed

## Related Docs
- Twingate configuration profiles guide (macOS pre-configuration)
- Twingate download page (PKG installer)
- Iru official documentation (Apple Business Manager enrollment)
- Apple Business Manager setup
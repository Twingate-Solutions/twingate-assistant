---
source: https://www.twingate.com/docs/kandji-mdm
type: docs
fetched: 2026-10-25
source_version: 42a22310deadab059031ef56ae77ab2a60a5f6fe21318b6714175d11c418c179
trust: official
---

# Deploying Twingate macOS and iOS Clients with Iru (Kandji) MDM

## Summary
Guide for distributing the Twingate Client to macOS and iOS devices using Iru (formerly Kandji) MDM. The recommended macOS method uses the Twingate Auto App, which automates VPN profile, system extension, and notification configuration. iOS distribution requires Apple Business Manager integration.

## Key Information
- **macOS Mac App Store version is deprecated** — use standalone PKG or Auto App only
- Auto App is preferred over custom app deployment for macOS
- iOS requires Apple Business Manager linkage with Iru before distribution is possible
- Pre-existing manually installed clients must be removed before MDM rollout

## Prerequisites
- Iru (Kandji) MDM account with Library access
- **macOS:** Twingate standalone PKG (download from Twingate download page) if using custom app method
- **iOS:** Devices enrolled in Apple Business Manager; Iru linked to Apple Business Manager

## Step-by-Step

### macOS (Recommended: Auto App)
1. Sign in to Iru
2. Select **Library** in the sidebar
3. Search for and select the Twingate Client app for macOS
4. Add as Auto App — automatically handles VPN profile, system extension, and notifications

### macOS (Alternative: Custom App)
1. Download Twingate PKG from the Twingate download page
2. Upload PKG to Iru as a custom app

### iOS
1. Add Twingate iOS app to Apple Business Manager
2. Enroll devices in Apple Business Manager (follow Iru's official documentation)
3. Link Iru to Apple Business Manager
4. Distribute Twingate iOS app from Iru Library

## Configuration Values
- Pre-configuration of macOS Client (VPN profile, system extension, network pre-population) is handled via **configuration profiles** — see the Twingate configuration profiles guide

## Gotchas
- **Remove manually installed clients first.** Users with pre-existing Twingate installs may experience version conflicts. Temporarily create a removal policy targeting all devices, then deactivate it before rolling out via Iru.
- Auto App is the only method that automatically enables VPN profile and system extension without extra configuration profiles.
- Custom app deployment requires manual configuration profile setup to enable VPN and system extension.

## Related Docs
- Twingate download page (macOS PKG)
- Twingate configuration profiles guide (macOS pre-configuration)
- Apple Business Manager setup
- Iru official documentation (device enrollment)
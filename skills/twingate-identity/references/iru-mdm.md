---
source: https://www.twingate.com/docs/iru-mdm
type: docs
fetched: 2026-10-25
source_version: 42a22310deadab059031ef56ae77ab2a60a5f6fe21318b6714175d11c418c179
trust: official
---

# Deploying Twingate Clients with Iru (formerly Kandji)

## Summary
Guide for distributing Twingate macOS and iOS clients via Iru MDM. macOS deployment is best handled via the Twingate Auto App in Iru's Library. iOS deployment requires Apple Business Manager integration.

## Key Information
- Mac App Store version of Twingate macOS Client is **no longer supported**; use standalone PKG
- Twingate Auto App (recommended) automatically handles: notifications, VPN profile, and system extension
- Custom app deployment (not recommended) requires uploading a PKG manually
- iOS distribution requires Apple Business Manager linkage with Iru

## Prerequisites
- Iru MDM account with admin access
- **macOS**: Twingate PKG from [Twingate download page](https://www.twingate.com/download) (if using custom app path)
- **iOS**: Devices enrolled in Apple Business Manager; Iru linked to Apple Business Manager

## Step-by-Step

### macOS (Auto App — Recommended)
1. Sign in to Iru
2. Select **Library** in the sidebar
3. Find **Twingate Client** (macOS) and select it
4. Deploy via Auto App — no custom configuration required

### macOS (Custom App — Not Recommended)
1. Download standalone PKG from Twingate download page
2. Upload PKG to Iru as a custom app
3. Configure and deploy

### iOS
1. Add Twingate iOS app to Apple Business Manager
2. Enroll devices in Apple Business Manager per Iru's documentation
3. Link Iru to Apple Business Manager
4. Sign in to Iru → **Library** → find Twingate iOS Client → distribute

## Configuration Values
- Pre-configuration of macOS Client (VPN profile, system extension, Network name) is done via **configuration profiles** — see the [configuration profiles guide](https://www.twingate.com/docs/configuration-profiles)

## Gotchas
- **Manually installed clients must be removed first**: Users with pre-existing manual installs may experience version conflicts
  - Create a temporary removal policy targeting all devices
  - Deactivate the removal policy before rolling out the MDM-distributed version
- Auto App handles VPN profile and system extension automatically; custom app deployments must configure these separately via configuration profiles

## Related Docs
- [Twingate download page](https://www.twingate.com/download)
- [Configuration profiles guide](https://www.twingate.com/docs/configuration-profiles)
- [Iru official documentation](https://support.kandji.io) (for Apple Business Manager enrollment steps)
# Deploying Twingate Clients with Iru (Kandji) MDM

## Summary
Guide for deploying Twingate macOS and iOS clients via Iru (formerly Kandji) MDM. macOS deployment uses the Twingate Auto App (recommended) or a custom PKG upload. iOS deployment requires Apple Business Manager integration.

## Key Information
- **Iru** is the current name for what was previously called Kandji
- macOS Auto App automatically handles: notifications, VPN profile, and system extension — no custom config needed
- iOS distribution requires Apple Business Manager to be linked to Iru first
- Custom PKG option available for macOS (not recommended over Auto App)

## Prerequisites
- Iru MDM account with Library access
- **iOS only**: Devices enrolled in Apple Business Manager; Iru linked to Apple Business Manager
- **macOS custom app only**: Twingate PKG downloaded from [Twingate download page](https://www.twingate.com/downloads)

## Step-by-Step

### macOS (Recommended — Auto App)
1. Sign in to Iru
2. Select **Library** in sidebar
3. Find Twingate Client app for macOS
4. Select it — Auto App handles VPN profile, notifications, and system extension automatically

### macOS (Custom App — Not Recommended)
1. Download Twingate PKG from the download page
2. Upload PKG to Iru as a custom app

### iOS
1. Add Twingate iOS Client to Apple Business Manager
2. Enroll devices in Apple Business Manager (follow Iru official docs)
3. Link Iru to Apple Business Manager
4. Distribute Twingate iOS app from Iru Library

## Configuration Values
- No CLI flags or env vars specific to Iru deployment
- Pre-configuration (VPN config, system extension, Network pre-population) done via [configuration profiles guide](https://www.twingate.com/docs/configuration-profiles)

## Gotchas
- **Manually installed clients must be removed first** — version conflicts can occur if users have self-installed Twingate before MDM rollout
  - Create a temporary removal policy targeting all devices
  - Deactivate the removal policy before rolling out the MDM-distributed version
- iOS deployment **will not work** without Apple Business Manager linked to Iru
- Custom PKG approach does **not** automatically configure VPN profile or system extension (requires manual configuration profiles)

## Related Docs
- [Twingate Configuration Profiles](https://www.twingate.com/docs/configuration-profiles) — pre-configure VPN, system extension, Network name
- [Iru official documentation](https://support.kandji.io) — Apple Business Manager device enrollment
- [Twingate Download Page](https://www.twingate.com/downloads) — PKG installer for custom app deployment
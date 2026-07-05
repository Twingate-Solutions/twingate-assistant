# Deploying Twingate Clients with Iru (Kandji) MDM

## Summary
Guide for distributing the Twingate macOS and iOS clients via Iru (formerly Kandji) MDM. macOS deployment is recommended via the Twingate Auto App; iOS requires Apple Business Manager integration.

## Key Information
- **Iru** is the current name for what was previously called Kandji
- macOS Auto App automatically handles: notifications permissions, VPN profile enablement, system extension approval
- iOS distribution requires Apple Business Manager (ABM) linkage with Iru
- Custom PKG deployment is supported but not recommended for macOS

## Prerequisites
- Access to Iru admin console
- **iOS only**: Devices enrolled in Apple Business Manager; Iru linked to ABM

## Step-by-Step

### macOS (Recommended: Auto App)
1. Sign in to Iru
2. Select **Library** in the sidebar
3. Find and select the Twingate Client app for macOS
4. Deploy via Auto App (no additional configuration required)

### macOS (Alternative: Custom PKG)
1. Download Twingate PKG from the [Twingate download page](https://www.twingate.com/download)
2. Upload PKG to Iru as a custom app

### iOS
1. Add Twingate iOS app to Apple Business Manager
2. Enroll devices in ABM (follow Iru's official documentation)
3. Link Iru with Apple Business Manager
4. Locate Twingate in Iru Library and distribute

## Configuration Values
- Pre-configuration of macOS client available via **configuration profiles** (separate guide)
  - Enables VPN configuration automatically
  - Enables system extension
  - Pre-populates Network for users

## Gotchas
- **Manually installed clients must be removed first** before rolling out MDM distribution — version mismatches cause issues for end users
  - Create a temporary removal policy targeting all devices
  - Deactivate the removal policy before deploying via Iru
- Auto App is strongly preferred over custom PKG; custom PKG requires manual handling of VPN profile, system extension, and notifications

## Related Docs
- [Twingate Configuration Profiles guide](https://www.twingate.com/docs/configuration-profiles) — for pre-configuring macOS client
- [Twingate Download Page](https://www.twingate.com/download) — PKG installer for custom app deployment
- Iru official documentation — for Apple Business Manager enrollment steps
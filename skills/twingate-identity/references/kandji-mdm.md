# Deploying Twingate Client with Iru (Kandji) MDM

## Summary
Covers deploying Twingate macOS and iOS clients via Iru (formerly Kandji) MDM. macOS deployment uses the Twingate Auto App (recommended) or a custom PKG upload. iOS deployment requires Apple Business Manager integration.

## Key Information
- **Iru** is the current name for what was previously called Kandji
- macOS Auto App automatically handles: notifications, VPN profile, and system extension — no custom config needed
- iOS requires Apple Business Manager linkage before distribution is possible
- Pre-configuration (VPN profile, system extension, network pre-population) is available via configuration profiles guide

## Prerequisites
- Access to Iru admin console
- **iOS only**: Devices enrolled in Apple Business Manager; Iru linked to Apple Business Manager
- **macOS custom app only**: Twingate PKG downloaded from Twingate download page

## Step-by-Step

### macOS (Recommended — Auto App)
1. Sign in to Iru
2. Select **Library** in the sidebar
3. Find the Twingate Client app for macOS
4. Select and deploy via Auto App

### macOS (Alternative — Custom App)
1. Download Twingate PKG from the Twingate download page
2. Upload PKG to Iru as a custom app
3. Deploy to target devices

### iOS
1. Add Twingate iOS app to Apple Business Manager
2. Enroll devices in Apple Business Manager (follow Iru's official docs)
3. Link Iru with Apple Business Manager
4. Sign in to Iru → **Library** → find Twingate iOS app → distribute

## Configuration Values
- No environment variables or CLI flags specific to Iru deployment
- macOS pre-configuration available via **configuration profiles** (separate guide) supporting:
  - VPN configuration auto-enable
  - System extension enable
  - Network pre-population

## Gotchas
- **Manually installed clients must be removed first** — version conflicts will occur if end users have a pre-existing Twingate install that differs from the MDM-distributed version
  - Workaround: Create a temporary removal policy targeting all devices, then deactivate it before rolling out the MDM-distributed version
- Custom PKG deployment is not recommended; Auto App is preferred for macOS
- iOS distribution is blocked until Apple Business Manager is fully configured and linked to Iru

## Related Docs
- Twingate configuration profiles guide (macOS pre-configuration)
- Twingate client download page (PKG installer)
- Iru official documentation (Apple Business Manager device enrollment)
- Apple Business Manager setup
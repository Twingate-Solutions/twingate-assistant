# Deploying Twingate Client with Iru (Kandji) MDM

## Summary
Covers distributing the Twingate macOS and iOS clients via Iru (formerly Kandji) MDM. macOS deployment is best handled via the Twingate Auto App; iOS requires Apple Business Manager integration.

## Key Information
- **Iru** is the current name for what was previously Kandji MDM
- macOS Auto App automatically handles: notifications, VPN profile, and system extension — no custom config needed
- iOS distribution requires Apple Business Manager to be linked to Iru first
- PKG installer available from Twingate download page for custom app deployments

## Prerequisites
- Access to Iru admin console
- **iOS only**: Devices enrolled in Apple Business Manager; Iru linked to Apple Business Manager
- **macOS custom app only**: Twingate PKG installer downloaded

## Step-by-Step

### macOS (Recommended — Auto App)
1. Sign in to Iru
2. Select **Library** in the sidebar
3. Find Twingate Client app for macOS and select it
4. Deploy via Auto App (no additional configuration required)

### macOS (Alternative — Custom App)
1. Download Twingate PKG from the download page
2. Upload PKG to Iru as a custom app

### iOS
1. Add Twingate iOS app to Apple Business Manager
2. Enroll devices in Apple Business Manager (follow Iru's official docs)
3. Link Iru with Apple Business Manager
4. Sign in to Iru → **Library** → find Twingate iOS Client → distribute

## Configuration Values
- Pre-configuration of macOS client (VPN config, system extension, network pre-population) done via **configuration profiles** — see separate configuration profiles guide

## Gotchas
- **Manually installed clients must be removed before MDM rollout** — version mismatches cause issues
  - Create a temporary removal policy targeting all devices
  - Deactivate the removal policy before rolling out via Iru
- Custom app deployment (PKG) is not recommended; use Auto App when possible
- Auto App handles VPN profile and system extension automatically — custom app deployments require manual configuration profile setup

## Related Docs
- Twingate macOS configuration profiles guide
- Twingate client download page
- Iru official documentation (Apple Business Manager enrollment)
- Apple Business Manager setup
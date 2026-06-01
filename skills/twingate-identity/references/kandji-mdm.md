# Deploying Twingate Client with Iru (Kandji) MDM

## Summary
Guide for distributing the Twingate macOS and iOS clients via Iru (formerly Kandji) MDM. macOS deployment is best handled via the Twingate Auto App; iOS requires Apple Business Manager integration.

## Key Information
- **Iru** is the current name for the MDM platform previously known as Kandji
- macOS Auto App automatically handles: notifications permission, VPN profile, system extension
- iOS distribution requires Apple Business Manager linkage with Iru
- Custom PKG deployment is supported but not recommended for macOS

## Prerequisites
- Access to Iru admin console
- **iOS only**: Devices enrolled in Apple Business Manager; Iru linked to Apple Business Manager

## Step-by-Step

### macOS (Recommended - Auto App)
1. Sign in to Iru
2. Select **Library** in the sidebar
3. Find the Twingate Client app for macOS and select it
4. Deploy via Auto App (no custom configuration needed)

### macOS (Alternative - Custom PKG)
1. Download Twingate PKG from the [Twingate download page](https://www.twingate.com/download)
2. Upload PKG to Iru as a custom app

### iOS
1. Add Twingate iOS Client to Apple Business Manager
2. Enroll devices in Apple Business Manager (follow Iru's official documentation)
3. Link Iru with Apple Business Manager
4. Sign in to Iru → **Library** → find Twingate iOS app → distribute

## Configuration Values
- Pre-configuration of macOS client available via **configuration profiles** (separate guide)
  - Can pre-populate: Network name, VPN configuration, system extension approval

## Gotchas
- **Manually installed clients conflict**: Users who self-installed Twingate before MDM rollout may experience version mismatch issues
  - Fix: Create a temporary removal policy to uninstall existing Twingate clients from all devices before deploying via Iru; deactivate the removal policy before rollout
- Custom PKG deployment requires manual VPN profile/system extension configuration (Auto App handles this automatically)

## Related Docs
- [Twingate Configuration Profiles guide](https://www.twingate.com/docs/configuration-profiles) — for pre-configuring macOS client
- [Twingate Download Page](https://www.twingate.com/download) — PKG installer source
- Apple Business Manager enrollment (Iru official documentation)
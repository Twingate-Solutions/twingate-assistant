# Deploying Twingate Client with Iru (Kandji) MDM

## Summary
Guide for deploying Twingate macOS and iOS clients via Iru (formerly Kandji) MDM. macOS deployment uses the Twingate Auto App (recommended) or a custom PKG upload. iOS deployment requires Apple Business Manager integration.

## Key Information
- **Iru** is the current name for what was previously called Kandji
- macOS Auto App automatically handles: notifications, VPN profile, and system extension — no custom configuration needed
- iOS requires Apple Business Manager linkage before distribution is possible
- App is found under **Library** in the Iru sidebar

## Prerequisites
- Active Iru (Kandji) account
- For iOS: Iru linked to Apple Business Manager; devices enrolled in Apple Business Manager
- For custom macOS PKG: Twingate PKG downloaded from the [Twingate download page](https://www.twingate.com/download)

## Step-by-Step

### macOS (Auto App — Recommended)
1. Sign in to Iru
2. Select **Library** in the sidebar
3. Find and select the Twingate Client app for macOS
4. Deploy via Auto App (no additional configuration required)

### macOS (Custom App — Not Recommended)
1. Download Twingate PKG from the download page
2. Upload PKG to Iru as a custom app

### iOS
1. Add Twingate iOS Client to Apple Business Manager
2. Enroll devices in Apple Business Manager (follow Iru's official docs)
3. Link Iru with Apple Business Manager
4. Distribute Twingate iOS app from Iru Library

## Configuration Values
- Pre-configuration of macOS client (VPN config, system extension, Network pre-population) done via **configuration profiles** — see separate configuration profiles guide

## Gotchas
- **Remove manually installed clients first**: Users with pre-existing manual installs may encounter version conflicts with MDM-distributed versions
  - Fix: Create a temporary removal policy targeting all devices; deactivate once MDM rollout begins
- Custom PKG deployment does **not** automatically configure VPN profile or system extension — requires manual configuration
- iOS distribution is blocked until Apple Business Manager integration is complete

## Related Docs
- [Twingate Configuration Profiles guide](https://www.twingate.com/docs/configuration-profiles) — for pre-configuring macOS client
- [Twingate Download Page](https://www.twingate.com/download) — for PKG installer
- Iru official documentation — for Apple Business Manager device enrollment steps
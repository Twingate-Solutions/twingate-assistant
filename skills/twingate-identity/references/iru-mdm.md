# Deploying Twingate macOS and iOS Clients with Iru (Kandji)

## Summary
Guide for distributing the Twingate Client via Iru (formerly Kandji) MDM on macOS and iOS. The recommended macOS approach uses the Twingate Auto App, which handles notifications, VPN profile, and system extension automatically. iOS distribution requires Apple Business Manager integration.

## Key Information
- **macOS recommended method**: Twingate Auto App (handles all permissions automatically)
- **macOS alternative**: Custom app via PKG upload (not recommended)
- **iOS requirement**: Must add Twingate to Apple Business Manager first
- PKG installer available at Twingate's download page

## Prerequisites
- Iru (Kandji) MDM account
- **iOS only**: Apple Business Manager account with devices enrolled; Iru linked to Apple Business Manager
- **macOS custom app only**: Twingate PKG installer downloaded

## Step-by-Step

### macOS (Auto App - Recommended)
1. Sign in to Iru
2. Select **Library** in the sidebar
3. Find Twingate Client app for macOS and select it
4. Deploy via Auto App (no additional configuration required)

### iOS
1. Add Twingate iOS Client to Apple Business Manager
2. Add devices to Apple Business Manager (follow Iru's official docs)
3. Link Iru with Apple Business Manager
4. Sign in to Iru → **Library** → find Twingate iOS app → distribute

### macOS (Custom App - Alternative)
1. Download PKG from Twingate download page
2. Upload PKG to Iru as a custom app

## Configuration Values
- Pre-configuration via **configuration profiles** guide (separate doc) enables:
  - VPN configuration auto-enable
  - System extension auto-enable
  - Pre-populate Network name for users

## Gotchas
- **Manually installed clients must be removed first** — version conflicts will occur if MDM-distributed version differs from manually installed version
  - Create a temporary removal policy targeting all devices before rollout
  - Deactivate removal policy before deploying via Iru
- Custom app distribution does **not** automatically configure VPN profile, notifications, or system extension (requires manual configuration profile setup)
- Auto App is preferred precisely because it handles VPN profile and system extension without extra steps

## Related Docs
- Twingate Configuration Profiles guide (for pre-configuring macOS Client)
- Iru official documentation (for Apple Business Manager device enrollment)
- Twingate download page (for PKG installer)
- Apple Business Manager setup documentation
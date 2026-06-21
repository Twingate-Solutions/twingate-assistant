# Deploying Twingate Client with Iru (MDM)

## Summary
Guide for deploying Twingate macOS and iOS clients via Iru (formerly Kandji) MDM. macOS deployment uses the Twingate Auto App (recommended) or a custom PKG upload. iOS deployment requires Apple Business Manager integration.

## Key Information
- **macOS Auto App** automatically handles: notifications permissions, VPN profile enablement, system extension approval
- **iOS** requires Apple Business Manager linked to Iru before distribution is possible
- Custom PKG for macOS available at Twingate's download page (not recommended vs Auto App)

## Prerequisites
- Iru (Kandji) MDM account
- **iOS only**: Apple Business Manager account with devices enrolled; Iru linked to Apple Business Manager
- Iru's official docs required for ABM device enrollment steps

## Step-by-Step

### macOS (Auto App - Recommended)
1. Sign in to Iru
2. Select **Library** in sidebar
3. Find Twingate Client app for macOS
4. Select and deploy via Auto App

### macOS (Custom App - Not Recommended)
1. Download PKG from Twingate download page
2. Upload PKG to Iru as a custom app

### iOS
1. Add Twingate iOS Client to Apple Business Manager
2. Link Iru with Apple Business Manager
3. Sign in to Iru → **Library** → find Twingate iOS app
4. Distribute to devices

## Configuration Values
- Pre-configuration via **configuration profiles** guide (separate doc) enables:
  - VPN configuration (auto-enable)
  - System extension (auto-approve)
  - Network pre-population (removes manual network entry for users)

## Gotchas
- **Manually installed clients must be removed first** — version conflicts will occur if pre-existing installs remain
  - Workaround: Create a temporary removal policy targeting all devices; deactivate once rollout begins
- Auto App is strongly preferred over custom PKG — custom app requires manual handling of VPN profile, system extension, and notifications
- iOS distribution is blocked entirely without Apple Business Manager linkage

## Related Docs
- [Twingate Configuration Profiles guide](https://www.twingate.com/docs) — for pre-configuring macOS client
- [Twingate download page](https://www.twingate.com/docs) — PKG installer for custom app deployment
- Iru official documentation — Apple Business Manager device enrollment
# Deploying Twingate Client with Iru (Kandji) MDM

## Summary
Guide for distributing the Twingate macOS and iOS clients via Iru (formerly Kandji) MDM. macOS deployment uses an Auto App for simplest setup; iOS requires Apple Business Manager integration.

## Key Information
- Iru was previously named Kandji
- macOS: Auto App is the **recommended** method (handles notifications, VPN profile, system extension automatically)
- macOS: Custom app (PKG upload) is an alternative but not recommended
- iOS: Requires Apple Business Manager linkage before distribution is possible

## Prerequisites
- Access to Iru admin console
- **iOS only**: Twingate app added to Apple Business Manager; devices enrolled in ABM; Iru linked to ABM

## Step-by-Step

### macOS (Auto App - Recommended)
1. Sign in to Iru
2. Select **Library** in the sidebar
3. Find Twingate Client app for macOS
4. Deploy via Auto App (no custom configuration required)

### macOS (Custom App - Alternative)
1. Download Twingate PKG from [Twingate download page](https://www.twingate.com/docs/downloads)
2. Upload PKG to Iru as a custom app

### iOS
1. Add Twingate iOS app to Apple Business Manager
2. Enroll devices in ABM (follow Iru's official docs)
3. Link Iru with Apple Business Manager
4. Sign in to Iru → **Library** → find Twingate iOS Client → distribute

## Configuration Values
- None required for Auto App deployment
- For advanced macOS pre-configuration (VPN config, system extension, Network pre-population): use [configuration profiles guide](https://www.twingate.com/docs/configuration-profiles)

## Gotchas
- **Pre-existing manual installs**: Users who manually installed Twingate before MDM rollout may experience version conflicts
  - Fix: Create a temporary removal policy targeting all devices before deploying via Iru; deactivate the removal policy before starting MDM rollout
- Auto App automatically handles: notification permissions, VPN profile enablement, system extension approval — no custom config needed
- Without ABM linkage, iOS distribution through Iru is not possible

## Related Docs
- [Twingate Configuration Profiles (macOS pre-configuration)](https://www.twingate.com/docs/configuration-profiles)
- [Twingate Download Page (PKG)](https://www.twingate.com/docs/downloads)
- Iru official documentation (for ABM device enrollment)
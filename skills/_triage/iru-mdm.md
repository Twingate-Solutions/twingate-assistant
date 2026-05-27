<!-- triage: unassigned URL: https://www.twingate.com/docs/iru-mdm -->

# Deploying Twingate Client with Iru (MDM)

## Summary
Guide for distributing Twingate macOS and iOS clients via Iru (formerly Kandji) MDM. macOS deployment is best handled via Auto App; iOS requires Apple Business Manager integration.

## Key Information
- Iru was previously named Kandji
- macOS supports two deployment methods: Auto App (recommended) or custom PKG
- iOS distribution requires Apple Business Manager linkage
- Auto App automatically handles notifications, VPN profile, and system extension permissions

## Prerequisites
- Iru MDM account
- **iOS only**: Devices enrolled in Apple Business Manager; Iru linked to Apple Business Manager
- **Custom PKG only**: PKG downloaded from [Twingate download page](https://www.twingate.com/download)

## Step-by-Step

### macOS (Auto App - Recommended)
1. Sign in to Iru
2. Select **Library** in sidebar
3. Find Twingate Client app for macOS
4. Deploy via Auto App (no additional configuration required)

### macOS (Custom PKG - Not Recommended)
1. Download PKG from Twingate download page
2. Upload PKG to Iru as a custom app

### iOS
1. Add Twingate iOS Client to Apple Business Manager
2. Link Iru with Apple Business Manager (follow Iru's official docs)
3. Sign in to Iru → **Library** → find Twingate iOS app
4. Distribute from Library

## Configuration Values
- Pre-configuration of macOS client available via [configuration profiles guide](https://www.twingate.com/docs/configuration-profiles)
- Configuration profiles can set: VPN configuration, system extension, pre-populate Network name

## Gotchas
- **Remove manually installed clients before rollout**: Users with pre-existing manual installs may experience version conflicts
  - Temporary fix: Create a policy to remove Twingate from all devices → deactivate policy before rolling out MDM-managed version
- Custom PKG deployment does **not** automatically configure VPN profile, notifications, or system extension (must be handled separately)
- Auto App is the only method that handles permissions automatically

## Related Docs
- [Configuration Profiles](https://www.twingate.com/docs/configuration-profiles) — pre-configure macOS client settings
- [Iru official documentation](https://support.kandji.io) — Apple Business Manager enrollment steps
- [Twingate download page](https://www.twingate.com/download) — PKG installer source
# Deploying Twingate Clients with Iru (MDM)

## Summary
Guide for deploying Twingate macOS and iOS clients via Iru (formerly Kandji) MDM. macOS deployment is best handled via the Twingate Auto App; iOS requires Apple Business Manager integration.

## Key Information
- **macOS**: Use Twingate Auto App (recommended) — automatically handles notifications, VPN profile, and system extension
- **macOS alternative**: Deploy as custom app using PKG installer from Twingate download page (not recommended)
- **iOS**: Requires Apple Business Manager; once Iru is linked to ABM, distribute from Iru Library

## Prerequisites
- Iru MDM account
- **iOS only**: Devices enrolled in Apple Business Manager; Iru linked to ABM
- **macOS custom app only**: Twingate PKG downloaded from Twingate download page

## Step-by-Step

### Locating the App in Iru
1. Sign in to Iru
2. Select **Library** in the sidebar
3. Find Twingate Client app (macOS and/or iOS)
4. Select it and configure distribution

### iOS Setup
1. Add Twingate iOS app to Apple Business Manager
2. Add devices to ABM (follow Iru's official documentation)
3. Link Iru to Apple Business Manager
4. Distribute Twingate iOS app from Iru Library

## Configuration
- Pre-configure macOS client via **configuration profiles** guide to:
  - Auto-enable VPN configuration
  - Enable system extension
  - Pre-populate the Twingate Network for users

## Gotchas
- **Manually installed clients cause conflicts**: Users who self-installed Twingate before MDM rollout may encounter version mismatch issues
  - Fix: Create a temporary removal policy targeting all devices; deactivate the policy before rolling out MDM-managed version
- Auto App is strongly preferred over custom PKG — custom PKG requires manual handling of VPN profile, system extension, and notifications

## Related Docs
- [Configuration Profiles guide](https://www.twingate.com/docs) — for pre-configuring macOS client
- Twingate Download Page — for PKG installer (custom app path)
- Iru's official ABM enrollment documentation

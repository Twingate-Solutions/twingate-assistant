# Deploying Twingate Client with Kandji MDM

## Summary
Guide for deploying Twingate macOS and iOS clients via Kandji MDM. macOS deployment uses the Twingate Auto App (recommended) or a custom PKG upload. iOS deployment requires Apple Business Manager integration.

## Key Information
- **macOS Auto App** automatically configures: notifications, VPN profile, and system extension — no custom configuration needed
- **macOS custom app** alternative: upload PKG from Twingate download page
- **iOS** requires Apple Business Manager linked to Kandji before distribution is possible
- Pre-configuration via configuration profiles can auto-enable VPN, system extension, and pre-populate Network

## Prerequisites
- Kandji account with Library access
- **iOS only**: Devices enrolled in Apple Business Manager; Kandji linked to Apple Business Manager
- **macOS custom app only**: Twingate PKG installer downloaded from Twingate download page

## Step-by-Step

### macOS (Recommended)
1. Sign in to Kandji
2. Select **Library** in sidebar
3. Find Twingate Client app for macOS
4. Select and deploy via Auto App

### iOS
1. Add Twingate Client to Apple Business Manager
2. Enroll devices in Apple Business Manager (follow Kandji's official docs)
3. Link Kandji with Apple Business Manager
4. Sign in to Kandji → **Library** → find Twingate iOS app → distribute

## Configuration Values
- Pre-configuration of macOS client: use [configuration profiles guide](https://www.twingate.com/docs/configuration-profiles)
  - Configurable: VPN profile, system extension, Network pre-population

## Gotchas
- **Manually installed clients must be removed first** — version conflicts will occur if pre-existing installations differ from the distributed version
  - Fix: create a temporary removal policy targeting all devices; deactivate it before rolling out Kandji-distributed client
- Custom app deployment (PKG) is not recommended — use Auto App when possible
- iOS distribution is blocked until Apple Business Manager is properly linked to Kandji

## Related Docs
- [Twingate Configuration Profiles](https://www.twingate.com/docs/configuration-profiles)
- [Twingate Download Page](https://www.twingate.com/downloads)
- Kandji official documentation (Apple Business Manager enrollment)
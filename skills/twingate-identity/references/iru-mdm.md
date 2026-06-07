# Deploying Twingate Clients with Iru (MDM)

## Summary
Guide for distributing Twingate macOS and iOS clients via Iru (formerly Kandji) MDM. macOS deployment uses the Twingate Auto App (recommended) or custom PKG upload. iOS deployment requires Apple Business Manager integration.

## Key Information
- **macOS Auto App** automatically handles: notifications permissions, VPN profile enablement, system extension approval — no custom configuration needed
- **macOS custom app** alternative: requires uploading PKG from [Twingate download page](https://www.twingate.com/docs/download)
- **iOS** requires Apple Business Manager linkage with Iru before distribution is possible
- Pre-configuration of macOS client available via configuration profiles (VPN config, system extension, Network pre-population)

## Prerequisites
- **macOS**: Iru account with Library access
- **iOS**: 
  - Devices enrolled in Apple Business Manager
  - Iru linked to Apple Business Manager

## Step-by-Step

### macOS (Auto App — Recommended)
1. Sign in to Iru
2. Select **Library** in sidebar
3. Find Twingate Client app for macOS
4. Select and deploy via Auto App

### iOS
1. Add Twingate iOS Client to Apple Business Manager
2. Enroll devices in Apple Business Manager (see Iru's official docs)
3. Link Iru with Apple Business Manager
4. Sign in to Iru → **Library** → find Twingate iOS app → distribute

## Configuration Values
- macOS pre-configuration via MDM configuration profiles (see [configuration profiles guide](https://www.twingate.com/docs/configuration-profiles))
  - VPN configuration auto-enable
  - System extension approval
  - Network name pre-population

## Gotchas
- **Pre-existing manual installs cause conflicts**: If users installed Twingate manually before MDM rollout, version mismatches can occur
  - Fix: Create a temporary removal policy targeting all devices → remove Twingate → deactivate policy → then deploy via Iru
- Custom app deployment (PKG) is **not recommended** — requires manual configuration that Auto App handles automatically
- iOS distribution **will not work** without Apple Business Manager linked to Iru first

## Related Docs
- [Configuration Profiles guide](https://www.twingate.com/docs/configuration-profiles)
- [Twingate Client download page](https://www.twingate.com/docs/download)
- Iru's Apple Business Manager enrollment documentation (external)
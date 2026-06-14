# Deploying Twingate Clients with Iru (MDM)

## Summary
Guide for distributing Twingate macOS and iOS clients via Iru (formerly Kandji) MDM. macOS deployment is recommended via Auto App; iOS requires Apple Business Manager integration.

## Key Information
- **macOS Auto App** (recommended): Automatically handles notifications, VPN profile, and system extension — no custom configuration needed
- **macOS custom app** (not recommended): Requires uploading a PKG from the [Twingate download page](https://www.twingate.com/downloads)
- **iOS**: Requires Apple Business Manager linkage with Iru before distribution is possible

## Prerequisites
- Access to Iru admin console
- **iOS only**: Twingate app added to Apple Business Manager; devices enrolled in Apple Business Manager; Iru linked to Apple Business Manager

## Step-by-Step

### Locating Twingate in Iru
1. Sign in to Iru
2. Select **Library** in the sidebar
3. Find Twingate Client app for macOS and/or iOS
4. Select and deploy

### iOS Setup
1. Add Twingate iOS app to Apple Business Manager
2. Enroll devices in Apple Business Manager (follow Iru's official docs)
3. Link Iru with Apple Business Manager
4. Distribute via Iru Library

## Configuration Values
- macOS pre-configuration via [configuration profiles guide](https://www.twingate.com/docs/configuration-profiles): enables VPN config, system extension, pre-populates Network name

## Gotchas
- **Manually installed clients must be removed first** — version conflicts will occur if pre-existing installations differ from MDM-distributed version
  - Create a temporary removal policy targeting all devices
  - Deactivate the removal policy before rolling out MDM distribution
- iOS distribution is blocked without Apple Business Manager — cannot distribute directly without it
- Custom app (PKG) deployment skips automatic VPN profile and system extension approval that Auto App handles

## Related Docs
- [Twingate Configuration Profiles](https://www.twingate.com/docs/configuration-profiles)
- [Twingate Download Page](https://www.twingate.com/downloads)
- Iru's Apple Business Manager enrollment documentation
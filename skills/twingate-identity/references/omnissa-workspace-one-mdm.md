# Deploying macOS & iOS Clients with Omnissa Workspace ONE

## Summary
Guide for distributing Twingate clients via Omnissa Workspace ONE MDM on macOS and iOS. macOS uses PKG-based non-App Store deployment; iOS requires Apple Business Manager integration.

## Key Information
- macOS deployment uses PKG installer (non-App Store app distribution)
- iOS deployment requires Apple Business Manager linked to Workspace ONE
- Pre-configuration profiles available for macOS to automate VPN setup, system extension, and Network pre-population

## Prerequisites
- Workspace ONE admin access
- **macOS**: Twingate PKG downloaded from Twingate download page
- **iOS**: Twingate app added to Apple Business Manager; Workspace ONE linked to ABM via VPP Managed Distribution

## Step-by-Step

### macOS
1. Download Twingate PKG from Twingate download page
2. Upload PKG to Workspace ONE as a non-App Store app
3. Follow Workspace ONE documentation for PKG distribution
4. Optionally apply configuration profiles for pre-configuration

### iOS
1. Add Twingate to Apple Business Manager
2. In Workspace ONE: **Settings → Apple (Devices & Users) → VPP Managed Distribution**
3. Link Apple Business Manager account; ensure **"Automatically Send Invites" is unchecked**
4. Navigate to **Applications → Native → Purchased**, select Twingate
5. From **More Actions → Enable Device Assignment** (prevents personal Apple ID requirement)
6. From **More Actions → Enable Auto Updates** (recommended)

## Configuration Values
- macOS pre-configuration via configuration profiles (separate guide): enables VPN config, system extension, Network pre-population

## Gotchas
- **Manually installed clients must be removed first** — version mismatch between user-installed and MDM-distributed versions causes issues
  - Create a temporary removal policy targeting all devices, deactivate it before rolling out MDM distribution
- **"Automatically Send Invites" must be unchecked** during ABM linking
- **Device Assignment must be explicitly enabled** — default deployment requires personal Apple ID

## Related Docs
- [Twingate Configuration Profiles (macOS)](https://www.twingate.com/docs/configuration-profiles)
- [Twingate Download Page](https://www.twingate.com/downloads)
- Workspace ONE official PKG distribution documentation
- Apple Business Manager documentation
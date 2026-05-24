# Deploying macOS & iOS Clients with Omnissa Workspace ONE

## Summary
Covers distributing the Twingate Client via Omnissa Workspace ONE MDM for macOS (as a non-App Store PKG) and iOS (via Apple Business Manager integration). Includes setup steps for device assignment, auto-updates, and pre-configuration.

## Key Information
- macOS uses PKG installer distributed as a non-App Store app
- iOS requires Apple Business Manager (ABM) linked to Workspace ONE
- Pre-configuration profiles available for macOS to automate VPN setup, system extension, and Network population

## Prerequisites
- **macOS:** Workspace ONE configured to distribute non-App Store apps; Twingate PKG downloaded from [download page](https://www.twingate.com/download)
- **iOS:** Twingate app added to Apple Business Manager; Workspace ONE linked to ABM via VPP Managed Distribution

## Step-by-Step

### macOS
1. Download Twingate PKG installer from the download page
2. Upload PKG to Workspace ONE as a non-App Store app
3. Follow Workspace ONE documentation for distribution

### iOS — Link ABM
1. Navigate to **Settings → Apple (Devices & Users) → VPP Managed Distribution**
2. Follow guided steps to link Apple Business Manager
3. Ensure **"Automatically Send Invites"** is **unchecked**

### iOS — Enable Device Assignment
1. Navigate to **Applications → Native → Purchased**
2. Select the Twingate iOS app
3. From **More Actions**, select **Enable Device Assignment**
   - Prevents requirement for personal Apple ID to accept app assignments

### iOS — Enable Auto Updates
1. Select the Twingate iOS app
2. From **More Actions**, select **Enable Auto Updates**

## Configuration Values
- macOS pre-configuration options (via configuration profiles):
  - Auto-enable VPN configuration
  - Enable system extension
  - Pre-populate Network name

## Gotchas
- **Manually installed clients must be removed first** — version conflicts can occur if users already have Twingate installed outside MDM
  - Create a temporary removal policy targeting all devices; deactivate it before rolling out MDM-managed version
- "Automatically Send Invites" must be **unchecked** during ABM linking
- Device assignment must be explicitly enabled; default deployment method requires personal Apple ID

## Related Docs
- [Twingate Configuration Profiles (macOS)](https://www.twingate.com/docs/configuration-profiles)
- [Apple Business Manager](https://business.apple.com)
- Workspace ONE official documentation (non-App Store app distribution, ABM integration)
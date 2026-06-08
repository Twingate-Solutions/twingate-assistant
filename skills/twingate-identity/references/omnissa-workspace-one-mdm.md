# Deploying macOS & iOS Clients with Omnissa Workspace ONE

## Summary
Guide for distributing the Twingate Client via Omnissa Workspace ONE MDM on macOS and iOS platforms. macOS uses a PKG-based non-App Store deployment; iOS uses Apple Business Manager integration.

## Key Information
- macOS deployment requires uploading a PKG file to Workspace ONE as a non-App Store app
- iOS deployment requires Apple Business Manager (ABM) linked to Workspace ONE
- PKG installer available from the [Twingate download page](https://www.twingate.com/download)

## Prerequisites
- **macOS**: Workspace ONE admin access; Twingate PKG installer downloaded
- **iOS**: Apple Business Manager account; Twingate app added to ABM; Workspace ONE linked to ABM via VPP Managed Distribution

## Step-by-Step

### macOS
1. Download Twingate PKG from the download page
2. Upload PKG to Workspace ONE as a non-App Store app
3. Follow Workspace ONE documentation for distribution configuration
4. Optionally apply pre-configuration via [configuration profiles](https://www.twingate.com/docs/configuration-profiles)

### iOS
1. Navigate to **Settings → Apple (under Devices & Users) → VPP Managed Distribution**
2. Link Apple Business Manager account (ensure "Automatically Send Invites" is **unchecked**)
3. Go to **Applications → Native → Purchased**, select Twingate iOS app
4. From **More Actions**, select **Enable Device Assignment** (prevents personal Apple ID requirement)
5. Optionally select **Enable Auto Updates** from **More Actions**

## Configuration Values
- Pre-configuration options (macOS): auto-enable VPN, enable system extension, pre-populate Network name — configured via configuration profiles guide

## Gotchas
- **Manually installed clients must be removed first** — version conflicts can occur if users already have Twingate installed; create a temporary removal policy before rollout, then deactivate it
- "Automatically Send Invites" must be **unchecked** during ABM linking
- Device Assignment must be explicitly enabled; default deployment requires users' personal Apple IDs

## Related Docs
- [Twingate Configuration Profiles (macOS)](https://www.twingate.com/docs/configuration-profiles)
- [Workspace ONE VPP/ABM Integration](https://docs.omnissa.com) (Workspace ONE official docs)
- [Apple Business Manager](https://business.apple.com)
- [Twingate Download Page](https://www.twingate.com/download)
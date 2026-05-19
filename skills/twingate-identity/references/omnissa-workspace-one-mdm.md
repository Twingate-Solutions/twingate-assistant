# Deploying macOS & iOS Clients with Omnissa Workspace ONE

## Summary
Covers distributing the Twingate Client via Omnissa Workspace ONE for macOS (as a non-App Store PKG) and iOS (via Apple Business Manager integration). Includes device assignment, auto-updates, and pre-configuration options.

## Key Information
- macOS deployment uses PKG installer uploaded to Workspace ONE as a non-App Store app
- iOS deployment requires Apple Business Manager linked to Workspace ONE
- Pre-configuration profiles available for macOS to automate VPN setup, system extension, and Network pre-population

## Prerequisites
- **macOS**: Workspace ONE configured for non-App Store app distribution; Twingate PKG downloaded from Twingate download page
- **iOS**: Twingate added to Apple Business Manager; Workspace ONE linked to Apple Business Manager via VPP Managed Distribution

## Step-by-Step

### macOS
1. Download Twingate PKG from the Twingate download page
2. Upload PKG to Workspace ONE as a non-App Store app
3. Follow Workspace ONE documentation to configure and distribute
4. Optionally apply configuration profiles for pre-configuration

### iOS
1. Add Twingate iOS Client to Apple Business Manager
2. In Workspace ONE navigate to **Settings → Apple (Devices & Users) → VPP Managed Distribution**
3. Link Apple Business Manager account; uncheck **"Automatically Send Invites"**
4. Navigate to **Applications → Native → Purchased**, select Twingate iOS app
5. Via **More Actions**, select **Enable Device Assignment** (prevents personal Apple ID requirement)
6. Via **More Actions**, select **Enable Auto Updates** (recommended)

## Configuration Values
- macOS pre-configuration options (via configuration profiles):
  - Auto-enable VPN configuration
  - Enable system extension
  - Pre-populate Network name

## Gotchas
- **Manually installed clients must be removed first**: Users with pre-existing manual installs may experience version conflicts. Create a temporary removal policy targeting all devices before rollout, then deactivate it
- **"Automatically Send Invites" must be unchecked** during Apple Business Manager linking
- **Device Assignment must be explicitly enabled** — default deployment method requires personal Apple ID otherwise

## Related Docs
- Twingate macOS configuration profiles guide
- Workspace ONE non-App Store app distribution documentation
- Apple Business Manager / Workspace ONE VPP integration documentation
- Twingate Client download page
# Deploying macOS & iOS Clients with Omnissa Workspace ONE

## Summary
Guide for distributing the Twingate Client via Omnissa Workspace ONE MDM for both macOS and iOS platforms. macOS uses PKG distribution; iOS requires Apple Business Manager integration.

## Key Information
- macOS deployment uses non-App Store PKG distribution
- iOS deployment requires Apple Business Manager (ABM) linked to Workspace ONE
- Pre-configuration of macOS client is supported via configuration profiles

## Prerequisites
- **macOS**: Workspace ONE configured for non-App Store app distribution; Twingate PKG downloaded from the Twingate download page
- **iOS**: Apple Business Manager account; Twingate iOS app added to ABM; Workspace ONE linked to ABM via VPP Managed Distribution

## Step-by-Step

### macOS
1. Download Twingate PKG installer from the Twingate download page
2. Upload PKG to Workspace ONE as a non-App Store app
3. Follow Workspace ONE documentation to configure and distribute
4. Optionally apply configuration profiles for pre-configuration (VPN config, system extension, Network pre-population)

### iOS
1. Add Twingate iOS Client to Apple Business Manager
2. In Workspace ONE, navigate to **Settings → Apple (Devices & Users) → VPP Managed Distribution**
3. Link Apple Business Manager account following guided steps
4. Ensure **"Automatically Send Invites"** is **unchecked**
5. Navigate to **Applications → Native → Purchased**, select Twingate iOS app
6. From **More Actions**, select **Enable Device Assignment** (prevents personal Apple ID requirement)
7. From **More Actions**, select **Enable Auto Updates** (recommended)

## Configuration Values
| Setting | Location | Value |
|---|---|---|
| Automatically Send Invites | VPP Managed Distribution setup | Unchecked |
| Device Assignment | More Actions on app | Enabled |
| Auto Updates | More Actions on app | Enabled (recommended) |

## Gotchas
- **Manually installed clients conflict**: Users who installed Twingate manually before MDM rollout may experience version mismatch issues. Create a temporary removal policy to uninstall existing clients before distributing via Workspace ONE; deactivate that policy before rollout.
- ABM integration must be completed before iOS app distribution is possible.
- Device assignment must be explicitly enabled — default deployment requires users to accept via personal Apple ID.

## Related Docs
- [Twingate Configuration Profiles (macOS pre-configuration)](https://www.twingate.com/docs/configuration-profiles)
- Workspace ONE non-App Store app distribution (Workspace ONE official docs)
- Workspace ONE + Apple Business Manager integration (Workspace ONE official docs)
- Apple Business Manager (Apple official docs)
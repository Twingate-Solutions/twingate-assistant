---
source: https://www.twingate.com/docs/omnissa-workspace-one-mdm
type: docs
fetched: 2026-08-14
source_version: 8ffd9e8ba107f6eab6f00119b74b52c3da3ac9648082ecf7a0a4ba931c836c53
---

# Deploying macOS & iOS Clients with Omnissa Workspace ONE

## Summary
Guide for distributing the Twingate Client via Omnissa Workspace ONE MDM for both macOS and iOS platforms. macOS uses PKG-based deployment; iOS uses Apple Business Manager integration.

## Key Information
- macOS deployment uses non-App Store (PKG) distribution method
- iOS deployment requires Apple Business Manager (ABM) linked to Workspace ONE
- Pre-configuration profiles available for macOS to automate VPN, system extension, and Network setup

## Prerequisites
- Omnissa Workspace ONE instance with admin access
- **macOS**: Twingate PKG installer (from Twingate download page)
- **iOS**: Apple Business Manager account with Twingate iOS app added; Workspace ONE linked to ABM

## Step-by-Step

### macOS
1. Download Twingate PKG from the Twingate download page
2. Upload PKG to Workspace ONE as a non-App Store app
3. Follow Workspace ONE's official documentation for PKG distribution
4. (Optional) Apply configuration profiles to pre-configure VPN, system extension, and Network

### iOS
1. Add Twingate iOS app to Apple Business Manager
2. In Workspace ONE, navigate to **Settings → Apple (under Devices & Users) → VPP Managed Distribution**
3. Follow guided steps to link ABM account
4. Ensure **"Automatically Send Invites" is unchecked**
5. Navigate to **Applications → Native → Purchased**, select Twingate iOS app
6. From **More Actions**, select **Enable Device Assignment** (prevents personal Apple ID requirement)
7. From **More Actions**, select **Enable Auto Updates** (recommended)

## Configuration Values
| Setting | Location | Value |
|---|---|---|
| Automatically Send Invites | VPP Managed Distribution setup | Unchecked |
| Device Assignment | More Actions → Enable Device Assignment | Enabled |
| Auto Updates | More Actions → Enable Auto Updates | Enabled (recommended) |

## Gotchas
- **Manually installed clients must be removed first**: Users with pre-existing manual installs may encounter version conflicts. Create a temporary removal policy before rollout, then deactivate it
- **"Automatically Send Invites" must be unchecked** during ABM linking or app assignment flow breaks
- Device Assignment must be explicitly enabled — default deployment method requires personal Apple ID

## Related Docs
- [Twingate macOS Configuration Profiles](https://www.twingate.com/docs/configuration-profiles) — for pre-configuring VPN, system extension, Network
- Twingate download page (for PKG installer)
- Workspace ONE official PKG distribution documentation
- Apple Business Manager documentation
- Workspace ONE × Apple Business Manager integration guide
---
source: https://www.twingate.com/docs/omnissa-workspace-one-mdm
type: docs
fetched: 2026-10-25
source_version: 660b7a7d9fd1dfd53125f4572d14abe3c6b14cfe26143ea7074ebf7a9de372d9
trust: official
---

# Deploying macOS & iOS Clients with Omnissa Workspace ONE

## Summary
Guide for distributing the Twingate Client via Omnissa Workspace ONE MDM on macOS and iOS. macOS uses PKG-based deployment; iOS uses Apple Business Manager integration. Pre-configuration profiles are supported for macOS.

## Key Information
- Mac App Store version is **no longer supported**; use standalone PKG only
- macOS distribution requires Workspace ONE's non-App Store app workflow
- iOS distribution requires Apple Business Manager (ABM) linked to Workspace ONE
- Device assignment must be explicitly enabled for iOS to avoid personal Apple ID prompts
- Auto-updates for iOS must be manually enabled

## Prerequisites
- Workspace ONE admin access
- **macOS:** PKG installer downloaded from [Twingate download page](https://www.twingate.com/docs/downloads)
- **iOS:** Apple Business Manager account with Twingate app added; Workspace ONE linked to ABM

## Step-by-Step

### macOS
1. Download the Twingate PKG installer from the Twingate download page
2. In Workspace ONE, configure and upload the PKG as a **non-App Store app**
3. Optionally apply a configuration profile to pre-configure the client (VPN config, system extension, Network name)

### iOS
1. Add Twingate iOS app to Apple Business Manager
2. In Workspace ONE, navigate to **Settings → Apple (Devices & Users) → VPP Managed Distribution**
3. Link Apple Business Manager account; ensure **"Automatically Send Invites" is unchecked**
4. Navigate to **Applications → Native → Purchased**, select Twingate iOS app
5. From **More Actions**, select **Enable Device Assignment**
6. From **More Actions**, select **Enable Auto Updates** (recommended)

## Configuration Values
| Setting | Location | Value |
|---|---|---|
| VPP Managed Distribution | Settings → Apple → VPP Managed Distribution | Link ABM account |
| Automatically Send Invites | VPP setup | **Unchecked** |
| Device Assignment | Applications → Native → Purchased → More Actions | Enabled |
| Auto Updates | Applications → Native → Purchased → More Actions | Enabled (recommended) |

## Gotchas
- **Do not skip removing manually installed clients** before MDM rollout — version conflicts will occur. Use a temporary removal policy before deploying via Workspace ONE, then deactivate that policy.
- Mac App Store version is deprecated; any existing App Store installs should be migrated to the PKG version.
- If device assignment is not enabled on iOS, users will be prompted for their personal Apple ID to accept app assignments.

## Related Docs
- [Twingate macOS/iOS Download Page](https://www.twingate.com/docs/downloads)
- [Twingate Configuration Profiles (macOS pre-config)](https://www.twingate.com/docs/configuration-profiles)
- Workspace ONE official docs: non-App Store app distribution
- Apple Business Manager + Workspace ONE integration docs
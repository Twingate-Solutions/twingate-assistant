# Deploying macOS & iOS Clients with Omnissa Workspace ONE

## Summary
Guide for distributing the Twingate Client via Omnissa Workspace ONE MDM for macOS and iOS platforms. macOS uses PKG-based deployment; iOS uses Apple Business Manager integration.

## Key Information
- macOS deployment requires PKG installer (non-App Store distribution)
- iOS deployment requires Apple Business Manager (ABM) linked to Workspace ONE
- Pre-configuration of macOS client is supported via configuration profiles

## Prerequisites
- Workspace ONE admin access
- **macOS**: Twingate PKG installer (from Twingate download page)
- **iOS**: Apple Business Manager account with Twingate app added; Workspace ONE linked to ABM

## Step-by-Step

### macOS
1. Download Twingate PKG from the Twingate download page
2. Upload PKG to Workspace ONE as a non-App Store app
3. Follow Workspace ONE documentation for PKG distribution
4. (Optional) Apply configuration profiles for pre-configuration

### iOS
1. Add Twingate iOS Client to Apple Business Manager
2. In Workspace ONE, navigate to **Settings → Apple (Devices & Users) → VPP Managed Distribution**
3. Link Apple Business Manager account (ensure "Automatically Send Invites" is **unchecked**)
4. Navigate to **Applications → Native → Purchased**, select Twingate iOS app
5. Via **More Actions → Enable Device Assignment** (prevents personal Apple ID requirement)
6. Via **More Actions → Enable Auto Updates** (recommended)

## Configuration Values
| Setting | Value/Location |
|---|---|
| VPP Managed Distribution | Settings → Apple → VPP Managed Distribution |
| Automatically Send Invites | Must be **unchecked** |
| Device Assignment | Applications → Native → Purchased → More Actions |
| Auto Updates | Applications → Native → Purchased → More Actions |

## Gotchas
- **Manually installed clients must be removed first** — version conflicts will occur if users have pre-existing manual installs; create a temporary removal policy before rollout, then deactivate it
- "Automatically Send Invites" must be unchecked during ABM linking or device assignment flow breaks
- Device Assignment must be explicitly enabled — default deployment requires personal Apple ID

## Related Docs
- Twingate macOS configuration profiles guide (for pre-populating Network, enabling VPN config and system extension)
- Workspace ONE official PKG distribution documentation
- Apple Business Manager documentation
- Twingate download page (PKG installer)
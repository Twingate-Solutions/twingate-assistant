# Deploying Twingate Client with Kandji MDM

## Summary
Guide for distributing Twingate macOS and iOS clients via Kandji MDM. macOS deployment uses Kandji's Auto App (recommended) or custom PKG upload. iOS deployment requires Apple Business Manager integration.

## Key Information

- **macOS Auto App** automatically handles: notifications permission, VPN profile enablement, system extension approval — no custom configuration needed
- **macOS custom app** alternative: requires uploading a PKG file from Twingate's download page
- **iOS** requires Apple Business Manager linked to Kandji before distribution is possible
- Pre-configuration via configuration profiles can auto-enable VPN, system extension, and pre-populate Network name

## Prerequisites

- Kandji admin access
- **iOS only**: Devices enrolled in Apple Business Manager; Kandji linked to Apple Business Manager
- **macOS custom app only**: Twingate PKG installer downloaded from Twingate download page

## Step-by-Step

### macOS (Recommended)
1. Sign in to Kandji
2. Select **Library** in the sidebar
3. Find Twingate Client app for macOS
4. Select the **Auto App** option — no further configuration required

### iOS
1. Add Twingate iOS Client to Apple Business Manager
2. Add devices to Apple Business Manager (follow Kandji's official docs)
3. Link Kandji with Apple Business Manager
4. Sign in to Kandji → **Library** → find Twingate iOS app → distribute

### macOS (Custom App Alternative)
1. Download Twingate PKG from Twingate download page
2. Upload PKG to Kandji as a custom app

## Configuration Values

- Pre-configuration options available via **configuration profiles** (separate guide):
  - VPN configuration auto-enable
  - System extension approval
  - Network name pre-population

## Gotchas

- **Manually installed clients cause conflicts**: If users installed Twingate before MDM rollout, version mismatches can occur
  - Fix: Create a temporary Kandji policy to remove Twingate from all devices before deploying via Kandji; deactivate the removal policy when ready to roll out
- Custom app deployment is **not recommended** — lacks Auto App's automatic permission handling
- iOS distribution will not work without Apple Business Manager linked to Kandji first

## Related Docs

- Twingate configuration profiles guide (macOS pre-configuration)
- Kandji official documentation (Apple Business Manager device enrollment)
- Twingate client download page (PKG installer)
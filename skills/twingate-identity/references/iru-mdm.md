# Deploying Twingate Clients with Iru (MDM)

## Summary
Guide for distributing the Twingate macOS and iOS clients via Iru (formerly Kandji) MDM. macOS deployment uses the Twingate Auto App (recommended) or a custom PKG upload. iOS deployment requires Apple Business Manager integration.

## Key Information
- **macOS recommended method**: Twingate Auto App in Iru Library (handles notifications, VPN profile, and system extension automatically)
- **macOS alternative**: Custom app via PKG upload (not recommended)
- **iOS method**: Requires Apple Business Manager linkage with Iru
- PKG installer available at Twingate's download page

## Prerequisites
- **macOS**: Access to Iru admin console
- **iOS**: 
  - Twingate iOS app added to Apple Business Manager
  - Devices enrolled in Apple Business Manager
  - Iru linked to Apple Business Manager

## Step-by-Step

### macOS (Auto App - Recommended)
1. Sign in to Iru
2. Select **Library** in sidebar
3. Find Twingate Client app for macOS and select it
4. Deploy via Auto App (no custom configuration needed)

### iOS
1. Add Twingate iOS app to Apple Business Manager
2. Enroll devices in Apple Business Manager
3. Link Iru with Apple Business Manager
4. Sign in to Iru → **Library** → find Twingate iOS Client → distribute

### macOS (Custom PKG - Alternative)
1. Download PKG from Twingate download page
2. Upload PKG to Iru as custom app
3. Deploy to target devices

## Configuration Values
- Pre-configuration via **configuration profiles** guide (separate doc) enables:
  - VPN configuration auto-enable
  - System extension auto-enable
  - Pre-populate Network/tenant name

## Gotchas
- **Manually installed clients cause conflicts**: If users previously installed Twingate manually, version mismatches can occur. Remediation:
  1. Create a temporary policy to remove Twingate from all devices
  2. Deactivate the removal policy before rolling out via Iru
- Auto App automatically handles VPN profile and system extension approval — custom app deployment does not
- iOS requires Apple Business Manager; direct App Store distribution through Iru alone is insufficient

## Related Docs
- Twingate Configuration Profiles guide (for pre-configuring macOS client)
- Iru official documentation (for Apple Business Manager enrollment)
- Twingate download page (for PKG installer)
- Apple Business Manager setup documentation
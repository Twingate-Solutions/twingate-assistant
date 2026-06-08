# Managed Devices

## Summary
Twingate supports deployment on managed devices via most major MDM solutions including AirWatch, Intune, Jamf, and Iru (formerly Kandji). Platform-specific installation packages are available for Windows, macOS, and iOS. The client creates a local VPN profile but routes no traffic externally.

## Key Information
- **Windows**: EXE or MSI installer with silent install and pre-configuration options
- **macOS/iOS**: Available via Apple App Store and as standalone PKG
- MDM solutions can deploy Mac/App Store versions if allocated through **Apple Business Manager**
- Client requires no special device privileges
- Creates a VPN profile with server address `127.0.0.1` — all VPN traffic stays local to the device
- No VPN traffic leaves the device

## Prerequisites
- MDM solution (AirWatch, Intune, Jamf, Iru/Kandji, or similar)
- For App Store deployment: Apple Business Manager allocation required

## Configuration Values
| Platform | Package Type | Notes |
|----------|-------------|-------|
| Windows | EXE or MSI | Supports silent install, pre-configuration |
| macOS | App Store or PKG | MDM deployable via ABM |
| iOS | App Store | MDM deployable via ABM |

## Gotchas
- The VPN profile VPN server address (`127.0.0.1`) is expected behavior — not a misconfiguration
- App Store deployment via MDM **requires** Apple Business Manager allocation; direct App Store apps cannot be pushed without it
- Client needs permission to create a VPN profile — this may require MDM policy configuration to allow VPN profile installation

## Related Docs
- AirWatch-specific instructions (sub-article)
- Intune-specific instructions (sub-article)
- Jamf-specific instructions (sub-article)
- Iru/Kandji-specific instructions (sub-article)
- Apple Business Manager documentation
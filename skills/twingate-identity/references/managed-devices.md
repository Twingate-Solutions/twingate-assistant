# Managed Devices

## Summary
Twingate supports deployment on managed devices via most MDM platforms including AirWatch, Intune, Jamf, and Kandji (formerly Iru). Installation packages are available for Windows (EXE/MSI) and macOS/iOS (App Store or PKG). The client creates a local VPN profile but all VPN traffic stays on-device.

## Key Information
- Compatible MDM platforms: AirWatch, Intune, Jamf, Kandji (formerly Iru)
- Windows: EXE or MSI with silent install and pre-configuration options
- macOS/iOS: Available via Apple App Store or standalone PKG
- Mac/iOS App Store deployments require apps allocated through **Apple Business Manager**
- Client requires no special device privileges
- Creates a VPN profile to operate; VPN server address is `127.0.0.1`
- No VPN traffic leaves the device — local tunnel only

## Prerequisites
- MDM solution already deployed
- For Mac App Store/iOS App Store deployment: Apple Business Manager account with app licenses allocated
- Platform-specific sub-guides available for each MDM

## Configuration Values
| Platform | Package Type | Notes |
|----------|-------------|-------|
| Windows | EXE or MSI | Supports silent install, pre-configuration flags |
| macOS | PKG or App Store | MDM must use Apple Business Manager for App Store version |
| iOS | App Store | MDM must use Apple Business Manager |

## Gotchas
- The VPN profile creation is required for operation — do not block VPN profile installation via MDM policy
- App Store deployment on macOS/iOS **requires** Apple Business Manager allocation; direct MDM push without ABM will not work
- VPN server showing `127.0.0.1` is expected and intentional — not a misconfiguration

## Related Docs
- Twingate Windows MDM deployment (sub-article)
- Twingate macOS MDM deployment (sub-article)
- Twingate iOS MDM deployment (sub-article)
- Apple Business Manager integration
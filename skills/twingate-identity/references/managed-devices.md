# Managed Devices

## Summary
Twingate supports deployment on managed devices via common MDM platforms (AirWatch, Intune, Jamf, Kandji/Iru). Installation options vary by OS, with silent/pre-configuration options available for Windows and App Store/PKG options for Apple platforms.

## Key Information
- Compatible MDM platforms: AirWatch, Intune, Jamf, Iru (formerly Kandji)
- Windows: EXE or MSI installer with silent install and pre-configuration support
- macOS/iOS: Available via Apple App Store or standalone PKG file
- Mac/iOS App Store deployment requires apps allocated through **Apple Business Manager**
- Client requires no special device privileges
- Client creates a local VPN profile to operate (VPN server address: `127.0.0.1`)
- No VPN traffic leaves the device — the VPN interface is used solely for local routing to the Twingate client

## Prerequisites
- For App Store deployment on macOS/iOS: Apple Business Manager account with app allocation configured
- MDM solution must support Mac App Store / iOS App Store app deployment

## Platform-Specific Notes

| Platform | Install Method |
|----------|---------------|
| Windows | EXE or MSI (silent + pre-config options) |
| macOS | Apple App Store or standalone PKG |
| iOS | Apple App Store |

## Gotchas
- The VPN profile creation may trigger OS-level VPN permission prompts on macOS/iOS — this is expected behavior, not a true VPN tunnel
- VPN server showing `127.0.0.1` is intentional; traffic does not leave the device through this interface
- macOS/iOS MDM App Store deployment **requires** Apple Business Manager — standard MDM enrollment alone is insufficient for App Store app distribution

## Related Docs
- Windows MDM-specific instructions (sub-article)
- macOS MDM-specific instructions (sub-article)
- iOS MDM-specific instructions (sub-article)
- Jamf deployment guide (sub-article)
- Iru/Kandji deployment guide (sub-article)
- AirWatch deployment guide (sub-article)
- Apple Business Manager (external)
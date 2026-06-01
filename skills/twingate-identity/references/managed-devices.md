# Managed Devices

## Page Title
Managed Devices

## Summary
Twingate supports deployment on managed devices via MDM solutions including AirWatch, Intune, Jamf, and Kandji (now Iru). Platform-specific installers are available for Windows, macOS, and iOS with silent/pre-configuration options.

## Key Information
- Compatible MDMs: AirWatch, Intune, Jamf, Iru (formerly Kandji)
- Windows: EXE or MSI installer with silent install and pre-configuration support
- macOS/iOS: Available via Apple App Store or standalone PKG
- Mac/iOS MDM deployment requires apps allocated through **Apple Business Manager**
- Client creates a local VPN profile; VPN server address is `127.0.0.1`
- No VPN traffic leaves the device — connection is local only

## Prerequisites
- For macOS/iOS MDM deployment: Apple Business Manager account with app allocation
- MDM solution already configured and managing target devices

## Configuration Values
- **Windows installer formats:** `.exe`, `.msi`
- **macOS installer formats:** App Store app, `.pkg`
- **VPN server address (local):** `127.0.0.1`
- Silent install and pre-configuration flags available (see platform-specific sub-articles)

## Gotchas
- The client requires permission to create a VPN profile on the device — ensure MDM policy allows this
- Despite creating a VPN profile, no traffic is tunneled externally; the VPN is used internally by the Twingate client only
- macOS/iOS MDM deployment via App Store apps requires Apple Business Manager — direct APK/IPA sideloading is not the documented path

## Related Docs
- Windows MDM setup (sub-article)
- macOS MDM setup (sub-article)
- iOS MDM setup (sub-article)
- Jamf-specific instructions (sub-article)
- Iru/Kandji-specific instructions (sub-article)
- AirWatch-specific instructions (sub-article)
- Intune-specific instructions (sub-article)
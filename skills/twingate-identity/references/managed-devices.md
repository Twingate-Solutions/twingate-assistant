# Managed Devices

## Summary
Twingate supports deployment on managed devices via MDM solutions including AirWatch, Intune, Jamf, and Kandji (formerly Iru). Platform-specific installation packages are available for Windows, macOS, and iOS with silent/pre-configuration options.

## Key Information
- Compatible MDM solutions: AirWatch, Intune, Jamf, Kandji (formerly Iru)
- Windows: EXE or MSI installer with silent install and pre-configuration support
- macOS/iOS: Available via Apple App Store or standalone PKG
- Mac/iOS App Store deployment requires apps allocated through **Apple Business Manager**
- Client creates a local VPN profile to operate; VPN server address is `127.0.0.1`
- No VPN traffic leaves the device — tunnel is local only

## Prerequisites
- For Mac/iOS App Store deployment: Apple Business Manager account with app allocation
- MDM solution configured for your organization

## Platform Notes

### Windows
- Use EXE or MSI package
- Supports silent install flags and pre-configuration options
- See Windows-specific sub-article for CLI flags

### macOS & iOS
- Deploy via Apple App Store (through MDM) or standalone PKG
- MDM platforms (Jamf, AirWatch, Kandji) can push App Store apps if allocated via Apple Business Manager

## Gotchas
- The client requires permission to create a VPN profile — this is mandatory for operation, not optional
- The VPN profile shows `127.0.0.1` as server address; this is expected behavior, not a misconfiguration
- No special device privileges required beyond VPN profile creation
- App Store deployment without Apple Business Manager allocation will fail

## Related Docs
- Windows MDM installation (sub-article)
- macOS MDM installation (sub-article)
- iOS MDM installation (sub-article)
- Jamf-specific instructions (sub-article)
- Kandji/Iru-specific instructions (sub-article)
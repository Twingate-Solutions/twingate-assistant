# Managed Devices

## Summary
Twingate supports deployment on managed devices via most MDM solutions including AirWatch, Intune, Jamf, and Iru (formerly Kandji). Platform-specific installation packages are available for Windows, macOS, and iOS with silent/pre-configuration options.

## Key Information
- Compatible MDMs: AirWatch, Intune, Jamf, Iru (formerly Kandji)
- Windows: EXE or MSI package with silent install and pre-configuration support
- macOS/iOS: Available via Apple App Store and as standalone PKG
- Mac/iOS MDM deployment requires apps allocated through **Apple Business Manager**
- Client creates a VPN profile on the device to operate
- VPN server address is `127.0.0.1` — no traffic leaves the device
- Client requires no special privileges on the device

## Prerequisites
- For macOS/iOS MDM deployment: Apple Business Manager account with app allocation
- MDM solution already configured and managing target devices

## Configuration Notes
- **Windows**: MSI/EXE supports silent install flags and pre-configuration options (see Windows sub-article)
- **macOS**: Standalone PKG available as alternative to App Store distribution
- VPN profile creation is required for client operation (handled automatically)

## Gotchas
- The VPN profile (`127.0.0.1` server address) is internal only — it's used solely for Twingate's local operation, not for routing external traffic
- MDM deployment of Mac/iOS App Store apps requires Apple Business Manager allocation; direct App Store installs cannot be pushed via MDM without it

## Related Docs
- Windows MDM installation sub-article
- macOS MDM installation sub-article (Jamf, Iru/Kandji, AirWatch)
- iOS MDM installation sub-article
- Apple Business Manager documentation
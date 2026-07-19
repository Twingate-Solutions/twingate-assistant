# Managed Devices

## Summary
Twingate supports deployment on managed devices via MDM solutions including AirWatch, Intune, Jamf, and Iru (formerly Kandji). The client creates a local VPN profile for internal routing only—no traffic leaves the device via VPN.

## Key Information
- Compatible MDMs: AirWatch, Intune, Jamf, Iru (formerly Kandji)
- Windows: EXE or MSI installer with silent install and pre-configuration options
- macOS/iOS: Available via Apple App Store or standalone PKG
- Mac/iOS MDM deployment requires apps allocated through **Apple Business Manager**
- Client requires no special device privileges
- Creates a VPN profile, but VPN server address is `127.0.0.1` (local only—no VPN traffic leaves the device)

## Prerequisites
- MDM solution already configured and managing target devices
- For Mac/iOS App Store deployment: Apple Business Manager account with Twingate allocated

## Platform Notes

| Platform | Installer Type | Silent Install |
|----------|---------------|----------------|
| Windows | EXE or MSI | Yes |
| macOS | PKG or App Store | Via MDM |
| iOS | App Store | Via MDM |

## Gotchas
- The VPN profile creation may trigger OS-level VPN permission prompts if not pre-approved via MDM configuration profiles
- iOS/macOS App Store deployment **requires Apple Business Manager**—direct App Store links alone are insufficient for MDM push
- VPN address `127.0.0.1` is expected behavior, not a misconfiguration

## Related Docs
- Platform-specific sub-articles: Windows MDM, Jamf, AirWatch, Iru/Kandji, Intune
- Apple Business Manager integration documentation
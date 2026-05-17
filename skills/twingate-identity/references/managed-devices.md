# Managed Devices

## Summary
Twingate supports deployment on managed devices via major MDM solutions including AirWatch, Intune, Jamf, and Kandji. The client creates a local VPN profile (127.0.0.1) solely for internal application use — no VPN traffic leaves the device.

## Key Information
- Compatible MDMs: AirWatch, Intune, Jamf, Kandji
- Windows: EXE or MSI installer with silent install and pre-configuration options
- macOS/iOS: Available via Apple App Store and standalone PKG
- Mac/iOS App Store deployment requires apps allocated through **Apple Business Manager**
- Client requires no special device privileges
- Creates a VPN profile pointed at `127.0.0.1` — traffic stays local to device

## Configuration Values
| Platform | Package Format | Notes |
|----------|---------------|-------|
| Windows | EXE, MSI | Silent install + pre-config supported |
| macOS | PKG, App Store | Requires Apple Business Manager for MDM App Store deployment |
| iOS | App Store | Requires Apple Business Manager for MDM deployment |

## Gotchas
- VPN profile creation is required for operation even though no external VPN traffic is generated — ensure MDM policies don't block VPN profile creation
- macOS/iOS App Store deployment via MDM (Kandji, Jamf, AirWatch) **requires** Apple Business Manager allocation; direct App Store apps cannot be pushed without it
- The `127.0.0.1` VPN server address is expected behavior, not a misconfiguration

## Related Docs
- Windows MDM-specific instructions (sub-article)
- macOS MDM-specific instructions (sub-article)
- iOS MDM-specific instructions (sub-article)
- Apple Business Manager integration
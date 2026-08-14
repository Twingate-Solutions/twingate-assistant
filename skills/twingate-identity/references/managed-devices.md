---
source: https://www.twingate.com/docs/managed-devices
type: docs
fetched: 2026-08-14
source_version: 34153b41f9e0649f205d4fa37c91da3996cc9c72817ccca63bb16481922ce857
---

# Managed Devices

## Summary
Twingate supports deployment on managed devices via MDM solutions including AirWatch, Intune, Jamf, and Kandji (formerly Iru). Platform-specific installation packages are available for Windows, macOS, and iOS with silent/pre-configuration options.

## Key Information
- Compatible MDMs: AirWatch, Intune, Jamf, Kandji (formerly Iru)
- Windows: EXE or MSI installer with silent install and pre-configuration support
- macOS/iOS: Available via Apple App Store or standalone PKG
- Mac/iOS MDM deployment requires apps allocated through **Apple Business Manager**
- Client requires no special device privileges
- Client creates a local VPN profile to operate (VPN server address: `127.0.0.1`)
- No VPN traffic leaves the device — local VPN is used only for Twingate's internal routing

## Prerequisites
- For macOS/iOS MDM deployment: Apple Business Manager account with Twingate allocated
- MDM solution already configured and managing target devices
- Windows: Access to EXE or MSI package

## Configuration Values
| Platform | Package Type | Notes |
|----------|-------------|-------|
| Windows | EXE, MSI | Supports silent install, pre-configuration |
| macOS | PKG, App Store | MDM requires Apple Business Manager |
| iOS | App Store | MDM requires Apple Business Manager |

## Gotchas
- VPN profile creation is required for operation — ensure MDM policy allows VPN profile installation by apps
- macOS/iOS MDM deployment via App Store **requires Apple Business Manager** allocation; direct App Store installs won't work with MDM deployment
- The `127.0.0.1` VPN server address is expected behavior, not a misconfiguration

## Related Docs
- Twingate Windows MDM deployment (sub-article)
- Twingate macOS MDM deployment (sub-article)
- Twingate iOS MDM deployment (sub-article)
- Apple Business Manager integration
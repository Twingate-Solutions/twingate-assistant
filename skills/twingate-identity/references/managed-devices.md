# Managed Devices

## Summary
Twingate supports deployment on managed devices via major MDM solutions. Installation packages are available for Windows, macOS, and iOS with silent/pre-configuration options. The client creates a local VPN profile (127.0.0.1) that never routes traffic off-device.

## Key Information
- Compatible MDMs: AirWatch, InTune, JAMF, Kandji
- Windows: EXE or MSI package with silent install and pre-configuration support
- macOS/iOS: Available via Apple App Store or standalone PKG
- Mac/iOS App Store deployments require apps allocated through **Apple Business Manager**
- Client requires no special device privileges
- Creates a VPN profile to operate, but VPN server address is `127.0.0.1` — no traffic leaves the device

## Prerequisites
- MDM solution configured for your organization
- For App Store deployments: Apple Business Manager account with Twingate allocated

## Configuration Notes
- Silent install options available for Windows MSI/EXE (see platform-specific sub-articles)
- PKG available as alternative to App Store for macOS managed deployments

## Gotchas
- The local VPN profile (`127.0.0.1`) may trigger VPN-detection policies or user alerts — it is not a traditional VPN
- MDMs deploying Mac/iOS App Store version must have the app allocated via Apple Business Manager first; direct MDM push without ABM allocation will fail
- Client needs permission to create VPN profiles; this may require MDM policy configuration even though no elevated privileges are needed

## Related Docs
- Windows MDM deployment (sub-article)
- macOS MDM deployment (sub-article)
- iOS MDM deployment (sub-article)
- Apple Business Manager integration
---
source: https://help.twingate.com/articles/3201241878-vpn-profile-fails-to-deploy-for-macos-using-jamf-pro
type: help
fetched: 2026-08-06
source_version: 47244c531b413e707a1dc1bbe6fff722848e37584ca7632f122fa6de047ad2ec
---

# VPN Profile Fails to Deploy for macOS Using Jamf Pro

## Summary
Jamf Pro 11.11 contains a bug (PI122416) that prevents Twingate VPN Custom Configuration Profiles from installing on macOS devices. A workaround exists using externally signed profiles. This bug was resolved in Jamf Pro version 11.12.1.

## Key Information
- **Affected version**: Jamf Pro 11.11
- **Fixed version**: Jamf Pro 11.12.1
- **Jamf bug ID**: PI122416 (critical severity)
- **Impact**: Twingate VPN Custom Configuration Profile fails to install on any macOS device managed via Jamf Pro

## Prerequisites
- Access to [iMazing Profile Editor](https://imazing.com/profile-editor) (or equivalent profile signing tool)
- A signing certificate available outside of Jamf Pro
- Existing Twingate VPN configuration profile settings

## Workaround: Build and Sign Profile Externally

1. **Create the profile** using iMazing Profile Editor (do not use Jamf Pro to build it)
2. **Configure VPN settings** within iMazing Profile Editor as required for Twingate
3. **Export the profile** and sign it with an external signing certificate during export
4. **Upload the signed profile** to Jamf Pro
5. **Verify**: Jamf Pro should display that the profile is signed and that "signature removal is required to make changes"
6. **Do not remove the signature** when prompted
7. **Deploy** the profile as normal through Jamf Pro

## Gotchas
- Uploading a pre-signed profile prevents Jamf Pro from modifying it on upload — this is intentional and required for the workaround
- If Jamf Pro shows the signature removal prompt, leave it signed; removing the signature re-introduces the bug
- Upgrading to Jamf Pro 11.12.1+ is the permanent fix — the workaround is only needed on 11.11

## Related Docs
- Twingate macOS Jamf Pro deployment documentation
- [iMazing Profile Editor](https://imazing.com/profile-editor)